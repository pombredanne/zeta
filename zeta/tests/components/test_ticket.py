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
import copy

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
from   zeta.tests.model.generate    import gen_tickets, future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses, \
                                           pop_projects
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
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
no_of_tickets   = 50
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
attachcomp  = None
projcomp    = None
tckcomp     = None
votcomp     = None
tckdata     = None
zwparser    = None
cachemgr    = None
cachedir    = '/tmp/testcache'

fjson1 = u"""
{ "tck_typename" : "%s", "tck_statusname" : "%s", "tck_severityname": "%s",
  "owner" : "%s", "componentname" : "%s", "milestone_name" : "%s",
  "version_name" : "%s"
}
"""
        


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, projcomp, tckcomp, tckdata, \
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
    attachcomp = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
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
    # Collect the expected database objects.
    tckdata = gen_tickets( no_of_tickets, no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_tickets=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_tickets )

    zwparser = ZWParser( lex_optimize=True, yacc_debug=True, yacc_optimize=False )

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


class TestTicket( object ) :

    def _validate_tickets( self, tckdata, tickets ) :
        """`tckdata` and `tickets` are sorted based on the ticket object"""
        assert_equal( len(tckdata), len(tickets),
                      'Mismatch with the number of tickets in the database'
                    )
        for i in range(len(tickets)) :
            tck         = tckdata[i]
            t           = tickets[i]
            summary     = tck['summary'].replace( '\r', ' ' ).replace( '\n', ' ' )
            tckfields   = ( summary, tck['description'],
                            tck['tck_typename'], tck['tck_severityname'],
                            tck['promptuser'], tck['project'] )
            dbtckfields = ( t.summary, t.description, t.type, t.severity,
                            t.promptuser, t.project )
            assert_equal( tckfields, dbtckfields,
                          'Mismatch in the ticket detail' )

    def _validate_ticketconfig( self, tckdata, tickets ) :
        """`tckdata` and `tickets` are sorted based on the ticket object"""
        assert_equal( len(tckdata), len(tickets),
                      'Mismatch with the number of tickets in the database'
                    )
        for i in range(len(tickets)) :
            tck         = tckdata[i]
            t           = tickets[i]
            tckfields   = ( tck['tck_typename'], tck['tck_severityname'],
                            tck['promptuser'], tck['parent'] )
            dbtckfields = ( t.type, t.severity, t.promptuser, t.parent )
            assert_equal( sorted(tck['components']), sorted(t.components),
                          'Mismatch in ticket components' )
            assert_equal( sorted(tck['milestones']), sorted(t.milestones),
                          'Mismatch in ticket milestones' )
            assert_equal( sorted(tck['versions']), sorted(t.versions),
                          'Mismatch in ticket versions' )
            blockedby   = [ tckcomp.get_ticket(id) in t.blockedby
                            for id in tck['blockedby'] ] or [ True ]
            assert_true( blockedby, 'Mismatch in blockedby tickets' )
            blocking    = [ tckcomp.get_ticket(id) in t.blocking
                            for id in tck['blocking'] ] or [ True ]
            assert_true( blocking, 'Mismatch in blocking tickets' )
            assert_equal( tckfields, dbtckfields,
                          'Mismatch in other configs for ticket' )

    def _validate_ticketstatus( self, tsdata, ticketstatus ) :
        """`tsdata` and `ticketstatus` are sorted based on the
        ticket_status_history object"""
        assert_equal( len(tsdata), len(ticketstatus),
                      'Mismatch with the number of ticket status entries' )
        for i in range(len(ticketstatus)) :
            tst        = tsdata[i]
            ts         = ticketstatus[i]
            tsfields   = [ tckcomp.get_tckstatus( tst['tck_statusname'] ),
                           tst['due_date'], tst['owner'] ]
            dbtsfields = [ ts.status, ts.due_date, ts.owner ]
            assert_equal( tsfields, dbtsfields,
                          'Mismatch in ticket status fields' )

    def _validate_ticketcomment( self, tcmtdata, ticketcomments ) :
        """`tcmtdata` and `ticketcomments` are sorted based on the
        ticket_comment object"""
        assert_equal( len(tcmtdata), len(ticketcomments),
                      'Mismatch with the number of ticket comment entries' )
        for i in range(len(ticketcomments)) :
            tcmt       = tcmtdata[i]
            tc         = ticketcomments[i]
            tcfields   = [ tcmt['text'], tcmt['commentby'] ]
            dbtcfields = [ tc.text, tc.commentby ]
            assert_equal( tcfields, dbtcfields,
                          'Mismatch in ticket comment field' )
            assert_equal( tc.texthtml, h.translate( tc, 'text' ),
                          'Mismatch in texthtml created for tcmt'
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
        assert result == ref, type + '... testcount : dump mismatch'

        # Test by comparing the html
        tu     = zwparser.parse( getattr( model, attr, '' ), debuglevel=0 )
        ref    = tu.tohtml()
        result = model.translate()
        assert result == ref, type + '... testcount : html mismatch'

        # Test by translating to html
        #tu   = zwparser.parse( wikitext, debuglevel=0 )
        #html = tu.tohtml()
        #et.fromstring( html ) 

    def test_0_gettcktype( self ) :
        """Testing method for getting ticket types"""
        log.info( "Testing method for getting ticket types" )
        types   = config['zeta.tickettypes']
        dbtypes = tckcomp.get_tcktype()
        assert_equal( sorted(types),
                      sorted([ t.tck_typename for t in dbtypes ]),
                      'Mismatch in ticket types'
                    )
        assert_equal( sorted(types),
                      sorted([ tckcomp.get_tcktype(
                                    choice([ t, t.id, t.tck_typename ])
                               ).tck_typename for t in dbtypes ]),
                      'Mismatch in getting individual tickets types'
                    )
    
    def test_1_gettckstatus( self ) :
        """Testing method for getting ticket status"""
        log.info( "Testing method for getting ticket status" )
        status   = config['zeta.ticketstatus']
        dbstatus = tckcomp.get_tckstatus()
        assert_equal( sorted(status),
                      sorted([ ts.tck_statusname for ts in dbstatus ]),
                      'Mismatch in ticket status'
                    )
        assert_equal( sorted(status),
                      sorted([ tckcomp.get_tckstatus(
                                    choice([ ts, ts.id, ts.tck_statusname ])
                               ).tck_statusname for ts in dbstatus ]),
                      'Mismatch in getting individual ticket status'
                    )

    def test_2_gettckseverity( self ) :
        """Testing method for getting ticket severity"""
        log.info( "Testing method for getting ticket severity" )
        severity   = config['zeta.ticketseverity']
        dbseverity = tckcomp.get_tckseverity()
        assert_equal( sorted(severity),
                      sorted([ tsv.tck_severityname for tsv in dbseverity ]),
                      'Mismatch in ticket severity'
                    )
        assert_equal( sorted(severity),
                      sorted([ tckcomp.get_tckseverity(
                                    choice([ tsv, tsv.id, tsv.tck_severityname ])
                               ).tck_severityname for tsv in dbseverity ]),
                      'Mismatch in getting individual ticket severity'
                    )

    def test_3_createticket( self ) :
        """Testing ticket creation"""
        log.info( "Testing ticket creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for tck in tckdata :
            tckdet    = ( tck['id'], tck['summary'], tck['description'],
                          tck['tck_typename'], tck['tck_severityname'] )
            tck['id'] = tckcomp.create_ticket(
                            tck['project'], tckdet,
                            tck['promptuser'], tck['promptuser']
                        )
            # Ticket creation automatically creates the initial status.
            ts = tck['id'].statushistory[0]
        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))

    def test_4_updateticket( self ) :
        """Testing ticket updation"""
        log.info( "Testing ticket updation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        types    = tckcomp.get_tcktype()
        severity = tckcomp.get_tckseverity()
        users    = userscomp.get_user()
        for i in range(len(tckdata)) :
            if choice([ True, False ]) :
                continue
            updtfields    = { 'summary'         : u'updatesummary',
                              'description'     : u'updatedescription',
                              'tck_typename'    : choice( types ),
                              'tck_severityname': choice( severity )
                            }
            tck      = tckdata[i]
            key      = choice( updtfields.keys() )
            tck[key] = updtfields[key]
            tck['promptuser'] = (choice([ True, False ]) and tck['promptuser']) or choice(users)
            tckdet = ( tck['id'], tck['summary'], tck['description'],
                       tck['tck_typename'], tck['tck_severityname'] )
            tck['id'] = tckcomp.create_ticket(
                                    tck['project'], tckdet,
                                    tck['promptuser'], update=True )

            if choice([0,0,1]) :
                # Updating description with None should not nullify the attribute
                tckdet    = ( tck['id'], tck['summary'], None,
                              tck['tck_typename'], tck['tck_severityname'] )
                tck['id'] = tckcomp.create_ticket(
                                        tck['project'], tckdet,
                                        tck['promptuser'], update=True )
                t = tckcomp.get_ticket( tck['id'].id )
                assert_equal( t.description, tck['description'],
                              'Fail, while updating tck_description with None'
                            )

                # Updating description with '' should nullify the attribute
                tck['description'] = u''
                tckdet    = ( tck['id'], tck['summary'], tck['description'],
                              tck['tck_typename'], tck['tck_severityname'] )
                tck['id'] = tckcomp.create_ticket(
                                        tck['project'], tckdet,
                                        tck['promptuser'], update=True )
                t = tckcomp.get_ticket( tck['id'].id )
                assert_equal( t.description, u'', 
                              'Fail, while updating tck_description with ""'
                            )

        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))

    def test_5_getticket( self ) :
        """Testing method for getting tickets"""
        log.info( "Testing method for getting tickets" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        dbtickets = tckcomp.get_ticket()
        assert_equal( sorted([ tck['id'] for tck in tckdata ]),
                      sorted(dbtickets),
                      'Mismatch in tickets'
                    )
        assert_equal( sorted([ tckcomp.get_ticket(tck['id']) for tck in tckdata ]),
                      sorted(dbtickets),
                      'Mismatch in ticket obtained by passing ticket instance'
                    )
        assert_equal( sorted([ tckcomp.get_ticket(tck['id'].id) 
                               for tck in tckdata ]),
                      sorted(dbtickets),
                      'Mismatch in ticket obtained by passing ticket id'
                    )

    def test_6_configticket( self ) :
        """Testing ticket configuration"""
        log.info( "Testing ticket configuration" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        types      = tckcomp.get_tcktype()
        severities = tckcomp.get_tckseverity()
        users      = userscomp.get_user()
        for tck in tckdata :
            type           = choice(types)
            severity       = choice(severities)
            promptuser     = choice(users)
            parent         = [ tckcomp.get_ticket( tck['parent'] ), None ]\
                                    [ tck['parent']==tck['id'].id ]
            possibleargs   = { 
                'components' : tck['components'],
                'milestones' : tck['milestones'],
                'versions'   : tck['versions'],
                'blockedby'  : tck['blockedby'],
                'blocking'   : tck['blocking'],
                'parent'     : parent,
                'type'       : type,
                'severity'   : severity,
                'promptuser' : promptuser,
            }
            tck['tck_typename']     = type
            tck['tck_severityname'] = severity
            tck['promptuser']       = promptuser
            tck['parent']           = parent
            while possibleargs :
                keys   = set( [ choice(possibleargs.keys())
                                for i in range(randint(0,len(possibleargs))) ])
                kwargs = dict([ ( k, possibleargs.pop( k )) for k in keys ]) 
                tckcomp.config_ticket( tck['id'], **kwargs )

        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))
        self._validate_ticketconfig( sorted( tckdata, key=lambda tck : tck['id'] ),
                                     sorted( tckcomp.get_ticket() ))

        # Redo config_ticket to check the effect of None and non-None empty
        # params
        for tck in tckdata :
            type = choice( types + [None, None] )
            if type != None :
                tck['tck_typename'] = type

            severity = choice( severities + [None, None] )
            if severity != None :
                tck['tck_severityname'] = severity

            promptuser = choice( users + [None, u'' ] )
            if promptuser == '' :
                tck['promptuser'] = None
            elif promptuser != None :
                tck['promptuser'] = promptuser

            if tck['parent'] and tck['parent']==tck['id'].id :
                parent = None
            parent = choice([ parent, None, u'' ])
            if parent == '' :
                tck['parent'] = None
            elif parent != None :
                tck['parent'] = parent

            components = choice([ tck['components'], None, [] ])
            if components != None :
                tck['components'] = components

            milestones = choice([ tck['milestones'], None, [] ])
            if milestones != None :
                tck['milestones'] = milestones

            versions = choice([ tck['versions'], None, [] ])
            if versions != None :
                tck['versions'] = versions

            blockedby = choice([ tck['blockedby'], None, [] ])
            if blockedby != None :
                tck['blockedby'] = blockedby

            blocking = choice([ tck['blocking'], None, [] ])
            if blocking != None :
                tck['blocking'] = blocking

            possibleargs   = { 
                'components' : components,
                'milestones' : milestones,
                'versions'   : versions,
                'blockedby'  : blockedby,
                'blocking'   : blocking,
                'parent'     : parent,
                'type'       : type,
                'severity'   : severity,
                'promptuser' : promptuser,
            }
            while possibleargs :
                keys   = set( [ choice(possibleargs.keys())
                                for i in range(randint(0,len(possibleargs))) ])
                kwargs = dict([ ( k, possibleargs.pop( k )) for k in keys ]) 
                kwargs.update({ 'append' : False })
                tckcomp.config_ticket( tck['id'], **kwargs )

        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))
        self._validate_ticketconfig( sorted( tckdata, key=lambda tck : tck['id'] ),
                                     sorted( tckcomp.get_ticket() ))

    def test_7_createticketstatus( self ) :
        """Testing ticket status creation"""
        log.info( "Testing ticket status creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for tck in tckdata :
            for ts in tck['statushistory'] :
                tsdet    = ( ts['id'], ts['tck_statusname'], ts['due_date'] )
                ts['id'] = tckcomp.create_ticket_status(
                                choice([ tck['id'].id, tck['id'] ]),
                                tsdet, ts['owner']
                           )
                if ts['promptuser'] :
                    tckcomp.config_ticket( tck['id'], promptuser=ts['promptuser'] )
                    tck['promptuser'] = userscomp.get_user( ts['promptuser'] )

                #ts['tck_statusname'] = ts['id'].status
                #ts['due_date']       = ts['id'].due_date
                #ts['owner']          = ts['id'].owner
        allticketstatus = []
        for tck in tckdata :
            tsdata = tck['statushistory']
            allticketstatus.extend( tck['id'].statushistory )
            self._validate_ticketstatus(
                sorted( tsdata, key=lambda tst : tst['id'] ),
                # The first status entry is auto-created by create_ticket
                sorted( tck['id'].statushistory[1:]
            ))
            assert_true( tck['id'].statushistory[-1].id == tck['id'].tsh_id,
                         'Mismatch in latest ticket status for ticket'
                       )

        dballticketstatus = tckcomp.get_ticket_status()
        assert_equal( sorted( allticketstatus ), sorted( dballticketstatus ),
                      'Mismatch in created ticket status history' )
        self._validate_ticketconfig( sorted( tckdata, key=lambda tck : tck['id'] ),
                                     sorted( tckcomp.get_ticket() ))
        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))
                                            
    def test_8_updateticketstatus( self ) :
        """Testing ticket status updation"""
        log.info( "Testing ticket status updation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        status   = tckcomp.get_tckstatus()
        for tck in tckdata :
            p        = tck['project']
            tckusers = [ p.admin ] + [ pr.user for pr in p.team ]
            for ts in tck['statushistory'] :
                ts['tck_statusname'] = choice( status )
                ts['due_date']       = future_duedate(
                                            *dt.datetime.utcnow().timetuple())
                ts['owner']          = choice(tckusers)
                ts['promptuser']     = (randint(0,4) and ts['owner']) or None
                tsdet = ( ts['id'], ts['tck_statusname'], ts['due_date'] )
                ts['id'] = tckcomp.create_ticket_status( 
                                choice([ tck['id'].id, tck['id'] ]),
                                tsdet, ts['owner'], update=True
                           )
                if ts['promptuser'] :
                    tckcomp.config_ticket( tck['id'], promptuser=ts['promptuser'] )
                    tck['promptuser'] = userscomp.get_user( ts['promptuser'] )
        allticketstatus = []
        for tck in tckdata :
            tsdata = tck['statushistory']
            allticketstatus.extend( tck['id'].statushistory )
            self._validate_ticketstatus(
                    sorted( tsdata, key=lambda tst : tst['id'] ),
                    # The first status entry is auto-created by create_ticket
                    sorted( tck['id'].statushistory[1:] ))
        dballticketstatus = tckcomp.get_ticket_status()
        assert_equal( sorted( allticketstatus ), sorted( dballticketstatus ),
                      'Mismatch in updated ticket status history' )
        self._validate_ticketconfig( sorted( tckdata, key=lambda tck : tck['id'] ),
                                     sorted( tckcomp.get_ticket() ))
        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))

    def test_9_getticketstatus( self ) :
        """Testing method for getting ticket status"""
        log.info( "Testing method for getting ticket status" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        dballticketstatus = tckcomp.get_ticket_status()
        allticketstatus   = [ tckcomp.get_ticket_status( ts.id ) 
                              for ts in dballticketstatus ]
        assert_equal( sorted( allticketstatus ), sorted(dballticketstatus),
                      'Mismatch in get_ticket_status() getting by `id`' )
        allticketstatus   = [ tckcomp.get_ticket_status( ts ) 
                              for ts in dballticketstatus ]
        assert_equal( sorted( allticketstatus ), sorted(dballticketstatus),
                      'Mismatch in get_ticket_status() getting by instance' )

    def test_A_createticketcomment( self ) :
        """Testing ticket comment creation"""
        log.info( "Testing ticket comment creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for tck in tckdata :
            tcmtdata = tck['comments']
            for tcmt in tcmtdata :
                tcmtdet    = ( tcmt['id'], tcmt['text'], tcmt['commentby'] )
                tcmt['id'] = tckcomp.create_ticket_comment( tck['id'], tcmtdet )
                tcmt['commentby'] = userscomp.get_user( tcmt['commentby'] )
        allticketcomments = []
        for tck in tckdata :
            tcmtdata = tck['comments']
            allticketcomments.extend( tck['id'].comments )
            self._validate_ticketcomment(
                    sorted( tcmtdata, key=lambda tcmt : tcmt['id'] ),
                    sorted( tck['id'].comments ))
        dballticketcomments = tckcomp.get_ticket_comment()
        assert_equal( sorted( allticketcomments ), sorted(dballticketcomments),
                      'Mismatch in created ticket comment' )
        self._validate_ticketconfig( sorted( tckdata, key=lambda tck : tck['id'] ),
                                     sorted( tckcomp.get_ticket() ))
        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))

    def test_B_updateticketcomment( self ) :
        """Testing ticket comment updation"""
        log.info( "Testing ticket comment updation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        for tck in tckdata :
            for tcmt in tck['comments'] :
                tcmt['text']      = u'Updated ticket comment'
                tcmt['commentby'] = choice(users)
                tcmtdet           = ( tcmt['id'], tcmt['text'], tcmt['commentby'] )
                tcmt['id']        = tckcomp.create_ticket_comment( 
                                            choice([ tck['id'].id, tck['id'] ]),
                                            tcmtdet, update=True
                                    )
        allticketcomments = []
        for tck in tckdata :
            tcmtdata = tck['comments']
            allticketcomments.extend( tck['id'].comments )
            self._validate_ticketcomment(
                    sorted( tcmtdata, key=lambda tcmt : tcmt['id'] ),
                    sorted( tck['id'].comments ))
        dballticketcomments = tckcomp.get_ticket_comment()
        assert_equal( sorted( allticketcomments ), sorted(dballticketcomments),
                      'Mismatch in updated ticket comment history' )
        self._validate_ticketconfig( sorted( tckdata, key=lambda tck : tck['id'] ),
                                     sorted( tckcomp.get_ticket() ))
        self._validate_tickets( sorted( tckdata, key=lambda tck : tck['id'] ),
                                sorted( tckcomp.get_ticket() ))

    def test_C_getticketcomment( self ) :
        """Testing method for getting ticket comments"""
        log.info( "Testing method for getting ticket comments" )
        dballticketcomments = tckcomp.get_ticket_comment()
        allticketcomments   = [ tckcomp.get_ticket_comment( tc.id ) 
                              for tc in dballticketcomments ]
        assert_equal( sorted( allticketcomments ), sorted(dballticketcomments),
                      'Mismatch in get_ticket_comment() getting by `id`' )
        allticketcomments   = [ tckcomp.get_ticket_comment( tc ) 
                              for tc in dballticketcomments ]
        assert_equal( sorted( allticketcomments ), sorted(dballticketcomments),
                      'Mismatch in get_ticket_comment() getting by instance' )

    def test_D_ticketreplies( self ) :
        """Testing ticket conversation"""
        log.info( "Testing ticket conversation" )
        for tck in tckdata :
            for i in range(0, len(tck['replies'])) :
                replyto = tck['replies'][i]
                replyto != -1 and tckcomp.comment_reply(
                                        tck['comments'][i]['id'], 
                                        tck['comments'][replyto]['id'] )
        for tck in tckdata :
            replies = {}
            for i in range(0, len(tck['replies'])) :
                replyto = tck['replies'][i]
                replyto != -1 and replies.setdefault(
                                    tck['comments'][replyto]['id'], []
                                  ).append( tck['comments'][i]['id'] )
            for tcmt in replies :
                tckcmt = tckcomp.get_ticket_comment( tcmt )
                assert_equal(
                    sorted([ tckcomp.get_ticket_comment(i) for i in replies[tcmt] ]),
                    sorted( tckcmt.replies ),
                    'Mismatch in ticket comment replies' 
                )

    def test_E_tags( self ) :
        """Testing tag additions and removals"""
        log.info( "Testing tag additions and removals" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for tck in tckdata :
            t         = tck['id']
            byuser    = choice( tck['tags'].keys() )
            tags      = tck['tags'][byuser]
            rmtag     = tags and choice(tags) or u''
            tckcomp.add_tags( choice([ t.id, t ]), tags, byuser=byuser )
            tckcomp.remove_tags( t, rmtag )
            rmtag and tags.remove(rmtag)
            assert_equal( sorted( tags ),
                          sorted([ tag.tagname for tag in t.tags ]),
                          'Mismatch in ticket tag methods'
                        )

    def test_F_attach( self ) :
        """Testing attachment additions and removals"""
        log.info( "Testing attachment additions and removals" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        attachs = {}
        for tck in tckdata :
            t = tck['id']
            attachs[t] = []
            for u in tck['attachs'] :
                for f in tck['attachs'][u] :
                    attach = attachcomp.create_attach(
                                            os.path.basename( f ),
                                            choice([ open( f, 'r' ), None  ]),
                                            uploader=u,
                                            summary=u'',
                             )
                    tckcomp.add_attach( t, attach )
                    attachs[t].append( (u, f, attach) )
            rmattach = [ tup for tup in attachs[t]  if choice([ True, False ]) ]
            for tup in rmattach :
                attachs[t].remove( tup )
                tckcomp.remove_attach( t, tup[2] )
                tck['attachs'][tup[0]].remove( tup[1] )
        for t in tckcomp.get_ticket() :
            atts = [ tup[2] for tup in attachs[t] ]
            assert_equal( sorted(atts), sorted(t.attachments),
                          'Mismatch in project attachments' )

    def test_G_properties( self ) :
        """Testing ticket component properties"""
        log.info( "Testing ticket component properties" )
        assert_equal( sorted([ tt.tck_typename 
                               for tt in tckcomp.get_tcktype() ]),
                      sorted( tckcomp.tcktypenames ),
                      'Mismatch in `tcktypenames` property'
                    )
        assert_equal( sorted([ tst.tck_statusname
                               for tst in tckcomp.get_tckstatus() ]),
                      sorted( tckcomp.tckstatusnames ),
                      'Mismatch in `tckstatusnames` property'
                    )
        assert_equal( sorted([ tsv.tck_severityname
                               for tsv in tckcomp.get_tckseverity() ]),
                      sorted( tckcomp.tckseveritynames ),
                      'Mismatch in `tckseveritynames` property'
                    )

        # Upgrade ticket fields
        n_tcmts   = len(tckcomp.get_ticket_comment())
        n_tickets = len(tckcomp.get_ticket())
        u_tickets, u_tcmts = tckcomp.upgradewiki()
        assert_true( u_tickets == n_tickets,
                     'Problem in upgrading ticket comments' )
        assert_true( u_tcmts == n_tcmts,
                     'Problem in upgrading ticket comments' )

    def test_H_ticketsts( self ) :
        """Testing Ticket status, type, severity creation"""
        log.info( "Testing Ticket status, type, severity creation" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        # Test Ticket type creation
        ref_tcktypes = tckcomp.tcktypenames
        add_tcktypes = [ u'tickettype1', u'tickettype2' ]
        ref_tcktypes += add_tcktypes
        tckcomp.create_tcktype( add_tcktypes )
        assert_equal( sorted(ref_tcktypes), sorted(tckcomp.tcktypenames),
                      'Mismatch in creating ticket types as list' )

        add_tcktypes = u'tickettype3'
        ref_tcktypes += [ add_tcktypes ]
        tckcomp.create_tcktype( add_tcktypes )
        assert_equal( sorted(ref_tcktypes), sorted(tckcomp.tcktypenames),
                      'Mismatch in creating ticket type as string' )

        # Test Ticket status creation
        ref_tckstatus = tckcomp.tckstatusnames
        add_tckstatus = [ u'ticketstatus1', u'ticketstatus2' ]
        ref_tckstatus += add_tckstatus
        tckcomp.create_tckstatus( add_tckstatus )
        assert_equal( sorted(ref_tckstatus), sorted(tckcomp.tckstatusnames),
                      'Mismatch in creating ticket status as list' )

        add_tckstatus = u'ticketstatus3'
        ref_tckstatus += [ add_tckstatus ]
        tckcomp.create_tckstatus( add_tckstatus )
        assert_equal( sorted(ref_tckstatus), sorted(tckcomp.tckstatusnames),
                      'Mismatch in creating ticket status as string' )

        # Test Ticket severity creation
        ref_tckseverity = tckcomp.tckseveritynames
        add_tckseverity = [ u'ticketseverity1', u'ticketseverity2' ]
        ref_tckseverity += add_tckseverity
        tckcomp.create_tckseverity( add_tckseverity )
        assert_equal( sorted(ref_tckseverity), sorted(tckcomp.tckseveritynames),
                      'Mismatch in creating ticket severity as list' )

        add_tckseverity = u'ticketseverity3'
        ref_tckseverity += [ add_tckseverity ]
        tckcomp.create_tckseverity( add_tckseverity )
        assert_equal( sorted(ref_tckseverity), sorted(tckcomp.tckseveritynames),
                      'Mismatch in creating ticket severity as string' )

    def test_I_wikitranslate( self ) :
        """Testing the wiki translation for ticket description and comments"""
        for tck in tckdata :
            self._testwiki_execute( 'tckdesc', tck['id'], 'description' )
            tcmtdata = tck['comments']
            for tcmt in tcmtdata :
                self._testwiki_execute( 'tckcmt', tcmt['id'], 'text' )
        for t in tckcomp.get_ticket() :
            self._testwiki_execute( 'tckdesc', t, 'description' )
        for tcmt in tckcomp.get_ticket_comment() :
            self._testwiki_execute( 'tckcmt', tcmt, 'text' )

    def test_J_favorites( self ) :
        """Testing favorite addition and deletion for tickets"""
        log.info( "Testing favorite addition and deletion for tickets" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for tck in tckdata :
            t = tck['id']
            if choice([ True, False ]) : # as list
                tckcomp.addfavorites( t, tck['favusers'] )
            else :                       # as byuser
                for u in tck['favusers'] :
                    tckcomp.addfavorites( t, u, byuser=u )
            rmfavusers = [ u for u in tck['favusers'] if choice([ 1, 0, 0 ]) ]
            [ tck['favusers'].remove( u ) for u in rmfavusers ]
            if choice([ True, False ]) : # as list
                tckcomp.delfavorites( t, rmfavusers )
            else :                       # as byuser
                for u in rmfavusers :
                    tckcomp.delfavorites( t, u, byuser=u )
        for tck in tckdata :
            t    = tckcomp.get_ticket( tck['id'].id )
            assert_equal( sorted(t.favoriteof),
                          sorted([ userscomp.get_user( u ) 
                                   for u in tck['favusers'] ]),
                          'Mismatch in creating ticket favorites'
                        )

    def test_K_voting( self ) :
        """Testing ticket voting"""
        log.info( "Testing ticket voting" )
        
        for tck in tckdata :
            t = tck['id']
            for u in tck['voteup'] :
                tckcomp.voteup( t, u )
            for u in tck['votedown'] :
                tckcomp.votedown( t, u )

        for tck in tckdata :
            t = tckcomp.get_ticket( tck['id'].id )
            upvotes   = votcomp.ticketvotes( t, votedas=u'up' )
            upusers   = [ v.voter for v in upvotes ]
            downvotes = votcomp.ticketvotes( t, votedas=u'down' )
            downusers = [ v.voter for v in downvotes ]
            assert_equal( sorted( upusers ), sorted( tck['voteup'] ),
                          'Mismatch in users voting for ticket' )
            assert_equal( sorted( downusers ), sorted( tck['votedown'] ),
                          'Mismatch in users voting against ticket' )

    def test_L_mstntickets( self ) :
        """Testing mstntickets() data crunching method"""
        log.info( "Testing mstntickets() data crunching method" )

        project = choice( projcomp.get_project() )
        ref = {}
        for m in project.milestones :
            if m.tickets :
                for t in m.tickets :
                    ts = tckcomp.get_ticket_status( t.tsh_id )
                    ref.setdefault( m.id, [] ).append(
                        ( t.type.tck_typename, t.severity.tck_severityname, 
                          ts.status.tck_statusname, ts.owner.username )
                    )
            else :
                ref[m.id] = [( None, None, None, None )]

        mstntickets = tckcomp.mstntickets( project )
        assert_equal( mstntickets, ref, 'Mismatch in mstntickets' )

    def test_M_misc( self ) :
        """Testing miscellaneous functions"""
        log.info( "Testing miscellaneous functions" )

        ttypes = tckcomp.get_tcktype()
        tstats = tckcomp.get_tckstatus()
        tsevs  = tckcomp.get_tckseverity()
        owners = userscomp.get_user()
        comps  = projcomp.get_component()
        mstns  = projcomp.get_milestone()
        vers   = projcomp.get_version()

        tickets = tckcomp.get_ticket()
        users   = userscomp.get_user()

        # Testing ticketids()
        p = choice( projcomp.get_project( attrload=['tickets'] ))
        assert_equal( sorted([ t.id for t in p.tickets ]),
                      sorted( 
                          tckcomp.ticketids(choice([ p.id, p.projectname, p ]))
                      ),
                      'Mismatch in computing ticketids()'
                    )

        # Testing ticketsummary()
        p = choice( projcomp.get_project( attrload=['tickets'] ))
        assert_equal( sorted( [ (t.id, t.summary) for t in p.tickets ],
                              key=lambda tup: tup[0] ),
                      sorted( 
                          tckcomp.ticketsummary(choice([ p.id, p.projectname, p ])),
                          key=lambda tup : tup[0]
                      ),
                      'Mismatch in computing ticketsummary()'
                    )

        # Testing projdetails()
        project = choice( projcomp.get_project() )
        pcomponents, pmilestones, pversions, projusers = \
            tckcomp.projdetails(choice([ project.id, project.projectname, project ]))
        assert_equal( sorted( pcomponents, key=lambda x: x[1] ),
                      sorted( [ (comp.componentname, comp.id ) 
                                for comp in  project.components ],
                              key=lambda x : x[1] ),
                      'Mismatch in projdetails, pcomponents'
                    )
                
        assert_equal( sorted( pmilestones, key=lambda x : x[1] ),
                      sorted( [ (mstn.milestone_name, mstn.id, mstn.completed,
                                 mstn.cancelled) 
                                for mstn in  project.milestones ],
                              key=lambda x : x[1]
                            ),
                      'Mismatch in projdetails, pmilestones'
                    )
        assert_equal( sorted( pversions, key=lambda x: x[1] ),
                      sorted( [ (ver.version_name, ver.id ) 
                                for ver in  project.versions ],
                              key=lambda x : x[1]
                            ),
                      'Mismatch in projdetails, pversions'
                    )
        assert_equal( sorted( projusers ),
                      sorted( projcomp.projusernames( project )),
                      'Mismatch in projdetails, projusers'
                    )

        # Testing user ticketlist()
        user    = choice( users )
        tcklist = tckcomp.ticketlist( user=user )
        reflist = {}
        for t in tickets :
            if user.username not in [ t.statushistory[-1].owner.username,
                                      t.promptuser and t.promptuser.username ] :
                continue
            ts   = tckcomp.get_ticket_status( t.tsh_id )
            comp = ( None, None )
            if t.components :
                comp = ( t.components[0].id, t.components[0].componentname )
            mstn = ( None, None )
            if t.milestones :
                mstn = ( t.milestones[0].id, t.milestones[0].milestone_name )
            ver = ( None, None )
            if t.versions :
                ver = ( t.versions[0].id, t.versions[0].version_name )

            l  = [ t.id, t.project.projectname, t.summary, t.created_on,
                   t.type.tck_typename, t.severity.tck_severityname,
                   ts.status.tck_statusname,  ts.id, ts.due_date,
                   ts.owner.username, t.promptuser.username,
                   comp[0], comp[1], mstn[0], mstn[1], ver[0], ver[1],
                   len([ v for v in t.votes if v.votedas == 'up' ]),
                   len([ v for v in t.votes if v.votedas == 'down' ])
                 ]
            reflist[t.id] = l
        assert_equal( reflist, tcklist, 'Mismatch in ticket list' )

        # Testing project ticketlist()
        project = choice( projcomp.get_project() )
        tcklist = tckcomp.ticketlist( project=project )
        assert_equal( sorted(tckcomp.ticketids( project )),
                      sorted(tcklist.keys()),
                      'Mismatch in ticketids while fetching ticketlist'
                    )
        reflist = {}
        for t in project.tickets :
            ts   = tckcomp.get_ticket_status( t.tsh_id )
            comp = ( None, None )
            if t.components :
                comp = ( t.components[0].id, t.components[0].componentname )
            mstn = ( None, None )
            if t.milestones :
                mstn = ( t.milestones[0].id, t.milestones[0].milestone_name )
            ver = ( None, None )
            if t.versions :
                ver = ( t.versions[0].id, t.versions[0].version_name )

            l  = [ t.id, t.project.projectname, t.summary, t.created_on,
                   t.type.tck_typename, t.severity.tck_severityname,
                   ts.status.tck_statusname,  ts.id, ts.due_date,
                   ts.owner.username, t.promptuser.username,
                   comp[0], comp[1], mstn[0], mstn[1], ver[0], ver[1],
                   len([ v for v in t.votes if v.votedas == 'up' ]),
                   len([ v for v in t.votes if v.votedas == 'down' ])
                 ]
            reflist[t.id] = l
        assert_equal( reflist, tcklist, 'Mismatch in ticket list' )

        # Testing project ticketlist() with type filters.
        filters  = {}
        ttype    = choice(ttypes).tck_typename
        filtlist = copy.deepcopy( reflist )
        filtlist = dict([ (k, v) for k, v in reflist.iteritems()
                                 if v[4] == ttype ])
        filters.update({ 'tck_typename' : ttype })
        assert_equal( tckcomp.ticketlist( project=project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with type filter added'
                    )
                      
        # Testing project ticketlist() with type+severity filters.
        tsev     = choice(tsevs).tck_severityname
        filters.update({ 'tck_severityname' : tsev })
        filtlist = dict([ (k, v) for k, v in filtlist.iteritems() 
                                 if v[5] == tsev ])
        assert_equal( tckcomp.ticketlist( project=project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with type+sev filter added'
                    )
                      
        # Testing project ticketlist() with sev+status filters.
        filters.pop( 'tck_typename' )
        tstat    = choice(tstats).tck_statusname
        filters.update({ 'tck_statusname' : tstat })
        filtlist = dict([ (k, v) for k, v in filtlist.iteritems()
                                 if v[6] == tstat ])
        assert_equal( tckcomp.ticketlist( project=project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with sev+status filter added'
                    )
                      
        # Testing project ticketlist() with s+o filters.
        filters.pop( 'tck_severityname' )
        owner    = choice(owners).username
        filters.update({ 'owner' : owner })
        filtlist = dict([ (k, v) for k, v in filtlist.iteritems()
                                 if v[9] == owner ])
        assert_equal( tckcomp.ticketlist( project=project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with s+o filter added'
                    )
        ownerlist = copy.deepcopy( filtlist )
                      
        # Testing project ticketlist() with o+c filters.
        filters.pop( 'tck_statusname' )
        comp     = choice(comps).componentname
        filters.update({ 'componentname' : comp })
        filtlist = dict([ (k, v) for k, v in ownerlist.iteritems()
                                 if v[12] == comp ])
        assert_equal( tckcomp.ticketlist( project=project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with owner+comp filter added'
                    )
                      
        # Testing project ticketlist() with o+m filters.
        filters.pop( 'componentname' )
        mstn     = choice(mstns).milestone_name
        filters.update({ 'milestone_name' : mstn })
        filtlist = dict([ (k, v) for k, v in ownerlist.iteritems()
                                 if v[14] == mstn ])
        assert_equal( tckcomp.ticketlist( project=project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with owner+mstn filter added'
                    )
                      
        # Testing project ticketlist() with o+v filters.
        filters.pop( 'milestone_name' )
        ver      = choice(vers).version_name
        filters.update({ 'version_name' : ver })
        filtlist = dict([ (k, v) for k, v in ownerlist.iteritems()
                                 if v[16] == ver ])
        assert_equal( tckcomp.ticketlist( project, filters=filters ),
                      filtlist,
                      'Mismatch in ticketlist with owner+ver filter added'
                    )

        # ticketcomments()
        t = choice( tickets )
        tcomments = dict([ (tcomment[0], tcomment)
                           for tcomment in tckcomp.tckcomments(t.id) ])
        assert_equal( len(tcomments), len(t.comments),
                      'Mismatch in number of ticket comments' )
        for tcmt in t.comments :
            assert_equal(
                [ tcmt.id, tcmt.text, tcmt.texthtml,
                  tcmt.created_on, tcmt.commentby.username ],
                list(tcomments[tcmt.id]),
                'Mismatch in tckcomments()'
            )

        # tckrcomment()
        t = choice( tickets )
        tcomments  = dict([ (tcomment[0], tcomment)
                           for tcomment in tckcomp.tckcomments(t.id) ])
        trcomments = {}
        for tcmt in tckcomp.tckrcomments( t.id ) :
            trcomments[ tcmt[0] ] = tuple(tcmt[:-2])
            for trcmt in tcmt[-1] :
                trcomments[trcmt[0]] = tuple(trcmt[:-2])
        assert_equal( tcomments, trcomments, 'Mismatch in tckrcomments()' )

        # ticketdetails()
        t   = choice( tickets )
        ts  = t.statushistory[-1]
        det = tckcomp.ticketdetails( t )
        ref = { 'id'              : t.id,                
                'summary'         : t.summary,
                'description'     : t.description,
                'descriptionhtml' : t.descriptionhtml,
                'summary'         : t.summary,
                'type'            : t.type.tck_typename,
                'severity'        : t.severity.tck_severityname,
                'status'          : ts.status.tck_statusname,
                'due_date'        : ts.due_date,          
                'created_on'      : t.created_on,
                'owner'           : ts.owner.username,
                'promptuser'      : t.promptuser.username,
                'compid'          : t.components and t.components[0].id or None,
                'compname'        : t.components and t.components[0].componentname or None,
                'mstnid'          : t.milestones and t.milestones[0].id or None,
                'mstnname'        : t.milestones and t.milestones[0].milestone_name or None,
                'verid'           : t.versions and t.versions[0].id or None,
                'vername'         : t.versions and t.versions[0].version_name or None,
                'parent'          : t.parent and t.parent.id or None,
              }
        assert_equal( ref, det, 'Mismatch in ticketdetails()' )

        # ticketstatus()
        t        = choice( tickets )
        statuses = tckcomp.ticketstatus( t )
        ref      = [ ( ts.id, ts.status.tck_statusname, ts.due_date,
                       ts.created_on, ts.owner.username
                     ) for ts in t.statushistory ]
        assert_equal( statuses, ref, 'Mismatch in ticketstatus()' )

        # blockersof()
        t = choice( tickets )
        assert_equal( sorted( tckcomp.blockersof( t )),
                      sorted([ tb.id for tb in t.blockedby ]),
                      'Mismatch in blockersof()' )

        # blockingfor()
        t = choice( tickets )
        assert_equal( sorted( tckcomp.blockingfor( t )),
                      sorted([ tb.id for tb in t.blocking ]),
                      'Mismatch in blockingfor()'
                    )

        # childrenfor()
        t = choice( tickets )
        assert_equal( sorted( tckcomp.childrenfor( t )),
                      sorted([ tc.id for tc in t.children ]),
                      'Mismatch in childrenfor()'
                    )

        # Count ticket votes, and ticketsproject(), allblockers(),
        # allparchild()
        ref1 = []
        ref2 = []
        ref3 = []
        for t in tckcomp.get_ticket(
                    attrload=[ 'votes', 'project', 'blockedby', 'children' ] ) :
            d = {}
            [ d.setdefault(v.votedas, []).append(1) for v in t.votes ]
            d['up']   = len(d['up'])
            d['down'] = len(d['down'])
            assert_equal( d, tckcomp.countvotes( ticket=t ),
                          'Mismatch in counting ticket votes' )

            ref1.append( (t.id, t.project.id, t.project.projectname) )
            ref2.extend([ (_t.id, t.id) for _t in t.blockedby ])
            ref3.extend([ (t.id, _t.id) for _t in t.children ])
        data = tckcomp.ticketsproject()
        assert_equal( sorted( ref1, key=lambda x : x[0] ),
                      sorted( data, key=lambda x : x[0] ),
                      'Mismatch in ticketsproject() method' )
        data = tckcomp.allblockers()
        assert_equal( set(ref2), set([ tuple(x) for x in data ]),
                      'Mismatch in allblockers() method' )
        data = tckcomp.allparchild()
        assert_equal( set(ref3), set([ tuple(x) for x in data ]),
                      'Mismatch in allparchild() method' )

        # isfavorite()
        user = choice( users )
        t    = user.favoritetickets and choice(user.favoritetickets)
        assert_true( tckcomp.isfavorite( user.id, t.id ),
                     'Mismatch in isfavorite()' )


    def test_N_attachments( self ) :
        """Testing method, attachments()"""
        log.info( "Testing method, attachments()" )

        projects = projcomp.get_project()
        for p in projects :
            tattachs= {}
            for t in p.tickets :
                attachs = {}
                for a in t.attachments :
                    attachs[a.id] = [ a.filename, a.size, a.summary, a.download_count,
                                      a.created_on, a.uploader.username,
                                      [ tag.tagname for tag in a.tags ]
                                    ]
                if attachs :
                    tattachs[t.id] = attachs
            attachments = tckcomp.attachments( p )
            assert_equal(
                attachments, tattachs, 
                'Mismatch in attachments, for tickets in project %s' % p.projectname
            )

    def test_M_userstats( self ) :
        """Testing method, userstats"""
        log.info( "Testing method, userstats" )

        for u in userscomp.get_user() :
            # For usertickets()
            reftcks = {}
            [ reftcks.setdefault( ts.ticket.id, [] ). append( ts.id ) 
              for ts in u.owntickets ]
            reftcks = dict([ (k, sorted(reftcks[k])) for k in reftcks ])
            tcks = tckcomp.usertickets( u )
            tcks = dict([ (k, sorted(tcks[k])) for k in tcks ])
            assert_equal( tcks, reftcks,
                          'Mismatch in usertickets(), for user %s' % u.username )

            # For usercomments()
            tcmtids = tckcomp.usercomments( u )
            assert_equal( sorted(tcmtids),
                          sorted([ tcmt.id for tcmt in u.ticketcomments ]),
                          'Mismatch in usercomments(), for user %s' % u.username )

    @attr(type='filters')
    def test_N_filters( self ) :
        """Testing ticket filter methods"""
        log.info( "Testing ticket filter methods" )

        t    = choice(tckcomp.get_tcktype()).tck_typename
        st   = choice(tckcomp.get_tckstatus()).tck_statusname
        sv   = choice(tckcomp.get_tckseverity()).tck_severityname
        own  = choice(userscomp.get_user()).username
        comp = choice(projcomp.get_component()).componentname
        mstn = choice(projcomp.get_milestone()).milestone_name
        ver  = choice(projcomp.get_version()).version_name
        user = choice(userscomp.get_user())
        
        # Create ticket filter
        json = fjson1 % ( t, st, sv, own, comp, mstn, ver )
        tf1 = tckcomp.create_ticketfilter( name=u'filter1',
                                          filterbyjson=json,
                                          foruser=g_byuser,
                                          byuser=g_byuser,
                                        )
        tf = tckcomp.get_ticketfilter( tf1.id )
        assert_equal( [tf.name, tf.filterbyjson, tf.foruser.username],
                      ['filter1', json, g_byuser],
                      'Mismatch in creating ticket filters'
                    )

        json = fjson1 % ( t, st, sv, own, comp, mstn, ver )
        tf2 = tckcomp.create_ticketfilter( name=u'filter2',
                                          filterbyjson=json,
                                          foruser=user,
                                          byuser=g_byuser,
                                        )
        tf = tckcomp.get_ticketfilter( tf2 )
        assert_equal( [tf.name, tf.filterbyjson, tf.foruser.username],
                      ['filter2', json, user.username],
                      'Mismatch in creating ticket filters'
                    )
        
        # Update ticket filter
        t    = choice(tckcomp.get_tcktype()).tck_typename
        json = fjson1 % ( t, st, sv, own, comp, mstn, ver )
        tf = tckcomp.create_ticketfilter( tf=tf,
                                          name=u'filter2..',
                                          filterbyjson=json,
                                          byuser=g_byuser,
                                          update=True
                                        )
        tf = tckcomp.get_ticketfilter( tf.id )
        assert_equal( [tf.name, tf.filterbyjson, tf.foruser.username],
                      ['filter2..', json, user.username],
                      'Mismatch in createing ticket filters'
                    )


        # Get ticket by user
        tfs = tckcomp.get_ticketfilter( user=user )
        tf2 = tckcomp.get_ticketfilter( tf2.id )
        assert_equal( tfs, [tf2], 'Mismatch in get_ticketfilter with user' )

        # Delete ticket filter
        tckcomp.del_ticketfilter( tfs=[tf1], byuser=g_byuser )
        assert_equal( tckcomp.get_ticketfilter(), [ tf2 ],
                      'Mismatch in deleting ticket_filters' )
