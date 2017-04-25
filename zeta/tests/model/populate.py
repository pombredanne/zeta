# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

from   __future__                import with_statement
from   random                    import randint, choice
import os
import datetime                  as dt
import time

from   pylons                    import config
from   pytz                      import all_timezones, timezone

from   zeta.model                import meta
from   zeta.model.create         import create_models, delete_models
from   zeta.model.tables         import *
from   zeta.lib.constants        import *
from   zeta.lib.helpers          import *
import zeta.lib.helpers          as h
from   zeta.lib.base             import BaseController
from   zeta.config.routing       import *
from   zwiki.test.testlib        import random_wiki
from   zeta.comp                 import *
from   zeta.tests.model.generate import *

g_byuser       = u'admin'
_resource_u    = [ 'wiki', 'p', 'u', 'ticket', 'source' ]
sampledata_dir = os.path.join( os.path.split(__file__)[0], 'sampledata' )
dirstosearch   = [ '/bin', '/usr/share/icons/kdeclassic/',
                   '/usr/share/man/man1', '/usr/share/doc' ]
cntlr = BaseController()

#------------------------- Populate Permission Tables ------------------------
def pop_permname() :
    """Create permission name without a corresponding permission group map."""
    msession = meta.Session()

def pop_permgroup( **kwargs ) :
    """Seed the database with permission group entries and its association
    table entries"""
    # Dirty heuristics,
    userscomp = h.fromconfig( 'userscomp' )

    pgdata    = gen_pgroups( **kwargs )
    for perm_group in pgdata :
        userscomp.create_permgroup( perm_group, byuser=g_byuser )
        userscomp.add_permnames_togroup( perm_group, pgdata[perm_group],
                                         byuser=g_byuser )

def pop_permissions( **kwargs ) :
    pop_permname()
    pop_permgroup( **kwargs )

#------------------------- Populate Permission Tables ------------------------
def pop_user( no_of_users=None, no_of_relations=None, seed=None ) :
    """Seed the database with user entries and its association table entries"""
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    attachcomp      = AttachComponent( compmgr )
    no_of_users     = no_of_users or randint( 50, 200 )
    no_of_relations = no_of_relations or randint( 0, 30 )
    
    pgdict   = dict([ (pg.perm_group, pg) for pg in userscomp.get_permgroup() ])
    userdata = gen_usercontent( no_of_users=no_of_users, seed=seed )
    for username in userdata :
        d         = userdata[username]
        photofile = d['photofile']
        iconfile  = d['iconfile']
        u     = [ username.lower(), d['emailid'], d['password'], d['timezone'] ]
        uinfo = [ d['firstname'], d['middlename'], d['lastname'],
                  d['addressline1'], d['addressline2'], d['city'], d['pincode'],
                  d['state'], d['country'], d['userpanes'] ]
        uobj    = userscomp.user_create( u, uinfo )
        d['id'] = uobj

        userscomp.get_user(
            uobj, 
            attrload=[ 'photofile', 'iconfile', 'permgroups' ]
        )

        if photofile :
            photo  = attachcomp.create_attach(
                        os.path.basename( photofile ),
                        fdfile=open( photofile, 'r' ),
                        uploader=uobj,
                     )
            userscomp.user_set_photo( uobj, photo )
        if iconfile :
            icon   = attachcomp.create_attach(
                        os.path.basename( iconfile ),
                        fdfile=open( iconfile, 'r' ),
                        uploader=uobj
                     )
            userscomp.user_set_icon( uobj, icon )
        d['disabled'] and userscomp.user_disable( uobj, byuser=uobj )
        userscomp.user_add_permgroup( uobj, d['perm_groups'], byuser=uobj )

    # User relations
    userreldata = gen_userrelations( userscomp.usernames, userscomp.reltypes,
                                     no_of_relations, seed=seed )
    cacheuser = dict([ ( u.username, u ) for u in userscomp.get_user() ])
    cachertype= dict([ ( r.userrel_type, r ) for r in userscomp.get_userrel_type() ])
    for username in userreldata :
        user = cacheuser[username]
        for d in userreldata[username] :
            userto = cacheuser[d['userto']]
            urel   = cachertype[d['userrel_type']]
            ur     = userscomp.user_add_relation(user, userto, urel, byuser=user)
            d['id'] = ur
            d['approved'] and \
                userscomp.user_approve_relation( ur, byuser=ur.userto )

