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
from   pytz                         import all_timezones, timezone

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 2
no_of_tags      = 2
no_of_attachs   = 50

g_byuser    = u'admin'

compmgr     = None
userscomp   = None
liccomp     = None
attachcomp  = None
tagcomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, tagcomp, liccomp, seed, cachemgr

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
    userscomp  = config['userscomp']
    compmgr    = config['compmgr']
    attachcomp = AttachComponent( compmgr )
    liccomp    = LicenseComponent( compmgr )
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    print "   Populating licenses ( no_of_tags=%s, no_of_attachs=%s ) ..." % \
                ( no_of_tags, no_of_attachs )
    pop_licenses( no_of_tags, no_of_attachs, seed=seed )
    print "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, no_of_attach=%s" % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs )

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


class TestAttachForms( object ) :

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

    def test_1_removeattachs( self ) :
        """Testing FormRemoveAttach with valid and invalid input"""
        log.info( "Testing FormRemoveAttach with valid and invalid input ..." )
        request = RequestObject()
        c = ContextObject()
        vf = VForm( compmgr )

        users           = userscomp.get_user()
        u               = choice( users )
        l               = choice( liccomp.get_license() )
        config['c']     = c
        c.authuser      = g_byuser

        # Clean attachments in license
        [ liccomp.remove_attach( l, attach ) for attach in l.attachments ]

        # Add attachments
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addlicattachs' )

        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'license_id', str(l.id) )
        attachmentfiles = []
        for i in range(randint(0,3)) :
            attach          = FileObject()
            attachfile      = choice( attachfiles )
            attach.filename = os.path.basename( attachfile )
            attach.file     = open( attachfile, 'r' )
            request.POST.add( 'attachfile', attach  )
            attachmentfiles.append( attach )
        user    = choice( userscomp.get_user() )
        vf.process( request, c, user=user.username )
        l = liccomp.get_license( l.licensename )
        assert_equal( sorted([ a.filename for a in l.attachments ]),
                      sorted([ attach.filename for attach in attachmentfiles ]),
                      'Mismatch in adding license attachment'
                    )

        # Remove attachments
        c.rclose    = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmattachs' )
        attach_ids = [ a.id for a in l.attachments ]
        request.POST.add( 'user_id', str(u.id) )
        [ request.POST.add( 'attach_id', str(id) ) for id in attach_ids ]

        defer = choice([True, False])
        vf.process( request, c, removeattach=True, defer=defer,
                    formnames=['rmattachs'] )

        if l.attachments :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted attachment' in u.logs[-1].log and \
                               l.attachments[-1].filename in u.logs[-1].log
            )

        l = liccomp.get_license( l.licensename )
        assert_false( l.attachments,
                      'Mismatch while removing attachments using FormRemoveAttach' )

    def test_2_addattach( self ) :
        """Testing FormAddAttachs with valid input"""
        log.info( "Testing FormAddAttachs with valid input ..." )
        request = RequestObject()
        c       = ContextObject()
        vf      = VForm( compmgr )

        users       = userscomp.get_user()
        u           = choice( users )
        config['c'] = c
        c.authuser  = g_byuser
        c.rclose    = h.ZResp()

        # Add attachments
        user    = choice( userscomp.get_user() )
        summary = u'Some summary for this attach'
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addattachs' )

        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'summary', summary )
        attach          = FileObject()
        attachfile      = choice( attachfiles )
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )
        request.POST.add( 'attachfile', attach  )

        defer = choice([True, False])
        vf.process( request, c, defer=defer, user=user.username,
                    formnames=['addattachs'] )

        self._validate_defer(
                user.id, defer, c,
                lambda u : 'Uploaded attachment' in u.logs[-1].log
        )

        a = sorted( attachcomp.get_attach(), key=lambda x:x.id )[-1]
        assert_equal( [ a.filename, a.summary, a.uploader.username ],
                      [ os.path.basename( attachfile ), summary, user.username ],
                      'Mismatch in adding attachment'
                    )

    def test_3_updateattach( self ) :
        """Testing FormAttachsUpdate with valid input"""
        log.info( "Testing FormAttachsUpdate with valid input ..." )
        request = RequestObject()
        c       = ContextObject()
        vf      = VForm( compmgr )

        users       = userscomp.get_user()
        u           = choice( users )
        config['c'] = c
        c.authuser  = g_byuser
        c.rclose    = h.ZResp()

        # Attachment summary
        user    = choice( userscomp.get_user() )
        a       = sorted( attachcomp.get_attach(), key=lambda x:x.id )[-1]
        summary = u'Updated summary for this attach'
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'attachssummary' )

        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'attachment_id', str(a.id) )
        request.POST.add( 'summary', summary )

        defer = choice([True, False])
        vf.process( request, c, defer=defer, user=user.username,
                    formnames=['attachssummary'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Updated summary' in u.logs[-1].log
        )

        a = attachcomp.get_attach( a.id )
        assert_equal( a.summary, summary,
                      'Mismatch while updating attachment summary' )


        # Attachment tags
        c.rclose    = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        user    = choice( userscomp.get_user() )
        tags    = [ u'helo', u'world' ]
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'attachstags' )

        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'attachment_id', str(a.id) )
        request.POST.add( 'tags', ', '.join([ tag for tag in tags ]) )

        defer = choice([True, False])
        vf.process( request, c, defer=defer, user=user.username,
                    formnames=['attachstags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added tags' in u.logs[-1].log or 
                           'deleted tags' in u.logs[-1].log,
        )

        a = attachcomp.get_attach( a.id )
        assert_equal( sorted([ tag.tagname for tag in a.tags ]),
                      sorted( tags ),
                      'Mismatch while updating attachment tags' )
