# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os.path                      import join, isdir, basename
import random
from   random                       import choice, randint

import pylons.test
from   pylons                       import tmpl_context as c
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true
from   nose.plugins.attrib          import attr
from   multigate                    import PermissionError, PermissionSetupError, \
                                           NotAuthenticatedError, NotAuthorizedError
from   paste.util.import_string     import eval_import

from   zeta.tests                   import *
from   zeta.tests.model.generate    import gen_pgroups
from   zeta.tests.model.populate    import pop_user, pop_licenses, pop_projects
from   zeta.tests.tlib              import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
import zeta.lib.cache               as cache
from   zeta.lib.constants           import LEN_NAME
from   zeta.lib.error               import *
from   zeta.auth.perm               import *
import zeta.auth.perm               as permmod
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.system             import SystemComponent

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
g_byuser        = u'admin'
permission_data = []
compmgr         = None
syscomp         = None
userscomp       = None
projcomp        = None
no_of_users     = 20
no_of_relations = 5
no_of_projects  = 2
no_of_tags      = 2
no_of_attachs   = 1

cachemgr= None
cachedir= '/tmp/testcache'
ctxt    = { 'strictauth' : choice(['True', 'False']) }

def setUpModule() :
    global compmgr, syscomp, userscomp, projcomp, permission_data, seed, cachemgr

    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )
    info = "   Creating models ..."
    log.info( info )
    print info

    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    # init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )
    print "   Generating data ..."
    permission_data = gen_pgroups( seed=seed )
    compmgr         = config['compmgr']
    userscomp       = config['userscomp']
    projcomp        = ProjectComponent( compmgr )
    syscomp         = SystemComponent( compmgr )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    print "   Populating licenses ( no_of_tags=%s, no_of_attachs=%s ) ..." % \
                ( no_of_tags, no_of_attachs )
    pop_licenses( no_of_tags, no_of_attachs, seed=seed )
    print "   Populating projects ( no_of_projects=%s ) ..." % no_of_projects
    pop_projects( no_of_projects, no_of_tags, no_of_attachs, seed=seed )

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
    info = "   Deleting models ... "
    log.info( info )
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )


class App( object ) :
    def __init__( self, *args, **kwargs ):
        pass


