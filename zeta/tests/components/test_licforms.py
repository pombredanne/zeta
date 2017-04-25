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
from   zeta.tests.model.generate    import gen_projects, future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 2
no_of_tags      = 5
no_of_attachs   = 2

g_byuser        = u'admin'

tagchars    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
taglist     = None 

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
    global compmgr, userscomp, attachcomp, liccomp, tagcomp, taglist, seed, \
           cachemgr

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
    tagcomp    = TagComponent( compmgr )
    liccomp    = LicenseComponent( compmgr )
    taglist = [ unicode(h.randomname( randint(0,LEN_TAGNAME), tagchars))
                            for i in range(randint(1,no_of_tags)) ]
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


class TestLicenseForms( object ) :

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

    def test_1_createlicense_valid( self ) :
        """Testing FormCreateLicense with valid input"""
        log.info( "Testing FormCreateLicense with valid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users   = userscomp.get_user()
        u       = choice( users )

        licname = u'somelicensename' 
        summary = u'somesummary' 
        text    = u'somelicensetext blah blah blah ...' 
        source  = u'straight from Thirisangu !!' 

        # Create license
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createlic' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'licensename', licname )
        request.POST.add( 'summary', summary )
        request.POST.add( 'text', text )
        request.POST.add( 'source', source )
        vf.process( request, c, defer=False, formnames=['createlic'] )

        self._validate_defer(
                c.authuser, False, c,
                lambda u : 'created new license' in u.logs[-1].log 
        )

        l = liccomp.get_license( u'somelicensename' )
        assert_equal( [ licname, summary, text, source ],
                      [ l.licensename, l.summary, l.text, l.source ],
                      'Mismatch in creating license'
                    )

        # update license
        c.rclose = h.ZResp()
        licname = u'updatedsomelicensename' 
        summary = u'updated license summary'
        source  = u'updated license source'
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updatelic' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'license_id', str(l.id) )
        request.POST.add( 'licensename', licname )
        request.POST.add( 'summary', summary )
        request.POST.add( 'text', text )
        request.POST.add( 'source', source )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['updatelic'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated license' in u.logs[-1].log
        )

        l = liccomp.get_license( u'updatedsomelicensename' )
        assert_equal( [ licname, summary, text, source ],
                      [ l.licensename, l.summary, l.text, l.source ],
                      'Mismatch in updating license'
                    )
        assert_false( liccomp.get_license( u'somelicensename' ),
                      'Same license name returned even after updating it' )

    def test_2_createlicense_invalid( self ) :
        """Testing FormCreateLicense with invalid input"""
        log.info( "Testing FormCreateLicense with invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users   = userscomp.get_user()
        u       = choice( users )

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createlic' )

        # Try creating license with in-sufficient inputs.
        request.POST.add( 'user_id', str(u.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        licname = u'somelicensename' 
        request.POST.add( 'licensename', licname )
        assert_raises( ZetaFormError, vf.process, request, c )
        summary = u'somesummary' 
        request.POST.add( 'summary', summary )
        assert_raises( ZetaFormError, vf.process, request, c )
        text    = u'somelicensetext blah blah blah ...' 
        request.POST.add( 'text', text )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try creating existing license
        l = choice( liccomp.get_license() )
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'licensename', l.licensename )
        request.POST.add( 'summary', l.summary )
        request.POST.add( 'text', l.text )
        request.POST.add( 'source', l.source )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_3_removelicense_valid( self ) :
        """Testing FormRemoveLicense with valid input"""
        log.info( "Testing FormRemoveLicense with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users   = userscomp.get_user()
        u       = choice( users )
        license = liccomp.get_license()

        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmlic' )
        rmlic = list(set([ choice(license) for i in range(3) ]))
        [ license.remove( l ) for l in rmlic ]
        request.POST.add( 'user_id', str(u.id) )
        [ request.POST.add( 'licensename', l.licensename ) for l in rmlic ]
        defer = choice([True, False])
        vf.process( request, c, defer, formnames=['rmlic'] )

        def _verify(u) :
            log = ', '.join([ u.logs[-i].log for i in range(1, len(rmlic)+1) ])
            return all([ l.licensename in log for l in rmlic ])

        self._validate_defer( c.authuser, defer, c, _verify )

        assert_equal( sorted(license),
                      sorted(liccomp.get_license()),
                      'Mismatch while removing license'
                    )

    def test_4_removelicense_invalid( self ) :
        """Testing FormRemoveLicense with invalid input"""
        log.info( "Testing FormRemoveLicense with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users   = userscomp.get_user()
        u       = choice( users )
        license = liccomp.get_license()

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmlic' )
        rmlic   = list(set([ choice(license) for i in range(2) ]))
        [ license.remove( l ) for l in rmlic ]
        request.POST.add( 'user_id', str(u.id) )
        [ request.POST.add( 'licensename', l.licensename ) for l in rmlic ]
        request.POST.add( 'licensename', u'invalid_license' )
        vf.process( request, c )
        assert_equal( sorted(license),
                      sorted(liccomp.get_license()),
                      'Mismatch while removing invalid license'
                    )

    def test_5_licensetags( self ) :
        """Testing FormLicenseTags with valid and invalid input"""
        log.info( "Testing FormLicenseTags with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        l       = choice( liccomp.get_license() )
        users   = userscomp.get_user()
        u       = choice( users )

        # Add tags to license.
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addlictags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set( filter( lambda t : tagcomp.is_tagnamevalid( t ),
                                      tagnames ) + \
                              [ t.tagname for t in l.tags ]
                    ))

        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'license_id', str(l.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in reftags ]) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addlictags'] )

        if tagnames :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'added tags' in u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        l = liccomp.get_license( l.licensename )
        assert_equal( sorted(reftags), 
                      sorted([ t.tagname for t in l.tags ]),
                      'Mismatch while creating tags'
                    )
        # delete tags to license.
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'dellictags' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'license_id', str(l.id) )
        rmtag    = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'tags', rmtag )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['dellictags'] )

        if rmtag :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted tags' in u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        l = liccomp.get_license( l.licensename )
        assert_equal( sorted( reftags ), 
                      sorted([ t.tagname for t in l.tags ]),
                      'Mismatch while deleting tags'
                    )

    def test_6_licenseattachs( self ) :
        """Testing FormLicenseAttachs with valid and invalid input"""
        log.info( "Testing FormLicenseAttachs with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        u               = choice( users )
        l               = choice( liccomp.get_license() )

        # Clean attachments in license
        [ liccomp.remove_attach( l, attach ) for attach in l.attachments ]

        # Add attachments
        c.rclose = h.ZResp()
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
        user = choice( userscomp.get_user() )

        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['addlicattachs'] )
        if attachmentfiles :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'uploaded attachment' in u.logs[-1].log
            )
        elif defer :
            c.rclose.close()

        l = liccomp.get_license( l.licensename )
        assert_equal( sorted([ a.filename for a in l.attachments ]),
                      sorted([ attach.filename for attach in attachmentfiles ]),
                      'Mismatch in adding license attachment'
                    )

        # Remove attachments
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'dellicattachs' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'license_id', str(l.id) )
        [ request.POST.add( 'attach_id', str(a.id) ) for a in l.attachments ]
        defer = choice([True, False])
        vf.process( request, c ,defer=defer, formnames=['dellicattachs'] )

        if l.attachments :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted attachment' in u.logs[-1].log
            )
        elif defer :
            c.rclose.close()

        l = liccomp.get_license( l.licensename )
        assert_false( l.attachments, 'Mismatch in removing license attachment' )
