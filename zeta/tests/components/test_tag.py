# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import random
from   random                       import randint, choice
import os
from   os.path                      import join, isdir, basename

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_true, assert_false

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 

from   zeta.lib.constants           import LEN_TAGNAME
from   zeta.lib.error               import ZetaTagError
from   zeta.tests.tlib              import *
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_vcs, pop_reviews, pop_tickets, \
                                           pop_wikipages
from   zeta.comp.tag                import TagComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.wiki               import WikiComponent

config     = pylons.test.pylonsapp.config
log        = logging.getLogger(__name__)

seed       = None
no_of_tags = 50
tagchars   = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#tagchars += '~`!@#$%^&*()_-+=\|]}[{\'";:/?.>,<'
taglist    = None 

no_of_users     = 20
no_of_relations = 3
no_of_tags      = 10
no_of_attachs   = 1
no_of_projects  = 5
no_of_vcs       = no_of_projects * 2
no_of_tickets   = 5
no_of_reviews   = 5
no_of_wikis     = 5
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
tagcomp     = None
attcomp     = None
liccomp     = None
projcomp    = None
tckcomp     = None
revcomp     = None
wikicomp    = None
g_byuser    = u'admin'
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, tagcomp, attcomp, liccomp, projcomp, tckcomp, revcomp, \
           wikicomp, taglist, seed, cachemgr

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
    compmgr  = config['compmgr']
    tagcomp  = TagComponent( compmgr )
    attcomp  = AttachComponent( compmgr )
    liccomp  = LicenseComponent( compmgr )
    projcomp = ProjectComponent( compmgr )
    tckcomp  = TicketComponent( compmgr )
    revcomp  = ReviewComponent( compmgr )
    wikicomp = WikiComponent( compmgr )
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
    print "   Populating tickets ( no_of_tickets=%s ) ..." % no_of_tickets
    pop_tickets( no_of_tickets, no_of_tags, no_of_attachs, seed=seed )
    print "   Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
    pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )

    taglist = [ unicode(h.randomname( randint(0,LEN_TAGNAME), tagchars))
                            for i in range(randint(0,no_of_tags)) ]
    print "   no_of_tags=%s", no_of_tags

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


