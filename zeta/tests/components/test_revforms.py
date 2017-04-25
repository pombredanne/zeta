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
                                           pop_licenses, pop_projects, pop_vcs, \
                                           pop_reviews
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 2
no_of_tags      = 3
no_of_attachs   = 1
no_of_projects  = 10
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 20
g_byuser        = u'admin'

tagchars    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
taglist     = None 

compmgr     = None
userscomp   = None
attachcomp  = None
tagcomp     = None
liccomp     = None
projcomp    = None
revcomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, tagcomp, projcomp, revcomp, \
           taglist, seed, cachemgr

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
    revcomp    = ReviewComponent( compmgr )
    taglist    = [ unicode(h.randomname( randint(0,LEN_TAGNAME), tagchars))
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
    print "   Populating vcs ( no_of_vcs=%s ) ..." % no_of_vcs
    pop_vcs( no_of_vcs=no_of_vcs, seed=seed )
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


class TestReviewForms( object ) :

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

    def test_1_createreview_valid( self ) :
        """Testing FormCreateReview with valid inputs"""
        log.info( "Testing FormCreateReview with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createrev' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        rsets        = revcomp.get_reviewset()

        # Create new review en-mass
        c.rclose = h.ZResp()
        u            = choice( users )
        p            = choice( projects )
        rset         = choice( rsets )
        resource_urls= [ u'some/resource_url1', u'some/resource_url2',
                         u'some/resource_url3', u'some/resource_url4' ]
        author       = choice( users )
        moderator    = choice( users )
        version      = randint( 1, 10 )
        participants = list(set([ choice(users) for i in range(randint(0,len(users))) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'resource_url', rurl ) for rurl in resource_urls ]
        request.POST.add( 'author', author.username )
        request.POST.add( 'moderator', moderator.username )
        request.POST.add( 'version', str(version) )
        [ request.POST.add( 'participant', u.username ) for u in participants ]
        request.POST.add( 'rset_id', str(rset.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createrev'] )

        defer and c.rclose.close()
        # TODO : After refactoring, the following check can be enabled.
        #self._validate_defer(
        #        c.authuser, defer, c,
        #        lambda u : 'created new review for' in u.logs[-1].log and \
        #                   u'some/resource_url4' in u.logs[-1].log 
        #)

        revs = revcomp.get_review()[-4:]
        for rurl, r in zip( resource_urls, revs ) :
            assert_equal( [ rurl, author.username, moderator.username, version ],
                          [ r.resource_url, r.author.username,
                            r.moderator.username, r.version ],
                          'Mismatch in revew details while creating review en-mass'
                        )
            assert_equal( sorted(r.participants), sorted(participants),
                          'Mismatch in review participants while creating review en-mass' )
            assert_equal( r.reviewset, rset,
                          'Mismatch in review set while creating review en-mass' )
        
        # Create a new review
        c.rclose = h.ZResp()
        request.POST.clearfields()
        u            = choice( users )
        p            = choice( projects )
        rset         = choice( rsets )
        resource_url = u'some/resource_url'
        author       = choice( users )
        moderator    = choice( users )
        version      = randint( 1, 10 )
        participants = list(set([ choice(users) for i in range(randint(0,len(users))) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'resource_url', resource_url )
        request.POST.add( 'author', author.username )
        request.POST.add( 'moderator', moderator.username )
        request.POST.add( 'version', str(version) )
        [ request.POST.add( 'participant', u.username ) for u in participants ]
        request.POST.add( 'rset_id', str(rset.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createrev'] )

        defer and c.rclose.close()
        # TODO : After refactoring, the following check can be enabled.
        #self._validate_defer(
        #        c.authuser, defer, c,
        #        lambda u : 'created new review for' in u.logs[-1].log and \
        #                   u'some/resource_url' in u.logs[-1].log 
        #)

        r = revcomp.get_review( sorted([ rev.id for rev in revcomp.get_review() ])[-1] )
        assert_equal( [ resource_url, author.username, moderator.username, version ],
                      [ r.resource_url, r.author.username, r.moderator.username, r.version ],
                      'Mismatch in revew details while creating review'
                    )
        assert_equal( sorted(r.participants), sorted(participants),
                      'Mismatch in review participants while creating review' )
        assert_equal( r.reviewset, rset,
                      'Mismatch in review set while creating review' )
        
        # Updating review en-mass
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configrev' )
        request.POST.clearfields()
        revs          = revcomp.get_review()[-4:]
        author        = choice( users )
        moderator     = choice( users )
        version       = randint( 1, 10 )
        participants_u  = []
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'review_id', str(r.id) ) for r in revs ]
        request.POST.add( 'author', author.username )
        request.POST.add( 'moderator', moderator.username )
        request.POST.add( 'version', str(version) )
        [ request.POST.add( 'participant', u.username ) for u in participants_u ]
        request.POST.add( 'rset_id', str(rset.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['configrev'] )

        defer and c.rclose.close()
        # TODO : After refactoring, the following check can be enabled.
        #self._validate_defer(
        #        c.authuser, defer, c,
        #        lambda u : 'Updated review details' in u.logs[-1].log and \
        #                   'Updated review details' in u.logs[-1].log 
        #)

        for r in revs :
            r = revcomp.get_review( r.id )
            assert_equal( [ author.username, moderator.username, version ],
                          [ r.author.username, r.moderator.username, r.version ],
                          'Mismatch in revew details while creating review'
                        )
            assert_equal( r.reviewset, rset,
                          'Mismatch in review set while updating review' )

        # Updating review
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configrev' )
        request.POST.clearfields()
        rset          = choice( rsets )
        r             = revcomp.get_review()[0]
        resource_url  = u'updated resource_url'
        author        = choice( users )
        moderator     = choice( users )
        version       = randint( 1, 10 )
        participants_u  = []
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'resource_url', resource_url )
        request.POST.add( 'author', author.username )
        request.POST.add( 'moderator', moderator.username )
        request.POST.add( 'version', str(version) )
        [ request.POST.add( 'participant', u.username ) for u in participants_u ]
        request.POST.add( 'rset_id', str(rset.id) )
        vf.process( request, c, defer=defer, formnames=['configrev'] )
        r = revcomp.get_review( r.id )
        assert_equal( [ resource_url, author.username, moderator.username, version ],
                      [ r.resource_url, r.author.username, r.moderator.username, r.version ],
                      'Mismatch in revew details while creating review'
                    )
        assert_equal( r.reviewset, rset,
                      'Mismatch in review set while updating review' )

        # Update review to remove author
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configrev' )
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'author', '' )
        vf.process( request, c, defer=defer, formnames=['configrev'] )
        r = revcomp.get_review( r.id )
        assert_false( r.author, 'Unable to remove author for review' )

        # Update review to remove moderator
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'moderator', '' )
        vf.process( request, c, defer=defer, formnames=['configrev'] )
        r = revcomp.get_review( r.id )
        assert_false( r.moderator, 'Unable to remove moderator for review' )


    def test_2_createreview_invalid( self ) :
        """Testing FormCreateReview with invalid inputs"""
        log.info( "Testing FormCreateReview with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createrev' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        # Create a new review
        u            = choice( users )
        p            = choice( projects )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        resource_url = u'some resource_url'
        request.POST.add( 'resource_url', resource_url )
        assert_raises( ZetaFormError, vf.process, request, c,
                       formnames=['createrev'] )
        author       = choice( users )
        request.POST.add( 'author', author.username )
        assert_raises( ZetaFormError, vf.process, request, c,
                       formnames=['createrev'] )
        moderator    = choice( users )
        request.POST.add( 'moderator', moderator.username )
        assert_raises( ZetaFormError, vf.process, request, c,
                       formnames=['createrev'] )

    def test_3_reviewparticipants( self ) :
        """Testing FormReviewParticipants with valid and invalid inputs"""
        log.info( "Testing FormReviewParticipants with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        u            = choice( users )
        p            = choice( projects )
        r = revcomp.get_review( sorted([ rev.id for rev in revcomp.get_review() ])[-1] )
        # Remove the current participants from review
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delparts' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        [ request.POST.add( 'participant', u.username ) for u in r.participants ]
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['delparts'] )

        if r.participants :
            self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'removed participants' in u.logs[-1].log 
            )
        else :
            c.rclose.close()

        # Add participants to review
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addparts' )
        participants = list(set([ choice(users)
                                  for i in range(randint(0,len(users))) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        [ request.POST.add( 'participant', u.username ) for u in participants ]
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addparts'] )

        if participants :
            self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added participants' in u.logs[-1].log 
            )
        else :
            c.rclose.close()

        r = revcomp.get_review(
                sorted([ rev.id for rev in revcomp.get_review() ])[-1] )
        assert_equal( sorted(r.participants), sorted(participants),
                      'Mismatch in adding review participants ' )

        # Replace participants to review
        request.params.clearfields()
        request.POST.clearfields()
        participants = list(set([ choice(users)
                                  for i in range(randint(0,len(users))) ]))
        refpartcpts  = participants or r.participants
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addparts' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        [ request.POST.add( 'participant', u.username ) for u in participants ]
        vf.process( request, c, append=False, formnames=['addparts'] )
        r = revcomp.get_review( r.id )
        assert_equal( sorted(r.participants), sorted(refpartcpts),
                      'Mismatch in adding review participants ' )

    def test_4_createreviewcomment_valid( self ) :
        """Testing FormCreateReviewComment with valid inputs"""
        log.info( "Testing FormCreateReviewComment with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'creatercmt' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        rnatures     = revcomp.get_reviewcomment_nature()
        u            = choice( users )
        p            = choice( projects )
        r = revcomp.get_review( sorted([ rev.id for rev in revcomp.get_review() ])[-1] )

        # Create review comment
        c.rclose = h.ZResp()
        position     = randint( 0, 10 )
        text         = u'some review comment'
        commentby    = choice( users )
        nature       = choice( rnatures ).naturename
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'position', str(position) )
        request.POST.add( 'text', text )
        request.POST.add( 'reviewnature', nature )
        request.POST.add( 'commentby', commentby.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['creatercmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'comment' in u.logs[-1].log and \
                           'position' in u.logs[-1].log
        )

        r = revcomp.get_review( r.id )
        rc = r.comments[-1]
        assert_equal( [ position, text, commentby.username, nature ],
                      [ rc.position, rc.text, rc.commentby.username,
                        rc.nature.naturename ],
                      'Mismatch in creating review comment'
                    )

        # Update review comment
        c.rclose = h.ZResp()
        request.POST.clearfields()
        position     = randint( 0, 10 )
        text         = u'updated review comment'
        commentby    = choice( users )
        nature       = choice( rnatures ).naturename
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'review_comment_id', str(rc.id) )
        request.POST.add( 'position', str(position) )
        request.POST.add( 'text', text )
        request.POST.add( 'reviewnature', nature )
        request.POST.add( 'commentby', commentby.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['creatercmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated comment' in u.logs[-1].log 
        )

        r = revcomp.get_review( r.id )
        rc = r.comments[-1]
        assert_equal( len( r.comments ), 1,
                      'Created a new review comment while updating an existing one'
                    )
        assert_equal( [ position, text, commentby.username, nature ],
                      [ rc.position, rc.text, rc.commentby.username,
                        rc.nature.naturename ],
                      'Mismatch in updating review comment'
                    )

    def test_5_createreviewcomment_invalid( self ) :
        """Testing FormCreateReviewComment with invalid inputs"""
        log.info( "Testing FormCreateReviewComment with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'creatercmt' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        u            = choice( users )
        p            = choice( projects )
        r = revcomp.get_review( sorted([ rev.id for rev in revcomp.get_review() ])[-1] )
        # Create review comment
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )

        position     = randint( 0, 10 )
        request.POST.add( 'position', str(position) )
        assert_raises( ZetaFormError,
                       vf.process, request, c, formnames=['creatercmt']
                     )
        text         = u'some review comment'
        request.POST.add( 'text', text )
        assert_raises( ZetaFormError,
                       vf.process, request, c, formnames=['creatercmt']
                     )

    def test_6_processreviewcomment( self ) :
        """Testing FormProcessReviewComment, FormCloseReview with valid and invalid inputs"""
        log.info( "Testing FormProcessReviewComment, FormCloseReview with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'processrcmt' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        u            = choice( users )
        p            = choice( projects )
        ractions     = revcomp.get_reviewcomment_action()
        rnatures     = revcomp.get_reviewcomment_nature()
        r  = revcomp.get_review( sorted([ rev.id for rev in revcomp.get_review() ])[-1] )
        rc = r.comments[-1]

        # Process review comment
        c.rclose = h.ZResp()
        position     = rc.position
        text         = rc.text
        approve      = choice([ 'true', 'false' ])
        raction      = choice( ractions )
        rnature      = choice( rnatures )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'review_comment_id', str(rc.id) )
        request.POST.add( 'approve', approve )
        request.POST.add( 'reviewaction', raction.actionname )
        request.POST.add( 'reviewnature', rnature.naturename )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['processrcmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'processing review comment' in u.logs[-1].log 
        )

        rc = revcomp.get_reviewcomment( rc.id )
        assert_equal( [ position, text, [ False, True ][ approve == 'true' ],
                        raction.actionname, rnature.naturename ],
                      [ rc.position, rc.text, rc.approved, rc.action.actionname,
                        rc.nature.naturename ],
                      'Mismatch in processing review comment'
                    )

        # Remove nature of a review comment
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'review_comment_id', str(rc.id) )
        request.POST.add( 'reviewnature', '' )
        vf.process( request, c, formnames=['processrcmt'] )
        rc = revcomp.get_reviewcomment( rc.id )
        assert_false( rc.nature, 'Unable to remove the review comment nature' )

        # Remove action on a review comment
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'review_comment_id', str(rc.id) )
        request.POST.add( 'reviewaction', '' )
        vf.process( request, c, formnames=['processrcmt'] )
        rc = revcomp.get_reviewcomment( rc.id )
        assert_false( rc.action, 'Unable to remove the review comment action' )

        # Try closing the review without approving the comment actions.
        rcomments = r.comments
        for cmt in rcomments :
            revcomp.process_reviewcomment( cmt, approve=True )

        if cmt :    # 'cmt' retains the last value in the previous loop
            c.rclose = h.ZResp()
            revcomp.process_reviewcomment( cmt, approve=False )
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'closerev' )
            request.POST.add( 'user_id', str(u.id) )
            request.POST.add( 'project_id', str(p.id) )
            request.POST.add( 'review_id', str(r.id) )
            request.POST.add( 'command', 'close' )
            defer = choice([True, False])
            assert_raises( ZetaFormError, vf.process, request, c,
                           defer=defer, formnames=['closerev'] )

            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'failed closing' in u.logs[-1].log 
            )

            # Try closing the review after approving all the comment actions.
            c.rclose = h.ZResp()
            revcomp.process_reviewcomment( cmt, approve=True )
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'closerev' )
            request.POST.add( 'user_id', str(u.id) )
            request.POST.add( 'project_id', str(p.id) )
            request.POST.add( 'review_id', str(r.id) )
            request.POST.add( 'command', 'close' )
            defer = choice([True, False])
            vf.process( request, c, defer=defer, formnames=['closerev'] )

            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'closed' in u.logs[-1].log 
            )

            r = revcomp.get_review( r.id )
            assert_true( r.closed, 'Review not closed' )

            # open a closed review
            c.rclose = h.ZResp()
            request.params.clearfields()
            request.POST.clearfields()
            request.params.add( 'form', 'submit' )
            request.params.add( 'formname', 'closerev' )
            request.POST.add( 'user_id', str(u.id) )
            request.POST.add( 'project_id', str(p.id) )
            request.POST.add( 'review_id', str(r.id) )
            request.POST.add( 'command', 'open' )
            defer = choice([True, False])
            vf.process( request, c, defer=defer, formnames=['closerev'] )

            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'opened' in u.logs[-1].log 
            )

            r = revcomp.get_review( r.id )
            assert_false( r.closed, 'Review not opened' )

    def test_7_reviewcommentreplies( self ) :
        """Testing review comment replies with valid and invalid inputs"""
        log.info( "Testing review comment replies with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'replyrcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        reviews  = revcomp.get_review()
        u        = choice( users )
        p        = choice( projects )
        r = revcomp.get_review( sorted([ rev.id for rev in revcomp.get_review() ])[-1] )
        rc       = r.comments[-1]

        # Create review comment
        position  = randint( 0, 10 )
        text      = u'second review comment'
        commentby = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'position', str(position) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        request.POST.add( 'replytocomment_id', str(rc.id) )
        vf.process( request, c, formnames=['creatercmt'] )
        rc        = revcomp.get_reviewcomment( rc.id )
        assert_equal( len( rc.replies ), 1,
                      'Mismatch in no of replies'
                    )
        assert_equal( rc.replies[0].text, text,
                      'Mismatch in reply comment text'
                    )

    def test_8_reviewfavorite( self ) :
        """Testing FormReviewFavorite with valid and invalid inputs"""
        log.info( "Testing FormReviewFavorite with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        reviews  = revcomp.get_review()
        user     = choice( users )
        p        = choice( projects )
        r        = choice( reviews )

        revcomp.delfavorites( r, r.favoriteof, byuser=g_byuser )

        # Add favorite user
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'revwfav' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'addfavuser', user.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['revwfav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added review as favorite' in u.logs[-1].log 
        )

        assert_equal( revcomp.get_review( r.id ).favoriteof, [ user ],
                      'Mismatch in adding favorite user for review'
                    )

        # Del favorite user
        c.rclose = h.ZResp()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'delfavuser', user.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['revwfav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'removed review from favorite' in u.logs[-1].log 
        )

        assert_equal( revcomp.get_review( r.id ).favoriteof, [],
                      'Mismatch in deleting favorite user for review'
                    )

    def test_9_reviewtags( self ) :
        """Testing FormReviewTags with valid and invalid input"""
        log.info( "Testing FormReviewTags with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        reviews  = revcomp.get_review()
        u        = choice( users )
        p        = choice( projects )
        r        = revcomp.get_review( sorted([ r.id for r in reviews ])[-1] )

        # Add tags to review.
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addrevtags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda tag : tagcomp.is_tagnamevalid(tag), 
                                tagnames ) + \
                        [ tag.tagname for tag in r.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addrevtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added tags' in u.logs[-1].log 
        )

        r = revcomp.get_review( r.id )
        assert_equal( sorted(reftags),
                      sorted([ tag.tagname for tag in r.tags ]),
                      'Mismatch while creating tags'
                    )

        # Delete tags to review.
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delrevtags' )
        rmtag = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        request.POST.add( 'tags', rmtag )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['delrevtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted tags' in u.logs[-1].log 
        )

        r = revcomp.get_review( r.id )
        assert_equal( sorted(reftags),
                      sorted([ tag.tagname for tag in r.tags ]),
                      'Mismatch while deleting tags'
                    )

    def test_A_reviewattachs( self ) :
        """Testing FormReviewAttachs with valid and invalid input"""
        log.info( "Testing FormReviewAttachs with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        reviews  = revcomp.get_review()
        u        = choice( users )
        p        = choice( projects )
        r        = revcomp.get_review( sorted([ r.id for r in reviews ])[-1] )

        # Clean attachments in review
        [ revcomp.remove_attach( r, attach ) for attach in r.attachments ]

        # Add attachments
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addrevattachs' )
        user    = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'review_id', str(r.id) )
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
        vf.process( request, c, user=user.username, defe=defer,
                    formnames=['addrevattachs'] )

        def _verify(u) :
            log = ', '.join([ u.logs[-i].log for i in range(1, len(attachmentfiles)+1) ])
            return all([ a.filename in log for a in attachmentfiles ])

        if attachmentfiles :
            self._validate_defer( c.authuser, defer, c, _verify )
        else :
            c.rclose.close()

        r = revcomp.get_review( r.id )
        assert_equal( sorted([ a.filename for a in r.attachments ]),
                      sorted([ attach.filename for attach in attachmentfiles ]),
                      'Mismatch in adding review attachment'
                    )

        # Remove attachments
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delrevattachs' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'review_id', str(r.id) )
        [ request.POST.add( 'attach_id', str(a.id) ) for a in r.attachments ]
        defer = choice([True, False])
        vf.process( request, c, removeattach=True, defer=defer,
                    formnames=['delrevattachs'] )

        if r.attachments :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted attachment' in u.logs[-1].log 
            )
        else :
            c.rclose.close()

        r = revcomp.get_review( r.id )
        assert_false( r.attachments,
                      'Mismatch in removing review attachment' )

    def test_B_reviewset( self ) :
        """Testing FormReviewSet"""
        log.info( "Testing FormReviewSet" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        p        = choice( projects )

        # Create review set
        c.rclose = h.ZResp()
        name = 'rsetname'
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createrset' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'name', name )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createrset'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Created review set' in u.logs[-1].log 
        )

        rset = revcomp.get_reviewset()[-1]
        assert_equal( rset.name, name, 'Mismatch while creating review set' )

        # Update review set
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updaterset' )
        name = u'updated_rsetname'
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'rset_id', str(rset.id) )
        request.POST.add( 'name', name )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createrset'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Updated review set name' in u.logs[-1].log 
        )

        rset = revcomp.get_reviewset( rset.id )
        assert_equal( rset.name, name, 'Mismatch while updating review set' )

        # Add review to review set
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addtorset' )
        review = choice(revcomp.get_review())
        rset   = choice(revcomp.get_reviewset())
        revcomp.remove_reviewfromset( review )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'review_id', str(review.id) )
        request.POST.add( 'rset_id', str(rset.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addtorset'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Added review' in u.logs[-1].log and \
                           'to review set' in u.logs[-1].log
        )

        review = revcomp.get_review( review.id )
        assert_equal( review.reviewset, rset,
                      'Mismatch while adding review to review set' )

        # Remove review from review set
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delfromrset' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'review_id', str(review.id) )
        request.POST.add( 'rset_id', str(review.reviewset.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['delfromrset'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Removed review' in u.logs[-1].log and \
                           'from review set' in u.logs[-1].log 
        )
        
        review = revcomp.get_review( review.id )
        assert_false( review.reviewset,
                      'Mismatch while deleting review from review set' )