#------------------------- Populate Generic Tables ---------------------------
def pop_licenses( no_of_tags=None, no_of_attachs=None, seed=None ) :
    """Seed the database with license entries and its association table 
    entries"""
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    no_of_tags    = no_of_tags or randint(3,6)
    no_of_attachs = no_of_attachs or randint(3,5)
    lictextdir    = os.path.join( sampledata_dir, 'licensetext' )
    # Instanstiate components
    attachcomp = AttachComponent( compmgr )
    liccomp    = LicenseComponent( compmgr )

    # Collect expected objects from database.
    usrdict  = dict([ (u.username, u) for u in userscomp.get_user() ])
    licdata  = gen_licenses( no_of_tags, no_of_attachs, seed=seed )
    for lic in licdata :
        d = licdata[lic]
        licdetail = ( d['id'], d['licensename'],  d['summary'], d['text'],
                      d['source'] )
        l         = liccomp.create_license( licdetail, byuser=g_byuser )
        d['id'] = l
        for u in d['tags'] :
            liccomp.add_tags( l, d['tags'][u], byuser=usrdict[u] )
        for u in d['attachs'] :
            for f in d['attachs'][u] :
                attach = attachcomp.create_attach(
                                        os.path.basename(f), 
                                        choice([ open(f,'r'), None  ]),
                                        uploader=u,
                                        summary='',
                         )
                liccomp.add_attach( l, attach, byuser=u )