class TestTag( object ) :

    def test_1_createtags( self ) :
        """Testing is_tagnamevalid"""
        log.info( "Testing is_tagnamevalid ..." )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        assert_true( tagcomp.is_tagnamevalid( 'hello' ),
                     'is_tagnamevalid failed -- 1' )
        assert_true( tagcomp.is_tagnamevalid( 'hello1' ),
                     'is_tagnamevalid failed -- 1' )
        assert_true( tagcomp.is_tagnamevalid( 'hello!0' ),
                     'is_tagnamevalid failed -- 1' )
        assert_false( tagcomp.is_tagnamevalid( 'hello ' ),
                     'is_tagnamevalid failed -- 1' )
        assert_false( tagcomp.is_tagnamevalid( 'hello w' ),
                     'is_tagnamevalid failed -- 1' )

    def test_2_createtags( self ) :
        """Testing tag creation"""
        log.info( "Testing tag creation ..." )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        tagnames    = tagcomp.tagnames
        for tagname in taglist[:] :
            if len(tagname) < 2 or len(tagname) > LEN_TAGNAME : # Is tagname length correct
                #assert_raises( ZetaTagError, tagcomp.create_tag, tagname  )
                taglist.remove( tagname )
                pass
            else :
                tagcomp.create_tag( tagname )
        # Add the standard tags to the generated tags in memory.
        tagnames.extend( taglist )
        tagnames.sort()
        # Obtain the tags from database.
        dbtaglist = sorted([ t.tagname for t in tagcomp.get_tag() ])
        # Validate
        assert_equal(
                dbtaglist,
                tagnames,
                'created tags does not match with the tagnames in database'
        )

    def test_3_existence( self ) :
        """Testing tag existence methods"""
        log.info( "Testing tag existence methods ..." )
        taglist_l = taglist[:]
        for i in range(len(taglist)/2) :
            tagname = taglist_l.pop(taglist_l.index(choice(taglist_l)))
            assert_equal( tagcomp.tag_exists( tagname ), True,
                          'Tag name expected to exist in the database' )

    def test_4_removetags( self ) :
        """Testing tag removal method"""
        log.info( "Testing tag removal method ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        tagnames = tagcomp.tagnames
        for i in range(len(tagnames)/2) :
            tagname = tagnames.pop(tagnames.index(choice(tagnames)))
            tag     = tagcomp.get_tag( tagname )
            tagcomp.remove_tag( choice( [tag.tagname, tag, tag.id ] ))
        dbtaglist = sorted([ t.tagname for t in tagcomp.get_tag() ])
        assert_equal( sorted(tagnames), sorted(dbtaglist),
                      'Remaining tags does not match' )
        assert_raises( ZetaTagError, tagcomp.create_tag, choice(dbtaglist) )

    def test_5_properties( self ) :
        """Testing tag properties."""
        log.info( "Testing tag properties ..." )
        tags        = tagcomp.get_tag()
        attachs     = attcomp.get_attach()
        license     = liccomp.get_license()
        projects    = projcomp.get_project()
        tickets     = tckcomp.get_ticket()
        reviews     = revcomp.get_review()
        wikis       = wikicomp.get_wiki()

        # Test 'tagnames' property
        assert_equal( sorted(tagcomp.tagnames),
                      sorted([ t.tagname for t in tagcomp.get_tag() ]),
                      'Mismatch in tagnames property'
                    )
        
        # Test 'tagstats' property
        tagstats    = tagcomp.tagstats
        assert_equal( sum([ len( tagstats[t][c] ) for t in tagstats.keys()
                                                  for c in tagstats[t].keys() ]),
                      sum([ sum([ len(t.licenses) + len(t.attachments) + \
                                  len(t.projects) + len(t.tickets) + len(t.reviews) + \
                                  len(t.wikipages)
                                ])
                            for t in tags ]),
                      'Mismatch number tags in tag statistics'
                    )
        assert_equal( set(sorted([ tag.tagname for a in attachs for tag in a.tags ])),
                      set(sorted([ t.tagname for t in tagstats if tagstats[t]['attachments'] ])),
                      'Mismatch attach tags in tags staticstics'
                    )
        assert_equal( set(sorted([ tag.tagname for l in license for tag in l.tags ])),
                      set(sorted([ t for t in tagstats if tagstats[t]['licenses'] ])),
                      'Mismatch license tags in tags staticstics'
                    )
        assert_equal( set(sorted([ tag.tagname for p in projects for tag in p.tags ])),
                      set(sorted([ t for t in tagstats if tagstats[t]['projects'] ])),
                      'Mismatch project tags in tags staticstics'
                    )
        assert_equal( set(sorted([ tag.tagname for t in tickets for tag in t.tags ])),
                      set(sorted([ t for t in tagstats if tagstats[t]['tickets'] ])),
                      'Mismatch ticket tags in tags staticstics'
                    )
        assert_equal( set(sorted([ tag.tagname for r in reviews for tag in r.tags ])),
                      set(sorted([ t for t in tagstats if tagstats[t]['reviews'] ])),
                      'Mismatch review tags in tags staticstics'
                    )
        assert_equal( set(sorted([ tag.tagname for w in wikis for tag in w.tags ])),
                      set(sorted([ t for t in tagstats if tagstats[t]['wikipages'] ])),
                      'Mismatch wiki tags in tags staticstics'
                    )

        # Test 'tagpercentile' property
        tagpercentile = tagcomp.tagpercentile
        assert_equal( sum([ tagpercentile[t][0] for t in tagpercentile ]),
                      sum([ sum([ len(t.licenses) + len(t.attachments) + \
                                  len(t.projects) + len(t.tickets) + len(t.reviews) + \
                                  len(t.wikipages)
                                ])
                            for t in tags ]),
                      'Mismatch number tags in tag statistics'
                    )  
