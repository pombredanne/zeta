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
from   nose.tools                   import assert_equal, assert_not_equal, \
                                           assert_raises, \
                                           assert_false, assert_true
from   nose.plugins.attrib          import attr

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_tickets
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
import zeta.lib.gviz                as gviz
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 5
no_of_attachs   = 1
no_of_projects  = 1
no_of_tickets   = 5
g_byuser        = u'admin'

tagchars    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
taglist     = None 

compmgr     = None
userscomp   = None
attachcomp  = None
tagcomp     = None
liccomp     = None
projcomp    = None
tckcomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'
dotdir      = os.path.join( os.path.dirname( __file__ ), 'dotdir' )

attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, tagcomp, projcomp, tckcomp, taglist,\
           seed, cachemgr

    isdir(dotdir) or os.makedirs(dotdir)

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
    tagcomp    = TagComponent( compmgr )
    liccomp    = LicenseComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
    taglist = [ unicode(h.randomname( randint(1,LEN_TAGNAME), tagchars))
                            for i in range(randint(1,no_of_tags)) ]
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
    print "   Populating tickets ( no_of_tickets=%s ) ..." % no_of_tickets
    pop_tickets( no_of_tickets, no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_tickets=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_tickets )

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


g_tckccodes ="""
[
    [ "", "", "#fffce1" ],

    [ "tck_statusname", "fixed", "#ebebeb" ],
    [ "tck_statusname", "duplicate", "#ebebeb" ],
    [ "tck_statusname", "wontfix", "#ebebeb" ],

    [ "tck_severityname", "blocker", "#ffe1e1" ],
    [ "tck_severityname", "critical" , "#ffe1e1" ],

    [ "tck_statusname", "new" , "#fafafa" ],
    [ "tck_statusname", "open" , "#fafafa" ],
    [ "tck_statusname", "reopen", "#fafafa" ]

]
"""