#------------------------- Populate Project Tables ---------------------------
def pop_projects( no_of_projects=None, no_of_tags=None, no_of_attachs=None,
                  seed=None ) :
    """Seed the database with project entries and its association table 
    entries"""
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    no_of_projects= no_of_projects or 10                    # Fixed number of projects.
    no_of_tags    = no_of_tags or randint(3,6)
    no_of_attachs = no_of_attachs or randint(3,5)
    # Instantiate the components.
    syscomp     = SystemComponent( compmgr )
    prjcomp     = ProjectComponent( compmgr )
    wikicomp    = WikiComponent( compmgr )
    attachcomp  = AttachComponent( compmgr )
    liccomp     = LicenseComponent( compmgr )
    # Collect the expected database objects.
    perm_groups = userscomp.perm_groups
    usernames   = userscomp.usernames
    teamtypes   = prjcomp.teams
    licenses    = liccomp.get_license()

    projdata = gen_projects( usernames, perm_groups, teamtypes, licenses,
                             no_of_projects, no_of_tags, no_of_attachs,
                             seed=seed )
    ttdict   = dict([ (tt.team_type, tt) for tt in prjcomp.get_teamtype() ])
    usrdict  = dict([ (u.username, u) for u in userscomp.get_user() ])
    byuser   = userscomp.get_user( g_byuser )

    for projectname in projdata :
        st = time.time()
        d       = projdata[projectname]
        admin   = d['admin']
        prjdet  = ( d['id'], d['projectname'], d['summary'], d['admin_email'],
                    d['license'], d['admin'] )
        prjidet = ( d['description'], )
        p = prjcomp.create_project( prjdet, prjidet, byuser=admin )
        p = prjcomp.get_project( p, attrload=[ 'admin', 'license' ] )

        mlists  = [ MailingList( unicode(m) ) for m in d['mailing_list'] ]
        ircch   = [ IRCChannel( unicode(irc) ) for irc in d['ircchannel'] ]
        prjcomp.config_project( p, disable=d['disabled'], byuser=p.admin )
        prjcomp.config_project( p, expose=d['exposed'], byuser=p.admin )
        prjcomp.set_mailinglists( p, mlists, byuser=p.admin )
        prjcomp.set_ircchannels( p, ircch, byuser=p.admin )
        # Add users under project teams
        projectteams = d['projectteams']
        [ prjcomp.add_project_user( p, team_type, u, byuser=p.admin )
          for team_type in projectteams for u in projectteams[team_type] ]
        pteams   = prjcomp.get_projectteam( project=p )
        [ prjcomp.approve_project_user( projectteam=pt ) for pt in pteams ]
        projusers = [ p.admin ] + [ pt.user for pt in p.team ]

        # Components
        for componentname in d['components'] :
            dcomp      = d['components'][componentname]
            compdetail = ( dcomp['id'], dcomp['componentname'],
                           dcomp['description'], dcomp['owner'] )
            c = prjcomp.create_component( p, compdetail, byuser=p.admin )
            for u in dcomp['tags'] :
                prjcomp.add_tags( p, 'component', c, dcomp['tags'][u],
                                  byuser=usrdict[u] )

        # milestones
        for mstnname in d['milestones'] :
            dmstn   = d['milestones'][mstnname]
            mstndet = ( dmstn['id'], dmstn['milestone_name'],
                        dmstn['description'], dmstn['due_date'] )
            m       = prjcomp.create_milestone( p, mstndet, byuser=p.admin )
            status  = dmstn['status']
            if status :
                prjcomp.close_milestone( m, dmstn['closing_remark'],
                                         dmstn['status'], byuser=p.admin )
            for u in dmstn['tags'] :
                prjcomp.add_tags( p, 'milestone', m, dmstn['tags'][u],
                                  byuser=usrdict[u] )

        # versions 
        for vername in d['versions'] :
            dver   = d['versions'][vername]
            verdet = ( dver['id'], dver['version_name'], dver['description'] )
            v = prjcomp.create_version( p, verdet, byuser=p.admin )
            for u in dver['tags'] :
                prjcomp.add_tags( p, 'version', v, dver['tags'][u],
                                  byuser=usrdict[u] )

        # Tags
        for u in d['tags'] :
            prjcomp.add_tags( p, tags=d['tags'][u], byuser=usrdict[u] )

        # Attachments
        for u in d['attachs'] :
            for f in d['attachs'][u] :
                attach = attachcomp.create_attach(
                                        os.path.basename(f), 
                                        choice([ open(f,'r'), None  ]),
                                        uploader=u,
                                        summary='',
                         )
                prjcomp.add_attach( p, attach, byuser=u )

        # Populate Project team permissions
        [ prjcomp.add_projectteam_perm(
                p, ttdict[team_type], pg, byuser=p.admin
          ) for team_type in d['teamperms'] for pg in d['teamperms'][team_type] ]

        # Populate Project level - user permissions
        [ prjcomp.add_project_permission(
                p, usrdict[username], pg, byuser=p.admin
          ) for username in d['projectperms'] for pg in d['projectperms'][username] ]

        # Add project logos and icons.
        logofile, logouploader = d['logofile']
        iconfile, iconuploader = d['iconfile']
        if os.path.exists( logofile ) :
            logo  = attachcomp.create_attach(
                        os.path.basename( logofile ),
                        fdfile=open( logofile, 'r' ),
                        uploader=logouploader
                     )
            prjcomp.config_project( p, logo=logo, byuser=logouploader )
        if os.path.exists( iconfile ) :
            icon   = attachcomp.create_attach(
                        os.path.basename( iconfile ),
                        fdfile=open( iconfile, 'r' ),
                        uploader=iconuploader
                     )
            prjcomp.config_project( p, icon=icon, byuser=iconuploader )

        # Add favorite users
        [ prjcomp.addfavorites( p, usrdict[u], byuser=p.admin ) 
          for u in d['favusers'] ]

        # On successfull project creation, create the default 'homepage',
        # create the `homepage` only after populating data for rest of the
        # project.
        def_wikitype = h.fromconfig( 'zeta.def_wikitype' )
        w = wikicomp.create_wiki(
                unicode( cntlr.url_wikiurl( p.projectname, PROJHOMEPAGE )),
                wtype=unicode(def_wikitype),
                creator=byuser
            )
        wikicomp.config_wiki( w, project=p )
        wikicomp.create_content(
            w.id, p.admin, syscomp.get_staticwiki( u'p_homepage' ).text
        )

        print time.time() - st


