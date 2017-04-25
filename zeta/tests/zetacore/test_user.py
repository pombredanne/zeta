# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# Note :
#   1. The sorting done by mysql is different from `sorted()` buildin function.

import logging
import sys
import os
from   os.path                      import join, isdir, basename
import random
from   random                       import choice, randint
from   hashlib                      import sha1

import pylons.test
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true
from   paste.util.import_string     import eval_import

from   zeta.auth.perm               import permissions
import zeta.auth.perm               as permmod
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaUserError
from   zeta.comp.attach             import AttachComponent
from   zeta.tests                   import *
from   zeta.tests.model.generate    import gen_usercontent, gen_userrelations
from   zeta.tests.tlib              import *

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None
no_of_users = 20
no_of_relations = 4
g_byuser = u'admin'
ctxt    = { 'strictauth' : choice(['True', 'False']) }

userdata    = []
userreldata = []
compmgr     = None
userscomp   = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    global userdata, userreldata, compmgr, userscomp, seed, cachemgr

    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )
    info = "   Creating models (module-level) ... "
    log.info( info )
    print info
    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    # init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )

    compmgr     = config['compmgr']
    userscomp   = config['userscomp']
    userreltypes= userscomp.reltypes
    userdata    = gen_usercontent( no_of_users=no_of_users, seed=seed )
    userreldata = gen_userrelations( userdata.keys(),
                                     userreltypes,
                                     no_of_relations=no_of_relations,
                                     seed=seed
                                   )
    for username in userdata :
        userdata[username]['userrels'] = userreldata[username]

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


