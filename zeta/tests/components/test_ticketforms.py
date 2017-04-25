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
from   nose.plugins.attrib          import attr

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_tickets
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.vote               import VoteComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 5
no_of_attachs   = 1
no_of_projects  = 10
no_of_tickets   = 30
g_byuser        = u'admin'

tagchars   = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
taglist     = None 

compmgr     = None
userscomp   = None
attachcomp  = None
tagcomp     = None
liccomp     = None
projcomp    = None
tckcomp     = None
votcomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, tagcomp, projcomp, tckcomp, taglist,\
           votcomp, seed, cachemgr

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
    tckcomp    = TicketComponent( compmgr )
    votcomp    = VoteComponent( compmgr )
    taglist = [ unicode(h.randomname( randint(1,LEN_TAGNAME), tagchars))
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
    print "   Populating tickets ( no_of_tickets=%s ) ..." % no_of_tickets
    pop_tickets( no_of_tickets, no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_tickets=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_tickets )

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


class TestTicketForms( object ) :

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

    def test_1_createticket_valid( self ) :
        """Testing FormCreateTicket with valid input"""
        log.info( "Testing FormCreateTicket with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createtck' )

        c.rclose = h.ZResp()
        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        tickets      = tckcomp.get_ticket()
        u            = choice( users )
        p            = choice( projects )
        tcktypes     = tckcomp.get_tcktype()
        tckseverity  = tckcomp.get_tckseverity()

        # Create ticket
        summary          = u'some ticket summary'
        description      = u'some ticket description'
        tck_typename     = choice( tcktypes ).tck_typename
        tck_severityname = choice( tckseverity ).tck_severityname
        promptuser       = choice( users ).username
        tagnames         = list(set([ choice( taglist ) 
                                      for i in range(randint(0,10)) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'summary',     summary )
        request.POST.add( 'description', description )
        request.POST.add( 'tck_typename', tck_typename )
        request.POST.add( 'tck_severityname', tck_severityname )
        request.POST.add( 'promptuser', promptuser )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createtck'] )

        defer and c.rclose.close()
        # TODO : After refactoring, the following check can be enabled.
        #self._validate_defer(
        #        c.authuser, defer, c,
        #        lambda u : 'created project ticket' in u.logs[-1].log 
        #)

        ticket_id       = len(tickets) + 1
        t               = tckcomp.get_ticket( ticket_id )
        assert_equal( [ t.summary, t.description, t.type.tck_typename,
                        t.severity.tck_severityname, t.promptuser.username,
                        t.project.id ],
                      [ summary, description, tck_typename, tck_severityname,
                        promptuser, p.id ],
                      'Mismatch in creating ticket'
                    )
        assert_equal( sorted([ tag.tagname for tag in t.tags ]),
                      sorted( tagnames ),
                    )

        # Update ticket
        c.rclose = h.ZResp()
        request.POST.clearfields()
        summary          = u'updated ticket summary'
        description      = u'updated ticket description'
        tck_typename     = choice( tcktypes ).tck_typename
        tck_severityname = choice( tckseverity ).tck_severityname
        promptuser       = choice( users ).username
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'summary',     summary )
        request.POST.add( 'description', description )
        request.POST.add( 'tck_typename', tck_typename )
        request.POST.add( 'tck_severityname', tck_severityname )
        request.POST.add( 'promptuser', promptuser )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createtck'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Updated ticket information' in u.logs[-2].log and \
                           'changed attributes' in u.logs[-1].log 
        )

        t               = tckcomp.get_ticket( ticket_id )
        assert_equal( [ t.summary, t.description, t.type.tck_typename,
                        t.severity.tck_severityname, t.promptuser.username,
                        t.project.id ],
                      [ summary, description, tck_typename, tck_severityname,
                        promptuser, p.id ],
                      'Mismatch in updating ticket'
                    )

    def test_2_createticket_invalid( self ) :
        """Testing FormCreateTicket with invalid input"""
        log.info( "Testing FormCreateTicket with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createtck' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        tickets      = tckcomp.get_ticket()
        u            = choice( users )
        p            = choice( projects )
        tcktypes     = tckcomp.get_tcktype()
        tckseverity  = tckcomp.get_tckseverity()
        # Create ticket
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtck']
                     )
        summary          = u'some ticket summary'
        request.POST.add( 'summary',     summary )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtck']
                     )
        description      = u'some ticket description'
        request.POST.add( 'description', description )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtck']
                     )
        tck_typename     = choice( tcktypes ).tck_typename
        request.POST.add( 'tck_typename', tck_typename )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtck']
                     )
        
    def test_3_ticketconfig( self ) :
        """Testing FormTicketConfig with valid and invalid input"""
        log.info( "Testing FormTicketConfig with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configtck' )

        c.rclose = h.ZResp()
        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        components   = projcomp.get_component()
        milestones   = projcomp.get_milestone()
        versions     = projcomp.get_version()
        tickets      = tckcomp.get_ticket()
        types        = tckcomp.get_tcktype()
        status       = tckcomp.get_tckstatus()
        severity     = tckcomp.get_tckseverity()
        u            = choice( users )
        p            = choice( projects )
        t            = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )

        type             = choice( types + [ None ] * 5 )
        severity         = choice( severity + [ None ] * 5 )
        promptuser       = choice( users + [ None ] * 5 )
        parent           = choice( tickets + [ None ] * 5 )
        component_ids    = [ components[i].id for i in range(randint(0,len(components))) ]
        milestone_ids    = [ milestones[i].id for i in range(randint(0,len(milestones))) ]
        version_ids      = [ versions[i].id for i in range(randint(0,len(versions))) ]
        block            = choice([ 'bi', 'be' ])
        bi_ids           = []
        be_ids           = []
        if block == 'bi' :
            bi_ids = [ tickets[i].id for i in range(randint(0,len(tickets)))
                       if tickets[i].id != t.id ]
        if block == 'be' :
            be_ids = [ tickets[i].id for i in range(randint(0,len(tickets)))
                       if tickets[i].id != t.id ]
        blocking_ids     = choice(
                            [ ', '.join([ str(id) for id in bi_ids ]),
                              ', ,, ,',
                              ''
                            ]
                           )
        blockedby_ids    = choice(
                            [ ', '.join([ str(id) for id in  be_ids ]),
                              ', ,, ,',
                              ''
                            ]
                           )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        type and request.POST.add( 'tck_typename', type.tck_typename )
        severity and request.POST.add( 'tck_severityname', severity.tck_severityname )
        promptuser and request.POST.add( 'promptuser', promptuser.username )
        parent and request.POST.add( 'parent_id', str(parent.id) )
        component_ids and [ request.POST.add( 'component_id', str(id) ) for id in component_ids ]
        milestone_ids and [ request.POST.add( 'milestone_id', str(id) ) for id in milestone_ids ]
        version_ids and [ request.POST.add( 'version_id', str(id) ) for id in version_ids ]
        if block == 'bi' :
            request.POST.add( 'blocking_ids', blocking_ids )
        elif block == 'be' :
            request.POST.add( 'blockedby_ids', blockedby_ids )

        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['configtck'] )
        
        if promptuser :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'changed attributes' in u.logs[-1].log and \
                               promptuser.username in u.logs[-1].log
            )
        elif defer :
            c.rclose.close()

        if type :
            assert_equal( t.type.tck_typename, type.tck_typename,
                          'Mismatch in ticket type while configuring the ticket' )
        if severity :
            assert_equal( t.severity.tck_severityname, severity.tck_severityname,
                          'Mismatch in ticket severity while configuring the ticket' )
        if promptuser :
            assert_equal( t.promptuser.username, promptuser.username,
                          'Mismatch in ticket promptuser while configuring the ticket' )
        if parent :
            assert_equal( parent.id, t.parent.id,
                          'Mismatch in ticket parent while configuring the ticket' )
        if component_ids :
            assert_equal( sorted(component_ids),
                          sorted([ c.id for c in t.components ]),
                          'Mismatch in ticket components while configuring the ticket' )
        if milestone_ids :
            assert_equal( sorted(milestone_ids),
                          sorted([ m.id for m in t.milestones ]),
                          'Mismatch in ticket milestones while configuring the ticket' )
        if version_ids :
            assert_equal( sorted(version_ids),
                          sorted([ v.id for v in t.versions ]),
                          'Mismatch in ticket versions while configuring the ticket' )
        if bi_ids and blocking_ids.strip( ', ' ) :
            assert_equal( sorted(bi_ids),
                          sorted([ tck.id for tck in t.blocking ]),
                          'Mismatch in blocking tickets while configuring the ticket' )
        if be_ids and blockedby_ids.strip( ', ' ) :
            assert_equal( sorted(be_ids),
                          sorted([ tck.id for tck in t.blockedby ]),
                          'Mismatch in blockedby tickets while configuring the ticket' )

        # With append as True
        request.POST.clearfields()
        component_ids    = component_ids + \
                           [ components[i].id for i in range(randint(0,len(components))) ]
        milestone_ids    = milestone_ids + \
                           [ milestones[i].id for i in range(randint(0,len(milestones))) ]
        version_ids      = version_ids + \
                           [ versions[i].id for i in range(randint(0,len(versions))) ]
        bi_ids           = bi_ids
        be_ids           = be_ids
        if block == 'bi' :
            bi_ids = bi_ids + [ tickets[i].id for i in range(randint(0,len(tickets)))
                                if tickets[i].id != t.id ]
        if block == 'be' :
            be_ids = be_ids + [ tickets[i].id for i in range(randint(0,len(tickets)))
                                if tickets[i].id != t.id ]
        blocking_ids     = choice(
                            [ ', '.join([ str(id) for id in bi_ids ]),
                              ', ,, ,',
                              ''
                            ]
                           )
        blockedby_ids    = choice(
                            [ ', '.join([ str(id) for id in  be_ids ]),
                              ', ,, ,',
                              ''
                            ]
                           )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        component_ids and [ request.POST.add( 'component_id', str(id) ) for id in component_ids ]
        milestone_ids and [ request.POST.add( 'milestone_id', str(id) ) for id in milestone_ids ]
        version_ids and [ request.POST.add( 'version_id', str(id) ) for id in version_ids ]
        if block == 'bi' :
            request.POST.add( 'blocking_ids', blocking_ids )
        elif block == 'be' :
            request.POST.add( 'blockedby_ids', blockedby_ids )
        vf.process( request, c, append=True, formnames=['configtck'] )
        if component_ids :
            assert_equal( sorted(list(set(component_ids))),
                          sorted([ c.id for c in t.components ]),
                          'Mismatch in ticket components while configuring the ticket' )
        if milestone_ids :
            assert_equal( sorted(list(set(milestone_ids))),
                          sorted([ m.id for m in t.milestones ]),
                          'Mismatch in ticket milestones while configuring the ticket' )
        if version_ids :
            assert_equal( sorted(list(set(version_ids))),
                          sorted([ v.id for v in t.versions ]),
                          'Mismatch in ticket versions while configuring the ticket' )
        if bi_ids and blocking_ids.strip( ', ' ) :
            assert_equal( sorted(list(set(bi_ids))),
                          sorted([ tck.id for tck in t.blocking ]),
                          'Mismatch in blocking tickets while configuring the ticket' )
        if be_ids and blockedby_ids.strip( ', ' ) :
            assert_equal( sorted(list(set(be_ids))),
                          sorted([ tck.id for tck in t.blockedby ]),
                          'Mismatch in blockedby tickets while configuring the ticket' )

        # With append as False
        request.POST.clearfields()
        component_ids    = [ components[i].id for i in range(randint(0,len(components))) ]
        milestone_ids    = [ milestones[i].id for i in range(randint(0,len(milestones))) ]
        version_ids      = [ versions[i].id for i in range(randint(0,len(versions))) ]
        bi_ids           = []
        be_ids           = []
        if block == 'bi' :
            bi_ids = [ tickets[i].id for i in range(randint(0,len(tickets)))
                       if tickets[i].id != t.id ]
        if block == 'be' :
            be_ids = [ tickets[i].id for i in range(randint(0,len(tickets)))
                       if tickets[i].id != t.id ]
        blocking_ids     = choice(
                            [ ', '.join([ str(id) for id in bi_ids ]),
                              ', ,, ,',
                              ''
                            ]
                           )
        blockedby_ids    = choice(
                            [ ', '.join([ str(id) for id in  be_ids ]),
                              ', ,, ,',
                              ''
                            ]
                           )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        component_ids and [ request.POST.add( 'component_id', str(id) ) for id in component_ids ]
        milestone_ids and [ request.POST.add( 'milestone_id', str(id) ) for id in milestone_ids ]
        version_ids and [ request.POST.add( 'version_id', str(id) ) for id in version_ids ]
        if block == 'bi' :
            request.POST.add( 'blocking_ids', blocking_ids )
        elif block == 'be' :
            request.POST.add( 'blockedby_ids', blockedby_ids )
        vf.process( request, c, append=False, formnames=['configtck'] )
        if component_ids :
            assert_equal( sorted(component_ids),
                          sorted([ c.id for c in t.components ]),
                          'Mismatch in ticket components while configuring the ticket' )
        if milestone_ids :
            assert_equal( sorted(milestone_ids),
                          sorted([ m.id for m in t.milestones ]),
                          'Mismatch in ticket milestones while configuring the ticket' )
        if version_ids :
            assert_equal( sorted(version_ids),
                          sorted([ v.id for v in t.versions ]),
                          'Mismatch in ticket versions while configuring the ticket' )
        if bi_ids and blocking_ids.strip( ', ' )  :
            assert_equal( sorted(bi_ids),
                          sorted([ tck.id for tck in t.blocking ]),
                          'Mismatch in blocking tickets while configuring the ticket' )
        if be_ids and blockedby_ids.strip( ', ' ) :
            assert_equal( sorted(be_ids),
                          sorted([ tck.id for tck in t.blockedby ]),
                          'Mismatch in blockedby tickets while configuring the ticket' )

        # Update summary and description using config
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configtck' )
        u            = choice( users )
        p            = choice( projects )
        t            = choice( tickets )
        summary      = u'updated ticket summary via config form'
        description  = u'updated ticket description via config form'
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'summary', summary )
        request.POST.add( 'description', description )
        vf.process( request, c, formnames=['configtck'] )
        t = tckcomp.get_ticket( t.id )
        assert_equal( t.summary, summary,
                      'Mismatch while updating ticket summary via config form' )
        assert_equal( t.description, description,
                      'Mismatch while updating ticket description via config form' )

    def test_4_createticketstatus_valid( self ) :
        """Testing FormCreateTicketStatus with valid input"""
        log.info( "Testing FormCreateTicketStatus with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createtstat' )

        c.rclose = h.ZResp()
        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        statuss  = [ ts for ts in tckcomp.get_tckstatus()
                        if ts.tck_statusname != 'new' ]

        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )
        status   = choice( statuss )
        due_date = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date = due_date.isoformat().split('T')[0]
        owner    = choice( users )

        # Create ticket status
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'tck_statusname', status.tck_statusname )
        request.POST.add( 'due_date', due_date )
        request.POST.add( 'owner', str(owner.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createtstat'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Moved ticket to status' in u.logs[-1].log 
        )

        t = tckcomp.get_ticket( t.id )
        ts = t.statushistory[-1]

        # Convert the due_date to UTC before comparing.
        due_date = h.usertz_2_utc(
                        dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                        timezone( u.timezone )
                   )
        assert_equal( [ status.tck_statusname, due_date, owner.username ],
                      [ ts.status.tck_statusname, ts.due_date,
                        ts.owner.username ],
                      'Mismatch in creating ticket status'
                    )

        # Update ticket status
        c.rclose = h.ZResp()
        request.POST.clearfields()
        status   = choice( statuss )
        due_date = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date = due_date.isoformat().split('T')[0]
        owner    = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'ticket_status_id', str(ts.id) )
        request.POST.add( 'tck_statusname', status.tck_statusname )
        request.POST.add( 'due_date', due_date )
        request.POST.add( 'owner', str(owner.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createtstat'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Updated ticket status' in u.logs[-1].log 
        )

        ts      = tckcomp.get_ticket_status( ts.id )
        t       = tckcomp.get_ticket( t.id )

        # Convert the due_date to UTC before comparing.
        due_date = h.usertz_2_utc(
                        dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                        timezone( u.timezone )
                   )
        assert_equal( len(t.statushistory), 2,
                      'Created new ticket status while updating an existing status' )
        assert_equal( [ status.tck_statusname, due_date, owner.username ],
                      [ ts.status.tck_statusname, ts.due_date, ts.owner.username ],
                      'Mismatch in updating ticket status'
                    )

    def test_5_createticketstatus_invalid( self ) :
        """Testing FormCreateTicketStatus with invalid input"""
        log.info( "Testing FormCreateTicketStatus with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createtstat' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        statuss  = tckcomp.get_tckstatus()

        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )

        # Try creating ticket status with insufficient data.
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )

        status   = choice( statuss )
        request.POST.add( 'tck_statusname', status.tck_statusname )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtstat']
                     )
        due_date = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date = due_date.isoformat().split('T')[0]
        request.POST.add( 'due_date', due_date )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtstat']
                     )

    def test_6_ticketstatusconfig( self ) :
        """Testing FormTicketStatusConfig with valid and invalid input"""
        log.info( "Testing FormTicketStatusConfig with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configtstat' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        statuss  = tckcomp.get_tckstatus()

        # configure / update existing ticket status
        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )
        ts       = t.statushistory[-1]
        status   = choice( statuss + [ None ] * 5 )
        due_date = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date = choice([ due_date.isoformat().split('T')[0], '' ])
        owner    = choice( users + [ None ] * 5 )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'ticket_status_id', str(ts.id) )
        status and request.POST.add( 'tck_statusname', status.tck_statusname )
        due_date and request.POST.add( 'due_date', due_date )
        owner and request.POST.add( 'owner', str(owner.id) )
        vf.process( request, c, formnames=['configtstat'] )
        t       = tckcomp.get_ticket( t.id )
        ts      = t.statushistory[-1]
        if status :
            assert_equal( status.tck_statusname, ts.status.tck_statusname,
                          'Mismatch while configuring tck_statusname' )
        if due_date :
            # Convert the due_date to UTC before comparing.
            due_date = h.usertz_2_utc(
                            dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                            timezone( u.timezone )
                       )
            assert_equal( due_date, ts.due_date,
                          'Mismatch while configuring due_date' )
        if owner :
            assert_equal( owner.username, ts.owner.username,
                          'Mismatch while configuring ticket status owner' )
        
    def test_7_createticketcomment_valid( self ) :
        """Testing FormCreateTicketComment with valid input"""
        log.info( "Testing FormCreateTicketComment with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'replytcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )

        # Create ticket comment
        c.rclose = h.ZResp()
        text = u'some ticket comment'
        commentby = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createtcmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'comment as,' in u.logs[-1].log 
        )

        t        = tckcomp.get_ticket( t.id )
        tc       = t.comments[-1]
        assert_equal( [ text, commentby.username ],
                      [ tc.text, tc.commentby.username ],
                      'Mismatch in creating ticket comment'
                    )

        # Update ticket comment
        c.rclose = h.ZResp()
        request.POST.clearfields()
        text      = u'updated ticket comment'
        commentby = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'ticket_comment_id', str(tc.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createtcmt'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated comment,' in u.logs[-1].log 
        )

        t        = tckcomp.get_ticket( t.id )
        tc       = t.comments[-1]
        assert_equal( len( t.comments ), 1,
                      'Created a new ticket comment while updating an existing one'
                    )
        assert_equal( [ text, commentby.username ],
                      [ tc.text, tc.commentby.username ],
                      'Mismatch in updating ticket comment'
                    )

    def test_8_createticketcomment_invalid( self ) :
        """Testing FormCreateTicketComment with invalid input"""
        log.info( "Testing FormCreateTicketComment with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createtcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )
        # Create ticket comment
        commentby = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        text      = u'some ticket comment'
        request.POST.add( 'text', text )
        assert_raises( ZetaFormError,
                       vf.process,
                       request,
                       c, formnames=['createtcmt']
                     )

    def test_9_ticketcommentreplies( self ) :
        """Testing ticket comment replies with valid and invalid input"""
        log.info( "Testing ticket comment replies with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createtcmt' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )
        tc       = t.comments[-1]
        # Create ticket comment
        text      = u'second ticket comment'
        commentby = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'text', text )
        request.POST.add( 'commentby', commentby.username )
        request.POST.add( 'replytocomment_id', str(tc.id) )
        vf.process( request, c, formnames=['createtcmt'] )
        tc        = tckcomp.get_ticket_comment( tc.id )
        assert_equal( len( tc.replies ), 1,
                      'Mismatch in no of replies'
                    )
        assert_equal( tc.replies[0].text, text,
                      'Mismatch in reply comment text'
                    )

    def test_A_tickettags( self ) :
        """Testing FormTicketTags with valid and invalid input"""
        log.info( "Testing FormTicketTags with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )

        # Add tags to ticket.
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addtcktags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda tag : tagcomp.is_tagnamevalid(tag), 
                                tagnames ) + \
                        [ tag.tagname for tag in t.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addtcktags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added tags, ' in u.logs[-1].log 
        )

        t = tckcomp.get_ticket( t.id )
        assert_equal( sorted(reftags),
                      sorted([ tag.tagname for tag in t.tags ]),
                      'Mismatch while creating tags'
                    )

        # Delete tags to ticket.
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deltcktags' )
        rmtag     = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'tags', rmtag )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['deltcktags'] )
        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted tags,' in u.logs[-1].log 
        )

        t = tckcomp.get_ticket( t.id )
        assert_equal( sorted(reftags),
                      sorted([ tag.tagname for tag in t.tags ]),
                      'Mismatch while deleting tags'
                    )

    def test_B_ticketattachs( self ) :
        """Testing FormTicketAttachs with valid and invalid input"""
        log.info( "Testing FormTicketAttachs with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        u        = choice( users )
        p        = choice( projects )
        t        = tckcomp.get_ticket( sorted([ t.id for t in tickets ])[-1] )

        # Clean attachments in ticket
        [ tckcomp.remove_attach( t, attach ) for attach in t.attachments ]

        # Add attachments
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addtckattachs' )
        user    = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'ticket_id', str(t.id) )
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
                    formnames=['addtckattachs'] )

        if attachmentfiles :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'uploaded attachment,' in u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        t = tckcomp.get_ticket( t.id )
        assert_equal( sorted([ a.filename for a in t.attachments ]),
                      sorted([ attach.filename for attach in attachmentfiles ]),
                      'Mismatch in adding ticket attachment'
                    )

        # Remove attachments
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deltckattachs' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        [ request.POST.add( 'attach_id', str(a.id) ) for a in t.attachments ]
        defer = choice([True, False])
        vf.process( request, c, removeattach=True, defer=defer,
                    formnames=['deltckattachs'] )

        if t.attachments :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted attachment,' in u.logs[-1].log 
            )
        elif defer :
            c.rclose.close()

        t = tckcomp.get_ticket( t.id )
        assert_false( t.attachments,
                      'Mismatch in removing ticket attachment' )

    def test_C_ticketfavorite( self ) :
        """Testing FormTicketFavorite with valid and invalid inputs"""
        log.info( "Testing FormTicketFavorite with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        user     = choice( users )
        p        = choice( projects )
        t        = choice( tickets )

        tckcomp.delfavorites( t, t.favoriteof, byuser=g_byuser )

        # Add favorite user
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'tckfav' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'addfavuser', user.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['tckfav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added ticket as favorite' in u.logs[-1].log 
        )

        assert_equal( tckcomp.get_ticket( t.id ).favoriteof, [ user ],
                      'Mismatch in adding favorite user for ticket'
                    )

        # Del favorite user
        c.rclose = h.ZResp()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'delfavuser', user.username )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['tckfav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'removed ticket from favorite' in u.logs[-1].log 
        )

        assert_equal( tckcomp.get_ticket( t.id ).favoriteof, [],
                      'Mismatch in deleting favorite user for ticket'
                    )

    def test_D_ticketvoting( self ) :
        """Testing FormTicketVote with valid and invalid inputs"""
        log.info( "Testing FormTicketVote with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        tickets  = tckcomp.get_ticket()
        user     = choice( users )
        p        = choice( projects )
        t        = choice( tickets )

        [ votcomp.remove_vote( v ) for v in t.votes ]

        # Vote up for ticket
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'votetck' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'votedas', u'up' )
        vf.process( request, c, defer=False, formnames=['votetck'] )
        
        self._validate_defer(
                user.id, False, c,
                lambda u : 'casted vote' in u.logs[-1].log 
        )

        t       = tckcomp.get_ticket( t.id )
        votes   = t.votes
        countup = votcomp.ticketvotes( t, votedas=u'up' )
        assert_equal( [ len(votes), len(countup), countup[0].voter ],
                      [ 1, 1, user ],
                      'Mismatch in number of votes for ticket' )

        # vote down for ticket
        c.rclose = h.ZResp()
        users.remove( user )
        user = choice( users )
        request.POST.clearfields()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ticket_id', str(t.id) )
        request.POST.add( 'votedas', u'down' )
        vf.process( request, c, defer=False, formnames=['votetck'] )

        self._validate_defer(
                user.id, False, c,
                lambda u : 'casted vote' in u.logs[-1].log 
        )

        t       = tckcomp.get_ticket( t.id )
        votes   = t.votes
        countdown = votcomp.ticketvotes( t, votedas=u'down' )
        assert_equal( [ len(votes), len(countdown), countdown[0].voter ],
                      [ 2, 1, user ],
                      'Mismatch in number of votes against ticket'
                    )

    @attr(type='filters')
    def test_E_ticketfilter( self ) :
        """Testing FormTicketFilter with valid and invalid inputs"""
        log.info( "Testing FormTicketFilter with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        user     = choice( users )
        fjson1   = u'{ "tck_typename" : "defect" }'

        # Add ticket filter
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addtckfilter' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'name', u'filter1' )
        request.POST.add( 'filterbyjson', fjson1 )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['addtckfilter'] )

        self._validate_defer(
                user.id, defer, c,
                lambda u : u.logs and 'ticket filter created' in u.logs[-1].log
        )

        tf = tckcomp.get_ticketfilter( 1 )
        assert_equal( [ tf.name, tf.filterbyjson, tf.foruser.username ],
                      [ 'filter1', fjson1, user.username ],
                      'Mismatch in addtckfilter' )

        # Delete ticket filter
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deltckfilter' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'tf_id', str(tf.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['deltckfilter'] )

        self._validate_defer(
                user.id, defer, c,
                lambda u : 'deleted ticket filter' in u.logs[-1].log 
        )

        tf      = tckcomp.get_ticketfilter()
        assert_false( tf, 'Mismatch in deltckfilter' )
