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

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.generate    import gen_wiki
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects, pop_tickets, \
                                           pop_wikipages
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.vote               import VoteComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 10
no_of_tickets   = 30
no_of_wikis     = 30
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
tckcomp     = None
wikicomp    = None
votcomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, tckcomp, wikicomp, votcomp, cachemgr

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
    tckcomp    = TicketComponent( compmgr )
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
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )

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


class TestVote( object ) :

    def test_1_getvotes( self ) :
        """Testing various forms of getting votes"""
        log.info( "Testing method for getting wiki types ..." )

        tickets  = tckcomp.get_ticket()
        wikis    = wikicomp.get_wiki()
        allvotes = []
        uservotes= {}

        # Get ticket votes
        for t in tickets :
            allvotes.extend( t.votes )
            assert_equal( sorted(t.votes),
                          sorted(votcomp.get_ticketvote( ticket=t )),
                          'Mismatch in votes for ticket %s' % t.id
                        )

            for v in t.votes :
                assert_equal( v,
                              votcomp.get_ticketvote( voter=v.voter, ticket=t ),
                              'Mismatch in voter %s on ticket  %s' % \
                              (v.voter.username, t.id)
                            )
                uservotes.setdefault( v.voter.username, [] ).append( v )

        # Get ticket votes
        for w in wikis :
            allvotes.extend( w.votes )
            assert_equal( sorted(w.votes),
                          sorted(votcomp.get_wikivote( wiki=w )),
                          'Mismatch in votes for wiki %s' % w.id
                        )

            for v in w.votes :
                assert_equal( v,
                              votcomp.get_wikivote( voter=v.voter, wiki=w ),
                              'Mismatch in voter %s on wiki  %s' % \
                              (v.voter.username, w.id)
                            )
                uservotes.setdefault( v.voter.username, [] ).append( v )

        # Get all votes
        for username in uservotes :
            assert_equal( sorted(uservotes[username]),
                          sorted(votcomp.get_vote( voter=username )),
                          'Mismatch in all votes by user %s' % username 
                        )

        assert_equal( sorted(allvotes), sorted(votcomp.get_vote()),
                      'Mismatch in all votes' )

    def test_2_countvotes( self ) :
        """Testing vote counts"""
        log.info( "Testing vote counts" )

        tickets  = tckcomp.get_ticket()
        wikis    = wikicomp.get_wiki()
        allvotes = []

        # Couting ticket votes.
        for t in tickets :
            tckvotes = votcomp.ticketvotes( t, u'up' )
            tckvotes.extend( votcomp.ticketvotes( t, u'down' ))
            assert_equal( sorted(tckvotes),
                          sorted(votcomp.get_ticketvote( ticket=t )),
                          'Mismatch in counting votes for ticket %s' % t.id
                        )
            allvotes.extend( tckvotes )

        # Couting wiki votes.
        for w in wikis :
            wikivotes = votcomp.wikivotes( w, u'up' )
            wikivotes.extend( votcomp.wikivotes( w, u'down' ))
            assert_equal( sorted(wikivotes),
                          sorted(votcomp.get_wikivote( wiki=w )),
                          'Mismatch in counting votes for wiki %s' % w.wikiurl
                        )
            allvotes.extend( wikivotes )

        assert_equal( sorted(allvotes), sorted(votcomp.get_vote()),
                      'Mismatch between counted votes and db votes'
                    )

    def test_3_uservotes( self ) :
        """Testing uservotes() method"""
        log.info( "Testing uservotes() method" )

        for u in userscomp.get_user() :
            refvotes = {}
            for v in u.votes :
                refvotes.setdefault( v.votedas, [] 
                                   ).append( [v.id, v.votedas, v.medium, v.created_on] )
            refvotes = dict([ (k,
                               sorted( map( lambda x : tuple(x), refvotes[k]),
                                       key=lambda x : x[0] )
                              ) for k in refvotes ])
            votes = votcomp.uservotes( u )
            votes = dict([ (k, sorted( votes[k], key=lambda x : x[0] ))
                           for k in votes ])
            assert_equal( refvotes, votes,
                          'Mismatch in uservotes(), for user %s' % u.username
                        )
