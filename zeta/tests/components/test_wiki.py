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
from nose.plugins.attrib            import attr

from   zwiki.zwparser               import ZWParser

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.generate    import gen_wiki
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects, pop_tickets, \
                                           pop_reviews, pop_vcs
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.vote               import VoteComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 5
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 3
no_of_tickets   = 10
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 10
no_of_wikis     = 50
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
tagcomp     = None
attachcomp  = None
projcomp    = None
wikicomp    = None
votcomp     = None
wikidata    = None
zwparser    = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, tagcomp, attachcomp, projcomp, wikicomp, wikidata, \
           votcomp, zwparser, seed, cachemgr

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
    tagcomp    = TagComponent( compmgr )
    attachcomp = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    votcomp    = VoteComponent( compmgr )
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
    print "   Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
    pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
    # Collect the expected database objects.
    wikidata = gen_wiki( no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_wikis=%s" )   % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_wikis )

    zwparser = ZWParser( lex_optimize=True, yacc_debug=True,
                         yacc_optimize=False )

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


class TestWiki( object ) :

    def _validate_wiki( self, wikidata, wikis ) :
        """`wikidata` and `wikis` are sorted based on the wiki object"""
        # Filter out automatically created 'homepage'
        wikis = [ w for w in wikis if PROJHOMEPAGE not in w.wikiurl ]
        assert_equal( len(wikidata), len(wikis),
                      'Mismatch with the number of wikis in the database'
                    )
        for i in range(len(wikis)) :
            wiki         = wikidata[i]
            w            = wikis[i]
            summary      = wiki['summary'].replace( '\n', ' ' ).replace( '\r', ' ' )
            wikifields   = [ wiki['wikiurl'], wiki['wiki_typename'],
                             wiki['creator'], summary, wiki['sourceurl'] ]
            dbwikifields = [ w.wikiurl, w.type, w.creator, w.summary, w.sourceurl ]
            assert_equal( wikifields, dbwikifields,
                          'Mismatch in the wiki detail' )

    def _validate_configwiki( self, wikidata, wikis ) :
        """`wikidata` and `wikis` are sorted based on the wiki object"""
        # Filter out automatically created 'homepage'
        wikis = [ w for w in wikis if PROJHOMEPAGE not in w.wikiurl ]
        assert_equal( len(wikidata), len(wikis),
                      'Mismatch with the number of wikis in the database'
                    )
        for i in range(len(wikis)) :
            wiki     = wikidata[i]
            w        = wikis[i]
            wproject = wiki['project'] and projcomp.get_project( wiki['project'] )
            assert_equal( wproject, w.project,
                          'Mismatch in the wiki project' )

    def _validate_wikicontent( self, wikicntdata, wikicnts ) :
        """`wikicntdata` and `wikicnts` are sorted based on the
        `wikipage` object"""
        assert_equal( len(wikicntdata), len(wikicnts),
                      'Mismatch with the number of wiki cnts in the database'
                    )
        for i in range(len(wikicnts)) :
            wikicnt     = wikicntdata[i]
            wcnt        = wikicnts[i]
            cntfields   = [ wikicnt['author'], wikicnt['text'] ]
            dbcntfields = [ userscomp.get_user(wcnt.author), wcnt.text ]
            assert_equal( cntfields, dbcntfields,
                          'Mismatch in wiki content fields' )
            assert_equal( wcnt.translate(), wcnt.texthtml, 
                          'Mismatch in texthtml created for wcnt'
                        )

    def _validate_wikicontents( self, wikidata, wikis ) :
        """`wikidata` and `wikis` are sorted based on the wiki object"""
        # Filter out automatically created 'homepage'
        wikis = [ w for w in wikis if PROJHOMEPAGE not in w.wikiurl ]
        assert_equal( len(wikidata), len(wikis),
                      'Mismatch with the number of wikis in the database'
                    )
        for i in range(len(wikis)) :
            wiki      = wikidata[i]
            w         = wikis[i]
            latestver = sorted([ wikicnt['id'].id for wikicnt in wiki['contents'] ])
            if latestver :
                assert_equal( w.latest_version, latestver[-1],
                              'Mismatch in wiki latest version' )
            self._validate_wikicontent(
                    sorted( wiki['contents'], key=lambda wcnt : wcnt['id'] ),
                    sorted( wikicomp.get_content(w, all=True) ),
            )

    def _validate_wikicomment( self, wikicmtdata, wikicmts ) :
        """`wikicmtdata` and `wikicmts` are sorted based on the
        `wiki_comment` object"""
        assert_equal( len(wikicmtdata), len(wikicmts),
                      'Mismatch with the number of wiki cmts in database'
                    )
        for i in range(len(wikicmts)) :
            wikicmt     = wikicmtdata[i]
            wcmt        = wikicmts[i]
            cmtfields   = [ wikicmt['commentby'], wikicmt['version_id'],
                            wikicmt['text'] ]
            dbcmtfields = [ wcmt.commentby, wcmt.version_id, wcmt.text ]
            assert_equal( cmtfields, dbcmtfields,
                          'Mismatch in wiki content fields' )
            assert_equal( wcmt.texthtml, h.translate( wcmt, 'text' ),
                          'Mismatch in texthtml created for wcmt'
                        )

    def _testwiki_execute( self, type, model, attr, ref='' ) :
        wikitext    = getattr( model, attr, '' )

        # Characterize the generated wikitext set the wikiproperties
        wikiprops = {}
        wikitext  = ( "@ %s " % wikiprops ) + '\n' + wikitext

        # Prepare the reference.
        ref         = ref or wikitext
        ref         = zwparser.wiki_preprocess( ref )
        props, ref  = zwparser._wiki_properties( ref )


        # Test by comparing the dumps
        try :
            tu      = zwparser.parse( wikitext, debuglevel=0 )
            result  = tu.dump()[:-1]
        except :
            tu     = zwparser.parse( wikitext, debuglevel=2 )
            result = tu.dump()[:-1]
        if result != ref :
            print ''.join(diff.ndiff( result.splitlines(1), ref.splitlines(1) ))
        assert result == ref, type + '... testcount : %s - dump mismatch' % count

        # Test by comparing the html
        tu     = zwparser.parse( getattr( model, attr, '' ), debuglevel=0 )
        ref    = tu.tohtml()
        result = model.translate()
        assert result == ref, type + '... testcount %s - html mismatch' % count

        # Test by translating to html
        #tu   = zwparser.parse( wikitext, debuglevel=0 )
        #html = tu.tohtml()
        #et.fromstring( html ) 

    def test_1_getwikitype( self ) :
        """Testing method for getting wiki types"""
        log.info( "Testing method for getting wiki types ..." )
        dbtypes = wikicomp.get_wikitype()
        assert_equal( sorted(config['zeta.wikitypes']),
                      sorted([ t.wiki_typename for t in dbtypes ]),
                      'Mismatch in getting all the wiki types'
                    )
        assert_equal( sorted(dbtypes),
                      sorted([ wikicomp.get_wikitype( t ) 
                               for t in config['zeta.wikitypes'] ]),
                      'Mismatch in getting wiki types by name'
                    )

    def test_2_createwiki( self ) :
        """Testing method for creating wikipages"""
        log.info( "Testing method for creating wikipages ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for wiki in wikidata :
            wiki['id'] = wikicomp.create_wiki(
                                    wiki['wikiurl'],
                                    wiki['wiki_typename'],
                                    wiki['summary'],
                                    wiki['sourceurl'],
                                    wiki['creator']
                         )
        self._validate_wiki( sorted( wikidata, key=lambda wiki : wiki['id'] ),
                             sorted( wikicomp.get_wiki() )
                           )

    def test_3_configwiki( self ) :
        """Testing method for configuring wikis"""
        log.info( "Testing method for configuring wikis ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        wikitypes = wikicomp.get_wikitype()
        projects  = projcomp.get_project()
        for wiki in wikidata :
            w = wiki['id']
            wiki['wiki_typename'] = choice( wikitypes )
            wiki['summary'] = u'Updated ' + wiki['summary']
            wiki['sourceurl'] = u'http://discoverzeta.com/zwiki'
            wproject = choice(projects)
            wiki['project'] = wproject
            wikicomp.config_wiki( choice([ w, w.id, w.wikiurl ]),
                                  project=wiki['project'] )
            wikicomp.config_wiki( choice([ w, w.id, w.wikiurl ]),
                                  wtype=wiki['wiki_typename'] )
            wikicomp.config_wiki( w, summary=wiki['summary'],
                                  sourceurl=wiki['sourceurl'] )
            wikicomp.config_wiki( choice([ w, w.id, w.wikiurl ]),
                                  project=wproject )
        self._validate_wiki( sorted( wikidata, key=lambda wiki : wiki['id'] ),
                             sorted( wikicomp.get_wiki() )
                           )
        self._validate_configwiki(
                            sorted( wikidata, key=lambda wiki : wiki['id'] ),
                            sorted( wikicomp.get_wiki() ) 
        )

    def test_4_getwiki( self ) :
        """Testing method for getting wikipages"""
        log.info( "Testing method for getting wikipages ..." )
        # homepage anomaly.
        homepage_ids  = [ w for w in wikicomp.get_wiki() 
                               if PROJHOMEPAGE in w.wikiurl ]
        wikis   = sorted([ wiki['id'] for wiki in wikidata ] + homepage_ids )
        dbwikis = wikicomp.get_wiki()
        assert_equal( sorted(wikis), sorted( wikicomp.get_wiki() ),
                      'Mismatch in getting wikis'
                    )
        assert_equal( sorted(wikis),
                      sorted([ wikicomp.get_wiki( w )
                               for w in wikicomp.get_wiki() ]),
                      'Mismatch in getting wikis by Wiki instance'
                    )
        assert_equal( sorted(wikis),
                      sorted([ wikicomp.get_wiki( w.id )
                               for w in wikicomp.get_wiki() ]),
                      'Mismatch in getting wikis by wiki.id'
                    )
        assert_equal( sorted(wikis),
                      sorted([ wikicomp.get_wiki( w.wikiurl )
                               for w in wikicomp.get_wiki() ]),
                      'Mismatch in getting wikis by wiki.wikiurl'
                    )

    def test_5_createcontent( self ) :
        """Testing method for creating wiki contents"""
        log.info( "Testing method for creating wiki contents ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        for wiki in wikidata :
            wcntdata = wiki['contents']
            for wikicnt in wcntdata :
                wikicnt['id'] = wikicomp.create_content(
                                        wiki['id'], wikicnt['author'],
                                        wikicnt['text'], wikicnt['version']
                                )
            for wikicnt in wcntdata :
                wikicnt['author'] = choice(users)
                wikicnt['text'] = u'Updated wiki content'
                wikicnt['version'] = wikicnt['id'].id
                wikicnt['id'] = wikicomp.create_content(
                                        wiki['id'], wikicnt['author'],
                                        wikicnt['text'], wikicnt['version']
                                )
        self._validate_wikicontents(
                        sorted( wikidata, key=lambda wiki : wiki['id'] ),
                        sorted( wikicomp.get_wiki() )
        )

    def test_6_removecontent( self ) :
        """Testing method for removing wiki contents"""
        log.info( "Testing method for removing wiki contents ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for wiki in wikidata :
            wcntdata = wiki['contents']
            rmwcnt   = [ wikicnt for wikicnt in wcntdata ]
            for wikicnt in rmwcnt :
                wikicomp.remove_content( wiki['id'], wikicnt['id'].id )
                wcntdata.remove( wikicnt )
        self._validate_wikicontents(
                        sorted( wikidata, key=lambda wiki : wiki['id'] ),
                        sorted( wikicomp.get_wiki() )
        )

    def test_7_getcontent( self ) :
        """Testing method for getting wiki contents"""
        log.info( "Testing method for getting wiki contents ..." )
        for wiki in wikidata :
            wikipages = wikicomp.get_content(
                                    wiki['id'], all=True,
                                    translate=choice([True, False])
                        )
            wcntdata  = wiki['contents']
            assert_equal( sorted( wikipages ),
                          sorted([ wikicnt['id'] for wikicnt in wcntdata ]),
                          'Mismatch in wiki pages for `%s`' % wiki['id'].wikiurl
                        )
            assert_equal( sorted( wikipages ),
                          sorted([ wikicomp.get_content(
                                                wiki['id'],
                                                version=wikicnt['id'].id,
                                                translate=choice([True, False])
                                   ) for wikicnt in wcntdata ]),
                          'Mismatch in wiki pages by id for `%s`' %  \
                                  wiki['id'].wikiurl
                        )

    def test_8_createcomment( self ) :
        """Testing method for creating wiki comments"""
        log.info( "Testing method for creating wiki comments ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for wiki in wikidata :
            wcmtdata = wiki['comments']
            for wikicmt in wcmtdata :
                wcmtdet       = ( wikicmt['id'], wikicmt['commentby'],
                                  wikicmt['version_id'], wikicmt['text'] )
                wikicmt['id'] = wikicomp.create_wikicomment( wiki['id'], wcmtdet )
                wikicmt['commentby'] = userscomp.get_user( wikicmt['commentby'] )
        allwikicomments = []
        for wiki in wikidata :
            wcmtdata = wiki['comments']
            allwikicomments.extend( wiki['id'].comments )
            self._validate_wikicomment(
                    sorted( wcmtdata, key=lambda wcmt : wcmt['id'] ),
                    sorted( wiki['id'].comments )
            )
        dballwikicomments = wikicomp.get_wikicomment()
        assert_equal( sorted( allwikicomments ), sorted(dballwikicomments),
                      'Mismatch in created wiki comment' )
        self._validate_configwiki(
                            sorted( wikidata, key=lambda wiki : wiki['id'] ),
                            sorted( wikicomp.get_wiki() ) 
        )
        self._validate_wiki( sorted( wikidata, key=lambda wiki : wiki['id'] ),
                             sorted( wikicomp.get_wiki() )
                           )

    def test_9_updatecomment( self ) :
        """Testing method for updating wiki comments"""
        log.info( "Testing method for updating wiki comments ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        for wiki in wikidata :
            wcmtdata = wiki['comments']
            wcntdata = wiki['contents']
            for wikicmt in wcmtdata :
                wikicmt['commentby']  = choice(users)
                wikicmt['version_id'] = wcntdata and randint(1, len(wcntdata)) \
                                        or None
                wikicmt['text'] = u'Updated wiki comment'
                wcmtdet = ( wikicmt['id'], wikicmt['commentby'],
                            wikicmt['version_id'], wikicmt['text'] )
                wikicmt['id'] = wikicomp.create_wikicomment( 
                                            choice([ wiki['id'].id, wiki['id'] ]),
                                            wcmtdet, update=True
                                )
        allwikicomments = []
        for wiki in wikidata :
            wcmtdata = wiki['comments']
            allwikicomments.extend( wiki['id'].comments )
            self._validate_wikicomment(
                    sorted( wcmtdata, key=lambda wikicmt : wikicmt['id'] ),
                    sorted( wiki['id'].comments )
            )
        dballwikicomments = wikicomp.get_wikicomment()
        assert_equal( sorted( allwikicomments ), sorted(dballwikicomments),
                      'Mismatch in updated wiki comment' )
        self._validate_configwiki(
                            sorted( wikidata, key=lambda wiki : wiki['id'] ),
                            sorted( wikicomp.get_wiki() ) 
        )
        self._validate_wiki( sorted( wikidata, key=lambda wiki : wiki['id'] ),
                             sorted( wikicomp.get_wiki() )
                           )

    # TODO : Calling this test case might interfere in the `commentreplies`
    # testcase
    #def test_A_removecomment( self ) :
    #    """Testing method for removing wiki comments"""
    #    for wiki in wikidata :
    #        wcmtdata = wiki[8]
    #        rmwcmt   = [ wikicmt for wikicmt in wcmtdata ]
    #        for wikicmt in rmwcmt :
    #            wikicomp.remove_wikicomment( wikicmt[0].id )
    #            wcmtdata.remove( wikicmt )
    #        self._validate_wikicomment(
    #                sorted( wcmtdata, key=lambda wikicmt : wikicmt[0] ),
    #                sorted( wiki[0].comments ))

    def test_B_getcomment( self ) :
        """Testing method for getting wiki comments"""
        log.info( "Testing method for getting wiki comments ..." )
        allwikicomments = [ wikicmt['id'] for wiki in wikidata
                                          for wikicmt in wiki['comments'] ]
        assert_equal( sorted( allwikicomments ),
                      sorted( wikicomp.get_wikicomment() ),
                      'Mismatch with database wiki comments'
                    )
        assert_equal( sorted( allwikicomments ),
                      sorted([ wikicomp.get_wikicomment( wcmt ) 
                               for wcmt in allwikicomments ]),
                      'Mismatch in getting wiki comments by WikiComment instance'
                    )
        assert_equal( sorted( allwikicomments ),
                      sorted([ wikicomp.get_wikicomment( wcmt.id ) 
                               for wcmt in allwikicomments ]),
                      'Mismatch in getting wiki comments by WikiComment id'
                    )

    def test_C_commentreplies( self ) :
        """Testing method for wiki comment replies"""
        log.info( "Testing method for wiki comment replies ..." )
        for wiki in wikidata :
            for i in range(0, len(wiki['replies'])) :
                replyto = wiki['replies'][i] 
                replyto != -1 and wikicomp.comment_reply(
                                        wiki['comments'][i]['id'],
                                        wiki['comments'][replyto]['id']
                                  )
        for wiki in wikidata :
            replies = {}
            for i in range(0, len(wiki['replies'])) :
                replyto = wiki['replies'][i]
                replyto != -1 and replies.setdefault(
                                    wiki['comments'][replyto]['id'], []
                                  ).append( wiki['comments'][i]['id'] )
            for wcmt in replies :
                wikicmt = wikicomp.get_wikicomment( wcmt )
                assert_equal(
                    sorted([ wikicomp.get_wikicomment(i) for i in replies[wcmt] ]),
                    sorted( wikicmt.replies ),
                    'Mismatch in wiki comment replies' 
                )

    def test_D_tags( self ) :
        """Testing wiki tags"""
        log.info( "Testing wiki tags ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for wiki in wikidata :
            w         = wiki['id']
            byuser    = choice( wiki['tags'].keys() )
            tags      = wiki['tags'][byuser]
            rmtag     = tags and choice(tags) or u''
            wikicomp.add_tags( choice([ w.id, w ]), tags, byuser=byuser )
            wikicomp.remove_tags( w, rmtag )
            rmtag and tags.remove(rmtag)
            assert_equal( sorted( tags ),
                          sorted([ t.tagname for t in w.tags ]),
                          'Mismatch in wiki tag methods'
                        )

    def test_E_attachs( self ) :
        """Testing wiki attachments"""
        log.info( "Testing wiki attachments ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        attachs = {}
        for wiki in wikidata :
            w   = wiki['id']
            attachs[w] = []
            for u in wiki['attachs'] :
                for f in wiki['attachs'][u] :
                    attach = attachcomp.create_attach(
                                            os.path.basename( f ),
                                            choice([ open( f, 'r' ), None  ]),
                                            uploader=u,
                                            summary='',
                             )
                    wikicomp.add_attach( wiki['id'], attach )
                    attachs[w].append( (u, f, attach) )
            rmattach = [ tup for tup in attachs[w]  if choice([ True, False ]) ]
            for tup in rmattach :
                attachs[w].remove( tup )
                wikicomp.remove_attach( w, tup[2] )
                wiki['attachs'][tup[0]].remove( tup[1] )
        for w in wikicomp.get_wiki() :
            if PROJHOMEPAGE in w.wikiurl :
                continue
            atts = [ tup[2] for tup in attachs[w] ]
            assert_equal( sorted(atts), sorted(w.attachments),
                          'Mismatch in wiki attachments' )

    def test_F_properties( self ) :
        """Testing wiki component properties"""
        log.info( "Testing wiki component properties ..."  )
        assert_equal( sorted([ wt.wiki_typename 
                               for wt in wikicomp.get_wikitype() ]),
                      sorted( wikicomp.typenames ),
                      'Mismatch in `typenames` property'
                    )

        # Upgrade wiki fields
        n_wcnts = sum([ len(wikicomp.get_content( w, all=True ))
                        for w in wikicomp.get_wiki()  ])
        n_wcmts = len(wikicomp.get_wikicomment())
        cnt_wcnt, cnt_wcmt = wikicomp.upgradewiki()
        assert_true( cnt_wcnt == n_wcnts, 'Problem in upgrading wiki contents' )
        assert_true( cnt_wcmt == n_wcmts, 'Problem in upgrading wiki comments' )

    def test_G_createwikitypes( self ) :
        """Testing wiki type creation"""
        log.info( "Testing wiki type creation ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        ref_wikitypes = wikicomp.typenames
        add_wikitypes = [ u'wikitype1', u'wikitype2' ]
        ref_wikitypes += add_wikitypes
        wikicomp.create_wikitype( add_wikitypes )
        assert_equal( sorted(ref_wikitypes), sorted(wikicomp.typenames),
                      'Mismatch in creating wiki types as list' )

        add_wikitypes = u'wikitype3'
        ref_wikitypes += [ add_wikitypes ]
        wikicomp.create_wikitype( add_wikitypes )
        assert_equal( sorted(ref_wikitypes), sorted(wikicomp.typenames),
                      'Mismatch in creating wiki type as string' )

    def test_H_translate( self ) :
        """Testing method for translating wiki content"""
        log.info( "Testing method for translating wiki content ..." )
        for wiki in wikidata :
            w = wiki['id']
            wcntdata  = wiki['contents']
            for wcnt in wcntdata :
                self._testwiki_execute( 'wikicontent', wcnt['id'], 'text' )

            wcmtdata = wiki['comments']
            for wikicmt in wcmtdata :
                self._testwiki_execute( 'wikicomment', wikicmt['id'], 'text' )

            wikipages = wikicomp.get_content( wiki['id'], all=True )
            for wikipage in wikipages :
                self._testwiki_execute( 'wikicontent', wikipage, 'text' )

            if wikipages :
                ref = wikipage.translate(wiki=w)
                assert_equal( h.translate(wikipage, wiki=w), ref,
                              "Mismatch in wikipage `translate()` translation" )

        for wcmt in wikicomp.get_wikicomment() :
            self._testwiki_execute( 'wikicomment', wcmt, 'text' )

    def test_I_favorites( self ) :
        """Testing favorite addition and deletion for wikis"""
        log.info( "Testing favorite addition and deletion for wikis" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for wiki in wikidata :
            w = wiki['id']
            if choice([ True, False ]) : # as list
                wikicomp.addfavorites( w, wiki['favusers'] )
            else :                       # as byuser
                for u in wiki['favusers'] :
                    wikicomp.addfavorites( w, u, byuser=u )
            rmfavusers = [ u for u in wiki['favusers'] if choice([ 1, 0, 0 ]) ]
            [ wiki['favusers'].remove( u ) for u in rmfavusers ]
            if choice([ True, False ]) : # as list
                wikicomp.delfavorites( w, rmfavusers )
            else :                       # as byuser
                for u in rmfavusers :
                    wikicomp.delfavorites( w, u, byuser=u )
        for wiki in wikidata :
            w    = wikicomp.get_wiki( wiki['id'].id )
            assert_equal( sorted(w.favoriteof),
                          sorted([ userscomp.get_user( u ) 
                                   for u in wiki['favusers'] ]),
                          'Mismatch in creating wiki favorites'
                        )

    def test_L_voting( self ) :
        """Testing wiki voting"""
        log.info( "Testing wiki voting" )
        
        for wiki in wikidata :
            w = wiki['id']
            for u in wiki['voteup'] :
                wikicomp.voteup( w, u )
            for u in wiki['votedown'] :
                wikicomp.votedown( w, u )

        for wiki in wikidata :
            w = wikicomp.get_wiki( wiki['id'].id )
            upvotes   = votcomp.wikivotes( w, votedas=u'up' )
            upusers   = [ v.voter for v in upvotes ]
            downvotes = votcomp.wikivotes( w, votedas=u'down' )
            downusers = [ v.voter for v in downvotes ]
            assert_equal( sorted( upusers ), sorted( wiki['voteup'] ),
                          'Mismatch in users voting for wiki' )
            assert_equal( sorted( downusers ), sorted( wiki['votedown'] ),
                          'Mismatch in users voting against wiki' )

            # countvotes()
            d = {}
            [ d.setdefault(v.votedas, []).append(1) for v in w.votes ]
            d['up']   = len(d.get( 'up', [] ))
            d['down'] = len(d.get( 'down', [] ))
            assert_equal( d, wikicomp.countvotes( wiki=w ),
                          'Mismatch in counting wiki votes' )


    @attr(type='zlinks')
    def test_M_zetalinks( self ) :
        """Testing zetalinks in wiki"""
        log.info( "Testing zetalinks in wiki" )

        projname = projcomp.get_project()[0].projectname
        testcases = [
            ("[[ @u1 ]]",     [ "/u/admin" ]),
            ("[[ @uadmin ]]", [ "/u/admin" ]),
            ("[[ @a1 ]]",     [ "/attachment/download/1" ]),
            ("[[ @g1 ]]",     [ "/tag/" ]),
            ("[[ @gZip ]]",   [ "/tag/Zip" ]),
            ("[[ @l1 ]]",     [ "/license/1" ]),
            ("[[ @p1 ]]",     [ "/p/" ]),
            ("[[ @p%s ]]" % projname,[ "/p/%s" % projname ]),
            ("[[ @t2 ]]",     [ "/p/", "/t/2" ]),
            ("[[ @r2 ]]",     [ "/p/", "/r/2" ]),
            ("[[ @s2 ]]",     [ "/p/", "/s/2/browse" ]),
        ]
        class W( object ) :
            pass
        # The following tag name is used for zetalink testing
        if not tagcomp.get_tag( u'Zip' ) :
            tagcomp.create_tag( u'Zip', u'admin' )
        for t, refs in testcases :
            w      = W()
            w.text = t
            h.translate(w, wtype=h.WIKITYPE_ZWIKI, cache=True)
            testresult = [ ref in w.texthtml for ref in refs ]
            assert_true( all(testresult), 'Mismatch in zetalinks' )

    def test_N_misc( self ) :
        """Testing miscellaneous functions"""
        log.info( "Testing miscellaneous functions" )

        wikis = wikicomp.get_wiki()
        # wikiurls()
        for p in projcomp.get_project( attrload=['wikis'] ) :
            project = choice([ p, p.id, p.projectname ])
            assert_equal( sorted(wikicomp.wikiurls(project),
                                 key=lambda x : x[1]),
                          sorted([ (w.id, w.wikiurl) for w in p.wikis ],
                                   key=lambda x : x[1] ),
                          'Mismatch in wikiurls() method'
                        )

        # wikicomments()
        w = choice( wikis )
        wcomments = dict([ (wcomment[0], wcomment)
                           for wcomment in wikicomp.wikicomments(w.id) ])
        assert_equal( len(wcomments), len(w.comments),
                      'Mismatch in number of wiki comments' )
        for wcmt in w.comments :
            assert_equal(
                [ wcmt.id, wcmt.version_id, wcmt.text, wcmt.texthtml,
                  wcmt.created_on, wcmt.commentby.username ],
                list(wcomments[wcmt.id]),
                'Mismatch in wikicomments()'
            )

        # wikircomment()
        w = choice( wikis )
        wcomments  = dict([ (wcomment[0], wcomment)
                           for wcomment in wikicomp.wikicomments(w.id) ])
        wrcomments = {}
        for wcmt in wikicomp.wikircomments( w.id ) :
            wrcomments[wcmt[0]] = tuple(wcmt[:-2])
            for wrcmt in wcmt[-1] :
                wrcomments[wrcmt[0]] = tuple(wrcmt[:-2])
        assert_equal( wcomments, wrcomments, 'Mismatch in wikircomments()' )

        # wikisproject()
        ref = [ (w.id, w.wikiurl, w.project.id, w.project.projectname)
                for w in wikicomp.get_wiki( attrload=['project'] ) ]
        assert_equal( sorted( ref, key=lambda x : x[0] ),
                      sorted( wikicomp.wikisproject(), key=lambda x : x[0] ),
                      'Mismatch in wikisproject()' )

    def test_O_attachments( self ) :
        """Testing method, attachments()"""
        log.info( "Testing method, attachments()" )

        projects = projcomp.get_project()
        for p in projects :
            wattachs= {}
            for w in p.wikis :
                attachs = {}
                for a in w.attachments :
                    attachs[a.id] = [ a.filename, a.size, a.summary,
                                      a.download_count, a.created_on,
                                      a.uploader.username,
                                      [ tag.tagname for tag in a.tags ]
                                    ]
                if attachs :
                    wattachs[(w.id, w.wikiurl)] = attachs
            attachments = wikicomp.attachments( p )
            assert_equal(
                attachments, wattachs, 
                'Mismatch in attachments, for wikis in project %s' % p.projectname
            )

    def test_P_userstats( self ) :
        """Testing method, userstats"""
        log.info( "Testing method, userstats" )

        for u in userscomp.get_user() :
            # For usercomments()
            wcmtids = wikicomp.usercomments( u )
            assert_equal( sorted(wcmtids),
                          sorted([ wcmt.id for wcmt in u.wikicomments ]),
                          'Mismatch in usercomments(), for user %s' % u.username )

