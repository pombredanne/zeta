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

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_wikipages
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.vote               import VoteComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 5
no_of_attachs   = 1
no_of_projects  = 5
no_of_wikis     = 50
g_byuser        = u'admin'

tagchars   = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
taglist     = None 

compmgr     = None
userscomp   = None
attachcomp  = None
tagcomp     = None
liccomp     = None
projcomp    = None
wikicomp    = None
votcomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, tagcomp, liccomp, projcomp, \
           wikicomp, votcomp, taglist, seed, cachemgr

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
    wikicomp   = WikiComponent( compmgr )
    votcomp    = VoteComponent( compmgr )
    taglist = [ unicode(h.randomname( randint(0,LEN_TAGNAME), tagchars))
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
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_wikis=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_wikis )

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


class TestWikiForms( object ) :

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

    def test_1_createwiki_valid( self ) :
        """Testing FormCreateWiki with valid input"""
        log.info( "Testing FormCreateWiki with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createwiki' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        u            = choice( users )
        p            = choice( projects )
        types        = wikicomp.get_wikitype()

        # Create a wiki page
        c.rclose = h.ZResp()
        wikiurl      = u'some wiki url'
        type         = choice( types )
        creator      = choice( users )
        sourceurl    = u"http://discoverzeta.com/zwiki"
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wikiurl', wikiurl )
        request.POST.add( 'wiki_typename', type.wiki_typename )
        request.POST.add( 'sourceurl', sourceurl )
        request.POST.add( 'creator', creator.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createwiki'] )

        self._validate_defer(
                creator, defer, c,
                lambda _u : 'created the wiki page' in _u.logs[-1].log
        )

        w = wikicomp.get_wiki(sorted([ w.id for w in wikicomp.get_wiki() ])[-1])
        assert_equal( [ wikiurl, type.wiki_typename, sourceurl, creator.username ],
                      [ w.wikiurl, w.type.wiki_typename, w.sourceurl,
                        w.creator.username ],
                      'Mismatch in creating wiki page'
                    )

        # Create a second wiki page
        request.POST.clearfields()
        wikiurl      = u'second wiki url'
        type         = choice( types )
        creator      = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wikiurl', wikiurl )
        request.POST.add( 'wiki_typename', type.wiki_typename )
        request.POST.add( 'creator', creator.username )
        vf.process( request, c )
        w = wikicomp.get_wiki(sorted([ w.id for w in wikicomp.get_wiki() ])[-1])
        assert_equal( [ wikiurl, type.wiki_typename, creator.username ],
                      [ w.wikiurl, w.type.wiki_typename, w.creator.username ],
                      'Mismatch in creating wiki page'
                    )

    def test_2_createwiki_invalid( self ) :
        """Testing FormCreateWiki with invalid input"""
        log.info( "Testing FormCreateWiki with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createwiki' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        p        = choice( projects )
        types    = wikicomp.get_wikitype()
        # Try creating wiki page with in sufficient data
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        wikiurl      = u'some wiki url'
        request.POST.add( 'wikiurl', wikiurl )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )
        type         = choice( types )
        request.POST.add( 'wiki_typename', type.wiki_typename )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )
        # Try creating wiki page with in-sufficient data
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        wikiurl      = u'some wiki url'
        request.POST.add( 'wikiurl', wikiurl )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )
        type         = choice( types )
        request.POST.add( 'wiki_typename', type.wiki_typename )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )

    def test_3_configwiki( self ) :
        """Testing FormConfigWiki with valid and invalid input"""
        log.info( "Testing FormConfigWiki with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        types    = wikicomp.get_wikitype()

        # Randomly config wiki.
        c.rclose = h.ZResp()
        w       = wikicomp.get_wiki( u'some wiki url' )
        p       = choice( projects + [ None ] * 5 )
        type    = choice( types + [ None ] * 5 )
        summary = choice([ u'some wiki summary' ] + [ None ] * 5 )
        sourceurl = choice([u"http://discoverzeta.com/zwikimarkup"] + [None]*5 )
        formname= choice([ 'configwiki', 'wikitype', 'wikisummary',
                           'wikisourceurl' ])
        request.params.add( 'formname', formname )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        type    and request.POST.add( 'wiki_typename', type.wiki_typename )
        summary and request.POST.add( 'summary', summary )
        sourceurl and request.POST.add( 'sourceurl', sourceurl )
        p       and request.POST.add( 'project_id', str(p.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=[formname] )

        if summary or sourceurl :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda _u : 'Changed,' in _u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        if type :
            assert_equal( type.wiki_typename, w.type.wiki_typename,
                          'Mismatch in configuring wiki type' )
        if summary :
            assert_equal( summary, w.summary,
                          'Mismatch in configuring wiki summary' )
        if sourceurl :
            assert_equal( sourceurl, w.sourceurl,
                          'Mismatch in configuring wiki sourceurl' )
        if p :
            assert_equal( p.projectname, w.project.projectname,
                          'Mismatch in configuring wiki project' )

    def test_4_wikicontent_valid( self ) :
        """Testing FormWikiContent with valid input"""
        log.info( "Testing FormWikiContent with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'wikicont' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        p        = choice( projects )

        # Create wiki content
        c.rclose = h.ZResp()
        w = wikicomp.get_wiki( u'some wiki url' )
        text = u"some wiki content for - 'some wiki url'"
        author = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'author', author.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['wikicont'] )

        self._validate_defer(
                author, defer, c,
                lambda _u : 'updated wiki content to version' in _u.logs[-1].log 
        )

        wp = wikicomp.get_content( w.id ) # Get latest wiki content
        wp_version = wp.id
        assert_equal( [ text, author.username ],
                      [ wp.text, wp.author ],
                      'Mismatch while creating wikipage content'
                    )

        # Creat second wiki content.
        request.POST.clearfields()
        text     = u"second wiki content for - 'some wiki url'"
        author   = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'author', author.username )
        vf.process( request, c )
        wp       = wikicomp.get_content( w.id ) # Get latest wiki content
        assert_equal( [ text, author.username ],
                      [ wp.text, wp.author ],
                      'Mismatch while creating wikipage content'
                    )
        # Get the specified version
        wp       = wikicomp.get_content( w.id, version=wp_version )

        # Update wiki content
        c.rclose = h.ZResp()
        request.POST.clearfields()
        text     = u"updated wiki content for - 'some wiki url'"
        author   = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'author', author.username )
        request.POST.add( 'version_id', str(wp_version) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['wikicont'] )

        self._validate_defer(
                author, defer, c,
                lambda _u : 'updated existing wiki version' in _u.logs[-1].log 
        )

        # Get the specified version
        wp       = wikicomp.get_content( w.id, version=wp_version )
        assert_equal( [ text, author.username ],
                      [ wp.text, wp.author ],
                      'Mismatch while updating wikipage content'
                    )

    def test_5_wikicontent_invalid( self ) :
        """Testing FormWikiContent with invalid input"""
        log.info( "Testing FormWikiContent with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'wikicont' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        p        = choice( projects )

        # Create wiki content
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        w        = wikicomp.get_wiki( u'some wiki url' )
        request.POST.add( 'wiki_id', str(w.id) )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )
        text     = u"some wiki content for - 'some wiki url'"
        request.POST.add( 'text', text )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c
                     )

    def test_6_removewikicontent( self ) :
        """Testing FormRemoveWikiContent with valid and invalid input"""
        log.info( "Testing FormRemoveWikiContent with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmwikicont' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )

        # Create wiki content
        c.rclose = h.ZResp()
        w = wikicomp.get_wiki( u'some wiki url' )
        wpages = wikicomp.get_content( w.id, all=True ) # Get all versions
        assert_true( len(wpages) == 2, 'Mismatch in no of created wiki contents' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'version_id', str(wpages[1].id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['rmwikicont'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'removed wiki page version' in _u.logs[-1].log 
        )

        wpages   = wikicomp.get_content( w.id, all=True ) # Get all versions
        assert_true( len(wpages) == 1, 'Mismatch in no of removed wiki contents' )

    def test_7_wikiredirect( self ) :
        """Testing FormWikiRedirect with valid and invalid input"""
        log.info( "Testing FormWikiRedirect with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'wikiredir' )

        users = userscomp.get_user()
        projects = projcomp.get_project()

        # Create a new wiki page
        u = choice( users )
        p = choice( projects )
        w = wikicomp.get_wiki( u'second wiki url' )
        target_w = wikicomp.get_wiki( u'some wiki url' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'wiki_target', str(target_w.id) )
        vf.process( request, c )
        wpages        = wikicomp.get_content( w.id, all=True ) # Get all versions
        target_wpages = wikicomp.get_content( target_w.id, all=True )
        assert_equal( target_wpages, wpages,
                      'Mismatch in wiki redirection' )

    def test_8_createwikicomment_valid( self ) :
        """Testing FormCreateWikiComment with valid input"""
        log.info( "Testing FormCreateWikiComment with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createwcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u = choice( users )
        p = choice( projects )
        w = wikicomp.get_wiki( u'some wiki url' )
        wpages   = wikicomp.get_content( w, all=True ) # Get all versions

        # Create wiki comment
        c.rclose = h.ZResp()
        text = u'some wiki comment'
        commentby  = choice( users )
        version_id = randint( 1, len(wpages) )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        request.POST.add( 'version_id', str(version_id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createwcmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'commented as,' in _u.logs[-1].log 
        )

        w = wikicomp.get_wiki( u'some wiki url' )
        wc = w.comments[-1]
        assert_equal( [ text, commentby.username, version_id ],
                      [ wc.text, wc.commentby.username, wc.version_id ],
                      'Mismatch in creating wiki comment'
                    )

        # Update wiki comment
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updatewcmt' )
        request.POST.clearfields()
        text = u'updated wiki comment'
        commentby = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'wiki_comment_id', str(wc.id) )
        request.POST.add( 'version_id', str(version_id) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['updatewcmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'updated comment,' in _u.logs[-1].log 
        )

        w        = wikicomp.get_wiki( u'some wiki url' )
        wc       = w.comments[-1]
        assert_equal( len( w.comments ), 1,
                      'Created a new wiki comment while updating an existing one'
                    )
        assert_equal( [ text, commentby.username, version_id ],
                      [ wc.text, wc.commentby.username, wc.version_id ],
                      'Mismatch in updating wiki comment'
                    )

    def test_9_createwikicomment_invalid( self ) :
        """Testing FormCreateWikiComment with invalid input"""
        log.info( "Testing FormCreateWikiComment with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createwcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u = choice( users )
        p = choice( projects )
        w = wikicomp.get_wiki( u'some wiki url' )
        wpages   = wikicomp.get_content( w, all=True ) # Get all versions

        # Create wiki comment
        c.rclose = h.ZResp()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        text       = u'some wiki comment'
        request.POST.add( 'text', text )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createwcmt']
                     )
        commentby  = choice( users )
        request.POST.add( 'commentby', commentby.username )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createwcmt']
                     )

    def test_A_wikicommentreplies( self ) :
        """Testing wiki comment replies with valid and invalid input"""
        log.info( "Testing wiki comment replies with valid and invalid input")
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'replywcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        p        = choice( projects )
        w        = wikicomp.get_wiki( u'some wiki url' )
        wpages   = wikicomp.get_content( w.id, all=True ) # Get the latest version
        wc       = w.comments[-1]

        # Create wiki comment
        text       = u'wiki comment as reply'
        commentby  = choice( users )
        version_id = randint( 1, len(wpages) )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'version_id', str(len(wpages)) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        request.POST.add( 'replytocomment_id', str(wc.id) )
        vf.process( request, c )
        wc        = wikicomp.get_wikicomment( wc.id )
        assert_equal( len( wc.replies ), 1,
                      'Mismatch in no of replies'
                    )
        assert_equal( wc.replies[0].text, text,
                      'Mismatch in reply comment text'
                    )


    def test_B_wikitags( self ) :
        """Testing FormWikiTags with valid and invalid input"""
        log.info( "Testing FormWikiTags with valid and invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        wikis    = wikicomp.get_wiki()
        u        = choice( users )
        p        = choice( projects )
        w        = wikicomp.get_wiki( u'some wiki url' )

        # Add tags to wiki.
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addwikitags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda t : tagcomp.is_tagnamevalid(t),
                                tagnames ) + \
                        [ tag.tagname for tag in w.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addwikitags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'added tags,' in _u.logs[-1].log 
        )

        w = wikicomp.get_wiki( w.id )
        assert_equal( sorted(reftags),
                      sorted([ tag.tagname for tag in w.tags ]),
                      'Mismatch while creating tags'
                    )

        # Delete tags to wiki.
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delwikitags' )
        rmtag     = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'tags', rmtag )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['delwikitags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'deleted tags,' in _u.logs[-1].log 
        )
        
        w = wikicomp.get_wiki( w.id )
        assert_equal( sorted(reftags),
                      sorted([ tag.tagname for tag in w.tags ]),
                      'Mismatch while deleting tags'
                    )

    def test_C_wikiattachs( self ) :
        """Testing FormWikiAttachs with valid and invalid input"""
        log.info( "Testing FormWikiAttachs with valid and invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        wikis    = wikicomp.get_wiki()
        u = choice( users )
        p = choice( projects )
        w = wikicomp.get_wiki( u'some wiki url' )

        # Clean attachments in wiki
        [ wikicomp.remove_attach( w, attach ) for attach in w.attachments ]

        # Add attachments
        c.rclose = h.ZResp()
        user    = choice( users )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addwikiattachs' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'project_id', str(p.id) )
        attachmentfiles = []
        for i in range(randint(0,3)) :
            attach          = FileObject()
            attachfile      = choice( attachfiles )
            attach.filename = os.path.basename( attachfile )
            attach.file     = open( attachfile, 'r' )
            request.POST.add( 'attachfile', attach  )
            attachmentfiles.append( attach )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['addwikiattachs'] )

        if attachmentfiles :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda _u : 'uploaded attachment' in _u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        w = wikicomp.get_wiki( w.id )
        assert_equal( sorted([ a.filename for a in w.attachments ]),
                      sorted([ attach.filename for attach in attachmentfiles ]),
                      'Mismatch in adding wiki attachment'
                    )

        # Remove attachments
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delwikiattachs' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        [ request.POST.add( 'attach_id', str(a.id) ) for a in w.attachments ]
        defer = choice([True, False])
        vf.process( request, c, removeattach=True, defer=defer,
                    formnames=['delwikiattachs'] )

        if w.attachments :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda _u : 'deleted attachment' in _u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        w = wikicomp.get_wiki( w.id )
        assert_false( w.attachments,
                      'Mismatch in removing wiki attachment' )

    def test_D_wikidiff( self ) :
        """Testing FormWikiDiff with valid and invalid inputs"""
        log.info( "Testing FormWikiDiff with valid and invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        wikis    = wikicomp.get_wiki()
        u        = choice( users )
        p        = choice( projects )
        w        = choice(wikis)

        # Test with valid inputs
        wcnt_oldver = choice(wikicomp.get_content( w, all=True ))
        wcnt_newver = wikicomp.get_content( w )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'wikidiff' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'oldver', str(wcnt_oldver.id) )
        request.POST.add( 'newver', str(wcnt_newver.id) )
        vf.process( request, c )
        assert_true( c.oldver == wcnt_oldver.id,
                     'Mismatch in oldversion while wiki diffing' )
        assert_true( c.newver == wcnt_newver.id,
                     'Mismatch in newversion while wiki diffing' )

        # Test with invalid inputs
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'oldver', str(wcnt_oldver.id) )
        vf.process( request, c )
        assert_true( c.oldver == wcnt_oldver.id,
                     'Mismatch in oldversion while wiki diffing' )
        assert_false( c.newver, 'newver while wiki diffing is not None' )

        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'newver', str(wcnt_newver.id) )
        vf.process( request, c )
        assert_false( c.oldver, 'oldver while wiki diffing is not None' )
        assert_true( c.newver == wcnt_newver.id,
                     'Mismatch in newversion while wiki diffing' )
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        vf.process( request, c )
        assert_false( c.oldver, 'oldver while wiki diffing is not None' )
        assert_false( c.newver, 'newver while wiki diffing is not None' )

    def test_E_wikifavorites( self ) :
        """Testing FormWikiFavorite with valid and invalid inputs"""
        log.info( "Testing FormWikiFavorite with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        wikis    = wikicomp.get_wiki()
        user     = choice( users )
        p        = choice( projects )
        w        = choice( wikis )

        wikicomp.delfavorites( w, w.favoriteof, byuser=g_byuser )

        # Add favorite user
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'wikifav' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'addfavuser', user.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['wikifav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'added wiki page as favorite' in _u.logs[-1].log
        )

        assert_equal( wikicomp.get_wiki( w.id ).favoriteof, [ user ],
                      'Mismatch in adding favorite user for wiki'
                    )

        # Del favorite user
        c.rclose = h.ZResp()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'delfavuser', user.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['wikifav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'removed wiki page from favorite' in _u.logs[-1].log
        )

        assert_equal( wikicomp.get_wiki( w.id ).favoriteof, [],
                      'Mismatch in deleting favorite user for wiki'
                    )

    def test_F_wikivoting( self ) :
        """Testing FormWikiVote with valid and invalid inputs"""
        log.info( "Testing FormWikiVote with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        wikis    = wikicomp.get_wiki()
        user     = choice( users )
        p        = choice( projects )
        w        = choice( wikis )

        [ votcomp.remove_vote( v ) for v in w.votes ]

        # Vote up for wiki
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'votewiki' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'votedas', u'up' )
        vf.process( request, c, defer=False, formnames=['votewiki'] )

        self._validate_defer(
                user.id, False, c,
                lambda _u : 'casted vote' in _u.logs[-1].log 
        )

        w       = wikicomp.get_wiki( w.id )
        votes   = w.votes
        countup = votcomp.wikivotes( w, votedas=u'up' )
        assert_equal( [ len(votes), len(countup), countup[0].voter ],
                      [ 1, 1, user ],
                      'Mismatch in number of votes for wiki'
                    )

        # vote down for wiki
        c.rclose = h.ZResp()
        user = choice( users )
        request.POST.clearfields()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'wiki_id', str(w.id) )
        request.POST.add( 'votedas', u'down' )
        vf.process( request, c, defer=False, formnames=['votewiki'] )

        self._validate_defer(
                user.id, False, c,
                lambda _u : 'casted vote' in _u.logs[-1].log 
        )

        w = wikicomp.get_wiki( w.id )
        votes   = w.votes
        countdown = votcomp.wikivotes( w, votedas=u'down' )
        assert_equal( [ len(votes), len(countdown), countdown[0].voter ],
                      [ 2, 1, user ],
                      'Mismatch in number of votes against wiki'
                    )

    def test_G_vcsfile2wiki( self ) :
        """Testing FormVcsfile2Wiki with valid and invalid inputs"""
        log.info( "Testing FormVcsfile2Wiki with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        wikis    = wikicomp.get_wiki()
        user     = choice( users )
        p        = choice( projects )
        w        = choice( wikis )

        # Map vcs-file to wiki page
        c.rclose = h.ZResp()
        sourceurl = u'file/souce/in/repository'
        pagename = u'fromrepository'
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'vcsfile2wiki' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'sourceurl', sourceurl )
        request.POST.add( 'pagename', pagename )
        defer = choice([True, False])
        vf.process( request, c, defer=False, formnames=['vcsfile2wiki'] )

        defer and c.rclose.close()
        wikiurl = h.url_for( h.r_projwiki, projectname=p.projectname,
                             wurl=pagename )
        #self._validate_defer(
        #        c.authuser, defer, c,
        #        lambda _u : 'create the wiki page' in _u.logs[-1].log and \
        #                    'Changed,' in _u.logs[-1].log and \
        #                    'updated wiki content to version' in _u.logs[-1].log
        #)

        w = wikicomp.get_wiki( wikiurl )
        assert_equal( [ w.sourceurl, w.type.wiki_typename ],
                      [ sourceurl, h.WIKITYPE_IFRAME ],
                      'Mismatch in number of votes for wiki'
                    )
