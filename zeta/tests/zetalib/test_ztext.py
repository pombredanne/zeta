# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import time
import unittest
import os
from   os                          import listdir
from   os.path                     import join, isdir, basename, dirname, isfile, \
                                          abspath
import random
from   random                      import choice, randint, shuffle, seed
from   datetime                    import datetime
import re
import pprint
import datetime                    as dt

import pylons.test
import pytz
from   nose.tools                  import assert_equal, assert_raises, \
                                          assert_true, assert_false
from   nose.plugins.attrib         import attr
import simplejson                  as json
from   sqlalchemy                  import engine_from_config
 
from   zeta.auth.perm              import permissions
from   zeta.model                  import init_model, create_models, delete_models
from   zeta.model                  import meta
import zeta.lib.cache              as cachemod 
import zeta.lib.helpers            as h
from   zeta.lib.mailclient         import OutMessage
from   zeta.lib.ztext              import *
from   zeta.lib.error              import ZetaFormError
from   zeta.comp.system            import SystemComponent
from   zeta.comp.attach            import AttachComponent
from   zeta.comp.project           import ProjectComponent
from   zeta.comp.ticket            import TicketComponent
from   zeta.comp.wiki              import WikiComponent
from   zeta.comp.review            import ReviewComponent
from   zeta.tests.model.populate   import pop_permissions, pop_user, \
                                          pop_licenses, pop_projects,\
                                          pop_wikipages, pop_reviews,\
                                          pop_tickets, pop_vcs
from   zeta.tests.tlib             import *
from   zeta.tests.model.generate   import genattachs
import zeta.tests.zetalib.ztextlib as ztl

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None

no_of_users     = 5
no_of_relations = 1
no_of_tags      = 5
no_of_attachs   = 1
no_of_projects  = 2
no_of_wikis     = 10
no_of_tickets   = 10
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 10
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
syscomp     = None
projcomp    = None
attcomp     = None
tckcomp     = None
wikicomp    = None
revcomp     = None

testtext = """

        reviewid:10000




During the last weeks, Kenn and I worked together to support EMF generated
editors running on RAP. I'm always mesmerized by how effective such synergies
can be used when people from different teams work together for a bigger goal.
Kudos to Kenn for his great work in EMF by refactoring the EMF UI bundles
(namely o.e.emf.ui.common and o.e.emf.ui.edit) in order to single-source them.
But what does that mean for the community?
"""

def setUpModule() :
    global compmgr, userscomp, syscomp, attcomp, projcomp, tckcomp, wikicomp, \
           revcomp, seed

    testdir  = os.path.basename( dirname( __file__ ))
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
    attcomp    = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    revcomp    = ReviewComponent( compmgr )
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
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
    print "   Populating vcs ( no_of_vcs=%s ) ..." % no_of_vcs
    pop_vcs( no_of_vcs=no_of_vcs, seed=seed )
    print "   Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
    pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_wikis=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_wikis )

def tearDownModule() :
    testdir  = os.path.basename( dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )
    info = "   Deleting models (module-level) ... "
    log.info( info )
    print info
    delete_models( meta.engine )


