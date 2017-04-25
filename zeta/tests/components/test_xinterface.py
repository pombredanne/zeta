# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

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
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_tickets, pop_wikipages, \
                                           pop_reviews, pop_vcs
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.comp.system             import SystemComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.xinterface         import XInterfaceComponent
from   zeta.tests.tlib              import *
from   zeta.tests.model.generate    import gen_tickets, future_duedate

from   zeta.controllers.xmlrpc      import _result

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
g_byuser        = u'admin'
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 5
no_of_tickets   = 20
no_of_wikis     = 2
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 2

compmgr     = None
userscomp   = None
liccomp     = None
attcomp     = None
syscomp     = None
projcomp    = None
wikicomp    = None
tckcomp     = None
revcomp     = None
xicomp      = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, liccomp, attcomp, syscomp, projcomp, wikicomp, \
           tckcomp, revcomp, xicomp, cachemgr

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
    liccomp    = LicenseComponent( compmgr )
    syscomp    = SystemComponent( compmgr )
    attcomp    = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
    revcomp    = ReviewComponent( compmgr )
    xicomp     = XInterfaceComponent( compmgr )

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
    print "   Populating vcs ( no_of_vcs=%s ) ..." % no_of_vcs
    pop_vcs( no_of_vcs=no_of_vcs, seed=seed )
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
    print "   Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
    pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_reviews=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_reviews )

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


