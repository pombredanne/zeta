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
from   os.path                      import dirname, abspath

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true
from   nose.plugins.attrib          import attr

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects, pop_tickets
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.tests.tlib              import *
from   zeta.comp.system             import SystemComponent
from   zeta.comp.wiki               import WikiComponent

config          = pylons.test.pylonsapp.config
log             = logging.getLogger( __name__ )
seed            = None
no_of_users     = 10
no_of_relations = 2
g_byuser        = u'admin'
ref_swikis      = {}

compmgr     = None
userscomp   = None
syscomp     = None
wikicomp    = None
pjoin       = os.path.join
cachemgr    = None
cachedir    = '/tmp/testcache'


sampledata_dir = os.path.abspath( pjoin( dirname( dirname(__file__)), 
                                         'model', 'sampledata' ))

def surf_dir( rootdir ) :
    swikis  = {}
    for wpath, dirs, files in os.walk( rootdir ) :
        for file in files : 
            swpath = pjoin( wpath, file )
            path   = swpath.split( rootdir )[1]
            path   = path[0] == os.sep and path[1:] or path # prune /
            swikis.setdefault( path, open(swpath).read() )
    return swikis

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, syscomp, wikicomp, seed, ref_swikis, cachemgr

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
    syscomp    = SystemComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    # Populate DataBase with sample entries
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )

    ref_swikis = surf_dir( pjoin( sampledata_dir, 'wikipages' ))

    # Setup cache manager
    #isdir( cachedir ) or os.makedirs( cachedir )
    #cachemgr = cachemod.cachemanager( cachedir )
    #config['cachemgr'] = cachemgr


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


