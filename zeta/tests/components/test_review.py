# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os.path                      import commonprefix, join, isdir, basename
import random
from   random                       import choice, randint
import datetime                     as dt

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true
from   nose.plugins.attrib          import attr

from   zwiki.zwparser               import ZWParser
from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.generate    import gen_reviewurls, gen_reviews, future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects, pop_vcs, pop_wikipages
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
import zeta.lib.vcsadaptor          as va
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.vcs                import VcsComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 10
no_of_vcs       = no_of_projects * 2
no_of_wikis     = 30
no_of_reviews   = 10
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
attachcomp  = None
projcomp    = None
wikicomp    = None
vcscomp     = None
revcomp     = None
revdata     = None
zwparser    = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, projcomp, wikicomp, vcscomp, \
           revcomp, revdata, zwparser, seed, cachemgr

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
    wikicomp   = WikiComponent( compmgr )
    vcscomp    = VcsComponent( compmgr )
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
    print "   Populating vcs ( no_of_vcs=%s ) ..." % no_of_vcs
    pop_vcs( no_of_vcs=no_of_vcs, seed=seed )
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
    # Collect the expected database objects.
    users     = userscomp.get_user()
    projects  = projcomp.get_project()
    rnatures  = revcomp.get_reviewcomment_nature()
    ractions  = revcomp.get_reviewcomment_action()
    revdata   = gen_reviews( rnatures, ractions, no_of_reviews, no_of_tags,
                             no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_reviews=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_reviews )

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