#------------------------- Populate Ticket Tables ---------------------------
def pop_tickets( no_of_tickets=None, no_of_tags=None, no_of_attachs=None,
                 seed=None ) :
    """Seed the database with ticket entries and its association table 
    entries"""
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    no_of_tickets = no_of_tickets or randint( 1, 1000 )
    no_of_tags    = no_of_tags or randint(3,6)
    no_of_attachs = no_of_attachs or randint(3,5)
    # Instanstiate components.
    attachcomp= AttachComponent( compmgr )
    liccomp   = LicenseComponent( compmgr )
    tagcomp   = TagComponent( compmgr )
    prjcomp   = ProjectComponent( compmgr )
    tckcomp   = TicketComponent( compmgr )

    tickets   = gen_tickets( no_of_tickets, no_of_tags, no_of_attachs, 
                             seed=seed )

    prjdict   = {}
    pudict    = {}
    projects  = prjcomp.get_project(
                        attrload=[ 'admin' ],
                        attrload_all=[ 'team.user' ]
                )
    for p in projects :
        prjdict.setdefault( p.projectname, p )
        pudict.setdefault( p.projectname,
                           list(set([ pt.user for pt in p.team ]))
                         )
    usrdict  = dict([ (u.username, u) for u in userscomp.get_user() ])

    for x in range(len(tickets)) :
        st = time.time()
        d = tickets.pop(0)    # Save memory.
        p = d['project']
        p = prjdict[p.projectname]
        tckusers= [ p.admin ] + pudict[p.projectname]
        tckdet  = ( d['id'], d['summary'], d['description'], d['tck_typename'],
                    d['tck_severityname'] )
        owner   = choice( tckusers )
        t       = tckcomp.create_ticket( p, tckdet, d['promptuser'], owner,
                                         byuser=owner )
        t.id in d['blockedby'] and d['blockedby'].remove( t.id )
        t.id in d['blocking'] and d['blocking'].remove( t.id )
        if t.id == d['parent'] :
            d['parent'] = None
        tckcomp.config_ticket( t, components=d['components'],
                                  milestones=d['milestones'],
                                  versions=d['versions'],
                                  blockedby=d['blockedby'],
                                  blocking=d['blocking'],
                                  parent=d['parent'],
                                  byuser=choice( tckusers )
                             )
        # Add entries for ticket_status_history
        for dst in d['statushistory'] :
            tsdet = ( dst['id'], dst['tck_statusname'], dst['due_date'] )
            ts    = tckcomp.create_ticket_status(
                                t, tsdet,
                                dst['owner'],
                                byuser=choice( tckusers )
                    )
            promptuser = dst['promptuser']
            promptuser and tckcomp.config_ticket( t, promptuser=promptuser,
                                                  byuser=choice( tckusers ))
        # Add ticket Comments
        for dcmt in d['comments'] :
            tcmtdet = ( dcmt['id'], dcmt['text'], dcmt['commentby'] )
            tcmt    = tckcomp.create_ticket_comment( t, tcmtdet,
                                                     byuser=choice( tckusers ))
            dcmt['id'] = tcmt
        # Ticket comment replies, `id` starts from 1
        replies  = d['replies']
        comments = d['comments']
        for i in range( 0, len(replies) ) :
            replyto = replies[i] 
            replyto != -1 and tckcomp.comment_reply(
                                    comments[i]['id'], comments[replyto]['id'] )
        # Tags
        for u in d['tags'] :
            tckcomp.add_tags( t, d['tags'][u], byuser=usrdict[u] )
        # Attachments
        for u in d['attachs'] :
            for f in d['attachs'][u] :
                attach = attachcomp.create_attach(
                                        os.path.basename(f), 
                                        choice([ open(f,'r'), None  ]),
                                        uploader=u,
                                        summary='',
                         )
                tckcomp.add_attach( t, attach, byuser=u )
        # Add favorite users
        [ tckcomp.addfavorites( t, usrdict[u], byuser=u )
          for u in d['favusers'] ]
        # Vote tickets
        [ tckcomp.voteup( t, u ) for u in d['voteup'] ]
        [ tckcomp.votedown( t, u ) for u in d['votedown'] ]
        print time.time() - st

