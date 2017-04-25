# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to interface with client XMLRPC requests"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   1. 'None' object cannot be marshalled via XMLRPC. So, it is marshalled as
#      'None' string.
#   2. `anonymous` users cannot use XMLRPC.
# Todo    : None


from   __future__               import with_statement
import logging
import os
import datetime                 as dt

from   pylons                   import request, response  
from   pylons                   import config
from   pylons                   import session
from   pylons                   import tmpl_context as c
from   pylons.controllers.util  import abort
from   pylons.controllers       import XMLRPCController
from   pytz                     import all_timezones, timezone

from   zeta.ccore               import Component
from   zeta.model               import meta
from   zeta.lib.error           import *
from   zeta.lib.base            import BaseController, render
from   zeta.lib.constants       import *
import zeta.lib.helpers         as h
import zeta.auth.perm           as permmod


log       = logging.getLogger(__name__)

authzfail = { 'rpcstatus' : 'fail', 'message' : 'Not authorized' }
authtfail = { 'rpcstatus' : 'fail', 'message' : 'Not authenticated' }

def _result( rpcstatus, failmsg='', d={} ) :
    if rpcstatus :
        res = { 'rpcstatus' : 'ok' } 
    else :
        res = { 'rpcstatus'  : 'fail', 'message' : failmsg }
    res.update( d )
    return res