class TestZText( object ) :

    @attr( type='swiki' )
    def test_A_swiki( self ) :
        """Testing Static Wiki text block"""
        log.info( "Testing Static Wiki text block" )

        swtypes = wikicomp.get_wikitype()

        # Test case one
        swtype  = choice(swtypes)
        text = ztl.sw_testcase_1(swtype)
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.sw_verify_1( syscomp, swtype ), 'Fail sw_verify_1()' )

        # Test case two
        text = ztl.sw_testcase_2()
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.sw_verify_2( syscomp ), 'Fail sw_verify_1()' )

        # Test case three
        text = ztl.sw_testcase_3()
        msg  = parse(text)
        assert_equal( msg.message, 'Unable to identify the purpose of text !!',
                      'Fail sw_testcase_3' )

        # Test case four
        text = ztl.sw_testcase_4()
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.sw_verify_4( syscomp ), 'Fail sw_verify_4()' )

    @attr( type='attach' )
    def test_B_attach( self ) :
        """Testing attachment text block"""
        log.info( "Testing attachment text block" )

        files = [ f for f in listdir( '.' ) if isfile(f) ]
        p     = choice(projcomp.get_project())

        # Test case one
        text = ztl.att_testcase_1()
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        file = choice(files)
        file = ( file, open( join( abspath(os.curdir), file )).read() )
        ctxt.commit( config, g_byuser, attachments=[file] )
        assert_true( ztl.att_verify_1( attcomp ), 'Fail att_verify_1()' )
        a = attcomp.get_attach()[-1]
        assert_equal( a.filename, file[0], 'Mismatch in file name' )
        assert_equal( attcomp.content(a), file[1], 'Mismatch in file content' )

        # Test case one
        text = ztl.att_testcase_2( p )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        file = choice(files)
        file = ( file, open( join( abspath(os.curdir), file )).read() )
        ctxt.commit( config, g_byuser, attachments=[file] )
        assert_true( ztl.att_verify_2( attcomp, p ), 'Fail att_verify_2()' )
        a = attcomp.get_attach()[-1]
        assert_equal( a.filename, file[0], 'Mismatch in file name' )
        assert_equal( attcomp.content(a), file[1], 'Mismatch in file content' )

        # Test case three
        text = ztl.att_testcase_3(a)
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.att_verify_3( attcomp ), 'Fail att_verify_3()' )
        a = attcomp.get_attach()[-1]
        assert_equal( a.filename, file[0], 'Mismatch in file name' )
        assert_equal( attcomp.content(a), file[1], 'Mismatch in file content' )

        # Test case four
        text = ztl.att_testcase_4()
        msg  = parse(text)
        assert_equal( msg.message, 'Unable to identify the purpose of text !!',
                      'Fail att_testcase_4' )

    @attr( type='wiki' )
    def test_C_wiki( self ) :
        """Testing Wiki text block"""
        log.info( "Testing Wiki text block" )

        files = [ f for f in listdir( '.' ) if isfile(f) ]
        p     = choice(projcomp.get_project())
        types = wikicomp.get_wikitype()
        user  = userscomp.get_user( g_byuser )

        # Test case one
        type  = choice(types)
        text  = ztl.wiki_testcase_1( p, type )
        ctxt  = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.wiki_verify_1( wikicomp, p, type ), 'Fail wiki_verify_1()' )

        # Test case two
        type = choice(types)
        summ = 'some wiki summary ...'
        text = ztl.wiki_testcase_2( p, type, summ )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.wiki_verify_2( wikicomp, p, type, summ ), 'Fail wiki_verify_2()' )

        # Test case three
        text = ztl.wiki_testcase_3( wikicomp, p )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.wiki_verify_3( wikicomp, p ), 'Fail wiki_verify_3()' )

        # Test case four
        text = ztl.wiki_testcase_4( p.id, user )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.wiki_verify_4( wikicomp, p, user ), 'Fail wiki_verify_4()' )

        # Test case five
        text = ztl.wiki_testcase_5( wikicomp, p )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        file = choice(files)
        file = ( file, open( join( abspath(os.curdir), file )).read() )
        ctxt.commit( config, g_byuser, attachments=[file] )
        assert_true( ztl.wiki_verify_5( wikicomp, p, user ), 'Fail wiki_verify_5()' )
        a = attcomp.get_attach()[-1]
        assert_equal( a.filename, file[0], 'Mismatch in file name' )
        assert_equal( attcomp.content(a), file[1], 'Mismatch in file content' )

        # Test case six
        text = ztl.wiki_testcase_6()
        msg  = parse(text)
        assert_equal( msg.message, 'Unable to identify the purpose of text !!',
                      'Fail wiki_testcase_6' )

        # Test case seven
        text = ztl.wiki_testcase_7()
        msg  = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )

    @attr( type='tck' )
    def test_D_ticket( self ) :
        """Testing Ticket text block"""
        log.info( "Testing Ticket text block" )

        files = [ f for f in listdir( '.' ) if isfile(f) ]
        p     = choice(projcomp.get_project())
        types = tckcomp.get_tcktype()
        severs= tckcomp.get_tckseverity()
        statuss= tckcomp.get_tckstatus()
        users = userscomp.get_user()
        user  = userscomp.get_user( g_byuser )
        tcks  = tckcomp.get_ticket()

        # Test case one
        type = choice(types)
        sev  = choice(severs)
        pu   = choice(users)
        comps= p.components and p.components[:1] or []
        text = ztl.tck_testcase_1( p, type, sev, pu, comps )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.tck_verify_1( tckcomp, type, sev, pu, comps ),
                     'Fail tck_verify_1()' )

        # Test case two
        type = choice(types)
        sev  = choice(severs)
        mstns= p.milestones and p.milestones[:1] or []
        vers = p.versions and p.versions[:1] or []
        text = ztl.tck_testcase_2( p, type, sev, mstns, vers )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.tck_verify_2( tckcomp, type, sev, mstns, vers ),
                     'Fail tck_verify_1()' )

        t = tckcomp.get_ticket()[-1]

        # Test case three
        bby  = tcks[:1]
        bking= tcks[1:3]
        type = choice(types)
        sev  = choice(severs)
        text = ztl.tck_testcase_3( t, type, sev, bby, bking )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.tck_verify_3( t, type, sev, bby, bking ),
                     'Fail tck_verify_3()' )

        # Test case four
        type = choice(types)
        par  = choice(tcks)
        text = ztl.tck_testcase_4( t, type, par, user )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.tck_verify_4( t, type, par, user ),
                     'Fail tck_verify_4()' )

        # Test case five
        text = ztl.tck_testcase_5( t )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        file = choice(files)
        file = ( file, open( join( abspath(os.curdir), file )).read() )
        ctxt.commit( config, g_byuser, attachments=[file] )
        assert_true( ztl.tck_verify_5( t, user ), 'Fail tck_verify_5()' )
        a = attcomp.get_attach()[-1]
        assert_equal( a.filename, file[0], 'Mismatch in file name' )
        assert_equal( attcomp.content(a), file[1], 'Mismatch in file content' )

        # Test case six
        text = ztl.tck_testcase_6()
        msg  = parse(text)
        assert_equal( msg.message, 'Unable to identify the purpose of text !!',
                      'Fail tck_testcase_6' )

        # Test case seven
        text = ztl.tck_testcase_7()
        msg  = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )

    @attr( type='revw' )
    def test_E_review( self ) :
        """Testing Review text block"""
        log.info( "Testing Review text block" )

        files = [ f for f in listdir( '.' ) if isfile(f) ]
        revws   = revcomp.get_review()
        natures = revcomp.get_reviewcomment_nature()
        actions = revcomp.get_reviewcomment_action()
        user    = userscomp.get_user( g_byuser )

        # Test case one
        r      = choice(revws)
        nature = choice(natures)
        text = ztl.revw_testcase_1( r, nature )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.revw_verify_1( revcomp, r, nature ),
                     'Fail revw_verify_1()' )

        # Test case two
        r    = choice(revws)
        text = ztl.revw_testcase_2( r )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        file = choice(files)
        file = ( file, open( join( abspath(os.curdir), file )).read() )
        ctxt.commit( config, g_byuser, attachments=[file] )
        assert_true( ztl.revw_verify_2( revcomp, r, user ),
                     'Fail revw_verify_1()' )
        a = attcomp.get_attach()[-1]
        assert_equal( a.filename, file[0], 'Mismatch in file name' )
        assert_equal( attcomp.content(a), file[1], 'Mismatch in file content' )

        # Test case three
        action = choice(actions)
        nature = choice(natures)
        approved = choice([True,False])
        text = ztl.revw_testcase_3( revcomp, r, action, nature, approved )
        ctxt = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
        assert_true( ztl.revw_verify_3( revcomp, r, user, action, nature,
                                        approved ),
                     'Fail revw_verify_3()' )

        # Test case four
        text = ztl.revw_testcase_4( r )
        msg  = parse(text)
        assert_equal( msg.message, 'Unable to identify the purpose of text !!',
                      'Fail revw_testcase_4' )

        # Test case five
        text = ztl.revw_testcase_5()
        ctxt  = parse(text)
        assert_true( isinstance( ctxt, Context ), 'parse return not a context' )
        ctxt.commit( config, g_byuser )
