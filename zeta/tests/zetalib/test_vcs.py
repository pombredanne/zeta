# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import os
from   os.path                      import join, isdir, basename
import random
from   random                       import choice, randint, shuffle, seed
import re

import pylons.test
import pylons
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, assert_true
import simplejson                   as json

from   zeta.auth.perm               import permissions
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
import zeta.lib.vcsadaptor          as va
from   zeta.comp.vcs                import VcsComponent
from   zeta.tests                   import *
from   zeta.tests.model.generate    import gen_vcs
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_vcs, pop_wikipages
from   zeta.tests.tlib              import *

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None
no_of_users     = 15
no_of_relations = 2
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 5
no_of_vcs       = no_of_projects * 2
g_byuser        = u'admin'

compmgr    = None
userscomp  = None
vcscomp    = None
cachemgr   = None
cachedir   = '/tmp/testcache'


def setUpModule() :
    global compmgr, vcscomp, seed, cachemgr

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
    compmgr    = config['compmgr']
    userscomp  = config['userscomp']
    vcscomp    = VcsComponent( compmgr )
    # Populate DataBase with sample entries
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    print "   Populating licenses ( no_of_tags=%s, no_of_attachs=%s ) ..." % \
                ( no_of_tags, no_of_attachs )
    pop_licenses( no_of_tags, no_of_attachs, seed=seed )
    print "   Populating projects ( no_of_projects=%s ) ..." % no_of_projects
    pop_projects( no_of_projects, no_of_tags, no_of_attachs, seed=seed )
    print "   Populating Vcs ( no_of_vcs=%s ) ..." % no_of_vcs
    pop_vcs( no_of_vcs, seed=seed )

    # Setup cache manager
    isdir( cachedir ) or os.makedirs( cachedir )
    cachemgr = cachemod.cachemanager( cachedir )
    config['cachemgr'] = cachemgr
    pylons.config = config


def tearDownModule() :
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )
    info = "   Deleting models (module-level) ... "
    log.info( info )
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )

class TestVcsSvn( object ) :

    def test_1_open_repository( self ) :
        """Testing open_repository()"""
        log.info( "Testing open_repository()" )
        
        vcsentries = vcscomp.get_vcs()
        v          = choice( vcsentries )
        vrep       = va.open_repository( v )

        # Test for apis in the repository module
        apis       = [ 'init', 'info', 'list', 'cat', 'diff', 'logs',
                       'changedfiles' ]
        [ assert_true(
                api in vrep.vcsmod.__dict__.keys(),
                'Mismatch VcsAdaptor api (%s) is not present' % api 
          ) for api in apis ]

        # Test for vrep attributes
        attrs = [ 'vcs', 'vcsmod', 'client' ]
        [ assert_true(
                attr in dir(vrep),
                'Mismatch, VcsRepository() attr(%s) is not present' % attr
          ) for attr in attrs ]

        # Test for vrep methods
        info = vrep.info( vrep.vcs.rooturl )
        [ assert_true( 
                k in info.keys(),
                'Mismatch, vrep.info method returns %s' % info
          ) for k in [ 'l_revision', 'l_author', 'l_date', 'mime_type',
                       'size', 'repos_path' ] 
        ]

        listing = vrep.list( vrep.vcs.rooturl )
        assert_equal( len(listing[0]), 7,
                      'Mismatch in the number of items in a list entry' )

        listing = vrep.logs( vrep.vcs.rooturl )
        assert_equal( len(listing[0]), 4,
                      'Mismatch in the number of items in a log entry' )

        re = vrep.linfo['l_revision']
        rs = re - 1
        vfiles  = vrep.changedfiles( vrep.vcs.rooturl, revstart=rs, revend=re )
        [ assert_true( 
                isinstance( f['vfile'], va.VcsFile ),
                'Mismatch in the file instance from changedfiles'
          ) for f in vfiles ]
        # Testing changedfile attributes
        attrs = [ 'repos_path', 'changetype', 'mime_type', 'vfile' ]
        [ assert_true(
                attr in vfiles[0].keys(),
                'Mismatch, VcsFile() attr(%s) is not present' % attr
          ) for attr in attrs ]
        # Testing vfile attributes
        attrs = [ 'vcs', 'vcsmod', 'client', 'url', 'revno', 'repopath', 
                  'vrep' ]
        [ assert_true(
                attr in dir(vfiles[0]['vfile']),
                'Mismatch, VcsFile() attr(%s) is not present' % attr
          ) for attr in attrs ]

        vfile = vfiles[0]['vfile']

        info = vfile.info()
        [ assert_true( 
                k in info.keys(),
                'Mismatch, vfile.info method returns %s' % info
          ) for k in [ 'l_revision', 'l_author', 'l_date', 'mime_type',
                       'size', 'repos_path' ] 
        ]

        content = vfile.cat()
        assert_equal(
            len(content[0]), 5,
            'Mismatch in the number of items in unannotated file content' 
        )
        assert_equal(
            content[0][2:], (None, None, None),
            'Mismatch, fields in unannotated file content are not None' 
        )
        content = vfile.cat( annotate=True)
        assert_equal(
            len(content[0]), 5,
            'Mismatch in the number of items in unannotated file content'
        )
        [ assert_true(
                field,
                'Mismatch, fields in unannotated file content are not None' 
          ) for field in content[0][2:] ]
