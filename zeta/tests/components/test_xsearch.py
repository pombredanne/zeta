# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

#
# Gotcha :
#   1. ircchannel removal from project still remain indexed.
#
import logging
import sys
import os
from   os.path                      import commonprefix, join, split, abspath, basename, isdir
import random
from   random                       import choice, randint
import datetime                     as dt

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
from   zeta.tests.model.generate    import gen_reviewurls, gen_reviews, future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects, pop_tickets, pop_wikipages, \
                                           pop_reviews, pop_vcs
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.system             import SystemComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.xsearch            import XSearchComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 2
no_of_tickets   = 3
no_of_wikis     = 2
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 2
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
liccomp     = None
attcomp     = None
syscomp     = None
projcomp    = None
wikicomp    = None
tckcomp     = None
revcomp     = None
srchcomp    = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, liccomp, attcomp, syscomp, projcomp, wikicomp, \
           tckcomp, revcomp, srchcomp, cachemgr

    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )

    # Clear the index
    indexdir = join( split( split( split( split( abspath(__file__) )[0] )[0])[0] )[0],
                     'defenv', 'data', 'xapian' )
    cmd      = 'rm -f %s/*' % indexdir
    print "   %s" % cmd
    os.system( cmd )

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
    liccomp    = LicenseComponent( compmgr )
    syscomp    = SystemComponent( compmgr )
    attcomp    = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
    revcomp    = ReviewComponent( compmgr )
    srchcomp   = XSearchComponent( compmgr )

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