class TestXInterface( object ) :

    def test_1_result( self ) :
        """Testing function _result() composing result value"""
        log.info( "Testing function _result() composing result value" )

        assert_equal( _result( True ),
                      { 'rpcstatus' : 'ok' },
                      'Mismatch in _result while composing +ve result'
                    )

        assert_equal( _result( True, d={ 'key1' : 'value1' } ),
                      { 'rpcstatus' : 'ok', 'key1' : 'value1' },
                      'Mismatch in _result while composing +ve result, with d'
                    )

        assert_equal( _result( False ),
                      { 'rpcstatus' : 'fail', 'message' : '' },
                      'Mismatch in _result while composing +ve result'
                    )

        assert_equal( _result( False, failmsg='Failure reason' ),
                      { 'rpcstatus' : 'fail', 'message' : 'Failure reason' },
                      'Mismatch in _result while composing -ve result, with msg'
                    )

        assert_equal( _result( False, failmsg='Failure reason',
                               d={ 'key1' : 'value1' } ),
                      { 'rpcstatus' : 'fail', 'message' : 'Failure reason',
                        'key1' : 'value1' },
                      'Mismatch in _result while composing +ve result, with msg and d'
                    )

    def test_2_listsw( self ) :
        """Testing method list_sw()"""
        log.info( "Testing method list_sw()" )

        rc, paths, msg = xicomp.list_sw()
        assert_equal( sorted(paths),
                      sorted([ sw.path for sw in syscomp.get_staticwiki() ]),
                      'Mismatch in list_sw()'
                    )

    def test_3_createsw( self ) :
        """Testing method create_sw()"""
        log.info( "Testing method create_sw()" )

        swtype       = choice(wikicomp.get_wikitype())
        sourceurl    = u"http://discoverzeta.com/zwikix"
        cont         = 'some static wiki content'
        rc, sw, msg  = xicomp.create_sw( u'some/path', cont, swtype=swtype,
                                         sourceurl=sourceurl, byuser=g_byuser )
        assert_true( rc, 'Mismatch in create_sw(), `rc`' )
        assert_true( sw, 'Mismatch in create_sw(), `sw`' )
        sw   = syscomp.get_staticwiki( u'some/path' )
        assert_equal( [sw.type.wiki_typename, sw.sourceurl, sw.text],
                      [swtype.wiki_typename, sourceurl, cont],
                      'Mismatch in content, create_sw()' )

        cont ='some static wiki content updated'
        rc, sw, msg = xicomp.create_sw( u'some/path', cont, byuser=g_byuser )
        assert_equal( msg, 'some/path, already exists',
                      'Mismatch in create_sw()' )

    def test_4_readsw( self ) :
        """Testing method read_sw()"""
        log.info( "Testing method read_sw()" )

        sw  = syscomp.get_staticwiki( u'some/path' )
        rc, d, msg = xicomp.read_sw( u'some/path' )
        assert_equal( d,
                      { 'path'      : sw.path,
                        'text'      : sw.text,
                        'texthtml'  : sw.texthtml
                      },
                      'Mismatch in read_sw()'
                    )

        rc, d, msg = xicomp.read_sw( u'some/path/dummy' )
        assert_equal( msg, 'StaticWiki some/path/dummy not found',
                      'Mismatch in read_sw()'
                    )

    def test_5_updatesw( self ) :
        """Testing method update_sw()"""
        log.info( "Testing method update_sw()" )

        swtype       = choice(wikicomp.get_wikitype())
        sourceurl    = u"http://discoverzeta.com/zwikiy"
        cont        = 'Updated static wiki content'
        rc, sw, msg = xicomp.update_sw( u'some/path', cont,
                                        swtype=swtype.wiki_typename,
                                        sourceurl=sourceurl, byuser=g_byuser
                                      )
        assert_true( rc, 'Mismatch in update_sw(), `rc`' )
        assert_true( sw, 'Mismatch in update_sw(), `sw`' )
        sw   = syscomp.get_staticwiki( u'some/path' )
        assert_equal( [sw.type.wiki_typename, sw.sourceurl, sw.text],
                      [swtype.wiki_typename, sourceurl, cont],
                      'Mismatch in updated staticwiki, update_sw()' )

        rc, sw, msg = xicomp.update_sw( u'some/path/dummy', cont, byuser=g_byuser )
        assert_equal( msg, 'Unable to update static wiki some/path/dummy',
                      'Mismatch in update_sw()'
                    )

    def test_6_myprojects( self ) :
        """Testing method myprojects()"""
        log.info( "Testing method myprojects()" )

        users = userscomp.get_user()
        user  = choice( users )

        # Test system 
        _rc, entries, _msg = xicomp.system()
        assert_equal( entries, syscomp.get_sysentry(), 'Mismatch in system()' )

        # Test Valid case
        _rc, projnames, _msg = xicomp.myprojects( user )
        assert_equal( projnames, sorted( h.myprojects( user )),
                      'Mismatch while valid call to myprojects()'
                    )

        # Test projecdetails()
        p = choice( projcomp.get_project() )
        _rc, d, _msg      = xicomp.projectdetails( p.projectname )
        d['components']   = sorted( d['components'], key=lambda i : i[0] )
        d['milestones']   = sorted( d['milestones'], key=lambda i : i[0] )
        d['versions']     = sorted( d['versions'], key=lambda i : i[0] )
        d['projectusers'] = sorted( d['projectusers'] )
        assert_equal(
            d,
            { 'components'   : sorted([ (comp.id, comp.componentname) for comp in p.components ],
                                      key=lambda i : i[0]),
              'milestones'   : sorted([ (m.id, m.milestone_name) for m in p.milestones ],
                                      key=lambda i : i[0]),
              'versions'     : sorted([ (v.id, v.version_name) for v in p.versions ],
                                      key=lambda i : i[0]),
              'projectusers' : sorted( projcomp.projusernames(p) ),
            },
            'Mismatch in projectdetails()'
        )
                      
    def test_7_listwiki( self ) :
        """Testing method list_wiki()"""
        log.info( "Testing method list_wiki()" )

        projects = projcomp.get_project()

        # For valid project
        p                  = choice( projects )
        rc, wikipages, msg = xicomp.list_wiki( p.projectname )
        assert_equal( sorted(wikipages),
                      sorted([ h.wiki_parseurl( w.wikiurl ) for w in p.wikis ]),
                      'Mismatch for valid call to list_wiki()'
                    )

        # For invalid project
        rc, wikipages, msg = xicomp.list_wiki( u'invalidproject' )
        assert_equal( wikipages, [],
                      'Mismatch for invalid call to list_wiki()'
                    )

    def test_7_wiki( self ) :
        """Testing method create_wiki(), read_wiki(), update_wiki()"""
        log.info(  "Testing method create_wiki()" )
        from   zeta.lib.base             import BaseController

        cntlr = BaseController()
        projects = projcomp.get_project()
        url      = u'path/someUrl'

        # Create a new wiki page
        p       = choice(projects)
        wikiurl = unicode(cntlr.url_wikiurl( p.projectname, url ))
        wtype   = u'iframe'
        summ    = choice([ u'summary for this wiki page', None, u'' ])
        srcurl  = choice([ 'http://discoverzeta/zwiki', None, u'' ])
        if summ == None :
            summ = u''
        rc, w, msg = xicomp.create_wiki(
                        p.projectname, wikiurl, wtype=wtype, summary=summ,
                        sourceurl=srcurl, byuser=g_byuser
                     )
        assert_true( rc, 'Mismatch in valid call to create_wiki()' )

        # Try creating existing wiki
        rc, w, msg = xicomp.create_wiki(
                        p.projectname, wikiurl, wtype=u'draft',
                        summary=u'summary for this wiki page', byuser=g_byuser
                     )
        assert_equal( msg, 'wiki page, %s already exists' % wikiurl,
                      'Mismatch in invalid call to create_wiki()'
                    )

        # Update existing wiki page
        cont       = u'Content for this wiki page'
        rc, w, msg = xicomp.update_wiki( p.projectname, wikiurl, cont, g_byuser)
        assert_true( rc, 'Mismatch in valid call to update_wiki()' )

        # Try updating a invalid wiki page
        rc, w, msg = xicomp.update_wiki(
                                p.projectname, u'invalid/Wikipage',
                                u'Content for invalid wiki page', g_byuser
                     )
        assert_equal( msg, 'wiki page, invalid/Wikipage does not exist',
                      'Mismatch in invalid call to update_wiki()'
                    )

        # Read wiki page.
        rc, d, msg = xicomp.read_wiki( p.projectname, wikiurl )
        srcurl = u'' if srcurl == None else srcurl
        assert_equal( d,
                      { 'type'      : wtype,
                        'summary'   : summ,
                        'sourceurl' : srcurl,
                        'text'      : cont
                      },
                      'Mismatch in valid call to read_wiki()'
                    )

        # Read non existing wiki page.
        rc, d, msg = xicomp.read_wiki( p.projectname, u'invalid/Url' )
        assert_equal( msg, 'Unable to read wiki page, invalid/Url',
                      'Mismatch in invalid call to read_wiki()'
                    )

        # Comment on wiki
        wiki        = wikicomp.get_wiki( wikiurl )
        comment     = u'Commenting on the wiki page'
        user        = choice( userscomp.get_user() )
        rc, wc, msg = xicomp.comment_wiki( p.projectname, wikiurl, comment, user )
        assert_true( rc, 'Mismatch in creating a valid wiki comment' )

        # Comment on invalid wiki
        rc, wc, msg = xicomp.comment_wiki( p.projectname, u'invalid/Url',
                                           u'Invalid comment', user )
        assert_equal( msg, 'Invalid wiki page, invalid/Url',
                      'Mismatch in creating comment on invalid wiki page'
                    )
                                
    def test_8_configwiki( self ) :
        """Testing config_wiki() method"""
        log.info( "Testing config_wiki() method" )

        w = choice( wikicomp.get_wiki() )
        p = w.project
        wtype = u'iframe'
        summ = u'Summary updated via configwiki'
        srcurl = 'http://discoverzeta/zwiki'
        rc, w, msg  = xicomp.config_wiki( p.projectname, w.wikiurl, wtype=wtype,
                                          summary=summ, sourceurl=srcurl,
                                          byuser=g_byuser )
        assert_true( rc, 'Mismatch in valid config_wiki()' )
        w = wikicomp.get_wiki( w.id )
        assert_equal( [ w.type.wiki_typename, w.summary, w.sourceurl ],
                      [ wtype, summ, srcurl ],
                      'Properties not updated via config_wiki()'
                    )

        # Config wiki for invalid wiki page
        rc, w, msg = xicomp.config_wiki( p.projectname, u'invalid/Url', wtype,
                                         summ, byuser=g_byuser )
        assert_equal( msg, 'Invalid wiki page, invalid/Url',
                      'Mismatch in config_wiki for invalid wiki page'
                    )

    def test_9_wikitags( self ) :
        """Testing wiki_tags() method"""
        log.info( "Testing wiki_tags() method" )

        w = choice( wikicomp.get_wiki() )
        u = choice( userscomp.get_user() )
        p = w.project

        # Add tags to wiki page
        addtags    = [ u'hello', u'world' ]
        rc, w, msg = xicomp.wiki_tags( p.projectname, w.wikiurl, addtags=addtags,
                                       byuser=u )
        assert_true( rc, 'Mismatch in wiki_tags()' )
        w = wikicomp.get_wiki( w.id )
        assert_true( 'hello' in [ t.tagname for t in w.tags ],
                     'Mismatch, added tags not found in wiki tags'
                   )
        assert_true( 'world' in [ t.tagname for t in w.tags ],
                     'Mismatch, added tags not found in wiki tags'
                   )
        
        # Delete tags in wiki page
        deltags    = [ u'hello', u'world' ]
        rc, w, msg = xicomp.wiki_tags( p.projectname, w.wikiurl, deltags=deltags,
                                       byuser=u )
        assert_true( rc, 'Mismatch in wiki_tags()' )
        w = wikicomp.get_wiki( w.id )
        assert_true( 'hello' not in [ t.tagname for t in w.tags ],
                     'Mismatch, deleted tags found in wiki tags'
                   )
        assert_true( 'world' not in [ t.tagname for t in w.tags ],
                     'Mismatch, deleted tags found in wiki tags'
                   )

        # Try adding/deleting tags for invalid wiki page
        rc, w, msg = xicomp.wiki_tags(
                                p.projectname, u'invalid/Url', 
                                addtags=['hello', 'world'],
                                deltags=['hello', 'world'],
                                byuser=u
                     )
        assert_equal( msg, 'Invalid wiki page, invalid/Url',
                      'Mismatch in invalid call to wik_tags()'
                    )

    def test_A_wikivote( self ) :
        """Testing wikivote() method"""
        log.info( "Testing wikivote() method" )

        w = choice( wikicomp.get_wiki() )
        p = w.project
        u = choice( userscomp.get_user() )

        # Upvote
        rc, w, msg = xicomp.wiki_vote( p.projectname, w.wikiurl, 'up', u )
        assert_true( rc, 'Mismatch in wiki_vote()' )

        # Downvote
        rc, w, msg = xicomp.wiki_vote( p.projectname, w.wikiurl, 'down', u )
        assert_true( rc, 'Mismatch in wiki_vote()' )

        # Vote invalid wiki
        rc, w, msg = xicomp.wiki_vote( p.projectname, u'invalid/Url', 'up', u )
        assert_equal( msg, 'Invalid wiki page, invalid/Url',
                      'Mismatch in invalid call to wik_vote()'
                    )

    def test_B_wikifav( self ) :
        """Testing wikifav() method()"""
        log.info( "Testing wikifav() method()" )

        w = choice( wikicomp.get_wiki() )
        p = w.project
        u = choice( userscomp.get_user() )

        # Add as favorite
        rc, w, msg = xicomp.wiki_fav( p.projectname, w.wikiurl, True, u )
        assert_true( rc, 'Mismatch in wiki_fav()' )
        u = userscomp.get_user( u.id )
        assert_true( w in u.favoritewikis, 'Mismatch in wiki favorite' )

        # Delete from favorites
        rc, w, msg = xicomp.wiki_fav( p.projectname, w.wikiurl, False, u )
        assert_true( rc, 'Mismatch in wiki_fav()' )
        u = userscomp.get_user( u.id )
        assert_true( w not in u.favoritewikis, 'Mismatch in wiki favorites' )

        # Favorites for invalid wiki page
        rc, w, msg = xicomp.wiki_fav( p.projectname, u'invalid/Url', True, u )
        assert_equal( msg, 'Invalid wiki page, invalid/Url',
                      'Mismatch in invalid call to wik_fav()'
                    )

    def test_C_ticket( self ) :
        """Testing method list, create, read, update, comment, tag, vote,
        favorite tickets"""
        log.info( "Testing method list, create, read, update, comment, tag, vote, favorite tickets" )

        projects = projcomp.get_project()
        # Check ticket listing
        p   = choice( projects )
        rc, d, msg = xicomp.list_ticket( p.projectname )
        assert_equal( d, { 'tickets' : dict([ (str(t.id), (t.summary,)) 
                                              for t in p.tickets ])
                         },
                      'Mismatch in list_tickets()'
                    )

        # Create a ticket
        tickets = tckcomp.get_ticket()
        p     = choice( projects )
        u     = choice( userscomp.get_user() )
        summ  = u'Some summary to create_ticket'
        type  = choice( tckcomp.get_tcktype() ).tck_typename
        sevr  = choice( tckcomp.get_tckseverity() ).tck_severityname
        desc  = u'Some description to create_ticket'
        comps = p.components and [ choice(p.components).id ]
        mstns = p.milestones and [ choice(p.milestones).id ]
        vers  = p.versions and [ choice(p.versions).id ]
        blkng = [ choice( tickets ).id ]
        blkby = [ choice( tickets ).id ]
        parent= choice( tickets ).id
        rc, d, failmsg = xicomp.create_ticket(
                                    p.projectname, summ, type, sevr, u,
                                    description=desc,
                                    components=comps and comps or None,
                                    milestones=mstns and mstns or None,
                                    versions=vers and vers or None,
                                    blocking=blkng, blockedby=blkby,
                                    parent=parent
                         )
        t = tckcomp.get_ticket()[-1]
        assert_equal( d, { 'id' : t.id }, 'Mismatch in create_ticket()' )
        assert_equal( [ summ, desc, type, sevr, u,
                        comps, mstns, vers, blkng, blkby, parent ],
                      [ t.summary, t.description, t.type.tck_typename,
                        t.severity.tck_severityname, t.statushistory[-1].owner,
                        [ comp.id for comp in t.components ],
                        [ m.id for m in t.milestones ],
                        [ v.id for v in t.versions ],
                        [ tbg.id for tbg in t.blocking ],
                        [ tby.id for tby in t.blockedby ],
                        t.parent.id,
                      ],
                      'Mismatch in create_ticket()'
                    )

        # Config ticket
        p = choice( projects )
        conftcks  = tckcomp.get_ticket()
        projusers = projcomp.projusernames( p ) + [ p.admin.username ]
        for t in p.tickets :
            owner = choice( projusers )
            comp  = p.components and choice( p.components )
            mstn  = p.milestones and choice( p.milestones )
            ver   = p.versions and choice( p.versions )
            blkng = conftcks and conftcks.pop(0).id
            blkby = conftcks and conftcks.pop(0).id
            parent= (conftcks and conftcks.pop(0).id) or None
            fields = { 'summary'     : u'config_ticket summary',
                       'description' : u'config_ticket description',
                       'type'        : choice( tckcomp.get_tcktype() ).tck_typename,
                       'severity'    : choice( tckcomp.get_tckseverity() ).tck_severityname,
                       'promptuser'  : choice( choice(projusers) ),
                       'components'  : comp and [ comp.id ] or [] ,
                       'milestones'  : mstn and [ mstn.id ] or [],
                       'versions'    : ver and [ ver.id ] or [],
                       'blocking'    : [ blkng ],
                       'blockedby'   : [ blkby ],
                       'parent'      : parent,
                     }
            status   = choice( tckcomp.get_tckstatus() ).tck_statusname
            due_date = future_duedate( *dt.datetime.utcnow().timetuple() )
            sfields  = { 'status' : status, 'due_date' : due_date }

            kwargs = dict([ (k, fields[k]) for k in fields.keys() if choice([ 0, 1 ]) ])
            choice([0, 1]) and kwargs.update( sfields )

            kwargs['byuser'] = userscomp.get_user( owner )
            rc, t, msg = xicomp.config_ticket( p.projectname, t, owner, **kwargs )
            assert_true( rc, 'Mismatch in config_ticket()' )

        # Read ticket
        p = choice( projects )
        for t in p.tickets :
            rc, d, msg = xicomp.read_ticket( p.projectname, t.id )
            ref = tckcomp.ticketdetails( t )
            ref.update({
                'blockedby' : tckcomp.blockersof( t ),
                'blocking'  : tckcomp.blockingfor( t ),
                'children'  : tckcomp.childrenfor( t ),
            })
            assert_equal( sorted(d.keys()), sorted(ref.keys()),
                          'Mismatch in read_ticket(), items' )
            for k in ref :
                if d[k] == '' and ref[k] == None : continue
                assert_equal( d[k], ref[k], 'Mismatch in read_ticket()' )

        rc, d, msg = xicomp.read_ticket( p.projectname, 10000 )
        assert_equal( msg, 'Invalid ticket, 10000',
                      'Mismatch for invalid call to read_ticket()'
                    )

        # Comment ticket
        p         = choice( projects )
        projusers = projcomp.projusernames( p ) + [ p.admin.username ]
        for t in p.tickets :
            cmt = u'Comment on ticket %s' % t.id
            cmtr= choice( projusers )
            rc, tc, msg = xicomp.comment_ticket( p.projectname, t.id, cmt, cmtr )
            assert_true( rc, 'Mismatch in comment_ticket()' )
        if p.tickets :
            rc, tc, msg = xicomp.comment_ticket( p.projectname, 10000, cmt, cmtr )
            assert_equal( msg, 'Invalid ticket, 10000',
                          'Mismatch for invalid call to comment_ticket()'
                        )

        # Tags, votes, favs
        p = choice( projects )
        projusers = projcomp.projusernames( p ) + [ p.admin.username ]
        for t in p.tickets :
            # Add tags to ticket page
            addtags     = [ u'hello', u'world' ]
            user        = userscomp.get_user( choice( projusers ))
            rc, t, msg = xicomp.ticket_tags( p.projectname, t.id,
                                             addtags=addtags, byuser=user )
            assert_true( rc, 'Mismatch in ticket_tags()')
            t = tckcomp.get_ticket( t.id )
            assert_true( 'hello' in [ tag.tagname for tag in t.tags ],
                         'Mismatch, added tags not found in ticket tags'
                       )
            assert_true( 'world' in [ tag.tagname for tag in t.tags ],
                         'Mismatch, added tags not found in ticket tags'
                       )
        
            # Delete tags in ticket page
            deltags    = [ u'hello', u'world' ]
            rc, t, msg = xicomp.ticket_tags( p.projectname, t.id,
                                             deltags=deltags, byuser=user )
            assert_true( rc, 'Mismatch in ticket_tags()' )
            t = tckcomp.get_ticket( t.id )
            assert_true( 'hello' not in [ tag.tagname for tag in t.tags ],
                         'Mismatch, deleted tags found in ticket tags'
                       )
            assert_true( 'world' not in [ tag.tagname for tag in t.tags ],
                         'Mismatch, deleted tags found in ticket tags'
                       )

            # Try adding/deleting tags for invalid ticket page
            rc, _t, msg = xicomp.ticket_tags( p.projectname, 10000,
                                              addtags=['hello', 'world'],
                                              deltags=['hello', 'world'],
                                              byuser=user
                                           )
            assert_equal( msg, 'Invalid ticket, 10000',
                          'Mismatch in invalid call to ticket_tags()'
                        )

            # Upvote
            rc, t, msg = xicomp.ticket_vote( p.projectname, t.id, u'up', user )
            assert_true( rc, 'Mismatch in ticket_vote()' )

            # Downvote
            rc, t, msg = xicomp.ticket_vote( p.projectname, t.id, u'down', user )
            assert_true( rc, 'Mismatch in ticket_vote()' )

            # Vote invalid ticket
            rc, _t, msg = xicomp.ticket_vote( p.projectname, 10000, u'up', user )
            assert_equal( msg, 'Invalid ticket, 10000',
                          'Mismatch in invalid call to ticket_vote()'
                        )

            # Add as favorite
            rc, t, msg = xicomp.ticket_fav( p.projectname, t.id, True, user )
            assert_true( rc, 'Mismatch in ticket_fav()' )
            user = userscomp.get_user( user.id )
            assert_true( t in user.favoritetickets, 'Mismatch in ticket favorite' )

            # Delete from favorites
            rc, t, msg = xicomp.ticket_fav( p.projectname, t.id, False, user )
            assert_true( rc, 'Mismatch in ticket_fav()' )
            user = userscomp.get_user( user.id )
            assert_true( t not in user.favoritetickets, 'Mismatch in ticket favorites' )

            # Favorites for invalid ticket
            rc, _t, msg = xicomp.ticket_fav( p.projectname, 10000,  True, user )
            assert_equal( msg, 'Invalid ticket, 10000',
                          'Mismatch in invalid call to ticket_fav()'
                        )