class TestSystem( object ) :

    def test_1_sysentry( self ) :
        """Testing the sysentry, getter and setter"""
        log.info( "Testing the sysentry, getter and setter" )
        n_entries = { u'field1' : u'value1',
                      u'field2' : u'value2' }
        refentries= syscomp.get_sysentry()

        syscomp.set_sysentry( refentries, byuser=g_byuser )
        entries   = syscomp.get_sysentry()
        assert_equal( sorted(refentries.keys()), sorted(entries.keys()),
                      'Mismatch in sysentry keys, while re-creating the same'
                    )
        [ assert_equal( refentries[k], syscomp.get_sysentry(k),
                        'Mismatch in value for key ' + k )
        for k in refentries.keys() ]

        syscomp.set_sysentry( n_entries, byuser=g_byuser )
        syscomp.set_sysentry({ u'field3' : u'value3' }, byuser=g_byuser)
        refentries.update({u'field3' : u'value3'})
        refentries.update(n_entries)
        entries = syscomp.get_sysentry()
        assert_equal( sorted(refentries.keys()), sorted(entries.keys()),
                      'Mismatch in sysentry keys, while re-creating the same'
                    )
        [ assert_equal( refentries[k], syscomp.get_sysentry(k),
                        'Mismatch in value for key ' + k )
        for k in refentries.keys() ]

    def test_2_interzeta( self ) :
        """Testing the interzeta, getter and setter"""
        log.info( "Testing the interzeta, getter and setter" )

        refmap = { u'google' : u'http://google.com',
                   u'yahoo'  : u'http://yahoo.com' }
        syscomp.set_interzeta( refmap, byuser=g_byuser )
        map    = syscomp.get_interzeta()
        assert_equal( sorted(refmap.keys()), sorted(map.keys()),
                      'Mismatch in keys for interzeta' )
        [ assert_equal( refmap[k], map[k], 'Mismatch in value for key' )
          for k in refmap ]

        syscomp.set_interzeta( {u'microsoft' : u'http://microsoft.com'},
                               byuser=g_byuser )
        refmap.update({u'microsoft' : u'http://microsoft.com'})
        map    = syscomp.get_interzeta()
        assert_equal( sorted(refmap.keys()), sorted(map.keys()),
                      'Mismatch in keys for interzeta' )
        [ assert_equal( refmap[k], syscomp.get_interzeta(k),
                        'Mismatch in value for key' )
          for k in refmap ]

    def test_3_staticwiki( self ) :
        """Testing the static wiki, getter and setter"""
        log.info( "Testing the static wiki, getter and setter" )
    
        class W( object ):
            pass

        wikipage = os.path.join( 
                        sampledata_dir, 'wikipages', 'creole1.0test.txt'
                      )
        text = unicode(open( wikipage ).read())

        # Try to create a fresh entry
        path = u'/some/page'
        swtype = choice(wikicomp.get_wikitype())
        sourceurl = u"http://discoverzeta.com"
        syscomp.set_staticwiki( path, text, swtype=swtype, sourceurl=sourceurl,
                                byuser=g_byuser )
        sw  = syscomp.get_staticwiki( path, translate=choice([True, False]) )
        ref = W()
        ref.text = text
        texthtml = h.translate( ref, 'text', wiki=sw )
        assert_equal( [sw.text, sw.type.wiki_typename, sw.sourceurl ],
                      [text, swtype.wiki_typename, sourceurl ],
                      'Mismatch in static file text' )
        assert_equal( texthtml, sw.texthtml,
                      'Mismatch in wiki translation for static file' )


        # Try to create a fresh entry
        path = u'/some/page'
        swtype = choice(wikicomp.get_wikitype())
        sourceurl = u"http://discoverzeta.com"
        text = text + 'hello world'
        syscomp.set_staticwiki( path, text, swtype=swtype, sourceurl=sourceurl,
                                byuser=g_byuser )
        sw = syscomp.get_staticwiki( path, translate=choice([True, False]) )
        ref = W()
        ref.text = text
        texthtml = h.translate( ref, 'text', wiki=sw )
        assert_equal( [sw.text, sw.type.wiki_typename, sw.sourceurl],
                      [text, swtype.wiki_typename, sourceurl],
                      'Mismatch in updating static wiki text' )
        assert_equal( texthtml, sw.texthtml,
                      'Mismatch in wiki translation for updated static wiki' )

        # Fetch all static wiki
        swikis = syscomp.get_staticwiki( translate=choice([True, False]) )
        assert_true( isinstance( swikis, list ),
                     'Get static wiki Not a list ' )
        assert_true( len(swikis) >= 3, 'No. of. static wiki is less than 3' )

        # Upgrade wiki
        assert_true( syscomp.upgradewiki( byuser=g_byuser ) == len(swikis),
                     'Problem in upgrading static wiki' )

    def test_4_push_staticwiki( self ) :
        """Testing static wiki push"""
        log.info( "Testing static wiki push")
    
        swikis = syscomp.get_staticwiki()
        [ syscomp.remove_staticwiki( sw.path, byuser=g_byuser ) for sw in swikis ]

        files, skipped  = syscomp.push_staticwiki(
                                    pjoin( sampledata_dir, 'wikipages' ),
                                    byuser=g_byuser
                          )
        swikis = syscomp.get_staticwiki()

        assert_equal( sorted(files+skipped), sorted(ref_swikis.keys()),
                      'Mismatch in the static wiki returned paths while pushing'
                    )

        for swpath in files :
            assert_equal( ref_swikis[swpath], syscomp.get_staticwiki( swpath ).text,
                          'Mismatch in static wiki content for %s while pushing' % \
                              swpath
                        )

    def test_5_pull_staticwiki( self ) :
        """Testing static wiki pull"""
        log.info( "Testing static wiki pull"  )

        tmpdir = pjoin( '/tmp/', 'zeta', dt.datetime.utcnow().strftime('%d_%h_%s') )

        files         = syscomp.pull_staticwiki( tmpdir )
        pulled_swikis = surf_dir( tmpdir )

        assert_equal( sorted(files), sorted(ref_swikis.keys()),
                      'Mismatch in the static wiki returned paths while pulling'
                    )
        assert_equal( sorted( pulled_swikis.keys() ),
                      sorted( ref_swikis.keys() ),
                      'Mismatch in the static wiki paths while pulling'
                    )

        for swpath in ref_swikis :
            assert_equal( ref_swikis[swpath], pulled_swikis[swpath],
                          'Mismatch in static wiki content for %s while pulling' % \
                                swpath
                        )

        cmd = 'rm -rf ' + tmpdir
        os.system( cmd )