class TestGViz( object ) :

    def test_1_graph( self ) :
        """Testing ticket graph and tree generation"""
        log.info( "Testing ticket graph and tree generation" )

        for t in tckcomp.get_ticket() :
            # Dependency graph
            tckdeps = gviz.calctckdep( tckcomp.allblockers(), tckcomp.ticketdeps() )
            dottext = gviz.tckdeptodot( t.id, tckdeps, h.tckccodes )
            srcfile = os.path.join( dotdir, "%sg.dot" % t.id )
            dstfile = os.path.join( dotdir, "%sg.svg" % t.id )
            open( srcfile, 'w' ).write( dottext )
            open( dstfile, 'w' ).write( gviz.tosvgtext( dottext ))

            # Hierarchy tree
            tckhier = gviz.calctckhier( tckcomp.allparchild(), tckcomp.ticketdeps() )
            dottext = gviz.tckhiertodot( t.id, tckhier, h.tckccodes )
            srcfile = os.path.join( dotdir, "%sh.dot" % t.id )
            dstfile = os.path.join( dotdir, "%sh.svg" % t.id )
            open( srcfile, 'w' ).write( dottext )
            open( dstfile, 'w' ).write( gviz.tosvgtext( dottext ))

    def test_B_cachedgraph( self ) :
        """Testing caching logic for ticket graph generation logic"""
        log.info( "Testing caching logic for ticket graph generation logic" )

        tickets = tckcomp.get_ticket() 
        t1      = tickets[2]
        t2      = tickets[3]
        tckdeps_a = gviz.calctckdep( tckcomp.allblockers(), tckcomp.ticketdeps() )
        tckdeps_b = gviz.calctckdep( tckcomp.allblockers(), tckcomp.ticketdeps() )
        assert_true( tckdeps_a == tckdeps_b, 'Mismatch in fetching from cache' )
        
        # Auto invalidation for calctckdep(), modifying blockedby
        if tickets[1].blockedby :
            tckcomp.config_ticket( tickets[1], blockedby=[], append=False,
                                   byuser=g_byuser )
        else :
            tckcomp.config_ticket( tickets[1], blockedby=[ tickets[2] ],
                                   append=False, byuser=g_byuser )
        tckdeps_b = gviz.calctckdep( tckcomp.allblockers(), tckcomp.ticketdeps() )
        assert_true( tckdeps_a != tckdeps_b, 'Mismatch in fetching from cache' )
        tckdeps_a = gviz.calctckdep( tckcomp.allblockers(), tckcomp.ticketdeps() )
        assert_true( tckdeps_a == tckdeps_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for calctckdep(), modifying summary
        tckcomp.create_ticket( tickets[1].project,
                               [ tickets[1].id, u'Updated summary ...',
                                 tickets[1].description, tickets[1].type,
                                 tickets[1].severity ],
                               byuser=g_byuser
                             )
        tckdeps_b = gviz.calctckdep( tckcomp.allblockers(), tckcomp.ticketdeps() )
        assert_true( tckdeps_a != tckdeps_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckdeptodot()
        dottext_a = gviz.tckdeptodot( t1.id, tckdeps_a, h.tckccodes )
        dottext_b = gviz.tckdeptodot( t1.id, tckdeps_a, h.tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckdeptodot(), modifying tid
        dottext_b = gviz.tckdeptodot( t2.id, tckdeps_a, h.tckccodes )
        assert_true( dottext_a != dottext_b, 'Mismatch in fetching from cache' )
        dottext_b = gviz.tckdeptodot( t1.id, tckdeps_a, h.tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckdeptodot(), modifying tckdeps
        dottext_b = gviz.tckdeptodot( t1.id, tckdeps_b, h.tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckdeptodot(),modifying tckccodes
        dottext_b = gviz.tckdeptodot( t1.id, tckdeps_b, g_tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

    def test_B_cachedtree( self ) :
        """Testing caching logic for ticket tree generation logic"""
        log.info( "Testing caching logic for ticket tree generation logic" )

        tickets = tckcomp.get_ticket() 
        t1      = tickets[2]
        t2      = tickets[3]
        tckhier_a = gviz.calctckhier( tckcomp.allparchild(), tckcomp.ticketdeps() )
        tckhier_b = gviz.calctckhier( tckcomp.allparchild(), tckcomp.ticketdeps() )
        
        assert_true( tckhier_a == tckhier_b, 'Mismatch in fetching from cache' )
        
        # Auto invalidation for calctckhier), modifying hierarchy
        if tickets[1].parent :
            tckcomp.config_ticket( tickets[1], parent='', byuser=g_byuser )
        else :
            tckcomp.config_ticket( tickets[1], parent=tickets[2], byuser=g_byuser )
        tckhier_b = gviz.calctckhier( tckcomp.allparchild(), tckcomp.ticketdeps() )
        assert_true( tckhier_a != tckhier_b, 'Mismatch in fetching from cache' )
        tckhier_a = gviz.calctckhier( tckcomp.allparchild(), tckcomp.ticketdeps() )
        assert_true( tckhier_a == tckhier_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for calctckhier(), modifying summary
        tckcomp.create_ticket( tickets[1].project,
                               [ tickets[1].id, u'Updated summary ...',
                                 tickets[1].description, tickets[1].type,
                                 tickets[1].severity ],
                               byuser=g_byuser
                             )
        tckhier_b = gviz.calctckhier( tckcomp.allparchild(), tckcomp.ticketdeps() )
        assert_true( tckhier_a != tckhier_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckhiertodot()
        dottext_a = gviz.tckhiertodot( t1.id, tckhier_a, h.tckccodes )
        dottext_b = gviz.tckhiertodot( t1.id, tckhier_a, h.tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckhiertodot(), modifying tid
        dottext_b = gviz.tckhiertodot( t2.id, tckhier_a, h.tckccodes )
        assert_true( dottext_a != dottext_b, 'Mismatch in fetching from cache' )
        dottext_b = gviz.tckhiertodot( t1.id, tckhier_a, h.tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckhiertodot(), modifying tckhier
        dottext_b = gviz.tckhiertodot( t1.id, tckhier_b, h.tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )

        # Auto invalidation for tckhiertodot(), modifying tckccodes
        dottext_b = gviz.tckhiertodot( t1.id, tckhier_b, g_tckccodes )
        assert_true( dottext_a == dottext_b, 'Mismatch in fetching from cache' )
