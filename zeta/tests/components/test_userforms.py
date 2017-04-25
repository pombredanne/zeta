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
from   hashlib                      import sha1

import pylons.test
from   pylons                       import config
from   paste.util.import_string     import eval_import
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true

from   zeta.auth.perm               import permissions
import zeta.auth.perm               as permmod
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.lib.mailclient          import MailDB, OutMessage, mime_attachfname
from   zeta.comp.forms              import *
from   zeta.comp.system             import SystemComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
syscomp     = None
attachcomp  = None
cachemgr    = None
cachedir    = '/tmp/testcache'
ctxt        = { 'strictauth' : choice(['True', 'False']) }


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, syscomp, attachcomp, seed, cachemgr

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
    syscomp    = SystemComponent( compmgr )
    attachcomp = AttachComponent( compmgr )
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )

    # initialize the PMS system
    mapmod = eval_import( config['zeta.pmap.module'] )
    permmod.init_pms = eval_import( config['zeta.pmap.mapfunc'] )
    permmod.pms_root = permmod.init_pms( ctxt=ctxt )
    permmod.default_siteperms = mapmod.default_siteperms
    permmod.default_projperms = mapmod.default_projperms

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


class TestUserForms( object ) :

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

    def test_2_createuser_valid( self ) :
        """Testing FormCreateUser with valid input"""
        log.info( "Testing FormCreateUser with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        for i in range(7) :
            # Create user
            c.rclose = h.ZResp()
            sample  = [
                    u'validusername',            u'valid@emailid',           #0
                    u'validpassword',            u'validpassword',           #2
                    choice( all_timezones ),                                 #3
                    u'validfirstname',           u'validmiddlename',         #5
                    u'validlastname',            u'valid, address, line, 1', #7
                    u'valid, address, line, 2',  u'validcity',               #9
                    u'vpcode',                   u'validstate',              #11
                    u'validcountry',             u'favorites,projects'       #13
            ]
            detnames = [
                'username', 'emailid', 'password', 'confpass', 'timezone',
                'firstname', 'middlename', 'lastname', 'addressline1',
                'addressline2', 'city', 'pincode', 'state', 'country',
                'userpanes'
            ]
            request.POST.clearfields()
            request.params.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'createuser' )

            userdet    = [ sample[det] + str(i) for det in range(8) ]
            userdet[4] = userdet[4][:-1]   # Dont do str(i) for timezone
            userdet.extend(
                [ sample[det] + str(i) for det in range(8, 8+i+1) ]
            )
            [ request.POST.add( detnames[det], userdet[det] )
              for det in range(8) ]
            [ request.POST.add( detnames[det], userdet[det] )
              for det in range(8, 8+i+1) ]

            vf.process( request, c, defer=False, test=True,
                        formnames=['createuser'] )

            self._validate_defer(
                    userdet[0], False, c,
                    lambda u : 'registered new user' in u.logs[-2].log
            )

            u = userscomp.get_user( userdet[0] )
            userdet[2] = sha1( userdet[2] ).hexdigest()
            userdet[3] = sha1( userdet[3] ).hexdigest()
            assert_equal( [ u.username, u.emailid, str(u.password),
                            str(u.password), u.timezone ],
                          [ userdet[det] for det in range(5) ],
                          'Mismatch in created user'
                        )
            assert_equal( [ getattr( u.userinfo, det ) 
                            for det in detnames[8:8+i+1] ],
                          [ userdet[det] for det in range(8, 8+i+1) ],
                          'Mismatch is created user info' 
                        )
            if i == 6 :
                assert_equal( filter( None, [ getattr( u.userinfo, det ) 
                                              for det in detnames[8+i+1:] ]),
                              [],
                              'Mismatch is left over user info' 
                            )
            else :
                assert_equal( filter( None, [ getattr( u.userinfo, det ) 
                                              for det in detnames[8+i+1:] ]),
                              ['siteuserpanes'],
                              'Mismatch is left over user info' 
                            )

            # update user
            c.rclose = h.ZResp()
            sample  = [
                    u'validusername',            u'updtd@emailid',           #0
                    u'updtdpassword',            u'updtdpassword',           #2
                    choice( all_timezones ),                                 #3
                    u'updtdfirstname',           u'updtdmiddlename',         #5
                    u'updtdlastname',            u'updtd, address, line, 1', #7
                    u'updtd, address, line, 2',  u'updtdcity',               #9
                    u'vpcode',                   u'updtdstate',              #11
                    u'updtdcountry',             u'projects,calendar'        #13
            ]
            detnames = [
                'username', 'emailid', 'password', 'confpass', 'timezone',
                'firstname', 'middlename', 'lastname', 'addressline1',
                'addressline2', 'city', 'pincode', 'state', 'country',
                'userpanes'
            ]
            request.POST.clearfields()
            request.params.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'updateuser' )
            request.POST.add( 'user_id', str(u.id) )
            userdet    = [ sample[det] + str(i) for det in range(8) ]
            userdet[4] = userdet[4][:-1]   # Dont do str(i) for timezone
            userdet.extend(
                [ sample[det] + str(i) for det in range(8, 8+i+1) ]
            )
            [ request.POST.add( detnames[det], userdet[det] )
              for det in range(8) ]
            [ request.POST.add( detnames[det], userdet[det] )
              for det in range(8, 8+i+1) ]
            defer = choice([True, False])
            vf.process( request, c, defer=defer, formnames=['updateuser'] )

            self._validate_defer(
                    userdet[0], defer, c,
                    lambda u : 'updated user preference' in u.logs[-1].log
            )

            u = userscomp.get_user( u.id )
            userdet[2] = sha1( userdet[2] ).hexdigest()
            userdet[3] = sha1( userdet[3] ).hexdigest()
            assert_equal( [ u.username, u.emailid, str(u.password),
                            str(u.password), u.timezone ],
                          [ userdet[det] for det in range(5) ],
                          'Mismatch in created user'
                        )
            assert_equal( [ getattr( u.userinfo, det ) 
                            for det in detnames[8:8+i+1] ],
                          [ userdet[det] for det in range(8, 8+i+1) ],
                          'Mismatch is created user info' 
                        )
            if i == 6 :
                assert_equal( filter( None, [ getattr( u.userinfo, det ) 
                                              for det in detnames[8+i+1:] ]),
                              [],
                              'Mismatch is left over user info' 
                            )
            else :
                assert_equal( filter( None, [ getattr( u.userinfo, det ) 
                                              for det in detnames[8+i+1:] ]),
                              [ 'siteuserpanes' ],
                              'Mismatch is left over user info' 
                            )

    def test_3_createuser_invalid( self ) :
        """Testing FormCreateUser with invalid input"""
        log.info( "Testing FormCreateUser with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createuser' )

        request.POST.add( 'username', u'someusername' )
        assert_raises( ZetaFormError, vf.process, request, c )
        request.POST.add( 'emailid', u'some@emailid' )
        assert_raises( ZetaFormError, vf.process, request, c )
        request.POST.add( 'password', 'somepassword' )
        request.POST.add( 'confpass', 'somepassword' )
        assert_raises( ZetaFormError, vf.process, request, c )
        timezone = choice(all_timezones) 
        request.POST.add( 'timezone', timezone )
        request.POST.add( 'firstname', u'somefirstname' )
        request.POST.add( 'middlename', u'somemiddlename' )
        request.POST.add( 'lastname', u'somelastname' )
        vf.process( request, c, test=True )
        u   = userscomp.get_user( u'someusername' )
        ref = [ u'someusername', u'some@emailid', 
                sha1( 'somepassword' ).hexdigest(),
                timezone,
                u'somefirstname', u'somemiddlename', u'somelastname' ]
        db  = [ u.username, u.emailid, str(u.password), u.timezone,
                u.userinfo.firstname, u.userinfo.middlename, u.userinfo.lastname
              ]
        assert_equal( ref, db, 'Mismatch in created user details' )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_4_updatepassword_valid( self ) :
        """Testing FormUpdatePassword with valid input"""
        log.info( "Testing FormUpdatePassword with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c

        username = u'p_someusername' 
        c.authuser = username

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createuser' )

        request.POST.add( 'username', username )
        request.POST.add( 'emailid', u'p_some@emailid' )
        request.POST.add( 'password', 'p_somepassword' )
        request.POST.add( 'confpass', 'p_somepassword' )
        timezone = choice(all_timezones) 
        request.POST.add( 'timezone', timezone )
        request.POST.add( 'firstname', u'p_somefirstname' )
        request.POST.add( 'middlename', u'p_somemiddlename' )
        request.POST.add( 'lastname', u'p_somelastname' )
        vf.process( request, c, test=True )

        u = userscomp.get_user( username )
        ref = [ username, u'p_some@emailid',
                sha1( 'p_somepassword' ).hexdigest(),
                timezone,
                u'p_somefirstname', u'p_somemiddlename', u'p_somelastname' ]
        db  = [ u.username, u.emailid, str(u.password), u.timezone,
                u.userinfo.firstname, u.userinfo.middlename, u.userinfo.lastname
              ]
        assert_equal( ref, db, 'Mismatch in created user details' )

        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updtpass' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'password', 'updatedpassword' )
        request.POST.add( 'confpass', 'updatedpassword' )
        vf.process( request, c, defer=False, formnames=['updtpass'] )

        self._validate_defer(
                u.id, False, c,
                lambda u : 'updated user preference' in u.logs[-1].log
        )

        ref = [ username, u'p_some@emailid',
                sha1( 'updatedpassword' ).hexdigest(),
                timezone,
                u'p_somefirstname', u'p_somemiddlename', u'p_somelastname' ]
        db  = [ u.username, u.emailid, str(u.password), u.timezone,
                u.userinfo.firstname, u.userinfo.middlename, u.userinfo.lastname
              ]
        assert_equal( ref, db, 'Mismatch in updated password' )

    def test_5_updatepassword_invalid( self ) :
        """Testing FormUpdatePassword with invalid input"""
        log.info( "Testing FormUpdatePassword with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updtpass' )

        assert_raises( ZetaFormError, vf.process, request, c )
        u = userscomp.get_user( u'p_someusername' ) 
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'password', 'updatedpassword' )
        request.POST.add( 'confpass', 'wrongconfpass' )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_6_userphoto_valid( self ) :
        """Testing FormUserPhoto with valid input"""
        log.info( "Testing FormUserPhoto with valid inputs" )
        request = RequestObject()
        c       = ContextObject()
        vf      = VForm( compmgr )

        # Add user photo
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'userphoto' )
        u               = userscomp.get_user( u'someusername' )
        attachfile      = choice( attachfiles )
        attach          = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'attachfile', attach  )
        user = choice( userscomp.get_user() )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['userphoto'] )

        self._validate_defer(
                u.id, defer, c,
                lambda u : 'uploaded user photo' in u.logs[-1].log
        )
        u = userscomp.get_user( u.id )  
        assert_equal( u.photofile.filename, attach.filename,
                      'Mismatch in photo attachment'
                    )
        a, cont = attachcomp.downloadattach(u.photofile.id)
        assert_equal( str(cont), open( attachfile ).read(),
                      'photo files mismatches between files `%s` and `%s`' % \
                      (attachfile, u.photofile.id)
                    )

        # Delete user photo
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deluserphoto' )
        request.POST.add( 'user_id', str(u.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['deluserphoto'] )
        self._validate_defer(
                u.id, defer, c,
                lambda u : 'removed user photo' in u.logs[-1].log
        )

        u  = userscomp.get_user( u.username )
        assert_false( u.photofile, 'Found photo attachment even after removing it' )

    def test_7_userphoto_invalid( self ) :
        """Testing FormUserPhoto with invalid input"""
        log.info( "Testing FormUserPhoto with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'userphoto' )

        u               = userscomp.get_user( u'someusername' )
        attachfile      = choice( attachfiles )
        attach          = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )

        assert_raises( ZetaFormError, vf.process, request, c )
        request.POST.add( 'user_id', str(u.id) )
        assert_raises( ZetaFormError, vf.process, request, c )
        request.POST.add( 'attachfile', attach  )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_8_usericon_valid( self ) :
        """Testing FormUserIcon with valid input"""
        log.info( "Testing FormUserIcon with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        # Add user icon
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'usericon' )
        u = userscomp.get_user( u'someusername' )
        attachfile = choice( attachfiles )
        attach = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file = open( attachfile, 'r' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'attachfile', attach  )
        user = choice( userscomp.get_user() )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['usericon'] )

        self._validate_defer(
                u.id, defer, c,
                lambda u : 'uploaded user icon' in u.logs[-1].log
        )

        u = userscomp.get_user( u.username )
        assert_equal( u.iconfile.filename, attach.filename,
                      'Mismatch in icon attachment'
                    )
        a, cont = attachcomp.downloadattach(u.iconfile.id)
        assert_equal( str(cont), open( attachfile ).read(),
                      'icon files mismatches between files `%s` and `%s`' % \
                      (attachfile, u.iconfile.id)
                    )
        
        # Delete user icon
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delusericon' )
        request.POST.add( 'user_id', str(u.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['delusericon'] )
        self._validate_defer(
                u.id, defer, c,
                lambda u : 'removed user icon' in u.logs[-1].log
        )

        u = userscomp.get_user( u.username )
        assert_false( u.iconfile, 'Found icon attachment even after removing it' )

    def test_9_usericon_invalid( self ) :
        """Testing FormUserIcon with invalid input"""
        log.info( "Testing FormUserIcon with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'usericon' )

        u               = userscomp.get_user( u'someusername' )
        attachfile      = choice( attachfiles )
        attach          = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )

        assert_raises( ZetaFormError, vf.process, request, c )
        request.POST.add( 'user_id', str(u.id) )
        assert_raises( ZetaFormError, vf.process, request, c )
        request.POST.add( 'attachfile', attach  )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_A_userdisable( self ) :
        """Testing FormUserDisable with valid input"""
        log.info( "Testing FormUserDisable with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        admin   = userscomp.get_user( u'admin' )

        # Enable all users
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'userenb' )
        request.POST.add( 'user_id', admin.username ) 
        [ request.POST.add( 'enable_user', u.username ) 
          for u in userscomp.get_user() ]
        vf.process( request, c )

        #  Validate user disabling
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'userdis' )
        request.POST.add( 'user_id', admin.username )
        org_users = userscomp.get_user()
        disusers  = list(set([ org_users.pop(org_users.index(choice(org_users)))
                               for i in range(len(org_users) / 2) ]))
        [ request.POST.add( 'disable_user', u.username ) for u in disusers ]
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['userdis'] )
        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'disabled user' in u.logs[-1].log
        )

        users = userscomp.get_user()
        assert_equal( sorted([ u for u in users if u.disabled == True ]),
                      sorted(disusers),
                      'Mismatch in disabled users' 
                    )

        #  Validate user enabling
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'userenb' )
        request.POST.add( 'user_id', admin.username )
        enusers = list(set([ choice(disusers) 
                             for i in range(len(disusers) / 2) ]))
        [ request.POST.add( 'enable_user', u.username ) for u in enusers ]
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['userenb'] )
        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'enabled user' in u.logs[-1].log
        )
        users = userscomp.get_user()
        assert_equal( sorted([ u for u in users if u.disabled==False ]),
                      sorted( org_users + enusers ),
                      'Mismatch in enabled users' 
                    )

    def test_B_userpermissions_valid( self ) :
        """Testing FormUserPermissions with valid input"""
        log.info( "Testing FormUserPermissions with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users      = userscomp.get_user()
        admin      = userscomp.get_user( u'admin' )
        permgroups = userscomp.get_permgroup()
        for u in userscomp.get_user() :
            c.rclose = h.ZResp()
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            if choice([ True, False ]) :
                formname = 'deluserperms'
                pg = list(set([ choice(u.permgroups) 
                                for i in range(randint(0,len(u.permgroups))) ]))
                ref_pg = [ p for p in u.permgroups if p not in pg ]
            else :
                formname = 'adduserperms'
                pg = list(set([ choice(permgroups)
                                for i in range(randint(0,3)) ]))
                ref_pg = list(set(pg + u.permgroups))
            request.params.add( 'formname', formname )
            request.POST.add( 'user_id', str(admin.id) )
            request.POST.add( 'username', u.username )
            [ request.POST.add( 'perm_group', p.perm_group ) for p in pg ]
            vf.process( request, c, defer=False, formnames=[formname] )

            def _verify(u) :
                rc = []
                if formname == 'adduserperms' and pg :
                    rc =[ 'added permission groups' in u.logs[-1].log ] + \
                        [ x.perm_group in u.logs[-1].log for x in pg ]
                elif formname == 'deluserperms' and pg :
                    rc =[ 'deleted permission groups' in u.logs[-1].log ] + \
                        [ x.perm_group in u.logs[-1].log for x in pg ]
                return all(rc)
            self._validate_defer( c.authuser, False, c, _verify )

            user = userscomp.get_user( u.username )
            assert_equal( sorted(user.permgroups), sorted(ref_pg),
                          'Mismatch in updating user permissions' )

    def test_C_userpermissions_invalid( self ) :
        """Testing FormUserPermissions with invalid input"""
        log.info( "Testing FormUserPermissions with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        # Without `user_id`
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'adduserperms' )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try adding invalid perm_group
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'adduserperms' )
        permgroups = userscomp.get_permgroup()
        u          = choice( userscomp.get_user() )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'username', u.username )
        pg         = list(set([ choice(permgroups) for i in range(3) ]))
        [ request.POST.add( 'perm_group', p.perm_group ) for p in pg ]
        request.POST.add( 'perm_group', 'invalid_group' )
        pg         = list(set( pg + u.permgroups ))
        vf.process( request, c )
        u          = userscomp.get_user( u.username )
        assert_equal( sorted( pg ),
                      sorted( u.permgroups),
                      'Mismatch while adding invalid perm_group'
                    )

        # Try removing invalid perm_group
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deluserperms' )
        request.POST.add( 'user_id', str(u.id) )
        rmpg       = [ p for p in u.permgroups if choice([ True, False ]) ]
        [ request.POST.add( 'perm_group', p.perm_group ) for p in pg ]
        request.POST.add( 'perm_group', 'invalid_group' )
        pg         = u.permgroups
        [ pg.remove( p ) for p in rmpg ]
        u          = userscomp.get_user( u.username )
        assert_equal( sorted( pg ),
                      sorted( u.permgroups),
                      'Mismatch while removing invalid perm_group'
                    )

    def test_D_userrelations_valid( self ):
        """Testing FormUserRelations with valid input"""
        log.info( "Testing FormUserRelations with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        u       = choice( userscomp.get_user() )
        userrels= userscomp.get_userrel()

        # Approve all the user relations.
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'approveuserrels' )
        request.POST.add( 'user_id', str(u.id) )
        [ request.POST.add( 'user_relation_id', str(ur.id) ) for ur in userrels ]
        vf.process( request, c )
        assert_true( all([ ur.approved  for ur in userscomp.get_userrel() ]),
                     'Mismatch in approving all user relations' )

        # Create user relations
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'adduserrels' )
        users   = userscomp.get_user()
        [ users.remove( ur.userto )
          for ur in u.userconnections if ur.userto in users ]
        touser  = choice( users )
        rel_type= choice( userscomp.get_userrel_type() )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'userrel_type', rel_type.userrel_type )
        request.POST.add( 'userfrom', u.username )
        request.POST.add( 'userto', touser.username )
        vf.process( request, c )
        ur = userscomp.get_userrel( userfrom=u.username, userto=touser.username,
                                    reltype=rel_type )
        assert_true( len(ur) == 1,
                     'Mismatch in creating user relation, more than one ur' )
        assert_true( isinstance( ur[0], UserRelation), 
                     'Mismatch in creating user relation' )

        # Delete user relations
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deluserrels' )
        userrels= userscomp.get_userrel()
        rmurs   = list(set([ choice(userrels) for i in range(3) ]))
        request.POST.add( 'user_id', str(u.id) )
        [ request.POST.add( 'user_relation_id', str(ur.id) ) for ur in rmurs ]
        [ userrels.remove( ur ) for ur in rmurs ]
        vf.process( request, c )
        assert_equal( sorted( userrels ),
                      sorted( userscomp.get_userrel() ),
                      'Mismatch in removing user relations' )

    def test_E_userrelations_invalid( self ) :
        """Testing FormUserRelations with invalid input"""
        log.info( "Testing FormUserRelations with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        # Without `user_id`
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'adduserrels' )
        assert_raises( ZetaFormError, vf.process, request, c )

        u       = choice( userscomp.get_user() )
        userrels= userscomp.get_userrel()

        # Try creating existing relation
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'adduserrels' )
        u        = choice([ u for u in userscomp.get_user() if u.userconnections ])
        ur       = choice( u.userconnections )
        userfrom = u
        userto   = ur.userto
        reltype  = ur.userreltype
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'userrel_type', reltype.userrel_type )
        request.POST.add( 'userfrom', userfrom.username )
        request.POST.add( 'userto', userto.username )
        vf.process( request, c )
        newur = [ ur1 for ur1 in userscomp.get_userrel()
                     if ur1.userfrom == userfrom
                     if ur1.userto == userto
                     if ur1.userreltype == reltype ]
        assert_true( len(newur) == 1,
                     'Mismatch while re-creating user relation, more than one ur' )
        assert_equal( ur, newur[0],
                     'Mismatch in re-creating user relation' )

    def test_F_inviteuser( self ) :
        """Testing FormInviteUser with valid input"""
        log.info( "Testing FormInviteUser with valid input" )

        # Setup mail-db
        mdb     = MailDB( config )
        assert_true( mdb.Session, "Mismatch, Session is false" )
        mdb.deldomains( mdb.listdomains() )
        [ mdb.deluser( e ) for e, p in mdb.listusers() ]

        mdb.adddomains( 'virtual.test' )
        mdb.adddomains( 'example.com' )
        mdb.adduser( config, 'pratap@virtual.test', 'pratap123' )
        mdb.adduser( config, 'sales@example.com', 'password' )

        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        environ     = { 'HTTP_HOST'   : 'sandbox.devwhiz.net',
                        'SCRIPT_NAME' : '/mount'
                      }
        request.environ = environ
        c.sysentries = syscomp.get_sysentry()
        
        u = choice( userscomp.get_user() )

        # Invite user
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'inviteuser' )

        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'emailid', u'prataprc@gmail.com' )
        vf.process( request, c, defer=False, formnames=['inviteuser'],
                    environ=environ )

        self._validate_defer(
                u.id, False, c,
                lambda u : 'Invited user' in u.logs[-1].log
        )

        # Cleanup db
        mdb     = MailDB( config )
        mdb.deldomains( mdb.listdomains() )
        [ mdb.deluser( e ) for e, p in mdb.listusers() ]

    def test_G_resetpass( self ) :
        """Testing FormResetPass with valid input"""
        log.info( "Testing FormResetPass with valid input" )

        # Setup mail-db
        mdb     = MailDB( config )
        assert_true( mdb.Session, "Mismatch, Session is false" )
        mdb.deldomains( mdb.listdomains() )
        [ mdb.deluser( e ) for e, p in mdb.listusers() ]

        mdb.adddomains( 'virtual.test' )
        mdb.adddomains( 'example.com' )
        mdb.adduser( config, 'pratap@virtual.test', 'pratap123' )
        mdb.adduser( config, 'sales@example.com', 'password' )

        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.rclose    = h.ZResp()

        u = choice( userscomp.get_user() )

        # Try adding invalid perm_group
        passwd = 'newpass123'
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'resetpass' )
        request.POST.add( 'confpass', passwd )
        request.POST.add( 'password', passwd )
    
        defer = choice([True, False])
        vf.process( request, c, defer=defer, emailid=u.emailid,
                    formnames=['resetpass'] )
        self._validate_defer(
                u.id, defer, c,
                lambda u : 'updated user preference' in u.logs[-1].log
        )

        assert_equal( u.password, sha1( passwd ).hexdigest(),
                      'Mismatch in resetting password' )

        # Cleanup db
        mdb     = MailDB( config )
        mdb.deldomains( mdb.listdomains() )
        [ mdb.deluser( e ) for e, p in mdb.listusers() ]