class TestUsers( object ) :

    _get_user    = lambda self, username : userscomp.get_user(username.lower())
    _normdbusers = lambda self, dbusernames : \
                    ( u'admin' in dbusernames and dbusernames.remove(u'admin'),
                      u'anonymous' in dbusernames and dbusernames.remove(u'anonymous') )
    _normdbemail = lambda self, dbemails : \
                    ( ADMIN_EMAIL in dbemails and dbemails.remove( ADMIN_EMAIL ),
                      ANONYMOUS_EMAIL in dbemails and dbemails.remove( ANONYMOUS_EMAIL ))

    def _validate_user( self, userdata ) :
        """Validate the user fields between the database and the generated
        one."""
        for username in userdata :
            d        = userdata[username]
            u        = userscomp.get_user( username )
            reffields= [ d['username'], d['emailid'], d['passdigest'],
                         d['timezone'] ]
            dbfields = [ u.username, u.emailid, str(u.password), u.timezone ]
            assert_equal( dbfields, reffields, 'Mismatch in user fields' )
            uinfo    = u.userinfo
            reffields= [ d['firstname'], d['middlename'], d['lastname'],
                         d['addressline1'], d['addressline2'], d['city'],
                         d['pincode'], d['state'], d['country'], d['userpanes']
                       ]
            dbfields = [ uinfo.firstname, uinfo.middlename, uinfo.lastname,
                         uinfo.addressline1, uinfo.addressline2, uinfo.city, uinfo.pincode,
                         uinfo.state, uinfo.country, uinfo.userpanes ]
            assert_equal( dbfields, reffields, 'Mismatch in user info fields' )

    def _validate_userattach( self, userdata ) :
        """Validate the user attachments between the database and the
        generated one."""
        for username in userdata :
            d     = userdata[username]
            u     = userscomp.get_user( username )
            assert_equal( os.path.basename( d['photofile'] ),
                          u.photofile.filename, 'Mismatch in user photo' )
            assert_equal( os.path.basename( d['iconfile'] ),
                          u.iconfile.filename, 'Mismatch in user icon' )

    def _validate_userperms( self, userdata ) :
        """Validate the user permissions between the database and the
        generated one."""
        for username in userdata :
            d = userdata[username]
            u = userscomp.get_user( username )
            assert_equal( sorted(d['perm_groups']),
                          sorted([ pg.perm_group for pg in u.permgroups ]),
                          'Mismatch in user permission groups' )

    def _validate_userdisable( self, userdata ) :
        """Validate the user disable status between the database and the
        generated one."""
        for username in userdata :
            d     = userdata[username]
            u     = userscomp.get_user( username )
            assert_equal( d['disabled'], u.disabled, 
                          'Mismatch in user disabled' )

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

    def test_A_usercreate( self ) :
        """Testing user creation"""
        log.info( "Testing user creation ..." )
        c = ContextObject()
        config['c'] = c

        usernames  = []
        for username in userdata :
            c.rclose = h.ZResp()
            d = userdata[username]
            u = [ username.lower(), d['emailid'], d['password'], d['timezone'] ]
            uinfo = [ d['firstname'], d['middlename'], d['lastname'],
                      d['addressline1'], d['addressline2'], d['city'], 
                      d['pincode'], d['state'], d['country'], d['userpanes'] ]
            defer = choice([True, False])
            uobj = userscomp.user_create( u, uinfo, c=c, defer=defer )
            self._validate_defer( uobj, defer, c, lambda u :len(u.logs) == 2 )
            assert_equal( [ pn.perm_name
                            for pg in uobj.permgroups for pn in pg.perm_names ],
                          permmod.default_siteperms,
                          'Mismatch, default_siteperms not created' )

            d['passdigest'] = sha1( d['password'] ).hexdigest()
            d['id'] = uobj
            usernames.append( username.lower() )
        dbusernames = [ u.username for u in userscomp.get_user() ]
        self._normdbusers(dbusernames)
        self._validate_user( userdata )

    def test_B_photoicon( self ) :
        """Testing user photo and icon methods"""
        log.info( "Testing user photo and icon methods ..." )
        c = ContextObject()
        config['c'] = c

        attachcomp = AttachComponent( config['compmgr'] )
        for username in userdata :
            d         = userdata[username]
            user      = userscomp.get_user( username.lower() )
            photofile = d['photofile']
            photo     = None

            # Photo file api
            c.rclose = h.ZResp()
            defer = choice([True, False])
            if photofile :
                photo = attachcomp.create_attach(
                            os.path.basename( photofile ),
                            fdfile=open( photofile, 'r' ),
                            uploader=user
                        )
                userscomp.user_set_photo(
                            choice([ user, user.username, user.id ]),
                            photo,
                            c=c, defer=defer
                )
                self._validate_defer(
                        user, defer, c, 
                        lambda u : 'uploaded user photo' in u.logs[-1].log 
                )

            # Icon file api
            c.rclose = h.ZResp()
            defer = choice([True, False])
            iconfile = d['iconfile']
            icon     = None
            if iconfile :
                icon  = attachcomp.create_attach(
                            os.path.basename( iconfile ),
                            fdfile=open( iconfile, 'r' ),
                            uploader=username
                        )
                userscomp.user_set_icon(
                            choice([ user, user.username, user.id ]),
                            icon,
                            c=c, defer=defer
                )
                self._validate_defer(
                        user, defer, c, 
                        lambda u : 'uploaded user icon' in u.logs[-1].log,
                )

            # Delete photo or icon
            c.rclose = h.ZResp()
            defer = choice([True, False])
            update = choice([ True, False ]) # Randomly update
            if update :
                userscomp.user_set_photo( user, photo=None, c=c, defer=defer )
                userscomp.user_set_icon( user, icon=None, c=c, defer=defer )
                d['photofile'] = photofile = None
                d['iconfile'] = iconfile = None

                # _validate_defer
                defer and c.rclose.close()
                user = userscomp.get_user( user.id, attrload=[ 'logs' ] )
                if iconfile :
                    assert_true( 'removed user icon' in user.logs[-1].log,
                                 'Mismatch in defer' )
                if photofile :
                    assert_true( 'removed user photo' in user.logs[-2].log,
                                 'Mismatch in defer' )

            if photofile :
                assert_equal( user.photofile.filename,
                              os.path.basename( photofile ),
                              'Mismatching photo file name'
                            )
                a, content = attachcomp.downloadattach(user.photofile)
                assert_equal( str(content), open( photofile, 'r' ).read(),
                              'Mismatch in user photo attachment'
                            )
            if iconfile :
                assert_equal( user.iconfile.filename,
                              os.path.basename( iconfile ),
                              'Mismatching icon file name'
                            )
                a, content = attachcomp.downloadattach(user.iconfile)
                assert_equal( str( content ), open( iconfile ).read(),
                              'Mismatch in user icon attachment'
                            )
        self._validate_user( userdata )

    def test_C_userupdate( self ) :
        """Testing updation of user entries"""
        log.info( "Testing updation of user entries ..." )
        # Use the following data to update user entries.
        udata      = {
                        'emailid'   : u'update.email@test.com',
                        'password'  : u'newpass123',
                        'timezone'  : u'UTC'
                     }
        uinfodata  = {
                        'firstname' : u'updatefname',
                        'middlename'    : u'updatemname',
                        'lastname'      : u'updatelname', 
                        'addressline1'  : u'updateaddrline1',
                        'addressline2'  : u'updateaddrline2',
                        'city'          : u'updatecity',
                        'pincode'       : u'pincode',
                        'state'         : u'updatestate',
                        'country'       : u'updatecountry',
                        'userpanes'     : u'projects,wikis,tickets',
                    }
        for username in userdata :
            d = userdata[username]
            # Update / remove user entries and fields.
            if choice([True,False,False]) :
                ukey  = choice(udata.keys())
                uikey = choice(uinfodata.keys())
                d[ukey]  = udata[ukey] + username
                d[uikey] = uinfodata[uikey]
                u        = [ username.lower(), d['emailid'], d['password'], 
                             d['timezone'] ]
                uinfo    = [ d['firstname'], d['middlename'], d['lastname'],
                             d['addressline1'], d['addressline2'], d['city'], 
                             d['pincode'], d['state'], d['country'],
                             d['userpanes'] ]
                userscomp.user_create( u, uinfo, update=True )
                d['passdigest'] = sha1( d['password'] ).hexdigest()

        self._validate_user( userdata )

    def test_D_userpermissions( self ) :
        """Testing user permission methods"""
        log.info( "Testing user permission methods ..." )
        c = ContextObject()
        config['c'] = c

        for username in userdata :
            c.rclose = h.ZResp()
            d = userdata[username]
            d['perm_groups'] = list(set(
                d['perm_groups'] + [
                    userscomp.get_permgroup(pg).perm_group
                    for pg in permmod.default_siteperms ]
            ))
            perm_groups = d['perm_groups']

            defer = choice([True, False])

            # Add permissions from user
            userscomp.user_add_permgroup( username, perm_groups, c=c,
                                          defer=defer, byuser=g_byuser
                                        )
            if perm_groups :
                self._validate_defer(
                    g_byuser, defer, c, 
                    lambda u : 'added permission groups' in u.logs[-1].log and \
                               username in u.logs[-1].log
                )

            # Remove permissions from user
            rmpg = [ perm_groups.pop( perm_groups.index(pg) )
                     for pg in perm_groups if choice([True,False,False]) ]
            userscomp.user_remove_permgroup( username, rmpg, c=c, defer=defer,
                                             byuser=g_byuser )
            if rmpg :
                self._validate_defer(
                    g_byuser, defer, c, 
                    lambda u : 'deleted permission groups' in u.logs[-1].log and \
                               username in u.logs[-1].log
                )

        self._validate_user( userdata )
        self._validate_userperms( userdata )

    def test_E_userrelation( self ) :
        """Testing user relation methods"""
        log.info( "Testing user relation methods ..." )
        for username in userdata :
            d    = userdata[username]
            urel = d['userrels']
            # Create / Add user relation entries and fields.
            for i in range(len(urel)) : # urel is list of list
                drel         = urel[i]
                userto       = drel['userto']
                relationtype = drel['userrel_type']
                approve      = drel['approved']
                ur = userscomp.user_add_relation( username, userto,
                                                  relationtype, byuser=username )
                approve and userscomp.user_approve_relation(
                                    choice([ ur, ur.id ]), byuser=ur.userto )
                drel['id'] = ur

                # Update user relation entries and fields.
                if approve and choice([True,False,False]) :
                    drel['approved'] = False
                    userscomp.user_approve_relation(
                                    ur.id, approve=False, byuser=ur.userto )
            # Remove user relation entries.
            rmurs = [ ( urel[i], urel[i]['id'].id )
                      for i in range(len(urel)) if choice([True,False,False]) ]
            for ur, ur_id in rmurs :
                userscomp.user_remove_relation( ur_id, byuser=username )
                urel.remove( ur )
        self._validate_user( userdata )
        self._validate_userperms( userdata )
        # Note : User relationship will be validated for get_connections()
        # testcase.

    def test_F_existence( self ) :
        """Testing user and user related existence methods"""
        log.info( "Testing user and user related existence method ..." )
        pg2pn = lambda pgroups : [ p.perm_name for pg in pgroups
                                               for p in pg.perm_names ]
        for username in userdata :
            d           = userdata[username]
            user        = userscomp.get_user( username )
            u           = choice([ username, user, user.id ])
            password    = d['password']
            perm_groups = [ userscomp.get_permgroup( pg ) 
                            for pg in d['perm_groups'] ]
            assert_true( userscomp.user_exists( u ),
                         'User `%s` does not exists' % username )
            assert_true( userscomp.user_has_password( u, password ),
                         'User `%s` password `%s` does not match' % \
                                 ( username, password )
                       )
            assert_true( userscomp.user_has_permnames(
                                    u, pg2pn( perm_groups ), checkall=True ),
                         'Mismatch in user_has_permnames' 
                       )
            assert_true( userscomp.user_has_permgroups(
                                    u,
                                    [ pg.perm_group for pg in perm_groups ],
                                    all=True ),
                         'Mismatch in user_has_permgroups' 
                       )

    def test_G_listing( self ) :
        """Testing list methods"""
        log.info( "Testing list methods ..." )
        usernames = map( lambda i : i.lower(), userdata.keys() )
        emails    = [ userdata[username]['emailid'] for username in userdata ]
        dbusers   = userscomp.list_users()
        self._normdbusers( dbusers )
        dbemails  = userscomp.list_emailids()
        self._normdbemail( dbemails )
        assert_equal( sorted(usernames),
                      dbusers,
                      'Mismatch in listing usernames'
                    )
        assert_equal( sorted(emails),
                      sorted(dbemails),
                      'Mismatch in listing user emailids'
                    )

    def test_H_getrelations( self ) :
        """Testing get_userrel_type() method"""
        log.info( "Testing get_userrel_type() methods ..." )
        # Test getting relation types.
        relnames = config['zeta.userrel_types']
        rels     = [ userscomp.get_userrel_type( r ) for r in relnames ]
        assert_equal( sorted(relnames),
                      sorted([ r.userrel_type for r in rels ]),
                      'Mismatch in user relation types'
                    )
        assert_equal( sorted(rels),
                      sorted([ userscomp.get_userrel_type( r ) for r in rels ]),
                      'Mismatch in get_userrel_type() passing ' + \
                      'UserRelation_type instances'
                    )
        assert_equal( sorted(rels),
                      sorted([ userscomp.get_userrel_type( r.id ) 
                                                        for r in rels ]),
                      'Mismatch in get_userrel_type() passing ' + \
                      'userrelation_type id'
                    )
        assert_equal( sorted(rels),
                      sorted([ userscomp.get_userrel_type( r.userrel_type ) 
                                                        for r in rels ]),
                      'Mismatch in get_userrel_type() passing ' + \
                      'userrel_type name'
                    )

    def test_I_getuser( self ) :
        """Testing get_user() method"""
        log.info( "Testing get_user() method ..." )
        usernames = map( lambda i : i.lower(), userdata.keys() )
        users     = userscomp.get_user()
        dbusers   = [ userscomp.get_user( u ) for u in usernames ]
        assert_equal( sorted(usernames),
                      sorted([ u.username for u in dbusers ]),
                      'Mismatch in usernames'
                    )
        dbusers   = [ userscomp.get_user( u.username ).username for u in users ]
        self._normdbusers(dbusers)
        assert_equal( sorted(usernames),
                      sorted(dbusers),
                      'Mismatch in usernames obtained by passing username'
                    )
        dbusers   = [ userscomp.get_user( u.id ).username for u in users ]
        self._normdbusers(dbusers)
        assert_equal( sorted(usernames),
                      sorted(dbusers),
                      'Mismatch in usernames obtained by passing id'
                    )
        dbusers   = [ userscomp.get_user( u ).username for u in users ]
        self._normdbusers(dbusers)
        assert_equal( sorted(usernames),
                      sorted(dbusers),
                      'Mismatch in usernames obtained by passing User instance'
                    )

    def test_J_getuserrel( self ) :
        """Testing get_userrel() method"""
        log.info( "Testing get_userrel method ..." )
        userto = {}
        for username in userdata :
            urel     = userdata[username]['userrels']
            userfrom = self._get_user( username )
            dbuserto = []
            [ dbuserto.extend(
                        userscomp.get_userrel( userfrom=userfrom,
                                               userto=item['userto'] )
              ) for item in urel ]
            [ userto.setdefault( item['userto'], [] ).extend(
                userscomp.get_userrel( userfrom=userfrom,
                                       userto=item['userto'],
                                       reltype=item['userrel_type'])
              ) for item in urel ]
            assert_equal( set(userscomp.get_userrel( userfrom=userfrom )),
                          set(dbuserto),
                          'Mismatch in get_userrel() for userfrom'
                        )
        for username in userto :
            assert_equal( set(userscomp.get_userrel( userto=username )),
                          set(userto[username]),
                          'Mismatch in get_userrel() for userto'
                        )

    def test_K_getconnections( self ) :
        """Testing get_connections() method"""
        log.info( "Testing get_connections() creation ..." )
        reltypes     = [ r.userrel_type for r in userscomp.get_userrel_type() ]
        allpotrels   = [ ( u.username, type ) for u in userscomp.get_user()
                                              for type in reltypes ]
        alltourels   = []
        allfromurels = []
        for username in userdata :
            d = userdata[username]
            touserrels, fromuserrels, potrels = userscomp.get_connections(
                                                    self._get_user( username )
                                                )
            [ alltourels.append( list(tup) + [type] )
                        for type in touserrels for tup in touserrels[type] ]
            [ allfromurels.append( list(tup) + [type] )
                        for type in fromuserrels for tup in fromuserrels[type] ]
            urel         = d['userrels']
            dbtouserrels = [ ( tup[0], type, tup[2] )
                             for type in touserrels for tup in touserrels[type]]
            touserrels_l = [ ( item['userto'], item['userrel_type'],
                               item['approved'] 
                             ) for item in urel ]
            assert_equal( sorted(touserrels_l),
                          sorted(dbtouserrels),
                          'Mismatch in touserrels from get_connections()'
                        )
            dbpotrels    = [ (uname, type)
                             for type in potrels for uname in potrels[type]]
            potrels_l    = allpotrels[:]
            [ potrels_l.remove(( item['userto'], item['userrel_type'] ))
                    for item in urel ]
            assert_equal( sorted(potrels_l),
                          sorted(dbpotrels),
                          'Mismatch in potrels from get_connections()'
                        )
        alltourels   = sorted( alltourels, key=lambda x : x[1] )
        allfromurels = sorted( allfromurels, key=lambda x : x[1] )
        assert_equal( len(alltourels), len(allfromurels),
                      'Mismatch in merged `alltourels` and `allfromurels`' )
        assert_equal( [ (t[1], t[2], t[3]) for t in alltourels ],
                      [ (f[1], f[2], f[3]) for f in allfromurels ],
                      'Mismatch in `alltourels` and `allfromurels`'
                    )
        for t, f in zip( alltourels, allfromurels ) :
            ur = userscomp.get_userrel( userrelation=t[1] )
            assert_equal( ur.userto.username, t[0],
                          'Mismatch in userto.username' )
            assert_equal( ur.userfrom.username, f[0],
                          'Mismatch in userto.username' )

    def test_L_removeuser( self ) :
        """Testing user remove methods"""
        log.info( "Testing user remove methods ..." )
        pass

    def test_M_misc( self ) :
        """Testing miscellaneous methods"""
        log.info( "Testing miscellaneous methods ..." )
        c = ContextObject()
        config['c'] = c

        for username in userdata :
            c.rclose = h.ZResp()
            d = userdata[username]
            disable = d['disabled']
            if disable :
                defer = choice([True, False])
                userscomp.user_disable( username, c=c, defer=defer, byuser=g_byuser )
                self._validate_defer(
                    g_byuser, defer, c,
                    lambda u : 'disabled users' in u.logs[-1].log and \
                               username in u.logs[-1].log
                )

                if choice([True,False]) :
                    d['disabled'] = False
                    userscomp.user_disable(
                            username, disable=False,c=c, defer=defer,
                            byuser=g_byuser )
                    self._validate_defer(
                        g_byuser, defer, c,
                        lambda u : 'enabled users' in u.logs[-1].log and \
                                   username in u.logs[-1].log
                    )

        for username in userdata :
            d    = userdata[username]
            user = userscomp.get_user( username )
            assert_equal( user.disabled, d['disabled'],
                          'Mismatch in disabled users' )
            assert_equal( d['passdigest'], str(userscomp.user_password( username )),
                          'Mismatch in `user_password()` method' )

    def test_N_properties( self ) :
        """Testing userscomp properties"""
        log.info( "Testing usercomp properties ..." )
        disusernames = []
        enusernames = []
        usernames    = []
        for username in userdata :
            d       = userdata[username]
            disable = d['disabled']
            disable and disusernames.append( username )
            not disable and enusernames.append( username )
            usernames.append( username )

        dbusers = userscomp.userstatus['enabled'][:]
        self._normdbusers( dbusers )
        assert_equal( sorted(enusernames),
                      sorted(dbusers),
                      'Mismatch in `userstatus(enabled)` property'
                    )

        dbusers = userscomp.userstatus['disabled'][:]
        self._normdbusers( dbusers )
        assert_equal( sorted(disusernames),
                      sorted(dbusers),
                      'Mismatch in `userstatus(disabled)` property'
                    )

        dbusers = userscomp.usernames[:]
        self._normdbusers( dbusers )
        assert_equal( sorted(usernames),
                      sorted(dbusers),
                      'Mismatch in `usernames` property'
                    )
        assert_equal( sorted(config['zeta.userrel_types']),
                      sorted(userscomp.reltypes),
                      'Mismatch in `reltypes` property'
                    )
        ref_projpnames = []
        ref_sitepnames = []
        for aplist in permissions.values() :
            for ap in aplist :
                if ap.project :
                    ref_projpnames.append( ap.perm_name )
                else :
                    ref_sitepnames.append( ap.perm_name )
        assert_equal( sorted( userscomp.site_permnames ),
                      sorted( ref_sitepnames ),
                      'Mismatch in "site_permnames" property'
                    )
        assert_equal( sorted( userscomp.proj_permnames ),
                      sorted( ref_projpnames ),
                      'Mismatch in "proj_permnames" property'
                    )

    def test_O_userrelationtypes( self ) :
        """Testing creation of user relation types"""
        log.info( "Testing creation of user relation types ..." )
        ref_reltypes = userscomp.reltypes
        add_reltypes = [ u'reltype1', u'reltype2' ]
        ref_reltypes += add_reltypes
        userscomp.userreltype_create( add_reltypes, byuser=g_byuser )
        assert_equal( sorted(ref_reltypes), userscomp.reltypes,
                      'Mismatch in creating relation types as list' )

        add_reltypes = u'reltype3'
        ref_reltypes += [ add_reltypes ]
        userscomp.userreltype_create( add_reltypes, g_byuser )
        assert_equal( sorted(ref_reltypes), userscomp.reltypes,
                      'Mismatch in creating relation types as string' )

    def test_P_datacruchers( self ) :
        """Testing data crunching methods"""
        log.info( "Testint data crunching methods" )

        users = userscomp.get_user()
        # Testing projectnames() method
        for u in users :
            u = userscomp.get_user( u.id, attrload=[ 'adminprojects' ],
                                          attrload_all=[ 'projectteams.project' ]
                                  )
            assert_equal( userscomp.projectnames( u ),
                          userscomp.projectnames(choice([ u.id, u.username ])),
                          'Mismatch in projectnames() method'
                        )

        # Testing userbyemailid() method
        for u in users :
            assert_equal( u.username,
                          userscomp.userbyemailid( u.emailid ).username,
                          'Mismatch in userbyemailid() method'
                        )

    def test_Q_userinvitation( self ) :
        """Testing user invitation methods"""
        log.info( "Testing user invitation methods" )

        users    = userscomp.get_user()

        # Testing inviteuser()
        user    = choice( users )
        emailid = u'email@domain.com'
        userscomp.inviteuser( user, emailid )

        uinvs   = userscomp.get_invitation()
        assert_equal( len(uinvs), 1, 'Mismatch in user invitation' )
        assert_equal( uinvs[0].emailid, emailid,
                      'Mismatch in `emailid` for userinvitation' )
        assert_equal( uinvs[0].byuser.username, user.username,
                      'Mismatch in `byuser` for userinvitation' )

        # Testing invbydigest()
        assert_equal( userscomp.invbydigest( uinvs[0].digest ),
                      uinvs[0],
                      'Mismatch for invbydigest() method'
                    )

        # Testing acceptedby()
        acceptuser = choice( users )
        userscomp.acceptedby( acceptuser, uinvs[0] )
        uinv = userscomp.get_invitation( uinvs[0].id )
        assert_equal( uinv.acceptedby, acceptuser.username,
                      'Mismatch in acceptedby() method' )

    def test_R_user_permnames( self ) :
        """Testing creation of user permission names"""
        log.info( "Testing creation of user permission names ..." )

        users     = userscomp.get_user()
        user      = choice( users )
        upnames   = userscomp.user_permnames( user )
        refpnames = [ pn.perm_name 
                      for pg in user.permgroups for pn in pg.perm_names ]
        assert_equal( sorted(refpnames), sorted(upnames),
                      'Mismatch in user permission names' )