class TestReview( object ) :

    def _validate_review( self, revdata, reviews ) :
        """validate the review fields.
        `revdata` and `reviews` are sorted based on the review object"""
        assert_equal( len(revdata), len(reviews),
                      'Mismatch in the no of created reviews' )
        for i in range(len(reviews)) :
            rev         = revdata[i]
            r           = reviews[i]
            rfields     = [ rev['resource_url'], rev['version'],
                            rev['author'], rev['moderator'] ]
            dbrfields   = [ r.resource_url, r.version, r.author, r.moderator ]
            assert_equal( rfields, dbrfields, 'Mismatch in review fields' )

    def _validate_reviewconfig( self, revdata, reviews ) :
        """validate the review fields.
        `revdata` and `reviews` are sorted based on the review object"""
        assert_equal( len(revdata), len(reviews),
                      'Mismatch in the no of created reviews' )
        for i in range(len(reviews)) :
            rev         = revdata[i]
            r           = reviews[i]
            assert_equal( sorted( rev['participants'] ), 
                          sorted( r.participants ),
                          'Mismatch in review participants' )
            assert_equal( rev['closed'], r.closed, 'Mismatch in review close status' )

    def _validate_reviewcomment( self, rcmtdata, reviewcomments ) :
        """`rcmtdata` and `reviewcomments` are sorted based on the
        review_comment object"""
        assert_equal( len(rcmtdata), len(reviewcomments),
                      'Mismatch with the number of review comment entries' )
        for i in range(len(reviewcomments)) :
            rcmt       = rcmtdata[i]
            rc         = reviewcomments[i]
            rcfields   = [ rcmt['position'], rcmt['text'], rcmt['commentby'],
                           rcmt['reviewnature'], rcmt['reviewaction'],
                           rcmt['approved'] ]
            dbrcfields = [ rc.position, rc.text, rc.commentby,
                           rc.nature, rc.action, rc.approved ]
            assert_equal( rcfields, dbrcfields, 'Mismatch in review comment field' )

            assert_equal( rc.texthtml, h.translate( rc, 'text' ),
                          'Mismatch in texthtml created for rcmt'
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

        # Characterize the generated wikitext set the wikiproperties
        wikiprops = {}
        wikitext  = ( "@ %s " % wikiprops ) + '\n' + wikitext

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

    def test_1_get_reviewaction( self ) :
        """Testing get_reviewcomment_action method"""
        log.info( "Testing get_reviewcomment_action method" )
        assert_equal( sorted(config['zeta.reviewactions']),
                      sorted([ rac.actionname for rac in revcomp.get_reviewcomment_action() ]),
                      'Mismatch in getting review actions' 
                    )

    def test_2_get_reviewnature( self ) :
        """Testing get_reviewcomment_nature method"""
        log.info( "Testing get_reviewcomment_nature method" )
        assert_equal( sorted(config['zeta.reviewnatures']),
                      sorted([ rn.naturename for rn in revcomp.get_reviewcomment_nature() ]),
                      'Mismatch in getting review natures' 
                    )

    def test_3_createreview( self ) :
        """Testing review creation"""
        log.info( "Testing review creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for rev in revdata :
            p         = rev['project']
            revdet    = ( rev['id'], rev['resource_url'], rev['version'],
                          rev['author'], rev['moderator'] )
            rev['id'] = revcomp.create_review( p, revdet )
        self._validate_review( sorted( revdata, key=lambda rev : rev['id'] ),
                               sorted( revcomp.get_review() ))

    def test_4_configreview( self ) :
        """Testing review updation and configuration"""
        log.info( "Testing review updation and configuration" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for i in range(len(revdata)) :
            rev       = revdata[i]
            p         = rev['project']
            authors   = [ p.admin ] + [ pr.user for pr in p.team ]
            moderators= [ p.admin ] + [ pr.user for pr in p.team ]
            rev['resource_url'] = u'review'+'-url'+str(i)
            rev['version']      = randint( 1,10 )
            rev['author']       = choice( authors )
            rev['moderator']    = choice( moderators )
            revdet    = ( rev['id'], rev['resource_url'], rev['version'],
                          rev['author'], rev['moderator'] )
            rev['id'] = revcomp.create_review( p, revdet, update=True )
        for rev in revdata :
            if rev['participants'] :
                revcomp.set_participants(
                            choice([ rev['id'].id, rev['id'] ]),
                            rev['participants'],
                )
                rmparticipants = choice( rev['participants'] )
                rmparticipants and rev['participants'].remove( rmparticipants )
                revcomp.set_participants( rev['id'], [ rmparticipants ],
                                          remove=True )
        self._validate_review( sorted( revdata, key=lambda rev : rev['id'] ),
                               sorted( revcomp.get_review() ))
        # Note: Participants setting will be validated by
        # _validate_reviewconfig() while closing the review.

    def test_5_getreview( self ) :
        """Testing methods for getting review(s)"""
        log.info( "Testing methods for getting review(s)" )
        dbreviews = revcomp.get_review()
        reviews   = [ revcomp.get_review( r.id ) for r in dbreviews ]
        assert_equal( sorted( dbreviews ), sorted( reviews ),
                      'Mismatch in getting review by `id`' )
        reviews   = [ revcomp.get_review( r ) for r in dbreviews ]
        assert_equal( sorted( dbreviews ), sorted( reviews ),
                      'Mismatch in getting review by instance' )

    def test_6_reviewset( self ) :
        """Testing reviewset methods"""
        log.info( "Testing reviewset methods" )
        
        projects  = projcomp.get_project()
        reviews   = revcomp.get_review()

        rset_data = [ 'rset1', 'rset2', 'rset3', 'rset4' ]

        # Create Review set
        for rsetname in rset_data :
            p    = choice(projects)
            rset = revcomp.create_reviewset( p, rsetname, byuser=g_byuser )
            rset = revcomp.get_reviewset( choice([ rset, rset.id ]),
                                       attrload=[ 'reviews' ] )
            assert_true( rset.name == rsetname,
                         'Mismatch in creating review set' )
        assert_true( len(revcomp.get_reviewset()) == 4,
                     'Mismatch in creating review sets' )

        # Update review set
        for rset in revcomp.get_reviewset() :
            revcomp.update_reviewset( choice([ rset, rset.id ]),
                                      'update' + rset.name,
                                      byuser=g_byuser )
        rset_data = [ 'update'+name for name in rset_data ]
        assert_equal( sorted( rset_data ),
                      sorted([ rset.name for rset in revcomp.get_reviewset() ]),
                      'Mismatch in review data set'
                    )

        # Add reviews to review set.
        rsets = revcomp.get_reviewset()
        rset  = choice( rsets )
        revcomp.add_reviewtoset( rset, reviews[0], byuser=g_byuser )
        assert_equal( rset.reviews, reviews[:1], 
                      'Mismatch while adding first review to review set'
                    )
        revcomp.add_reviewtoset( rset, reviews[1], byuser=g_byuser )
        assert_equal( sorted(rset.reviews), sorted(reviews[:2]), 
                      'Mismatch while adding first review to review set'
                    )

        # Remove review from review set
        revcomp.remove_reviewfromset( reviews[0], byuser=g_byuser )
        assert_equal( sorted(rset.reviews), sorted(reviews[1:2]),
                      'Mismatch in removing review from review set'
                    )


    def test_6_createcomment( self ) :
        """Testing review comment creation"""
        log.info( "Testing review comment creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users     = userscomp.get_user()
        rnatures  = revcomp.get_reviewcomment_nature()
        ractions  = revcomp.get_reviewcomment_action()
        for rev in revdata :
            rcmtdata = rev['comments']
            for revcmt in rcmtdata :
                rcmtdet      = ( revcmt['id'], revcmt['position'],
                                 revcmt['text'], revcmt['commentby'],
                                 revcmt['reviewnature'], None )
                revcmt['id'] = revcomp.create_reviewcomment( rev['id'], rcmtdet )
            for revcmt in rcmtdata :
                revcmt['reviewnature'] = choice(rnatures)
                revcmt['reviewaction'] = choice(ractions)
                revcmt['position']     = 100
                revcmt['text']         = u'updated text'
                revcmt['commentby']    = choice(users)
                rcmtdet      = ( revcmt['id'], revcmt['position'],
                                 revcmt['text'], revcmt['commentby'], None, None )
                revcmt['id'] = revcomp.create_reviewcomment(
                                    rev['id'], rcmtdet, update=True )
                revcomp.process_reviewcomment(
                                        revcmt['id'],
                                        reviewnature=revcmt['reviewnature'],
                                        reviewaction=revcmt['reviewaction'],
                                        approve=revcmt['approved'],
                )
        allreviewcomments = []
        for rev in revdata :
            rcmtdata = rev['comments']
            allreviewcomments.extend( rev['id'].comments )
            self._validate_reviewcomment(
                    sorted( rcmtdata, key=lambda rcmt : rcmt['id'] ),
                    sorted( rev['id'].comments ))
        dballreviewcomments = revcomp.get_reviewcomment()
        assert_equal( sorted( allreviewcomments ), sorted(dballreviewcomments),
                      'Mismatch in updated review comment' )
        self._validate_review( sorted( revdata, key=lambda rev : rev['id'] ),
                               sorted( revcomp.get_review() ))

    def test_7_getcomments( self ) :
        """Testing methods for getting review comments"""
        log.info( "Testing methods for getting review comments" )
        dbreviewcomments = revcomp.get_reviewcomment()
        reviewcomments   = [ revcomp.get_reviewcomment( rc.id )
                             for rc in dbreviewcomments ]
        assert_equal( sorted( dbreviewcomments ), sorted( reviewcomments ),
                      'Mismatch in getting review comment by `id`' )
        reviewcomments   = [ revcomp.get_reviewcomment( rc )
                             for rc in dbreviewcomments ]
        assert_equal( sorted( dbreviewcomments ), sorted( reviewcomments ),
                      'Mismatch in getting review comment by instance' )

    def test_8_reviewreplies( self ) :
        """Testing replies to review comments"""
        log.info( "Testing replies to review comments" )
        for rev in revdata :
            for i in range(0, len(rev['replies'])) :
                replyto = rev['replies'][i] 
                replyto != -1 and revcomp.comment_reply( 
                                        rev['comments'][i]['id'],
                                        rev['comments'][replyto]['id']
                                  )
        for rev in revdata :
            replies = {}
            for i in range(0, len(rev['replies'])) :
                replyto = rev['replies'][i] 
                replyto != -1 and replies.setdefault(
                                        rev['comments'][replyto]['id'], []
                                  ).append( rev['comments'][i]['id'] )
            for rcmt in replies :
                revcmt = revcomp.get_reviewcomment( rcmt )
                assert_equal(
                    sorted([ revcomp.get_reviewcomment(i) for i in replies[rcmt] ]),
                    sorted( revcmt.replies ),
                    'Mismatch in review comment replies' 
                )

    def test_9_closereview( self ) :
        """Testing review closing"""
        log.info( "Testing review closing" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for rev in revdata :
            rev['closed'] = revcomp.close_review( rev['id'], rev['closed'] )
        allreviewcomments = []
        for rev in revdata :
            rcmtdata = rev['comments']
            allreviewcomments.extend( rev['id'].comments )
            self._validate_reviewcomment(
                    sorted( rcmtdata, key=lambda rcmt : rcmt['id'] ),
                    sorted( rev['id'].comments ))
        dballreviewcomments = revcomp.get_reviewcomment()
        assert_equal( sorted( allreviewcomments ), sorted(dballreviewcomments),
                      'Mismatch in updated review comment' )
        self._validate_review( sorted( revdata, key=lambda rev : rev['id'] ),
                               sorted( revcomp.get_review() ))
        self._validate_reviewconfig( sorted( revdata, key=lambda rev : rev['id'] ),
                                     sorted( revcomp.get_review() ))

    def test_A_properties( self ) :
        """Testing review component properties"""
        log.info( "Testing review component properties" )
        assert_equal( sorted([ ra.actionname 
                               for ra in revcomp.get_reviewcomment_action() ]),
                      sorted( revcomp.actionnames ),
                      'Mismatch in `actionnames` property'
                    )
        assert_equal( sorted([ rn.naturename 
                               for rn in revcomp.get_reviewcomment_nature() ]),
                      sorted( revcomp.naturenames ),
                      'Mismatch in `naturenames` property'
                    )

        # Upgrade review wiki fields
        n_rcmts = len(revcomp.get_reviewcomment())
        assert_true( revcomp.upgradewiki() == n_rcmts,
                     'Problem in upgrading review comments' )

    def test_B_reviewaction( self ) :
        """Testing review comment action creation"""
        log.info( "Testing review comment action creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        ref_revactn = revcomp.actionnames
        add_revactn = [ u'revaction1', u'revaction2' ]
        ref_revactn += add_revactn
        revcomp.create_reviewaction( add_revactn )
        assert_equal( sorted(ref_revactn), sorted(revcomp.actionnames),
                      'Mismatch in creating review actions as list' )

        add_revactn = u'revaction3'
        ref_revactn += [ add_revactn ]
        revcomp.create_reviewaction( add_revactn )
        assert_equal( sorted(ref_revactn), sorted(revcomp.actionnames),
                      'Mismatch in creating review action as string' )

    def test_C_reviewnature( self ) :
        """Testing review comment nature creation"""
        log.info( "Testing review comment nature creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        ref_revnatr = revcomp.naturenames
        add_revnatr = [ u'revnature1', u'revnature2' ]
        ref_revnatr += add_revnatr
        revcomp.create_reviewnature( add_revnatr )
        assert_equal( sorted(ref_revnatr), sorted(revcomp.naturenames),
                      'Mismatch in creating review nature as list' )

        add_revnatr = u'revnature3'
        ref_revnatr += [ add_revnatr ]
        revcomp.create_reviewnature( add_revnatr )
        assert_equal( sorted(ref_revnatr), sorted(revcomp.naturenames),
                      'Mismatch in creating review nature as string' )

    def test_D_tags( self ) :
        """Testing tag additions and removals"""
        log.info( "Testing tag additions and removals" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for rev in revdata :
            r         = rev['id']
            byuser    = choice( rev['tags'].keys() )
            tags      = rev['tags'][byuser]
            rmtag     = tags and choice(tags) or u''
            revcomp.add_tags( choice([ r.id, r ]), tags, byuser=byuser )
            revcomp.remove_tags( r, rmtag )
            rmtag and tags.remove(rmtag)
            assert_equal( sorted( tags ),
                          sorted([ tag.tagname for tag in r.tags ]),
                          'Mismatch in review tag methods'
                        )

    def test_E_attach( self ) :
        """Testing attachment additions and removals"""
        log.info( "Testing attachment additions and removals" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        attachs = {}
        for rev in revdata :
            r = rev['id']
            attachs[r] = []
            for u in rev['attachs'] :
                for f in rev['attachs'][u] :
                    attach = attachcomp.create_attach(
                                            os.path.basename( f ),
                                            choice([ open( f, 'r' ), None  ]),
                                            uploader=u,
                                            summary='',
                             )
                    revcomp.add_attach( r, attach )
                    attachs[r].append( (u, f, attach) )
            rmattach = [ tup for tup in attachs[r]  if choice([ True, False ]) ]
            for tup in rmattach :
                attachs[r].remove( tup )
                revcomp.remove_attach( r, tup[2] )
                rev['attachs'][tup[0]].remove( tup[1] )
        for r in revcomp.get_review() :
            atts = [ tup[2] for tup in attachs[r] ]
            assert_equal( sorted(atts), sorted(r.attachments),
                          'Mismatch in project attachments' )

    def test_F_favorites( self ) :
        """Testing favorite addition and deletion for reviews"""
        log.info( "Testing favorite addition and deletion for reviews" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for rev in revdata :
            r = rev['id']
            if choice([ True, False ]) : # as list
                revcomp.addfavorites( r, rev['favusers'] )
            else :                       # as byuser
                for u in rev['favusers'] :
                    revcomp.addfavorites( r, u, byuser=u )
            rmfavusers = [ u for u in rev['favusers'] if choice([ 1, 0, 0 ]) ]
            [ rev['favusers'].remove( u ) for u in rmfavusers ]
            if choice([ True, False ]) : # as list
                revcomp.delfavorites( r, rmfavusers )
            else :                       # as byuser
                [ revcomp.delfavorites( r, u, byuser=u ) for u in rmfavusers ]
        for rev in revdata :
            r    = revcomp.get_review( rev['id'].id )
            assert_equal( sorted(r.favoriteof),
                          sorted([ userscomp.get_user( u ) 
                                   for u in rev['favusers'] ]),
                          'Mismatch in creating review favorites'
                        )

    @attr( type='guess' )
    def test_G_guess_revwsource( self ) :
        """Testing api, guess_revwsource()"""
        log.info( "Testing api, guess_revwsource()" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        projects    = filter( lambda p : p.vcslist, projcomp.get_project() )
        p           = choice( projects )
        projusers   = [ projcomp.projusernames( p ) + [ p.admin.username ] ]
        author      = choice( projusers )
        moderator   = choice( projusers )

        # Review for vcs file
        urls        = gen_reviewurls( p, types=['vcsfile'] )
        url         = choice( urls )
        revdetail   = ( None,
                        unicode( url[0] ), 
                        url[1] == url[2] and url[1] or randint(url[1], url[2]),
                        author,
                        moderator
                      )
        r         = revcomp.create_review( p, revdetail, byuser=g_byuser )
        filelines, _difflno = revcomp.guess_revwsource( r )
        vcs       = [ vcs
                      for vcs in vcscomp.get_vcs() 
                      if commonprefix([ r.resource_url, vcs.rooturl ]) == vcs.rooturl
                    ][0]
        vrep      = va.open_repository( vcs )
        vfile     = vrep.file( r.resource_url, revno=r.version )
        reflines  = vfile.cat( revno=r.version )
        assert_equal( [ l[1] for l in reflines ], filelines,
                      'Mismatch in guessing the review source - vcs file' )

        # Review for vcs web url
        urls        = gen_reviewurls( p, types=['vcsweburl'] )
        url         = choice( urls )
        revdetail   = ( None,
                        unicode( url[0] ), 
                        url[1] == url[2] and url[1] or randint(url[1], url[2]),
                        author,
                        moderator
                      )
        r         = revcomp.create_review( p, revdetail, byuser=g_byuser )
        filelines, _difflno = revcomp.guess_revwsource( r )
        routes_map= config['routes.map']
        d, robj   = routes_map.routematch( url[0] )
        id        = d.get( 'vcsid', '' )
        filepath  = d.get( 'filepath', '' )
        vcs       = vcscomp.get_vcs( int(id) )
        vrep      = va.open_repository( vcs )
        vfile     = vrep.file( vcs.rooturl + '/' + filepath.lstrip('/'), revno=r.version )
        reflines  = vfile.cat( revno=r.version )
        assert_equal( [ l[1] for l in reflines], filelines,
                      'Mismatch in guessing the review source - vcsweburl' )

        # Review for wiki
        urls        = gen_reviewurls( p, types=['wiki'] )
        url         = choice( urls )
        revdetail   = ( None,
                        unicode( url[0] ), 
                        url[1] == url[2] and url[1] or 1,
                        author,
                        moderator
                      )
        r         = revcomp.create_review( p, revdetail, byuser=g_byuser )
        filelines, _difflno = revcomp.guess_revwsource( r )
        w         = wikicomp.get_wiki( r.resource_url )
        wcnt      = wikicomp.get_content( w, version=r.version )
        reflines  = wcnt.text.splitlines()
        assert_equal( reflines, filelines,
                      'Mismatch in guessing the review source - wiki' )

    def test_H_wikitranslate( self ) :
        """Testing the wiki translation for review comment text"""
        log.info( "Testing the wiki translation for review comment text" )
        for rev in revdata :
            rcmtdata = rev['comments']
            for rcmt in rcmtdata :
                self._testwiki_execute( 'revcmt', rcmt['id'], 'text' )
        for rcmt in revcomp.get_reviewcomment() :
            self._testwiki_execute( 'revcmt', rcmt, 'text' )


    def test_I_misc( self ) :
        """Testing miscellaneous functions"""
        log.info( "Testing miscellaneous functions" )

        # Test reviewlist()
        p        = choice( projcomp.get_project() )
        revwlist = revcomp.reviewlist( p )
        assert_equal( len(p.reviews), len(revwlist), 
                      'Mismatch in count of project reviews' )
        for r in p.reviews :
            assert_equal( revwlist[r.id],
                          [ r.id, r.resource_url,
                            r.reviewset and r.reviewset.name,
                            r.reviewset and r.reviewset.id,
                            r.version, r.author and r.author.username,
                            r.moderator and r.moderator.username,
                            r.created_on ],
                          'Mismatch in review, for method reviewlist()'
                        )

        # Test addabletorset()
        p    = choice( projcomp.get_project() )
        rset = revcomp.projectrset(p)
        rset = rset and revcomp.get_review(choice(rset))
        if p and rset :
            revwlist = revcomp.addabletorset( p, rset )
            ref = set(p.reviews).difference(set(rset.reviews))
            assert_equal(len(ref), len(revwlist), 
                          'Mismatch in count of project reviews addable to rset')
            for r in revwlist :
                ref = revcomp.get_review(r[0])
                assert_equal( [ref.id, ref.resource_url, ref.version], r,
                              'Mismatch in review list' )

        # Test countcomments()
        r = choice( revcomp.get_review() )
        assert_equal( len( r.comments ), revcomp.countcomments( r ),
                      'Mismatch in coutcomments()'
                    )

        # Test reviewopts()
        p = choice( projcomp.get_project() )
        assert_equal( sorted( [ (r.id, r.resource_url) for r in p.reviews ],
                              key=lambda tup : tup[0]
                            ),
                      sorted( revcomp.reviewopts(choice([ p.id, p.projectname, p ])), 
                              key=lambda tup : tup[0]
                            ),
                      'Mismatch in reviewopts()'
                    )

        # Test projectrset()
        p = choice( projcomp.get_project() )
        assert_equal( sorted( [ (rs.id, rs.name) for rs in p.reviewsets ],
                              key=lambda tup : tup[0]
                            ),
                      sorted( revcomp.projectrset(choice([ p.id, p.projectname, p ])), 
                              key=lambda tup : tup[0]
                            ),
                      'Mismatch in projectrset()'
                    )

        # Test reviewrcomments()
        r   = choice( revcomp.get_review() )
        res = revcomp.reviewrcomments( r )
        assert_equal( len(r.comments),
                      sum(map( lambda x : x[0]+x[1],
                               [ (1, len(res[k][-1])) for k in res ] )),
                      'Mismatch in number of review-reply-comments'
                    )

        for k in res :
            tup = res[k]
            cmt = revcomp.get_reviewcomment( k )
            assert_equal( [ cmt.id, cmt.position, cmt.text, cmt.texthtml, 
                            cmt.approved, cmt.created_on,
                            cmt.commentby.username,
                            cmt.nature.naturename,
                            cmt.action.actionname,
                          ],
                          tup[:9],
                          'Mismatch of review comment %s' % k 
                        )
            for rtup in tup[-1] :
                cmt = revcomp.get_reviewcomment( rtup[0] )
                assert_equal( [ cmt.id, cmt.position, cmt.text, cmt.texthtml, 
                                cmt.approved, cmt.created_on,
                                cmt.commentby.username,
                                cmt.nature.naturename,
                                cmt.action.actionname,
                              ],
                              rtup[:9],
                              'Mismatch of review comment %s' % k 
                            )

    def test_J_attachments( self ) :
        """Testing method, attachments()"""
        log.info( "Testing method, attachments()" )

        projects = projcomp.get_project()
        for p in projects :
            rattachs= {}
            for r in p.reviews :
                attachs = {}
                for a in r.attachments :
                    attachs[a.id] = [ a.filename, a.size, a.summary, a.download_count,
                                      a.created_on, a.uploader.username,
                                      [ tag.tagname for tag in a.tags ]
                                    ]
                if attachs :
                    rattachs[(r.id, r.resource_url)] = attachs
            attachments = revcomp.attachments( p )
            assert_equal(
                attachments, rattachs, 
                'Mismatch in attachments, for review in project %s' % p.projectname
            )

    def test_K_userstats( self ) :
        """Testing method, userstats"""
        log.info( "Testing method, userstats" )

        for u in userscomp.get_user() :
            # For userasauthor()
            revwids = revcomp.userasauthor( u )
            assert_equal( sorted(revwids),
                          sorted([ r.id for r in u.authorreviews ]),
                          'Mismatch in userasauthor(), for user %s' % u.username
                        )

            # For userasmoderator()
            revwids = revcomp.userasmoderator( u )
            assert_equal( sorted(revwids),
                          sorted([ r.id for r in u.moderatereviews ]),
                          'Mismatch in userasmoderator(), for user %s' % u.username
                        )

            # For userasparticipant()
            revwids = revcomp.userasparticipant( u )
            assert_equal( sorted(revwids),
                          sorted([ r.id for r in u.participatereviews ]),
                          'Mismatch in userasparticipant(), for user %s' % u.username
                        )

            # For usercomments() 
            rcmtids = revcomp.usercomments( u )
            assert_equal( sorted(rcmtids),
                          sorted([ rcmt.id for rcmt in u.reviewcomments ]),
                          'Mismatch in usercomments(), for user %s' % u.username )

        # Test allapproved() method
        for r in revcomp.get_review() :
            if not revcomp.allapproved( r ) :
                [ revcomp.process_reviewcomment( rcmt, approve=True )
                  for rcmt in r.comments ]
                assert_equal( revcomp.allapproved(r), True,
                              'Mismatch in all approved, True' )
            else :
                [ revcomp.process_reviewcomment( rcmt, approve=False )
                  for rcmt in r.comments ]
                if r.comments :
                    assert_equal( revcomp.allapproved(r), False,
                                  'Mismatch in all approved, False' )

        # Test reviewsproject() method
        ref  = [ (r.id, r.project.id, r.project.projectname)
                 for r in revcomp.get_review( attrload=[ 'project' ]) ]
        data = revcomp.reviewsproject()
        assert_equal( sorted( ref, key=lambda x : x[0] ),
                      sorted( data, key=lambda x : x[0] ),
                      'Mismatch in reviewsproject() method' )
