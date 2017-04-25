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
from   zeta.tests.model.generate    import gen_vcs, gen_vcsmounts
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.vcs                import VcsComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 2
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 10
no_of_vcs       = no_of_projects * 2
g_byuser        = u'admin'

compmgr         = None
userscomp       = None
attachcomp      = None
projcomp        = None
vcscomp         = None
vcsdata         = None
cachemgr        = None
cachedir        = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, projcomp, vcscomp, vcsdata, \
           seed, cachemgr

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
    attachcomp = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
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
    # Collect the expected database objects.
    vcsdata = gen_vcs( no_of_vcs=no_of_vcs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_vcs=%s" )   % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_vcs )

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


class TestVcs( object ) :

    def _validate_vcs( self, vcsdata, vcsentries ) :
        """`vcsdata` and `vcsentries` are sorted based on the vcs object"""
        assert_equal( len(vcsdata), len(vcsentries),
                      'Mismatch with the number of vcsentries in the database'
                    )
        for i in range(len(vcsentries)) :
            vcs       = vcsdata[i]
            v         = vcsentries[i]
            vcsfields = [ vcs['type'], vcs['name'], vcs['rooturl'], 
                          vcs['loginname'], vcs['password'], vcs['project']
                        ]
            dbvcsfields = [ v.type.vcs_typename, v.name, v.rooturl,
                            v.loginname, v.password, v.project.projectname ]
            assert_equal( vcsfields, dbvcsfields, 'Mismatch in the vcs detail' )


    def test_1_get_vcstype( self ) :
        """Testing get_vcstype() method"""
        log.info( "Testing get_vcstype() method ..." )
        dbtypes = vcscomp.get_vcstype()
        assert_equal( sorted(config['zeta.vcstypes']),
                      sorted([ v.vcs_typename for v in dbtypes ]),
                      'Mismatch in getting all the vcs types'
                    )
        assert_equal( sorted(dbtypes),
                      sorted([ vcscomp.get_vcstype( v ) 
                               for v in config['zeta.vcstypes'] ]),
                      'Mismatch in getting vcs types by name'
                    )
        assert_equal( sorted(dbtypes),
                      sorted([ vcscomp.get_vcstype( v.id ) for v in dbtypes ]),
                      'Mismatch in getting vcs types by id'
                    )

    def test_2_create_vcstype( self ) :
        """Testing creating vcstype"""
        log.info( "Testing creating vcstype" )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        ref_vcstypes = vcscomp.vcstypenames
        add_vcstypes = [ u'vcstype1', u'vcstype2' ]
        ref_vcstypes += add_vcstypes
        vcscomp.create_vcstype( add_vcstypes )
        assert_equal( sorted(ref_vcstypes), sorted(vcscomp.vcstypenames),
                      'Mismatch in creating vcs types as list' )

        add_vcstypes = u'vcstype3'
        ref_vcstypes += [ add_vcstypes ]
        vcscomp.create_vcstype( add_vcstypes )
        assert_equal( sorted(ref_vcstypes), sorted(vcscomp.vcstypenames),
                      'Mismatch in creating vcs type as string' )

    def test_3_integrate_vcs( self ) :
        """Testing integrate_vcs() method"""
        log.info( "Testing integrate_vcs() method ..." )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for vcs in vcsdata :
            vcsdetail = [ vcs['type'], vcs['name'], vcs['rooturl'],
                          vcs['loginname'], vcs['password'] ]
            vcs['id'] = vcscomp.integrate_vcs(
                                    vcs['project'],
                                    vcsdetail,
                                    byuser=g_byuser
                         )
        self._validate_vcs( sorted( vcsdata, key=lambda vcs : vcs['id'] ),
                            sorted( vcscomp.get_vcs() )
                          )

    def test_4_config_vcs( self ) :
        """Testing config_vcs() method"""
        global  vcsdata
        log.info( "Testing config_vcs() method ..." )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        types = [ vcscomp.get_vcstype( vt ) for vt in config['zeta.vcstypes'] ]
        users = userscomp.get_user()
        for vcs in vcsdata :
            type   = choice( types )
            byuser = choice( users )
            possibleargs   = { 
                'name'      : u'updated_name',
                'type'      : type.vcs_typename,
                'rooturl'   : u'updated:///some/path/to/url',
                'loginname' : u'someuser',
                'password'  : u'somepassword',
                'byuser'    : byuser.username,
            }
            vcs['name']     = possibleargs['name']
            vcs['type']     = possibleargs['type']
            vcs['rooturl']  = possibleargs['rooturl']
            vcs['loginname']= possibleargs['loginname']
            vcs['password'] = possibleargs['password']

            while possibleargs :
                keys   = set([ choice(possibleargs.keys())
                               for i in range(randint(0,len(possibleargs))) ])
                kwargs = dict([ ( k, possibleargs.pop( k )) for k in keys ]) 
                vcscomp.config_vcs( vcs['id'], **kwargs )
        self._validate_vcs( sorted( vcsdata, key=lambda vcs : vcs['id'] ),
                            sorted( vcscomp.get_vcs() ))

    def test_5_delete_vcs( self ) :
        """Testing delete_vcs() method"""
        global vcsdata
        log.info( "Testing delete_vcs() method ..." )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        vcsentries  = vcscomp.get_vcs()
        rmvcs       = [ v for v in vcsentries if choice([True, False]) ]
        [ vcscomp.delete_vcs( v, byuser=g_byuser ) for v in rmvcs ]
        vcsdata1    = vcsdata[:]
        [ vcsdata1.remove( v ) for v in vcsdata if v['id'] in rmvcs ]
        vcsdata     = vcsdata1
        self._validate_vcs( sorted( vcsdata, key=lambda vcs : vcs['id'] ),
                            sorted( vcscomp.get_vcs() ))

    def test_6_vcsmounts( self ) :
        """Testing vcs mounts methods """
        log.info( "Testing vcs mount methods ..." )

        svnurl    = unicode(h.fromconfig( 'svnurl' ))
        bzrurl    = unicode(h.fromconfig( 'bzrurl' ))

        projects  = projcomp.get_project()

        # Fix vcs data
        for vcs in vcsdata :
            type    = choice( config['zeta.vcstypes'] )
            rooturl = svnurl if type == 'svn' else bzrurl
            vcscomp.config_vcs( vcs['id'], type=type, rooturl=rooturl )

        # Create mounts
        mounts    = []
        delmounts = []
        mountdata = gen_vcsmounts( no_of_vcs=no_of_vcs, seed=seed )
        for d in mountdata :
            v = vcscomp.get_vcs( d['vcs_id'] )
            if not v : continue
            vmount  = vcscomp.create_mount( v, d['name'], d['repospath'],
                                            d['content'], byuser=g_byuser )
            d['id'] = vmount.id

            # Update mounts
            kwargs = { 'byuser' : g_byuser }
            if choice([0, 1]) :
                kwargs.setdefault( 'name', u'updatemountname' )
            if choice([0, 1]) :
                kwargs.setdefault( 'repospath', u'updated/relative/path' )
            if choice([0, 1]) :
                kwargs.setdefault( 'content', choice(vcscomp.mountcontents) )

            vcscomp.update_mount( vmount, **kwargs )

            # Update mounts
            if choice([0, 1]) :
                vcscomp.delete_mount( vmount, byuser=g_byuser )
                delmounts.append( vmount )
            else :
                mounts.append( vmount )

        assert_equal( sorted( mounts, key=lambda m : m.name),
                      sorted( vcscomp.get_mount(), key=lambda m : m.name),
                      'Mismatch in creating / updating / deleting vcs mounts'
                    )

        for d in mountdata :
            m = vcscomp.get_mount( d['id'] )
            if d['id'] in delmounts :
                assert_false( m, 'Mismatch in deleted mount' )
            elif d['id'] in mounts :
                assert_true( vcscomp.get_mount( choice([ m.id, m ]) ),
                             'Mismatch in created mount' )
            else :
                assert "Mount not recognized"

        # Check projmounts method
        alldets = []
        for p in projects :
            mdets = vcscomp.projmounts( choice([ p, p.id, p.projectname ]) )
            for mdet in mdets :
                m = vcscomp.get_mount( mdet[0] )
                assert_equal( [ m.id, m.name, m.content, m.repospath,
                                m.created_on ],
                                list(mdet[:5]),
                              'Mismatch in mount point'
                            )
            alldets.extend( mdets )
        assert_equal( len(alldets), len(vcscomp.get_mount()),
                      'Mismatch in total number of mount points' )


    def test_A_properties( self ) :
        """Testing vcs properties"""
        log.info( "Testing vcs properties ..." )
        
        assert_equal( sorted([ vt.vcs_typename 
                               for vt in vcscomp.get_vcstype() ]),
                      sorted( vcscomp.vcstypenames ),
                      "Mismatch in vcstypenames properties"
                    )