class TestPerm( object ) :

    def _validate_permissions( self ) :
        permnames  = sorted([ p.perm_name for p in  userscomp.get_permname() ])
        permgroups = sorted([ pg.perm_group
                              for pg in userscomp.get_permgroup() ])
        assert_equal( sorted(permnames),
                      sorted([ pg[7:].upper()
                               for pg in permgroups if pg[:7] == 'defgrp_' ]),
                      'Mismatch in permission validation'
                    )

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

    def test_1_permissions( self ) :
        """Testing Zeta Permissions"""
        log.info( "Testing Zeta Permissions ..." )
        zetaperms = []
        [ zetaperms.append( p.perm_name )
                for plist in permissions.values() for p in plist ]
        assert_equal( sorted( zetaperms ),
                      sorted([ p.perm_name for p in userscomp.get_permname() ]),
                      "Zeta permissions does not match the permission names " +\
                      "defined in the database"
                    )
        permnames = userscomp.get_permname()
        assert_equal( sorted( zetaperms ),
                      sorted([ userscomp.get_permname(
                                        choice([ p, p.id, p.perm_name ])
                               ).perm_name 
                               for p in permnames ]),
                      'Mismatch in get_permname()'
                    )
        assert_equal( sorted( userscomp.list_permnames() ),
                      sorted([ p.perm_name for p in permnames ]),
                      'Mismatch in list_permnames()'
                    )

        self._validate_permissions()

        [ assert_true( userscomp.permname_exists( p.perm_name ))
          for p in permnames ]

    def test_2_basicpermgroups( self ) :
        """Testing Zeta PermissionGroups"""
        log.info( "Testing Zeta PermissionGroups ..." )
        for permname in userscomp.get_permname() :
            pg = 'defgrp_' + permname.perm_name.lower()
            pg = userscomp.get_permgroup( pg )
            assert_equal( pg.perm_names, [ permname ],
                'Permission name and its `defgrp_` does not match' + \
                '`%s` and `%s`' % ( pg, permname )
            )
        pgroups = userscomp.get_permgroup()
        assert_equal( sorted([ pg.perm_group for pg in pgroups ]),
                      sorted([ userscomp.get_permgroup(
                                        choice([ pg, pg.id, pg.perm_group ])
                               ).perm_group 
                               for pg in pgroups ]),
                      'Mismatch in get_permgroup()'
                    )
        self._validate_permissions()
        
        [ assert_true( userscomp.permgroup_exists( pg.perm_group ))
          for pg in pgroups ]
    
    def test_3_pgroups( self ) :
        """Testing PermissionGroup creation"""
        log.info( "Testing PermissionGroup creation ..." )
        pgroups      = sorted( [ pg for pg in permission_data ] + \
                               userscomp.mappedpgroups )
        for perm_group in permission_data :
            permnames = permission_data[perm_group]
            # Randomize perm_name selection id.
            permnames_rand = [ choice([p, p.perm_name, p.id ])
                               for p in permnames ]
            # Create PermGroup and add permission names
            pg = userscomp.create_permgroup(
                        perm_group, defer=choice([True, False ]),
                        byuser=g_byuser
                 )
            userscomp.add_permnames_togroup(
                        choice([pg, pg.id, pg.perm_group]),
                        permnames_rand,
                        defer=choice([True, False]),
                        byuser=g_byuser
            )

            # Randomly Remove PermNames
            rmpn = [ permnames.pop( permnames.index(choice(permnames)) )
                     for i in range(len(permnames) / 2 ) ]
            userscomp.remove_permnames_fromgroup(
                        choice([pg, pg.id, pg.perm_group]), rmpn,
                        defer=choice([True, False]),
                        byuser=g_byuser
            )

            # Validate deferred post processing, actually in this test case
            # even if defer is set to `True`, post processing will happen
            # immediately because `rclose` is not available in the context.
            user = userscomp.get_user( g_byuser, attrload=['logs'] )
            idx = -1
            if rmpn :
                assert_true( 'deleted permnames from permgroup' in user.logs[idx].log,
                             'Mismatch in defer' )
                idx = idx-1 
            if permnames_rand :
                assert_true( 'added permnames to permgroup' in user.logs[idx].log,
                             'Mismatch in defer' )
                idx = idx-1
            assert_true( 'created new permission group' in user.logs[idx].log,
                         'Mismatch in defer' )

            assert_equal( pg.perm_names, permnames,
                          'Permission Names after addition and removals does not match ...' )

        oldgroupname = choice( userscomp.custompgroups )
        pg = userscomp.get_permgroup( oldgroupname )
        userscomp.change_permgroup( pg, 'newgroupname',
                                    defer=choice([True, False]),
                                    byuser=g_byuser
                                  )

        # Validate deferred post processing.
        user = userscomp.get_user( g_byuser, attrload=['logs'] )
        assert_true( 'changed permission group name to' in user.logs[-1].log,
                     'Mismatch in defer' )

        assert_true( 'newgroupname' in userscomp.list_permgroups(),
                     'Mismatch in change_permgroup not matching the new name' )
        assert_false( oldgroupname in userscomp.list_permgroups(),
                      'Mismatch in change_permgroup not matching the old name' )
        self._validate_permissions()

    def test_4_rmpgroups( self ) :
        """Testing PermissionGroup removal"""
        log.info( "Testing PermissionGroup removal ..." )
        pgroups   = userscomp.get_permgroup()
        rmpg = []
        for pg in pgroups :
            if choice([True,True,False]) or pg.perm_group[:7] == 'defgrp_' :
                continue
            pgroups.remove(pg)
            rmpg.append( pg )

        if choice([ True, False ]) :
            [ userscomp.remove_permgroup(
                        choice([ pg.id, pg.perm_group, pg]),
                        defer=choice([True, False ]), byuser=g_byuser
              ) for pg in rmpg ]
        else :
            [ userscomp.remove_permgroup(
                 rmpg, defer=choice([ True , False ]), byuser=g_byuser )]

        if rmpg :
            user = userscomp.get_user( g_byuser, attrload=['logs'] )
            assert_true( 'deleted permission groups' in user.logs[-1].log,
                         'Mismatch in defer' )

        assert_equal( sorted([ pg.perm_group for pg in pgroups ]),
                      sorted(userscomp.list_permgroups()),
                      'Permission Groups mismatch after removing few groups ...'
                    )
        self._validate_permissions()

    def test_5_misc( self ) :
        """Testing miscellaneous"""
        log.info( "Testing miscellaneous ..." )
        # Normalizing the permission group names
        normgroups = userscomp.normalize_perms( userscomp.list_permgroups() )
        assert_equal( sorted(normgroups),
                      sorted(userscomp.mixedpnames),
                      'Mismatch between normalized permissions and`mixedpnames`.'
                    )
        # Data crunch method on user permission maps.
        updict = userscomp.userpermission_map()
        for u in updict :
            assert_equal( sorted( updict[u][0] + updict[u][1] ),
                          sorted( userscomp.site_permnames ),
                          'Mismatch in permissions that the user have and have not'
                        )
            user = userscomp.get_user( u )
            assert_equal( sorted([ userscomp.get_permgroup(pg)
                                   for pg in updict[u][0] ]),
                          sorted([ pg for pg in user.permgroups ]),
                          'Mismatch in permission groups assigned to user'
                        )

        # Data crunch method on user permission map, for a subset of user
        usernames = userscomp.usernames
        usernames = [ usernames.pop(0) for i in range(len(usernames)/4) ]
        updict    = userscomp.userpermission_map( usernames=usernames )
        assert_equal( sorted(usernames), sorted(updict.keys()),
                      'Mismatch in user permission map for selected user' )

        self._validate_permissions()

    def test_6_properties( self ) :
        """Testing properties"""
        log.info( "Testing properties ..." )
        zetaperms = []
        [ zetaperms.append( p.perm_name )
                for plist in permissions.values() for p in plist ]
        assert_equal( sorted(userscomp.perm_names), sorted(zetaperms),
                      '`perm_names` property does not match zeta-permissions'
                    )
        assert_equal( sorted(userscomp.perm_groups),
                      sorted(userscomp.list_permgroups()),
                      '`perm_groups` property does not match list_permgroups()'
                    )
        assert_equal( sorted(userscomp.mappedpgroups),
                      sorted([ 'defgrp_'+pn.lower()
                               for pn in userscomp.perm_names ]),
                      '`mappedpgroups` does not match' 
                    )
        assert_equal( sorted(userscomp.custompgroups),
                      sorted( set(userscomp.perm_groups).difference(
                                        userscomp.mappedpgroups
                              )),
                      '`custompgroups` does not match'
                    )
        pgmap = userscomp.pgmap
        assert_equal( sorted([ userscomp.get_permgroup( id ).perm_group
                               for id in pgmap.keys() ]), 
                      sorted( userscomp.custompgroups ),
                      'Mismatch in `pgmap` perm_groups' 
                    )
        for id in pgmap :
            assert_equal( sorted( userscomp.perm_names ),
                          sorted( pgmap[id][1] + pgmap[id][2] ),
                          'Mismatch in `pgmap` permission groups'
                        )
        self._validate_permissions()

        assert_equal( sorted(userscomp.proj_permnames),
                      sorted([ a.perm_name for c in permissions
                               for a in permissions[c] if a.project ]),
                      'Mismatch in proj_permnames'
                    )

        assert_equal( sorted(userscomp.site_permnames),
                      sorted([ a.perm_name for c in permissions
                               for a in permissions[c] if not a.project ]),
                      'Mismatch in site_permnames'
                    )
        

    def test_7_apppermissions( self ) :
        """Testing AppPermission class"""
        log.info( "Testing AppPermission class ..." )
        a = AppPermission( 'testcomp', 'SOME_PERM1' )
        assert_equal( a.comp, 'testcomp' )
        assert_equal( a.perm_name, 'SOME_PERM1' )
        assert_true( 'testcomp' in permissions )
        assert_equal( [ 'SOME_PERM1' ],
                      [ a.perm_name for a in permissions['testcomp'] ]
                    )
        a = AppPermission( 'testcomp', 'SOME_PERM2' )
        assert_equal( [ 'SOME_PERM1', 'SOME_PERM2' ],
                      [ a.perm_name for a in permissions['testcomp'] ]
                    )
        assert_raises( ZetaPermError, AppPermission, 'testcomp', 'SOME_PERM2' )
        permissions.pop( 'testcomp' )

    def test_8_pgroupsbytype( self ) :
        """Testing pgroupsbytype() method"""
        log.info( "Testing pgroupsbytype() method ..." )
        bytype = userscomp._pgroupsbytype()
        assert_equal( sorted([ pg for pg in bytype['mapped'] ]),
                      sorted(userscomp.mappedpgroups),
                      'Mismatch in mapped groups for pgroupsbytype'
                    )
        assert_equal( sorted([ pg for pg in bytype['custom'] ]),
                      sorted(userscomp.custompgroups),
                      'Mismatch in custom groups for pgroupsbytype'
                    )

    @attr(type='permclass')
    def test_9_userin( self ) :
        """Testing UserIn class"""
        log.info( "Testing UserIn class ..." )
        environ        = {  'REMOTE_USER' : None,
                         }

        start_response = None
        uin = UserIn([ 'user1' ])
        assert_raises( NotAuthorizedError, uin.check, App, environ,
                       start_response )

        environ['REMOTE_USER'] = 'user1'
        uin.check( App, environ, start_response )

        uin = UserIn([ 'user1', 'user2' ])
        uin.check( App, environ, start_response )

        environ['REMOTE_USER'] = 'user3'
        assert_raises( NotAuthorizedError, uin.check, App, environ, start_response )

    @attr(type='permclass')
    def test_A_haspermname( self ) :
        """Testing HasPermname class"""
        log.info( "Testing HasPermname class ..." )
        users      = userscomp.get_user()
        teamtypes  = projcomp.get_teamtype()
        teamtype   = choice( teamtypes )
        projects   = projcomp.get_project()
        project    = choice( projects )
        start_response = None

        projusers  = [ pt.user.username for pt in project.team ] + \
                     [ project.admin.username ]
        'admin' in projusers and projusers.remove( 'admin' )
        username   = choice( projusers )
        uteams     = projcomp.userinteams( project, username )
        teams      = projcomp.teamperms( project )
        pnames     = []
        [ pnames.extend( map( lambda x: x[1], teams[team][0] ) )
          for team in uteams ]
        x_pnames   = list(set(userscomp.perm_names).difference( set(pnames) ))
        # prune x_pnames from site permissions
        [ x_pnames.remove( pn )
          for pn in userscomp.site_permnames if pn in x_pnames ]

        environ = {}

        # Try for an invalid user
        environ['REMOTE_USER'] = u'invalid_user'
        hpn    = HasPermname( permnames=[], project=project )
        assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )

        # Try for anonymous user
        environ['REMOTE_USER'] = 'anonymous'
        hpn    = HasPermname( permnames=pnames, project=project, strict='True', all=True )
        assert_raises( NotAuthenticatedError, hpn.check, App, environ, start_response )

        # Try with mix of valid and invalid invalid permission name, to match
        # any permission
        environ['REMOTE_USER'] = username
        hpn    = HasPermname( permnames=pnames + [ 'INVALID_PERM' ],
                              project=project, strict='False', all=False )
        if pnames :
            hpn.check( App, environ, start_response )
        else :
            assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )

        # Try with mix of valid and invalid invalid permission name, to match
        # all permission
        hpn    = HasPermname( permnames=pnames + [ 'INVALID_PERM' ],
                              project=project, strict='False', all=True )
        assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )

        # Try with valid team permission names, matching all permissions.
        hpn    = HasPermname( permnames=pnames, project=project, strict='False', all=True )
        if pnames :
            hpn.check( App, environ, start_response )
        else :
            assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )

        # Try with valid and invalid team permission names, matching all
        # permissions 
        hpn    = HasPermname( permnames=pnames+x_pnames,
                              project=project, strict='False', all=True )
        if x_pnames :
            assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )
        else :
            hpn.check( App, environ, start_response )

        # Try with valid and invalid team permission names, matching any
        # permission
        hpn    = HasPermname( permnames=pnames+x_pnames,
                              project=project, strict='False', all=False )
        if pnames :
            hpn.check( App, environ, start_response )
        else :
            assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )

        ##### Site permissions
        user   = userscomp.get_user( username )
        spname = choice( userscomp.site_permnames )

        # Try with valid site permission names, matching all permissions.
        userscomp.user_add_permgroup( user, [ 'defgrp_'+spname.lower() ], byuser=g_byuser )
        hpn    = HasPermname( permnames=[ spname ], project=project, strict='False',
                              all=True )
        hpn.check( App, environ, start_response )

        userscomp.user_remove_permgroup( user, [ 'defgrp_'+spname.lower() ], byuser=g_byuser )
        hpn    = HasPermname( permnames=[ spname ], project=project, strict='False',
                              all=True )
        assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )

    #@attr(type='permclass')
    #def test_B_haspermgroup( self ) :
    #    """Testing HasPermgroup class"""
    #    log.info( "Testing HasPermgroup class ..." )
    #    users = userscomp.get_user()
    #    user  = choice( users )
    #    start_response = None
    #    permgroups = [ pg.perm_group for pg in user.permgroups ]
    #    x_pgroups = list(set(userscomp.perm_groups).difference(set(permgroups)))
    #    environ = {}

    #    environ['REMOTE_USER'] = u'invalid_user'
    #    pgroups = []
    #    hpg     = HasPermgroup( permgroups=[] )
    #    assert_raises( NotAuthorizedError, hpg.check, App, environ, start_response )

    #    environ['REMOTE_USER'] = 'anonymous'

    #    pgroups = permgroups
    #    hpg     = HasPermgroup( permgroups=pgroups, strict=True, all=True )
    #    assert_raises( NotAuthenticatedError, hpg.check, App, environ, start_response )

    #    environ['REMOTE_USER'] = user.username

    #    pgroups = permgroups + [ 'INVALID_PERM' ] 
    #    hpg     = HasPermgroup( permgroups=pgroups, strict=False )
    #    assert_raises( NotAuthorizedError, hpg.check, App, environ, start_response )

    #    pgroups = permgroups
    #    hpg     = HasPermgroup( permgroups=pgroups, strict=False, all=True )
    #    hpg.check( App, environ, start_response )

    #    pgroups = permgroups + x_pgroups
    #    hpg     = HasPermgroup( permgroups=pgroups, strict=False, all=True )
    #    assert_raises( NotAuthorizedError, hpg.check, App, environ, start_response )

    #    pgroups = permgroups + x_pgroups
    #    hpg     = HasPermgroup( permgroups=pgroups, strict=False, all=False )
    #    if permgroups :
    #        hpg.check( App, environ, start_response )
    #    else :
    #        assert_raises( NotAuthorizedError, hpg.check, App, environ, start_response )

    @attr(type='permclass')
    def test_C_validuser( self ) :
        """Testing ValidUser class"""
        log.info( "Testing ValidUser class ..." )
        users = userscomp.get_user()
        user  = choice( users )
        start_response = None
        environ = {}

        environ['REMOTE_USER'] = u'invalid_user'
        vu = ValidUser( strict='False' )
        assert_raises( NotAuthorizedError, vu.check, App, environ, start_response )

        environ['REMOTE_USER'] = u'anonymous'
        vu = ValidUser( strict='True' )
        assert_raises( NotAuthenticatedError, vu.check, App, environ, start_response )

        environ['REMOTE_USER'] = user.username
        vu = ValidUser( strict='True' )
        if user.username == 'anonymous' :
            assert_raises( NotAuthenticatedError, vu.check, App, environ, start_response )
        else :
            vu.check( App, environ, start_response )

    @attr(type='permclass')
    def test_D_siteadmin( self ) :
        """Testing SiteAdmin class"""
        log.info( "Testing Siteadmin class ..." )
        users = userscomp.get_user()
        user  = choice( users )
        start_response = None
        environ = {}
        spnames = [ pn.perm_name for pg in user.permgroups for pn in pg.perm_names ]

        environ['REMOTE_USER'] = config['zeta.siteadmin']
        sau = SiteAdmin( strict='False' )
        sau.check( App, environ, start_response )

        environ['REMOTE_USER'] = 'anonymous'
        sau = SiteAdmin( strict='True' )
        assert_raises( NotAuthenticatedError, sau.check, App, environ, start_response )

        environ['REMOTE_USER'] = user.username
        sau = SiteAdmin( strict='False' )
        if user.username == config['zeta.siteadmin'] :
            sau.check( App, environ, start_response )
        elif 'SITE_ADMIN' in spnames :
            sau.check( App, environ, start_response )
        else :
            assert_raises( NotAuthorizedError, sau.check, App, environ, start_response )

    @attr(type='permclass')
    def test_E_projectadmin( self ) :
        """Testing ProjectAdmin class"""
        log.info( "Testing ProjectAdmin class ..." )
        users = userscomp.get_user()
        user  = choice( users )
        project = choice( projcomp.get_project() )
        start_response = None
        environ = {}

        environ['REMOTE_USER'] = project.admin.username
        pau = ProjectAdmin( project, strict='False' )
        pau.check( App, environ, start_response )

        environ['REMOTE_USER'] = u'anonymous'
        pau = ProjectAdmin( project, strict='True' )
        assert_raises( NotAuthenticatedError, pau.check, App, environ, start_response )

        environ['REMOTE_USER'] = user.username
        pau = ProjectAdmin( project, strict='False' )
        if user.username == project.admin.username :
            pau.check( App, environ, start_response )
        else :
            assert_raises( NotAuthorizedError, pau.check, App, environ, start_response )

    @attr( type='pms' )
    def test_F_mapforteamperms( self ) :
        """Testing teampermission mapping"""
        log.info( "Testing teampermission mapping ..." )

        maps    = projcomp.mapfor_teamperms()
        ptp_all = projcomp.get_projectteamperm()
        maps_pnames = []
        [ maps_pnames.extend( v ) for v in maps.values() ]
        assert_equal( len(ptp_all), len(maps_pnames),
                      'Mismatch in permission map count for team permissions'
                    )

        dbmaps  = {}
        [ dbmaps.setdefault( (p, t), [] )
          for p in projcomp.projectnames for t in projcomp.teams ]
        for ptp in ptp_all :
            dbmaps.setdefault( 
                ( ptp.project.projectname, ptp.teamtype.team_type ),
                []
            ).append( userscomp.normalize_perms( ptp.permgroup.perm_group ) )

        assert_equal( sorted(dbmaps.keys()), sorted(maps.keys()),
                      'Mismatch in sorted keys for team permission maps'
                    )
        for k in dbmaps :
            assert_equal( sorted(dbmaps[k]), sorted(maps[k]),
                          'Mismatch in team permission maps')

    @attr( type='pms' )
    def test_G_mapforprojadmins( self ) :
        """Testing project admins mapping"""
        log.info( "Testing project admins mapping ..." )

        maps     = projcomp.mapfor_projadmins()
        projects = projcomp.get_project()
        assert_equal( len(maps.keys()), len(projects),
                      'Mismatch in permission map count for ' + \
                      'projadmin permissions'
                    )

        dbmaps  = {}
        for p in projects :
            dbmaps[( p.projectname, p.admin.username )] = \
                    ['PMS_PROJECT_ADMIN'] + userscomp.proj_permnames

        assert_equal( sorted(dbmaps.keys()), sorted(maps.keys()),
                      'Mismatch in sorted keys for projadmin ermission maps'
                    )
        for k in dbmaps :
            assert_equal( sorted(dbmaps[k]), sorted(maps[k]),
                          'Mismatch in projadmin permission maps' )

    def test_H_siteadmin( self ) :
        """Testing siteadmin() method"""
        log.info( "Testing siteadmin() method" )

        usernames  = sorted( userscomp.usernames )
        userstatus = userscomp.userstatus
        permmap    = userscomp.userpermission_map()

        userstatus['disabled'] = sorted(userstatus['disabled'])
        userstatus['enabled']  = sorted(userstatus['enabled'])

        usernames.remove( 'admin' )
        usernames1 = usernames[:]
        usernames1.remove( 'anonymous' )
        permmap.pop( 'admin', None )

        assert_equal( permmap,
                      userscomp.userpermission_map( usernames=usernames ),
                      'Mismatch in calling userpermission_map() with arguments'
                    )
        
        dbusernames, dbpermmap, dbuserstatus = userscomp.siteadmin()
        dbuserstatus['disabled'] = sorted( dbuserstatus['disabled'] )
        dbuserstatus['enabled']  = sorted( dbuserstatus['enabled'] )
        permmap.pop( 'anonymous', None )
        assert_equal( ( dbusernames, dbpermmap, dbuserstatus ),
                      ( usernames1, permmap, userstatus ),
                      'Mismatch with method siteadmin()'
                    )

    def test_I_anonymousaccess( self ) :
        """Testing anonymous access with or with out strict authentication"""
        log.info( "Testing anonymous access with or with out strict authentication" )

        users      = userscomp.get_user()
        teamtypes  = projcomp.get_teamtype()
        teamtype   = choice( teamtypes )
        projects   = projcomp.get_project()
        project    = choice( projects )
        start_response = None

        allowedpermnames = [ 'LICENSE_VIEW', 'PROJECT_VIEW', 'TICKET_VIEW',
                             'REVIEW_VIEW', 'WIKI_VIEW',
                             'SEARCH_VIEW'
                           ]
        environ = {}
        for pn in allowedpermnames :
            hpn    = HasPermname( permnames=[pn], project=project )
            if ctxt.get( 'strictauth' ) == 'False' :
                hpn.check( App, environ, start_response )
            elif ctxt.get( 'strictauth' ) == 'True' :
                assert_raises( NotAuthorizedError, hpn.check, App, environ, start_response )