class TestXSearch( object ) :

    def _validate_query( self, query, prefixes, type, id, assrt=True ) :
        """Verify the match for 'type' and 'id'"""
        matches = srchcomp.query( query, prefixes )
        match   = False
        for m in matches :
            doc   = m.document
            if doc.get_value( 0 ) == type and doc.get_value( 1 ) == str(id) :
                match = True
                break
        assert_equal( match, assrt,
                      'Mismatch for type %s id %s' % (type, id)
                    )

    def test_1_userindex( self ) :
        """Testing user indexing via xapian search engine"""
        log.info( "Testing user indexing via xapian search engine" )

        user  = ( u'testuser', u'testemail@user.com', 'test123', 'UTC' )
        uinfo = ( u'testfname', u'testmname', u'testlname', u'testaddr1',
                  u'testaddr2', u'testcity', u'123456', u'teststate',
                  u'testcountry' )
        u     = userscomp.user_create( user, uinfo )

        # Query and verify
        prefixes = [('', 'XCLASSuser')]
        self._validate_query( 'testuser', prefixes, 'user', u.id )
        self._validate_query( 'testemail', prefixes, 'user', u.id )
        self._validate_query( 'testfname', prefixes, 'user', u.id )
        self._validate_query( 'testmname', prefixes, 'user', u.id )
        self._validate_query( 'testlname', prefixes, 'user', u.id )
        self._validate_query( 'testaddr1', prefixes, 'user', u.id )
        self._validate_query( 'testaddr2', prefixes, 'user', u.id )
        self._validate_query( 'testcity', prefixes, 'user', u.id )
        self._validate_query( 'teststate', prefixes, 'user', u.id )
        self._validate_query( 'testcountry', prefixes, 'user', u.id )

    def test_2_licenseindex( self ) :
        """Testing license indexing via xapian search engine"""
        log.info( "Testing license indexing via xapian search engine" )
        prefixes = [('', 'XCLASSlicense')]

        # Test adding license
        licdet = ( None, u'testlicname', u'test licfidasummary',
                   u'test text summary licfidatext', u'testlicsource' )
        l      = liccomp.create_license( licdet, byuser=g_byuser )

        self._validate_query( 'testlicname', prefixes, 'license', l.id )
        self._validate_query( 'licfidasummary', prefixes, 'license', l.id )
        self._validate_query( 'licfidatext', prefixes, 'license', l.id )
        self._validate_query( 'testlicsource', prefixes, 'license', l.id )

        # Test updating license
        licdet = ( l.id, u'tupdatelicname', u'tupdate licgawasummary',
                   u'update text summary licgawatext', u'tupdatelicsource' )
        liccomp.create_license( licdet, update=True, byuser=g_byuser )

        self._validate_query( 'tupdatelicname', prefixes, 'license', l.id )
        self._validate_query( 'licgawasummary', prefixes, 'license', l.id )
        self._validate_query( 'licgawatext', prefixes, 'license', l.id )
        self._validate_query( 'tupdatelicsource', prefixes, 'license', l.id )

        # Test adding license tags
        liccomp.add_tags( l, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'license', l.id )

        # Test removing license tags
        liccomp.remove_tags( l, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'license', l.id, assrt=False )

    def test_3_attachindex( self ) :
        """Testing attachment indexing via xapian search engine"""
        log.info( "Testing attachment indexing via xapian search engine" )

        prefixes = [('', 'XCLASSattach')]

        class TestFD( object ) :
            def __init__( self, data ) :
                self.data = data 
            def read( self ) :
                return self.data
            def close( self ) :
                return
        
        # Test adding attachment
        a = attcomp.create_attach( u'testfidaname',
                                   TestFD( u'attach fidacontent' ),
                                   uploader='testuser',
                                   summary=u'summary fidasummary'
                                 )

        self._validate_query( 'testfidaname', prefixes, 'attach', a.id )
        self._validate_query( 'fidacontent', prefixes, 'attach', a.id )
        self._validate_query( 'testuser', prefixes, 'attach', a.id )
        self._validate_query( 'fidasummary', prefixes, 'attach', a.id )

        # Test adding attachment tags
        attcomp.add_tags( a, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'attach', a.id )

        # Test removing attachment tags
        attcomp.remove_tags( a, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'attach', a.id, assrt=False )

    def test_4_staticwikiindex( self ) :
        """Testing staticwiki indexing via xapian search engine"""
        log.info( "Testing staticwiki indexing via xapian search engine" )
        prefixes = [('', 'XCLASSstaticwiki')]
        swtype = choice(wikicomp.get_wikitype())
        swiki = syscomp.set_staticwiki( u'test/staticwiki/swfida', 
                                        u'staticwiki fidacontent',
                                        swtype=swtype,
                                        sourceurl=u"http://discoverzeta.com",
                                        byuser=g_byuser 
                                      )
        self._validate_query( 'swfida', prefixes, 'staticwiki', swiki.path )
        self._validate_query( 'fidacontent', prefixes, 'staticwiki', swiki.path )
        self._validate_query( swtype.wiki_typename, prefixes, 'staticwiki', swiki.path )
        self._validate_query( 'discoverzeta', prefixes, 'staticwiki', swiki.path )

    def test_5_projectindex( self ) :
        """Testing project indexing via xapian search engine"""
        log.info( "Testing project indexing via xapian search engine" )

        prefixes = [('', 'XPROJECTtestprojname')]

        # Test creating project
        projdet  = ( 'None', u'testprojname', u'test project fidasummary', 
                     u'fidaadmin@project.com', u'tupdatelicname', u'testuser' )
        p        = projcomp.create_project( projdet, (u'test fidadescription',),
                                            byuser=g_byuser 
                                          )

        self._validate_query( 'testprojname', prefixes, 'project', p.id )
        self._validate_query( 'fidasummary', prefixes, 'project', p.id )
        self._validate_query( 'fidaadmin', prefixes, 'project', p.id )
        self._validate_query( 'tupdatelicname', prefixes, 'project', p.id )
        self._validate_query( 'fidadescription', prefixes, 'project', p.id )

        # Test updating project
        projdet  = ( p.id, u'tupdateprojname', u'test project gawasummary', 
                     u'gawaadmin@project.com', u'tupdatelicname', u'testuser' )
        projcomp.create_project( projdet, (u'test gawadescription',),
                                 update=True, byuser=g_byuser
                               )

        prefixes = [('', 'XPROJECTtupdateprojname')]

        self._validate_query( 'tupdateprojname', prefixes, 'project', p.id )
        self._validate_query( 'gawasummary', prefixes, 'project', p.id )
        self._validate_query( 'gawaadmin', prefixes, 'project', p.id )
        self._validate_query( 'tupdatelicname', prefixes, 'project', p.id )
        self._validate_query( 'gawadescription', prefixes, 'project', p.id )

        # Test configure project
        l = choice( liccomp.get_license() )
        projcomp.config_project( p, license=l, byuser=g_byuser )
        if l.licensename != 'tupdatelicname' :
            self._validate_query(
                'tupdatelicname', prefixes, 'project', p.id, assrt=False )
        self._validate_query( '"%s"' % l.licensename, prefixes, 'project', p.id )

        # Test adding mailing list
        projcomp.set_mailinglists( p, [ u'pmlistfida@project.com' ], byuser=g_byuser )
        self._validate_query( 'pmlistfida', prefixes, 'project', p.id )

        # Test removing mailing list
        projcomp.set_mailinglists( p, [ u'pmlistgawa@project.com' ], byuser=g_byuser )
        self._validate_query( 'pmlistfida', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'pmlistgawa', prefixes, 'project', p.id )


        # Test adding ircchannel
        projcomp.set_ircchannels( p, [ u'pircfida#project.com' ], byuser=g_byuser )
        self._validate_query( 'pircfida#project.com', prefixes, 'project', p.id )

        # Test removing ircchannel
        projcomp.set_ircchannels( p, [ u'pircgawa#project.com' ], byuser=g_byuser )
        # self._validate_query( 'pircfida#project.com', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'pircgawa#project.com', prefixes, 'project', p.id )

        # Test creating component
        compdet = ( None, u'testfidacomp', u'compfidadescription', 'testuser' )
        comp = projcomp.create_component( p, compdet, byuser=g_byuser )
        self._validate_query( 'testfidacomp', prefixes, 'project', p.id )
        self._validate_query( 'compfidadescription', prefixes, 'project', p.id )

        # Test updating component
        compdet = ( comp.id, u'testgawacomp', u'compgawadescription', 'testuser' )
        projcomp.create_component( p, compdet, byuser=g_byuser, update=True )
        self._validate_query( 'testfidacomp', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'testgawacomp', prefixes, 'project', p.id )
        self._validate_query( 'compgawadescription', prefixes, 'project', p.id )

        # Test removing component
        projcomp.remove_component( p, comp, byuser=g_byuser )
        self._validate_query( 'testgawacomp', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'compgawadescription', prefixes, 'project', p.id, assrt=False  )

        # Test creating milestone
        mstndet = ( None, u'testfidamstn', u'mstnfidadescription',
                    dt.datetime( 2009,1,1 )
                  )
        mstn = projcomp.create_milestone( p, mstndet, byuser=g_byuser )
        self._validate_query( 'testfidamstn', prefixes, 'project', p.id )
        self._validate_query( 'mstnfidadescription', prefixes, 'project', p.id )

        # Test updating milestone
        mstndet = ( mstn.id, u'testgawamstn', u'mstngawadescription',
                    dt.datetime( 2009,1,1 )
                  )
        projcomp.create_milestone( p, mstndet, byuser=g_byuser, update=True )
        self._validate_query( 'testfidamstn', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'testgawamstn', prefixes, 'project', p.id )
        self._validate_query( 'mstngawadescription', prefixes, 'project', p.id )

        # Test closing milestone
        projcomp.close_milestone( mstn, u'closefidamstn', byuser=g_byuser )
        self._validate_query( 'closefidamstn', prefixes, 'project', p.id )

        # Test removing milestone
        projcomp.remove_milestone( p, mstn, byuser=g_byuser )
        self._validate_query( 'testgawamstn', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'mstngawadescription', prefixes, 'project', p.id, assrt=False )

        # Test creating version
        verdet = ( None, u'testfidaver', u'verfidadescription' )
        ver = projcomp.create_version( p, verdet, byuser=g_byuser )
        self._validate_query( 'testfidaver', prefixes, 'project', p.id )
        self._validate_query( 'verfidadescription', prefixes, 'project', p.id )

        # Test updating version
        verdet = ( ver.id, u'testgawaver', u'vergawadescription' )
        ver = projcomp.create_version( p, verdet, byuser=g_byuser, update=True )
        self._validate_query( 'testfidaver', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'testgawaver', prefixes, 'project', p.id )
        self._validate_query( 'vergawadescription', prefixes, 'project', p.id )

        # Test removing version
        projcomp.remove_version( p, ver, byuser=g_byuser )
        self._validate_query( 'testgawaver', prefixes, 'project', p.id, assrt=False )
        self._validate_query( 'vergawadescription', prefixes, 'project', p.id, assrt=False )

        # Test adding project user
        user  = choice(userscomp.get_user())
        ttype = choice(projcomp.get_teamtype())
        pt    = projcomp.add_project_user( p, ttype, user, byuser=g_byuser )
        self._validate_query( user.username, prefixes, 'project', p.id )

        # Test removing project user
        projcomp.remove_project_users( pt, byuser=g_byuser )
        self._validate_query( user.username, prefixes, 'project', p.id, assrt=False )

        # Test adding project tags
        projcomp.add_tags( p, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'project', p.id )

        # Test removing project tags
        projcomp.remove_tags( p, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'project', p.id, assrt=False )

    def test_6_ticketindex( self ) :
        """Testing ticket indexing via xapian search engine"""
        log.info( "Testing ticket indexing via xapian search engine" )

        prefixes = [('', 'XCLASSticket')]
        p        = projcomp.get_project( 1 ) 

        # Test creating ticket
        type     = choice( tckcomp.get_tcktype() )
        severity = choice( tckcomp.get_tckseverity() )
        owner    = choice( userscomp.get_user() )
        tckdet   = ( None, u'testtckfida', u'tckfidadescription', type, severity )
        t = tckcomp.create_ticket( p, tckdet, owner=owner, byuser=g_byuser )
        self._validate_query( 'testtckfida', prefixes, 'ticket', t.id )
        self._validate_query( 'tckfidadescription', prefixes, 'ticket', t.id )

        # Test configuring ticket
        comps = p.components and [choice( p.components )] or []
        mstns = p.milestones and [choice( p.milestones )] or []
        vers  = p.versions   and [choice( p.versions )]   or []
        tckcomp.config_ticket( t, components=comps, milestones=mstns,
                               versions=vers, byuser=g_byuser )
        if comps :
            self._validate_query( comps[0].componentname, prefixes, 'ticket', t.id )
        if mstns :
            self._validate_query( mstns[0].milestone_name, prefixes, 'ticket', t.id )
        if vers :
            self._validate_query( vers[0].version_name, prefixes, 'ticket', t.id )

        # Test creating ticket status
        owner = choice( userscomp.get_user() )
        tsdet = ( None, choice( tckcomp.get_tckstatus() ),
                  dt.datetime( 2009, 1, 1 )
                )
        tckcomp.create_ticket_status( t, tsdet, owner, byuser=g_byuser )
        self._validate_query( owner.username, prefixes, 'ticket', t.id )

        # Test creating ticket comment
        commentor = choice( userscomp.get_user() )
        tcmtdet   = ( None,  u'testtckcommentfida', commentor )
        tckcomp.create_ticket_comment( t, tcmtdet, byuser=g_byuser )
        self._validate_query( 'testtckcommentfida',  prefixes, 'ticket', t.id )
        self._validate_query( commentor.username, prefixes, 'ticket', t.id )

        # Test adding tags
        tckcomp.add_tags( t, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'ticket', t.id )

        # Test removing tags
        tckcomp.remove_tags( t, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'ticket', t.id, assrt=False )

    def test_7_wikiindex( self ) :
        """Testing wiki indexing via xapian search engine"""
        log.info( "Testing wiki indexing via xapian search engine" )
        from   zeta.lib.base             import BaseController

        cntlr = BaseController()
        prefixes = [('', 'XCLASSwiki')]
        p        = choice( projcomp.get_project() )
        # Create wiki and wiki contents.
        wikiurl = unicode(cntlr.url_wikiurl( p.projectname, u'WikiFida' ))
        creator = choice( userscomp.get_user() )
        author  = choice( userscomp.get_user() )
        wtype   = choice( wikicomp.get_wikitype() )
        w       = wikicomp.create_wiki( wikiurl, wtype, u'wikifidasummary',
                                        u'http://discoverzeta.com/zwikimarkupx',
                                        creator )
        wikicomp.config_wiki( w, project=p, byuser=g_byuser )
        wikicomp.create_content( w, author, u'wikifidacontent' )

        self._validate_query( creator.username, prefixes, 'wiki', w.id )
        self._validate_query( author.username, prefixes, 'wiki', w.id )
        self._validate_query( 'wikifidasummary', prefixes, 'wiki', w.id )
        self._validate_query( wtype.wiki_typename, prefixes, 'wiki', w.id )
        self._validate_query( 'zwikimarkupx', prefixes, 'wiki', w.id )
        self._validate_query( 'wikifidacontent', prefixes, 'wiki', w.id )

        # Config wiki 
        wikicomp.config_wiki( w, summary=u'wikigawasummary', byuser=g_byuser )
        wikicomp.config_wiki( w,
                              sourceurl=u'http::/discoverzeta.com/zwikimarkupy',
                              byuser=g_byuser )
        self._validate_query( 'wikigawasummary', prefixes, 'wiki', w.id )
        self._validate_query( 'zwikimarkupy', prefixes, 'wiki', w.id )

        # Create wiki comment
        commentby = choice( userscomp.get_user() )
        wcmtdet   = ( None, commentby, 1, u'wikifidacomment' )
        wikicomp.create_wikicomment( w, wcmtdet, byuser=g_byuser )
        self._validate_query( 'wikifidacomment', prefixes, 'wiki', w.id )
        self._validate_query( commentby.username, prefixes, 'wiki', w.id )

        # Test adding tags
        wikicomp.add_tags( w, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'wiki', w.id )

        # Test removing tags
        wikicomp.remove_tags( w, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'wiki', w.id, assrt=False )

    def test_8_reviewindex( self ) :
        """Testing review indexing via xapian search engine"""
        log.info( "Testing review indexing via xapian search engine" )

        prefixes = [('', 'XCLASSreview')]
        p        = choice( projcomp.get_project() )
        # Test creating review
        author    = choice( userscomp.get_user() )
        moderator = choice( userscomp.get_user() )
        revdet    = ( None, u'/some/url/', 1, author, moderator )
        r = revcomp.create_review( p, revdet, byuser=g_byuser )
        self._validate_query( author.username, prefixes, 'review', r.id )
        self._validate_query( moderator.username, prefixes, 'review', r.id )

        # Test setting participants
        participants = [choice( userscomp.get_user() )]
        revcomp.set_participants( r, participants, byuser=g_byuser )
        self._validate_query( participants[0].username, prefixes, 'review', r.id )

        # Test add review comments
        commentor = choice( userscomp.get_user() )
        nature    = choice( revcomp.get_reviewcomment_nature() )
        action    = choice( revcomp.get_reviewcomment_action() )
        rcmtdet = ( None, 10, u'fidareviewcomment', commentor, nature, action )
        revcomp.create_reviewcomment( r, rcmtdet, byuser=g_byuser )
        self._validate_query( commentor.username, prefixes, 'review', r.id )
        self._validate_query( u'fidareviewcomment', prefixes, 'review', r.id )

        # Test adding tags
        revcomp.add_tags( r, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'review', r.id )

        # Test removing tags
        revcomp.remove_tags( r, tags=[u'mongoose'], byuser=g_byuser )
        self._validate_query( 'mongoose', prefixes, 'review', r.id, assrt=False )