#------------------------- Populate Review Tables ---------------------------
def pop_reviews( no_of_reviews=None, no_of_tags=None, no_of_attachs=None,
                 seed=None ) :
    """Seed the database with review entries and its association table 
    entries"""
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    no_of_reviews = no_of_reviews or randint( 0, 20 )
    no_of_tags    = no_of_tags or randint(3,6)
    no_of_attachs = no_of_attachs or randint(3,5)
    tagcomp   = TagComponent( compmgr )
    attachcomp= AttachComponent( compmgr )
    prjcomp   = ProjectComponent( compmgr )
    revcomp   = ReviewComponent( compmgr )

    users     = userscomp.get_user()
    projects  = prjcomp.get_project()
    rnatures  = revcomp.get_reviewcomment_nature()
    ractions  = revcomp.get_reviewcomment_action()

    reviews   = gen_reviews( rnatures, ractions, no_of_reviews, no_of_tags,
                             no_of_attachs, seed=seed )

    usrdict  = dict([ (u.username, u) for u in userscomp.get_user() ])

    for d in reviews :
        st = time.time()
        revdet  = ( d['id'], d['resource_url'], d['version'], d['author'],
                    d['moderator'] )
        r       = revcomp.create_review( d['project'], revdet, 
                                         byuser=choice( users ))
        revcomp.set_participants( r, d['participants'], byuser=choice(users) )
        # Review set
        if d['reviewset' ] :
            rset = revcomp.get_reviewset( d['reviewset'] )
            rset = rset or revcomp.create_reviewset( d['project'],
                                                     d['reviewset'],
                                                     byuser=choice(users) )
            revcomp.add_reviewtoset( rset, r, byuser=choice(users) )
        # Review comments
        for dcmt in d['comments'] :
            rcmtdet = ( dcmt['id'], dcmt['position'], dcmt['text'],
                        dcmt['commentby'], dcmt['reviewnature'], None )
            rcmt    = revcomp.create_reviewcomment( r, rcmtdet, 
                                                    byuser=choice(users) )
            dcmt['id'] = rcmt
            revcomp.process_reviewcomment( rcmt,
                                           reviewaction=dcmt['reviewaction'],
                                           approve=dcmt['approved'],
                                           byuser=choice(users),
                                         )
        # Review comment replies, `id` starts from 1
        comments = d['comments']
        replies  = d['replies']
        for i in range( 0, len(replies) ) :
            replyto = replies[i] 
            replyto != -1 and revcomp.comment_reply( comments[i]['id'],
                                                     comments[replyto]['id'] )
        d['closed'] and revcomp.close_review( r, byuser=choice(users) )
        for dcmt in comments :
            del dcmt['id']
        # Tags
        for u in d['tags'] :
            revcomp.add_tags( r, d['tags'][u], byuser=usrdict[u] )
        # Attachments
        for u in d['attachs'] :
            for f in d['attachs'][u] :
                attach = attachcomp.create_attach(
                                        os.path.basename(f), 
                                        choice([ open(f,'r'), None  ]),
                                        uploader=u,
                                        summary='',
                         )
                revcomp.add_attach( r, attach, byuser=u )
        # Add favorite users
        [ revcomp.addfavorites( r, u, byuser=u ) for u in d['favusers'] ]
        print time.time() - st

#------------------------- Populate Wiki Tables ---------------------------
def pop_vcs( no_of_vcs=None, seed=None ) :
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    prjcomp   = ProjectComponent( compmgr )
    vcscomp   = VcsComponent( compmgr )

    no_of_vcs = no_of_vcs or randint( 0, len(prjcomp.get_project()) * 2 )

    vcsdata   = gen_vcs( no_of_vcs=no_of_vcs, seed=seed )
    for vcs in vcsdata :
        p = prjcomp.get_project( vcs['project'] )
        vcsdetail = ( vcs['type'], vcs['name'], vcs['rooturl'],
                      vcs['loginname'], vcs['password'] )
        vcscomp.integrate_vcs( p, vcsdetail, byuser=p.admin.username )

    mountdata = gen_vcsmounts( no_of_vcs=no_of_vcs, seed=seed )
    for m in mountdata :
        p = prjcomp.get_project( m['project'] )
        v = vcscomp.get_vcs( m['vcs_id'] )
        vcscomp.create_mount( v, m['name'], m['repospath'],
                              byuser=p.admin.username )