class XmlrpcController( XMLRPCController ) :
    """Controller providing XMLRPC interface"""

    def __before__( self, environ=None ) :
        """Called before calling any actions under this controller"""
        from zeta.config.environment    import syscomp, userscomp

        # Collect the query values into 'context'
        c.username   = request.params.get( 'username', None )
        c.password   = request.params.get( 'password', None )

        # setup Environment, since we are not calling standard
        # self.beforecontrollers()
        environ   = request.environ
        c.sysentries = syscomp.get_sysentry()

        # Initialize Permission Mapping System.
        permmod.pms_root = permmod.init_pms( ctxt=c.sysentries )

        # Authenticate user, `anonymous` users cannot use XMLRPC
        user = userscomp.get_user( unicode(c.username) )
        if user and user.password == c.password :
            c.authuser     = user
            c.authusername = user.username
        else :
            c.authuser     = None
            c.authusername = ''

    def _marshalNone( self, val, default='None' ) :
        """`None` python data-type is not supported by XMLRPC, instead, it is
        marshalled as 'None' string"""
        if val == None :
            return default
        elif isinstance( val, list ) :
            newlist = []
            [ newlist.append( [ v, default ][ v == None ] ) for v in val ]
            return newlist
        else :
            return val

    def _demarshalNone( self, *args ) :
        """Interpret 'None' as None"""
        def translate( arg ) :
            if arg == 'None' :
                return None
            elif isinstance( arg, list ) :
                newlist = []
                [ newlist.append( [ l, None ][ l == 'None' ] ) for l in arg ]
                return newlist
            else :
                return arg

        if len(args) == 1 :
            return translate( args[0] )
        elif len(args) > 1 :
            return [ translate( arg ) for arg in args ]

    def _stripurl( self, url ) :
        """`url` to identify wiki pages and static wiki pages will have to be
        striped off `spaces`, `tabs`, and leading '/'"""
        return unicode( url.strip( ' \t' ).lstrip( '/' ))

    def _permissions( self, user, authz ) :
        """Check for successful authentication and authorization"""
        if not user :
            res = authtfail
        elif not authz :
            res = authzfail
        else :
            res = {}
        return res

    def system( self ) :
        """
        === System()
        
        :Description ::
            Get the system table entries,

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus' : 'ok',
                  'entries'   : { key : value, .... }
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, entries, failmsg = xicomp.system() 
            return _result( True, d={ 'entries' : entries } )


    def myprojects( self ) :
        """
        === myprojects()
        :Description ::
            List of participating projects, by the requesting user,

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus'    : 'ok',
                  'projectnames' : [ <projectname>, <projectname>, .... ]
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, projnames, failmsg = xicomp.myprojects( c.authuser )
            return _result( True, d={ 'projectnames' : projnames } )

    def projectdetails( self, projectname ) :
        """
        === projectdetails( projectname )
        
        :Description ::
            Project details like components, milestones, versions, teams for
            project, `projectname`,

        Positional arguments,
        |= projectname | name of the project for which the details are required

        :Return::
            On success,
                [<PRE
                { 'rpcstatus'    : 'ok',
                  'components'   : [ ( <compid>, <compname> ), ... ],
                  'milestones'   : [ ( <mstnid>, <milestonename> ), ... ],
                  'versions'     : [ ( <verid>, <versionname> ), ...   ],
                  'projectusers' : [ username, ... ],
                  
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp
        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, details, failmsg = xicomp.projectdetails( unicode(projectname) )
            return _result( True, d=details )

    def liststaticwikis( self ) :
        """
        === liststaticwikis()

        :Description ::
            List all the static wiki page names,

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus' : 'ok',
                  'paths'     : [ <path-url>, <path-url>, .... ]
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, paths, failmsg = xicomp.list_sw()
            return _result( True, d={ 'paths' : paths } )

    def newstaticwiki( self, path, content, swtype, sourceurl ) :
        """
        === newstaticwiki( path, content )

        :Description ::
            Create a new static wiki page, under path-url `path`, published
            with `content`
        
        Positional arguments,
        |= path      | url-path, for the new static wiki page
        |= content   | wiki text to publish.
        |= wtype     | type of wiki page, if False, will be skipped
        |= sourceurl | source url, if False, will be skipped

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser,
                    h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))
              )
        if res : 
            return res
        else :
            path = self._stripurl( path )
            swtype, sourceurl = self._demarshalNone( swtype, sourceurl )
            rc, sw, failmsg = xicomp.create_sw(
                                    path, unicode(content), swtype=swtype,
                                    sourceurl=sourceurl
                              )
            return _result( rc, failmsg=failmsg )

    def staticwiki( self, path ) :
        """
        === staticwiki( path )

        :Description ::
            Read a static wiki page from url `path`

        Positional arguments,
        |= path     | a valid and existing url-path

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus' : 'ok',
                  'path'      : <path-url>,
                  'text'      : <wiki-text>,
                  'texthtml'  : <html-text>,
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res     = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            path    = self._stripurl( path )
            rc, d, failmsg = xicomp.read_sw( path )
            return _result( rc, d=d, failmsg=failmsg )

    def publishstaticwiki( self, path, content, swtype, sourceurl ) :
        """
        === publishstaticwiki( path, content )

        :Description ::
            Publish new content, (or updated content) onto a static wiki page,

        Positional arguments,
        |= path     | a valid and existing url-path
        |= content  | wiki text to publish

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser,
                    h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))
              )
        if res :
            return res
        else :
            path    = self._stripurl( path )
            swtype, sourceurl = self._demarshalNone( swtype, sourceurl )
            rc, sw, failmsg = xicomp.update_sw(
                                    path, unicode(content), swtype=swtype,
                                    sourceurl=sourceurl
                              )
            return _result( rc, failmsg=failmsg )

    def listwikipages( self, projectname ) :
        """
        === listwikipage( projectname )

        :Description ::
            List wiki pages under project, `projectname`,

        Positional arguments,
        |= projectname | a valid project-name

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus' : 'ok',
                  'wikipages' : [ <page-name>, <page-name>, .... ]
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'WIKI_VIEW' ))
              )
        if res :
            return res
        else :
            rc, wikipages, failmsg = xicomp.list_wiki( unicode(projectname) )
            return _result( True, d={ 'wikipages' : sorted(wikipages) })

    def newwikipage( self, projectname, pagename, wtype, summary, sourceurl ) :
        """
        === newwikipage( projectname, wtype, summary, sourceurl )

        :Description ::
            Create a new wiki-page for project, `projectname`.

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | new wiki page-name under project,
        |= wtype       | type of wiki page, if False, default type will be used
        |= summary     | summary string, if False, will assume empty string
        |= sourceurl   | source url, if False, will assume empty string

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'WIKI_CREATE' ))
              )
        if res :
            return res
        else :
            wtype, summary, sourceurl = \
                    self._demarshalNone( wtype, summary, sourceurl )
            rc, wiki, failmsg = xicomp.create_wiki( unicode(projectname),
                                                    wikiurl,
                                                    wtype=unicode(wtype),
                                                    summary=unicode(summary),
                                                    sourceurl=unicode(sourceurl),
                                                    byuser=c.authuser
                                                  )
            return _result( rc, failmsg=failmsg )

    def wiki( self, projectname, pagename ) :
        """
        === wiki( projectname, pagename )

        :Description ::
            Read wiki-page `pagename`, for project, `projectname`,

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name

        :Return ::
            On success,
                { 'rpcstatus' : 'ok',
                  'type'      : <wiki type string>
                  'summary'   : <wiki summary string>
                  'sourceurl' : <source url to be interpreted based on wiki type>
                  'text'      : <wiki text string>
                }
            On failure,
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                }
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        if res :
            return res
        else :
            res = self._permissions(
                        c.authuser, h.authorized( h.HasPermname( 'WIKI_VIEW' ))
                  )
            rc, d, failmsg = xicomp.read_wiki( unicode(projectname), wikiurl )
            # Marshal None into 'None'
            for k in d :
                d[k] = self._marshalNone( d[k] )
            return _result( rc, d=d, failmsg=failmsg )

    def publishwiki( self, projectname, pagename, content ) :
        """
        === publishwiki( projectname, pagename, content )
        
        :Description ::
            Publish new content, (or updated content) for wiki-page `pagename`,
            under project, `projectname`,

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name
        |= content     | content to be published (as the next version).

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        author  = c.authuser
        res     = self._permissions(
                        c.authuser, h.authorized( h.HasPermname( 'WIKI_CREATE' ))
                  )
        if res :
            return res
        else :
            rc, wiki, failmsg = xicomp.update_wiki( unicode(projectname), wikiurl,
                                                    unicode(content), author )
            return _result( rc, failmsg=failmsg )

    def configwiki( self, projectname, pagename, wtype, summary, sourceurl ) :
        """
        === configwiki( projectname, pagename, wtype, summary, sourceurl )
        
        :Description ::
            Config wiki-page, `pagename` under project, `projectname`,

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name
        |= wtype       | type of wiki page, if False, will be skipped
        |= summary     | summary string, if False, will be skipped
        |= sourceurl   | source url, if False, will be skipped

        On success,
            [<PRE { 'rpcstatus'  : 'ok' } >]
        On failure,
            [<PRE
            { 'rpcstatus' : 'fail',
              'message'   : <msg string indicating reason for failure>
            } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'WIKI_CREATE' ))
              )
        if res :
            return res
        else :
            wtype, summary, sourceurl = \
                    self._demarshalNone( wtype, summary, sourceurl )
            rc, wiki, failmsg = xicomp.config_wiki( unicode(projectname),
                                                    wikiurl, wtype, summary,
                                                    sourceurl )
            return _result( rc, failmsg=failmsg )

    def commentonwiki( self, projectname, pagename, comment ) :
        """
        === commentonwiki( projectname, pagename, comment )

        :Description ::
            Comment on wiki-page, `pagename under project, `projectname`,

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name
        |= comment     | comment as wiki text

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        commentor = c.authuser
        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'WIKICOMMENT_CREATE' ))
              )
        if res :
            return res
        else :
            rc, wcmt, failmsg = xicomp.comment_wiki( unicode(projectname), wikiurl,
                                                     unicode(comment), commentor )
            return _result( rc, failmsg=failmsg )

    def tagwiki( self, projectname, pagename, addtags, deltags ) :
        """
        === tagwiki( projectname, pagename, addtags, deltags )
       
        :Description ::
            Add or delete tags from wiki-page `pagename`, under project
            `projectname`.

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name
        |= addtags     | list of tagnames to add, if False, will be skipped
        |= deltags     | list of tagnames to delete, if False, will be skipped

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'WIKI_CREATE' ))
              )
        if res :
            return res
        else :
            addtags, deltags = self._demarshalNone( addtags, deltags )
            addtags = addtags and [ unicode(t) for t in addtags ]
            deltags = deltags and [ unicode(t) for t in deltags ]
            rc, wiki, failmsg = xicomp.wiki_tags( unicode(projectname), wikiurl,
                                                  addtags, deltags )
            return _result( rc, failmsg=failmsg )

    def votewiki( self, projectname, pagename, vote ) :
        """
        === votewiki( projectname, pagename, vote )
        
        :Description ::
            Upvote or Downvote wiki-page `pagename`, under project `projectname`

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name
        |= vote        | either 'up' (up-vote page) or 'down' (down-vote page)

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus'  : 'fail',
                  'message' : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, wiki, failmsg = xicomp.wiki_vote( unicode(projectname), wikiurl,
                                                  unicode(vote), c.authuser )
            return _result( rc, failmsg=failmsg )

    def wikifav( self, projectname, pagename, favorite ) :
        """
        === wikifav( projectname, pagename, favorite )

        :Description ::
            Add or remove wiki-page as favorite from `user`

        Positional arguments,
        |= projectname | a valid project-name
        |= pagename    | valid and existing wiki page-name
        |= favorite    | True (to add as favorite) or False (to remove from favorite)

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus'  : 'fail',
                  'message' : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        wikiurl = unicode(self.url_wikiurl( projectname, self._stripurl( pagename) ))
        res     = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, wiki, failmsg = xicomp.wiki_fav( unicode(projectname), wikiurl,
                                                 favorite, c.authuser )
            return _result( rc, failmsg=failmsg )

    def listtickets( self, projectname ) :
        """
        === listtickets( projectname )
        
        :Description ::
            List all tickets under project `projectname`,

        Positional arguments,
        |= projectname | a valid project-name

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus' : 'ok',
                  'tickets' : { <ticket-id> : [ <summary> ], ... }
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'TICKET_VIEW' ))
              )
        if res :
            return res
        else :
            rc, d, failmsg = xicomp.list_ticket( unicode(projectname) )
            return _result( rc, d=d, failmsg=failmsg )

    def newticket( self, projectname, summary, type, severity,
                   description, components, milestones, versions,
                   blocking, blockedby, parent ) :
        """
        === newticket( projectname, summary, type, severity, description,
        compenents, milestones, versions, blocking, blockedby, parent )
        
        :Description ::
            Create new ticket under project `projectname`

        Positional arguments,
        |= projectname | a valid project-name
        |= summary     | must be a valid summary string
        |= type        | must be a valid ticket type
        |= severity    | must be a valid ticket severity
        |= description | description string, if False, will be skipped
        |= components  | list of component ids, if False, will be skipped
        |= milestones  | list of milestone ids, if False, will be skipped
        |= versions    | list of version ids, if False, will be skipped
        |= blocking    | list of ticket ids blockedby this ticket, if False, will be skipped
        |= blockedby   | list of ticket ids blocking this ticket, if False, will be skipped
        |= parent      | parent ticket id

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus' : 'ok',
                  'id'        : <id>
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'TICKET_CREATE' ))
              )
        if res :
            return res
        else :
            projectname = unicode(projectname)
            summary     = unicode(summary)
            type        = unicode(type)
            severity    = unicode(severity)

            description, components, milestones, versions, blocking, \
                    blockedby, parent = \
            self._demarshalNone( description, components, milestones,
                                 versions, blocking, blockedby, parent )
            rc, d, failmsg = xicomp.create_ticket(
                                    projectname, summary, type, severity,
                                    c.authuser, description=description,
                                    components=components, 
                                    milestones=milestones, versions=versions,
                                    blocking=blocking, blockedby=blockedby,
                                    parent=parent
                             )
            return _result( rc, d=d, failmsg=failmsg )

    def ticket( self, projectname, ticket ) :
        """
        === ticket( projectname, ticket )
        
        :Description ::
            Read ticket `ticket, under project `projectname`

        Positional arguments,
        |= projectname | a valid project-name
        |= ticket      | a valid ticket id

        :Return ::
            On success,
                [<PRE
                { 'rpcstatus'    : 'ok',
                  'id'        : <id>,
                  'summary'   : <summary string>,
                  'type'      : <type string>,
                  'severity'  : <severity string>,
                  'status'    : <status string>,
                  'due_date'  : <due_date in DD/MM/YYYY format>
                  'created_on': <created_in DD/MM/YYYY format>
                  'owner'     : <owner string>,
                  'promptuser': <promptuser string>,
                  'compid'    : <component-id>,
                  'compname'  : <componentname>,
                  'mstnid'    : <milestone-id>,
                  'mstnname'  : <milestone_name>,
                  'verid'     : <version-id>,
                  'vername'   : <version_name>,
                  'parent'    : <parent-ticketid>,
                  'description'      : <description string>,
                  'descriptionhtml'  : <description as html>,
                  'blockedby' : [ <ticket-id>, <ticket-id>, ... ],
                  'blocking'  : [ <ticket-id>, <ticket-id>, ... ],
                  'children'  : [ <ticket-id>, <ticket-id>, ... ]
                } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                }
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'TICKET_VIEW' ))
              )
        if res :
            return res
        else :
            rc, d, failmsg = xicomp.read_ticket( unicode(projectname), ticket )
            if d : # Convert datetimes to user-timezone
                due_date   = d.get( 'due_date', None )
                created_on = d.get( 'created_on', None )
                if due_date :
                    due_date = h.utc_2_usertz( due_date, c.authuser.timezone 
                                             ).strftime( "%d/%m/%Y" )
                if created_on :
                    created_on = h.utc_2_usertz( created_on, c.authuser.timezone 
                                               ).strftime( "%d/%m/%Y" )
                d['due_date']   = due_date
                d['created_on'] = created_on
            # Marshal None into 'None'
            for k in d :
                d[k] = self._marshalNone( d[k] )
            return _result( rc, d=d, failmsg=failmsg )
            
    def configticket( self, projectname, ticket, summary, type, severity, 
                      description, promptuser, components, milestones, versions,
                      blocking, blockedby, parent, status, due_date
                    ) :
        """
        === configticket( projectname, ticket, summary, type, severity,
        description, promptuser, components, versions, blocking, blockedby,
        parent, status, due_date )
        
        :Description ::
            Configure ticket, `ticket` under project, `projectname`

        Positional arguments,
        |= projectname | a valid project-name
        |= ticket      | a valid ticket id
        |= summary     | summary string, if False, will be skipped
        |= type        | valid ticket type, if False, will be skipped
        |= severity    | valid ticket severity, if False, will be skipped
        |= description | description string, if False, will be skipped
        |= components  | list of component ids, if False, will be skipped
        |= milestones  | list of milestone ids, if False, will be skipped
        |= versions    | list of version ids, if False, will be skipped
        |= blocking    | list of ticket ids blockedby this ticket, if False, will be skipped
        |= blockedby   | list of ticket ids blocking this ticket, if False, will be skipped
        |= parent      | parent ticket id
        |= status      | valid ticket status, if False, will be skipped
        |= due_date    | due_date in mm/dd/yyyy format

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'TICKET_CREATE' ))
              )
        if res :
            return res
        else :
            if due_date and isinstance( due_date, (str, unicode) ) :
                due_date = h.duedate2dt( due_date, c.authuser.timezone )

            summary, type, severity, description, promptuser, \
                components, milestones, versions, blocking, blockedby, parent, \
                status, due_date = \
            self._demarshalNone( summary, type, severity, description, promptuser,
                                 components, milestones, versions, blocking,
                                 blockedby, parent,
                                 status, due_date )
            rc, t, failmsg = xicomp.config_ticket(
                                projectname, ticket, c.authuser, summary=summary,
                                type=type, severity=severity, description=description,
                                promptuser=promptuser, components=components,
                                milestones=milestones, versions=versions,
                                blocking=blocking, blockedby=blockedby, parent=parent,
                                status=status, due_date=due_date
                             )
            return _result( rc, failmsg=failmsg )

    def commentonticket( self, projectname, ticket, comment ) :
        """
        === commentonticket( projectname, ticket, comment )
        
        :Description ::
            Comment on `ticket` under project `projectname`

        Positional arguments,
        |= projectname | a valid project-name
        |= ticket      | a valid ticket id
        |= comment     | comment as wiki text

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        commentor = c.authuser
        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'TICKET_COMMENT_CREATE' ))
              )
        if res :
            return res
        else :
            rc, tcmt, failmsg = xicomp.comment_ticket(  
                                    unicode(projectname), int(ticket),
                                    unicode(comment), commentor
                                )
            return _result( rc, failmsg=failmsg )

    def tagticket( self, projectname, ticket, addtags, deltags ) :
        """
        === tagticket( projectname, ticket, addtags, deltags )
        
        :Description ::
            Add or delete tags from `ticket`,

        Positional arguments,
        |= projectname | a valid project-name
        |= ticket      | a valid ticket id
        |= addtags     | list of tagnames to add, if False, will be skipped
        |= deltags     | list of tagnames to delete, if False, will be skipped

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions(
                    c.authuser, h.authorized( h.HasPermname( 'TICKET_CREATE' ))
              )
        if res :
            return res
        else :
            addtags, deltags = self._demarshalNone( addtags, deltags )
            addtags = addtags and [ unicode(t) for t in addtags ]
            deltags = deltags and [ unicode(t) for t in deltags ]
            rc, t, failmsg = xicomp.ticket_tags( unicode(projectname), ticket,
                                                 addtags, deltags )
            return _result( rc, failmsg=failmsg )

    def voteticket( self, projectname, ticket, vote ) :
        """
        === voteticket( projectname, ticket, vote )
        
        :Description ::
            Upvote or Downvote a `ticket`

        Positional arguments,
        |= projectname | a valid project-name
        |= ticket      | a valid ticket id
        |= vote        | either 'up' (up-vote ticket) or 'down' (down-vote ticket)

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, t, failmsg = xicomp.ticket_vote( unicode(projectname), ticket,
                                                 unicode(vote), c.authuser )
            return _result( rc, failmsg=failmsg )

    def ticketfav( self, projectname, ticket, favorite ) :
        """
        === ticketfav( projectname, ticket, favorite )
        
        :Description :: 
            Add or remove ticket as favorite,

        :Return ::
            On success,
                [<PRE { 'rpcstatus'  : 'ok' } >]
            On failure,
                [<PRE
                { 'rpcstatus' : 'fail',
                  'message'   : <msg string indicating reason for failure>
                } >]
        """
        from zeta.config.environment    import xicomp

        res = self._permissions( c.authuser, True )
        if res :
            return res
        else :
            rc, t, failmsg = xicomp.ticket_fav( unicode(projectname), ticket,
                                                favorite, c.authuser )
            return _result( rc, failmsg=failmsg )

    def xmlrpc_fault( code, message ) :
        """Convenience method to return a Pylons response XMLRPC Fault"""
        print message

    def __after__( self ) :
        pass

