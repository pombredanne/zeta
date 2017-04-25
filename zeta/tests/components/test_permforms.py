# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os.path                      import join, isdir, basename
import random
from   random                       import choice, randint
import datetime                     as dt

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 2
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 10
g_byuser        = u'admin'

compmgr   = None
userscomp = None
cachemgr  = None
cachedir  = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, seed, cachemgr

    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )
    info = "   Creating models (module-level) ... "
    log.info( info )
    print info
    # Setup SQLAlchemy database engine
    engine  = engine_from_config( config, 'sqlalchemy.' )
    # init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )
    userscomp = config['userscomp']
    compmgr   = config['compmgr']
    print "   Populating permissions ..."
    pop_permissions( seed=seed )

    # Setup cache manager
    isdir( cachedir ) or os.makedirs( cachedir )
    cachemgr = cachemod.cachemanager( cachedir )
    config['cachemgr'] = cachemgr


def tearDownModule() :
    """Clean up database."""
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )
    info = "   Deleting models (module-level) ... "
    log.info( info )
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )


class TestPermForms( object ) :

    def _validate_defer( self, user, defer, c, assertlogic ) :
        user = isinstance( user, (int, long)) and user \
               or isinstance( user, (str, unicode)) and user \
               or user.id

        if defer :
            user = userscomp.get_user( user, attrload=['logs'] )
            assert_false( assertlogic(user), 'Mismatch in defer' )
        defer and c.rclose.close()
        user = userscomp.get_user( user, attrload=[ 'logs' ] )
        assert_true( assertlogic(user), 'Mismatch in defer' )

    def test_1_createpermgroup_valid( self ) :
        """Testing FormCreatePermgroup with valid input"""
        log.info( "Testing FormCreatePermgroup with valid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        for i in range( 2, len(userscomp.perm_names) / 6 ) :
            # Create
            c.rclose = None
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'createpg' )
            perm_group = 'group_developers' + str(i)
            perm_names = list(set([ choice( userscomp.perm_names ) 
                                    for j in range(i) ]))
            request.POST.add( 'perm_group', perm_group )
            [ request.POST.add( 'perm_name', pn ) for pn in perm_names ]
            defer=choice([True, False])
            vf.process( request, c, defer=defer, formnames=['createpg'] )
            
            self._validate_defer(
                    c.authuser, False, c,
                    lambda u : \
                        'created new permission group' in u.logs[-2].log and \
                        'added permnames to permgroup' in u.logs[-1].log
            )

            # Update perm_group name
            c.rclose = h.ZResp()
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'updatepg' )
            pg = userscomp.get_permgroup( perm_group )
            new_perm_group = 'updated_perm_group' + str(i) \
                             if choice([ True, False ]) else perm_group
            request.POST.add( 'perm_group_id', str(pg.id) )
            request.POST.add( 'perm_group', new_perm_group )
            defer = choice([True, False])
            vf.process( request, c, defer=defer, formnames=['updatepg'] )
            if new_perm_group != perm_group :
                self._validate_defer(
                        c.authuser, defer, c,
                        lambda u : 'changed permission group' in u.logs[-1].log
                )

            # append
            c.rclose = h.ZResp()
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'addpntopg' )
            add_perm_names = list(set([ choice( userscomp.perm_names ) 
                                        for j in range(i) ]))
            perm_names = list(set( perm_names + add_perm_names ))
            request.POST.add( 'perm_group_id', str(pg.id) )
            [ request.POST.add( 'perm_name', pn ) for pn in add_perm_names ]
            defer = choice([True, False])
            vf.process( request, c, defer=defer, formnames=['addpntopg'] )

            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'added permnames to permgroup' in u.logs[-1].log
            )

            # remove
            c.rclose = h.ZResp()
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'delpnfrompg' )
            rmpn = list(set([ choice(perm_names) for j in range(i/2) ]))
            request.POST.add( 'perm_group_id', str(pg.id) )
            [ ( request.POST.add( 'perm_name', pn ), perm_names.remove(pn) )
              for pn in rmpn ]
            defer = choice([True, False])
            vf.process( request, c, defer=defer, formnames=['delpnfrompg'] ) 
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted permnames from permgroup' in u.logs[-1].log,
            )

            pg  = userscomp.get_permgroup( new_perm_group )
            assert_equal( new_perm_group, pg.perm_group,
                          'Form Mismatch in created perm_group' )
            assert_equal( sorted(perm_names),
                          sorted([ pn.perm_name for pn in pg.perm_names ]),
                          'Form Mismatch in created perm_names' )

    def test_2_createpermgroup_invalid( self ) :
        """Testing FormCreatePermgroup with invalid input"""
        log.info( "Testing FormCreatePermgroup with invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createpg' )

        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )

        request.POST.clearfields()
        request.POST.add( 'perm_group', 'ab' )
        vf.process( request, c )

        request.POST.clearfields()
        request.POST.add( 'perm_group', 'a' * LEN_NAME + 'b'  )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )

    def test_3_deletepermgroup_valid( self ) :
        """Testing DeletePermgroup with valid input"""
        log.info( "Testing DeletePermgroup with valid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delpg' )

        permgroups = userscomp.get_permgroup()
        rmpg = list(set(
                    [ choice(permgroups) 
                      for i in range(randint( 0, len(permgroups) )) ]
                ))
        [ ( request.POST.add( 'perm_group', pg.perm_group ),
            permgroups.remove( pg ) 
          ) for pg in permgroups ]
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['delpg'] )
        if rmpg :
            self._validate_defer(
                c.authuser, False, c,
                lambda u : 'deleted permission groups' in u.logs[-1].log,
            )

        assert_equal( sorted(permgroups),
                      sorted(userscomp.get_permgroup()),
                      'Mismatch in removed permgroups' 
                    )

    def test_4_deletepermgroup_invalid( self ) :
        """Testing DeletePermgroup with invalid input"""
        log.info( "Testing DeletePermgroup with invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delpg' )

        permgroups = userscomp.get_permgroup()
        vf.process( request, c )
        assert_equal( sorted(permgroups),
                      sorted(userscomp.get_permgroup()),
                      'Mismatch in removed permgroups' 
                    )

        request.POST.add( 'perm_group', 'invalid_perm_group' )
        vf.process( request, c )
        assert_equal( sorted(permgroups),
                      sorted(userscomp.get_permgroup()),
                      'Mismatch in removed permgroups' 
                    )

        rmpg = list(set(
                    [ choice(permgroups).perm_group
                      for i in range(randint( 0, len(permgroups) )) ]
                ))
        [ ( request.POST.add( 'perm_group', pg.perm_group ),
            permgroups.remove( pg ) 
          ) for pg in permgroups ]
        request.POST.add( 'perm_group', 'invalid_perm_group' )
        vf.process( request, c )
        assert_equal( sorted(permgroups),
                      sorted(userscomp.get_permgroup()),
                      'Mismatch in removed permgroups' 
                    )