#------------------------- Populate Wiki Tables ---------------------------
def pop_wikipages( no_of_tags=None, no_of_attachs=None, seed=None ) :
    """Seed the database with review entries and its association table 
    entries"""
    # Dirty heuristics,
    userscomp   = h.fromconfig( 'userscomp' )
    compmgr     = h.fromconfig( 'compmgr' )

    no_of_tags    = no_of_tags or randint(3,6)
    no_of_attachs = no_of_attachs or randint(3,5)
    attachcomp    = AttachComponent( compmgr )
    tagcomp       = TagComponent( compmgr )
    prjcomp       = ProjectComponent( compmgr )
    wikicomp      = WikiComponent( compmgr )

    permgroups  = userscomp.get_permgroup()
    users       = userscomp.get_user()
    projects    = prjcomp.get_project()
    wikitypes   = wikicomp.get_wikitype()

    usrdict  = dict([ (u.username, u) for u in userscomp.get_user() ])

    wikidata = gen_wiki( no_of_tags, no_of_attachs, seed=seed )
    for d in wikidata :
        st = time.time()
        p         = d['project']
        projusers = [ p.admin ] + [ pt.user for pt in p.team ]
        w         = wikicomp.create_wiki( d['wikiurl'], wtype=d['wiki_typename'],
                                          creator=d['creator'] )
        wikicomp.config_wiki( w,
                              project=p,
                              summary=d['summary'],
                              sourceurl=d['sourceurl'],
                              byuser=choice( projusers )
                            )
        for dcnt in d['contents'] :
            wcnt = wikicomp.create_content( w, dcnt['author'], dcnt['text'],
                                            dcnt['version'] )
        for dcmt in d['comments'] :
            wcmtdetail = ( dcmt['id'], dcmt['commentby'], dcmt['version_id'],
                           dcmt['text'] )
            wcmt = wikicomp.create_wikicomment( w, wcmtdetail,
                                                byuser=dcmt['commentby'] )
            dcmt['id'] = wcmt

        # Wiki comment replies, `id` starts from 1
        comments = d['comments']
        replies  = d['replies']
        for i in range( 0, len(replies) ) :
            replyto = replies[i] 
            replyto != -1 and wikicomp.comment_reply( comments[i]['id'],
                                                      comments[replyto]['id'] )
        for dcmt in comments :
            del dcmt['id']
        # Tags
        for u in d['tags'] :
            wikicomp.add_tags( w, d['tags'][u], byuser=usrdict[u] )
        # Attachments
        for u in d['attachs'] :
            for f in d['attachs'][u] :
                attach = attachcomp.create_attach(
                                        os.path.basename(f), 
                                        choice([ open(f,'r'), None  ]),
                                        uploader=u,
                                        summary='',
                         )
                wikicomp.add_attach( w, attach, byuser=u )
        # Add favorite users
        [ wikicomp.addfavorites( w, u, byuser=u ) for u in d['favusers'] ]
        # Vote wiki
        [ wikicomp.voteup( w, u ) for u in d['voteup'] ]
        [ wikicomp.votedown( w, u ) for u in d['votedown'] ]
        print time.time() - st


def fix_mstn_duedate( seed=None ) :
    """due_date for milestone should be re-computed based on created_on"""
    import zeta.lib.helpers          as h

    # Dirty heuristics,
    compmgr     = h.fromconfig( 'compmgr' )

    prjcomp = ProjectComponent( compmgr )

    for m in prjcomp.get_milestone() :
        if choice([ True, False ]) :
            m.created_on = future_duedate( *m.created_on.timetuple(), **{'maxday':100} )
            m.due_date = future_duedate( *m.created_on.timetuple(), **{'maxday':365} )

def fix_ts_duedate( seed=None ) :
    """due_date for ticket status should be re-computed based on created_on"""
    import zeta.lib.helpers          as h

    # Dirty heuristics,
    compmgr = h.fromconfig( 'compmgr' )
    tckcomp = TicketComponent( compmgr )

    for t in tckcomp.get_ticket() :
        prev_duedate = None
        for ts in t.statushistory :
            if prev_duedate and choice([ True, False ]):
                y, mo, d, h, mi, s, t0, t1, t2 = \
                        future_duedate( *prev_duedate.timetuple(), **{'maxday':10}
                                      ).timetuple()
                ts.created_on = dt.datetime( y, mo, d, h, mi, s, 0 )
            ts.due_date  = future_duedate( *ts.created_on.timetuple(), **{'maxday':30} )
            prev_duedate = ts.due_date
