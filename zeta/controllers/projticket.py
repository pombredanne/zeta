# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage project ticket pages."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

import logging
import datetime                as dt

from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config
import simplejson              as json

from   zeta.lib.base           import BaseController, render
from   zeta.config.environment import tckfilters
import zeta.lib.helpers        as h
import zeta.lib.gviz           as gviz
import zeta.lib.analytics      as ca
from   zeta.lib.constants      import *

log = logging.getLogger( __name__ )

# Permission maps for forms
tckperm  = {}
tckperm.update(
    dict([ ( formname, h.HasPermname( 'TICKET_CREATE' ))
           for formname in [ 'createtck', 'configtck', 'tcktype', 'tckseverity',
                             'tckpromptuser', 'tckcomponent', 'tckmilestone',
                             'tckversion', 'tckparent', 'tckblockedby', 
                             'tckblocking', 'tcksummary',
                             'addtcktags', 'deltcktags' ]
        ])
)
tckperm.update(
    dict([ ( formname, h.HasPermname( 'TICKET_STATUS_CREATE' ))
           for formname in [ 'createtstat', 'configtstat', 'tststatus',
                             'tstduedate' ]
         ])
)
tckperm.update(
    dict([ ( formname, h.HasPermname( 'TICKET_COMMENT_CREATE' ))
           for formname in [ 'createtcmt', 'updatetcmt', 'replytcmt' ]
         ])
)

class ProjticketController( BaseController ) :
    """Class to handle project ticket page request"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )
        c.mainnavs = mainnav( c.projectname, c.controllername )

        # Collect the query values into 'context'
        c.graph   = request.params.get( 'graph', None )
        c.tree    = request.params.get( 'tree', None )
        c.forowner= request.params.get( 'owner', None )
        c.forcomp = request.params.get( 'comp', None )
        c.formstn = request.params.get( 'mstn', None )
        c.forver  = request.params.get( 'ver', None )

        c.ticket  = tckcomp.get_ticket(
                         c.ticket_id,
                         attrload=[ 'attachments', 'tags', 'type', 'severity' ]
                    ) if c.tckid else None
        c.project = projcomp.get_project(
                        c.projectname, attrload=[ 'logofile', ]
                    ) if c.projectname else None
        c.prjlogo = c.project and c.project.logofile and \
                    self.url_attach( c.project.logofile.id )

        c.searchfaces = [ ( 'project', c.projectname ), 
                          ( 'ticket', '1' )
                        ]

    def formpermission( self ) :
        return ( c.form == 'submit'
               ) and ( c.formname in tckperm 
               ) and ( not h.authorized( tckperm[c.formname] ) )

    def _seltickets( self ) :
        p = c.projectname
        fn = lambda tckid : [ self.url_ticket( p, tckid ), str(tckid) ]
        return map( fn, tckcomp.ticketids(c.project) )

    def _ticketattachs( self, ticket ) :
        """For JSON consumption.
        Massage the ticket attachments"""
        return self.modelattachments( ticket )

    def _tickettags( self, ticket ) :
        """For JSON consumption.
        Massage the ticket tags"""
        return self.modeltags( ticket )

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def _json_ticketlist( self ) :                          # JSON-GRID
        """Fetch the json object with caching, under `projectname`
       JSON: { id   : 'id',
               label: 'ticket_id',
               items: [ { id             : tck.id,
                          projectname    : tck.project.projectname,
                          ts_id          : ts.id ,
                          ticketurl      : url_for(ticket) ,
                          summary        : tck.summary,
                          tck_typename   : tck.type.typename,
                          tck_severityname : tck.severity.tck_severityname,
                          tck_statusname : tck.status.tck_statusname,
                          due_date       : ts.due_date ,
                          owner          : ts.owner.username,
                          promptuser     : tck.promptuser.username,
                          component_id   : component.id,
                          componentname  : component.componentname,
                          milestone_id   : milestone.id,
                          milestone_name : milestone.milestone_name,
                          version_id     : version.id,,
                          version_name   : version.version_name,
                          upvotes        : upvotes ,
                          downvotes      : downvotes,
                          age            : age          },
                        ... ]
             }"""
        from zeta.config.environment    import tckcomp

        def format_item( tup ) :
            due_date = tup[8].astimezone( h.timezone( c.authuser.timezone)
                       ) if tup[8] else None
            ymd = [ due_date.year, due_date.month, due_date.day
                  ] if due_date else []
            age = h.olderby( dt.datetime.utcnow().toordinal() - tup[3].toordinal() )
            d = {
                'id'              : tup[0],
                'projectname'     : tup[1],
                'ticketurl'       : self.url_ticket( c.project.projectname, tup[0] ),
                'summary'         : tup[2],
                'tck_typename'    : tup[4],
                'tck_severityname': tup[5],
                'tck_statusname'  : tup[6],
                'ts_id'           : tup[7],
                'due_date'        : ymd,
                'owner'           : tup[9],
                'promptuser'      : tup[10],
                'component_id'    : tup[11],
                'componentname'   : tup[12],
                'milestone_id'    : tup[13],
                'milestone_name'  : tup[14],
                'version_id'      : tup[15],
                'version_name'    : tup[16],
                'upvotes'         : tup[17],
                'downvotes'       : tup[18],
                'age'             : age,
            }
            d = tckcomp.computefilters( d, tckfilters=c.tckfilters )[0]
            return (d.get(c.stdfilter, True) and d) if c.stdfilter else d

        c.tckfilters = h.compile_tckfilters( tckfilters )
        savfilters   = dict([
                         ( tf.id, h.json.loads(tf.filterbyjson)
                         ) for tf in tckcomp.get_ticketfilter(user=c.authuser)
                       ])
        filters = savfilters.get( c.savfilter, {} )
        tcklist = tckcomp.ticketlist(project=c.project, filters=filters)
        tcklist = sorted( tcklist.values(), key=lambda l : l[0], reverse=True )
        _tl =  h.todojoreadstore( tcklist,
                                  format_item,
                                  id='id',
                                  label='ticket_id'
                                )
        return _tl

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def _json_tckattachs( self ) :                          # JSON
        """JSON: { id : [ id, url, filename, summary ], ... } """
        return json.dumps( self._ticketattachs( c.ticket ) )

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def _json_tcktags( self ) :                             # JSON
        """JSON: { tagname : tagname ... } """
        return json.dumps( self._tickettags( c.ticket ) )

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def _json_tckcomments( self ) :                         # JSON
        """JSON: { id : 'ticket_comment_id',
                   label : 'ticket_comment_id',
                   items: [ { ticket_comment_id : tcmt.id,
                              commentby         : tcmt.commentby.username,
                              text              : tcmt.text,
                              html              : tcmt.texthtml,
                              commentbyicon     : usericon,
                              commentbyurl      : userurl,
                              datestr           : tcmt.created_on },
                            ... ]
                 }"""
        from zeta.config.environment    import tckcomp

        def format_item( qres ) :
            d = {
                'ticket_comment_id' : qres[0],
                'commentby'         : qres[4],
                'text'              : qres[1],
                'html'              : qres[2],
                'commentbyicon'     : '',
                'commentbyurl'      : self.url_user( qres[4] ),
                'datestr'           : h.utc_2_usertz(
                                         qres[3], c.authuser.timezone
                                      ).strftime( '%d %b %Y, %r'),
            }
            return d

        return h.todojoreadstore(
                        tckcomp.tckcomments( c.ticket.id ),
                        format_item,
                        id='ticket_comment_id',
                        label='ticket_comment_id'
               )

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def _json_tckrcomments( self ) :                        # JSON
        """JSON: { id : 'ticket_comment_id',
                   label: 'ticket_comment_id',
                   items: [ { ticket_comment_id : tcmt.id,
                              commentby         : tcmt.commentby.username ,
                              text              : tcmt.text,
                              html              : tcmt.texthtml,
                              commentbyicon     : usericon,
                              commentbyurl      : userurl,
                              datestr           : tcmt.created_on },
                            ... ]
                 }"""
        from zeta.config.environment    import tckcomp

        def format_item( qres ) :
            d = {
                'ticket_comment_id' : qres[0],
                'commentby'         : qres[4],
                'text'              : qres[1],
                'html'              : qres[2],
                'commentbyicon'     : '',
                'commentbyurl'      : self.url_user( qres[4] ),
                'datestr'           : h.utc_2_usertz(
                                         qres[3], c.authuser.timezone
                                      ).strftime( '%d %b %Y, %r'),
            }
            return d

        tcomments = tckcomp.tckrcomments( c.ticket.id )
        items = []
        while tcomments :
            tcomment = tcomments.pop( 0 )
            d_tcmt = format_item( tcomment )
            d_tcmt.setdefault(
                'replies',
                [ format_item( rtcomment ) for rtcomment in tcomment[-1] ]
            )
            items.append( d_tcmt )

        return h.todojoreadstore(
                        items,
                        lambda v : v,
                        id='ticket_comment_id',
                        label='ticket_comment_id'
               )

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def ticketindex( self, environ, projectname ) :
        """Project tickets
        URLS :
            /p/{projectname}/t
            /p/{projectname}/t?stdfilter=<stdfilter>&savfilter=<savfilter>
            /p/{projectname}/t?jsonobj=ticketlist&view=js
            /p/{projectname}/t?form=submit&formname=configtck&view=js
            /p/{projectname}/t?form=submit&formname=configtstat&view=js
            /p/{projectname}/t?form=submit&formname=addtckfilter&view=js
            /p/{projectname}/t?form=submit&formname=deltckfilter&view=js
        """
        from zeta.config.environment    import vfcomp, projcomp, tckcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % tckperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'configtck', 'configtstat', 'addtckfilter',
                            'deltckfilter' ], 
                user=c.authuser
            )

        # Setup context for both html page and AJAX request.
        c.projsummary = c.project.summary
        c.tckfilters = h.compile_tckfilters( tckfilters )
        c.title = '-Skip-'

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)

        elif c.view != 'js' and not (c.stdfilter or c.savfilter) and c.tckfilters :
            url = self.url_tcklist( projectname, stdfilter=c.tckfilters[0][0] )
            h.redirect_url( url )

        elif c.view != 'js' :
            # Setup context for html page
            c.tck_typenames = tckcomp.tcktypenames
            c.tck_statusnames = tckcomp.tckstatusnames
            c.tck_severitynames = tckcomp.tckseveritynames
            c.seltickets = self._seltickets()

            c.pcomponents, c.pmilestones, c.pversions, c.projusers = \
                              tckcomp.projdetails( c.project )
            c.projusers = self.projusers( c.project )
            c.pmilestones = [ m[:2] for m in c.pmilestones if not any(m[2:]) ]
            c.mstnnames = sorted([ m[0] for m in c.pmilestones ])
            c.pcompnames = sorted([ comp[0] for comp in c.pcomponents ])
            c.vernames = sorted([ ver[0] for ver in c.pversions ])
            c.tckeditable = h.authorized( h.HasPermname( 'TICKET_CREATE' ))
            c.tckccodes = h.tckccodes
            c.tstat_resolv = h.parse_csv( c.sysentries.get( u'ticketresolv', '' ))
            userfilters = tckcomp.get_ticketfilter( user=c.authuser )
            fn = lambda tf : ( tf.id, [ tf.name, tf.filterbyjson ] )
            c.savfilterlist = dict(map( fn, userfilters ))
            c.savfilterval = c.savfilterlist.get( c.savfilter, ['', ''] )
            c.savfiltername = c.savfilterval[0]
            fn = lambda k, v : [ self.url_tcklist(c.projectname, savfilter=k), v[0] ]
            c.savfilterlist = map( fn, c.savfilterlist.iteritems() )
            c.title  = 'Ticket:list'
            html = render( '/derived/projects/ticketindex.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'TICKET_CREATE' ))
    def createticket( self, environ, projectname ) :
        """Create ticket
        URLS :
            /p/{projectname}/t/createticket?form=request&formname=createtck
            /p/{projectname}/t/createticket?form=submit&formname=createtck
        """
        from zeta.config.environment    import vfcomp, projcomp, tckcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=['createtck'], user=c.authuser
        )

        # Setup context for page generation
        c.project = c.project or projcomp.get_project( projectname )
        c.projectname = c.project.projectname
        c.projsummary = c.project.summary

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.form == 'submit' :
            h.flash( MESSAGE_FLASH + 'Created ticket ...' )
            # Ticket creation, redirect after submit
            c.title = '-Skip-'
            h.redirect_url( h.url_ticketcreate )

        else :
            # Setup context for page generation
            c.seltickets = self._seltickets()
            c.tck_typenames = tckcomp.tcktypenames
            c.tck_statusnames = tckcomp.tckstatusnames
            c.tck_severitynames = tckcomp.tckseveritynames

            c.pcomponents, c.pmilestones, c.pversions, c.projusers = \
                              tckcomp.projdetails( c.project )
            c.projusers = list(set( c.projusers + [c.project.admin.username] ))
            c.pmilestones = [ m[:2] for m in c.pmilestones if not any(m[2:]) ]
            c.mstnnames = sorted([ m[0] for m in c.pmilestones ])

            c.pcompnames = sorted([ comp[0] for comp in c.pcomponents ])
            c.vernames = sorted([ ver[0] for ver in c.pversions ])
            c.pcomponents = [ (tup[1], tup[0]) for tup in c.pcomponents ]
            c.pmilestones = [ (tup[1], tup[0]) for tup in c.pmilestones ]
            c.pversions = [ (tup[1], tup[0]) for tup in c.pversions ]
            c.title = 'CreateTicket'
            c.tckeditable = h.authorized( h.HasPermname( 'TICKET_CREATE' ))
            html = render( '/derived/projects/ticketcreate.html' )
            h.flash.pop_messages() # Clear flashmessage if any ! after page generation

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def ticket( self, environ, projectname, tckid ) :
        """Each ticket
        URLS : 
            /p/{projectname}/t/{tckid}
            /p/{projectname}/t/{tckid}?jsonobj=tckattachs&view=js
            /p/{projectname}/t/{tckid}?jsonobj=tcktags&view=js
            /p/{projectname}/t/{tckid}?jsonobj=tckcomments&view=js
            /p/{projectname}/t/{tckid}?jsonobj=tckrcomments&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=createtstat&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=addtckattachs&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=deltckattachs&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=addtcktags&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=deltcktags&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=createtcmt&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=updatetcmt&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=replytcmt&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=tckfav&view=js
            /p/{projectname}/t/{tckid}?form=submit&formname=votetck&view=js
        """
        from zeta.config.environment import vfcomp, projcomp, tckcomp, votcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % tckperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'createtstat', 'addtckattachs', 'deltckattachs',
                            'addtcktags', 'deltcktags', 'createtcmt', 'updatetcmt',
                            'replytcmt', 'tckfav', 'votetck' ], 
                user=c.authuser
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        if not c.jsonobj :
            c.tckeditable = c.att_editable = c.tag_editable = h.authorized(
                    h.HasPermname('TICKET_CREATE')
            )
            c.seltickets = self._seltickets()
            c.tckccodes = h.tckccodes
            c.tck_typenames = tckcomp.tcktypenames
            c.tck_statusnames = tckcomp.tckstatusnames
            c.tck_severitynames = tckcomp.tckseveritynames
            c.pcomponents, c.pmilestones, c.pversions, c.projusers = \
                              tckcomp.projdetails( c.project )
            c.pmilestones = [ m[:2] for m in c.pmilestones if not any(m[2:]) ]
            c.pcomponents = [ (tup[1], tup[0]) for tup in c.pcomponents ]
            c.pmilestones = [ (tup[1], tup[0]) for tup in c.pmilestones ]
            c.pversions   = [ (tup[1], tup[0]) for tup in c.pversions ]
            c.items_tckcomments = self._json_tckcomments()
            c.attachs = self._ticketattachs( c.ticket )
            c.tags = self._tickettags( c.ticket )
            c.isuserfavorite = tckcomp.isfavorite( c.authuser.id, c.ticket.id )
            c.ticketdetail = tckcomp.ticketdetails( c.ticket )
            c.ticketstatus = tckcomp.ticketstatus( c.ticket )
            c.blockers = tckcomp.blockersof( c.ticket )
            c.blocking = tckcomp.blockingfor( c.ticket )
            c.children = tckcomp.childrenfor( c.ticket )
            c.ticketresolv = h.parse_csv(c.sysentries.get( 'ticketresolv', '' ))
            c.title = 'Ticket:%s' % tckid

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.view == 'js' and c.formname in [ 'addtckattachs' ] :
            html = IFRAME_RET

        elif c.jsonobj and c.view == 'js' :
            html = self.handlejson(environ)

        elif c.textobj and c.view == 'text' :
            html = self.handletext(environ)

        elif c.view != 'js' :
            uservote = votcomp.get_ticketvote( c.authuser, c.ticket )
            votes = tckcomp.countvotes( ticket=c.ticket )
            c.upvotes = votes.get( 'up', 0 )
            c.downvotes = votes.get( 'down', 0 )
            c.currvote = uservote and uservote.votedas or ''
            html = render( '/derived/projects/ticket.html' )
        else :
            html = ''

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'TICKET_VIEW' ))
    def ticketgraph( self, environ, projectname, tckid, file ) :
        """Each ticket
        URLS :
            /p/{projectname}/t/{tckid}/{graph.svg}
            /p/{projectname}/t/{tckid}/{tree.svg}
        """
        from zeta.config.environment    import tckcomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.tckccodes = h.tckccodes

        # HTML page generation
        if file == 'graph.svg' :    # Dependency graph
            x = tckcomp.allblockers()
            y = tckcomp.ticketdeps() 
            tckdeps = gviz.calctckdep( x, y )
            z = gviz.tckdeptodot( c.ticket.id, tckdeps, c.tckccodes )
            html = gviz.tosvgtext(z)
            response.content_type = 'image/svg+xml'

        elif file == 'tree.svg' :   # Hierarchy graph
            x = tckcomp.allparchild()
            y = tckcomp.ticketdeps() 
            tckhier = gviz.calctckhier( x, y )
            z = gviz.tckhiertodot( c.ticket.id, tckhier, c.tckccodes )
            html = gviz.tosvgtext(z)
            response.content_type = 'image/svg+xml'

        if file == 'graph.png' :    # Dependency graph
            x = tckcomp.allblockers()
            y = tckcomp.ticketdeps()
            tckdeps = gviz.calctckdep( x, y )
            z = gviz.tckdeptodot( c.ticket.id, tckdeps, c.tckccodes )
            html  = gviz.topng(z)
            response.content_type = 'image/png'

        elif file == 'tree.png' :   # Hierarchy graph
            x = tckcomp.allparchild()
            y = tckcomp.ticketdeps() 
            tckhier   = gviz.calctckhier( x, y )
            z = gviz.tckhiertodot( c.ticket.id, tckhier, c.tckccodes )
            html = gviz.topng(z)
            response.content_type = 'image/png'
        else :
            html = ''

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'TICKET_VIEW' ]))
    def timelines( self, environ, projectname ) :
        """Activities under project tickets or individual ticket
        URLS :
            /p/{projectname}/t/timeline
        """
        from zeta.config.environment    import projcomp, tckcomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        c.seltickets = self._seltickets()
        routeargs = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projtckstline, routeargs, ['ticket', 'project'],
            fromoff, logid, dir, c.project
        )
        c.title    = 'Tickets:timeline'

        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.rclose.append(render( '/derived/projects/tickettline.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'TICKET_VIEW' ]))
    def timeline( self, environ, projectname, tckid ) :
        """Activities under project tickets or individual ticket
        URLS :
            /p/{projectname}/t/timeline/{tckid}
        """
        from zeta.config.environment    import projcomp, tckcomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        c.seltickets = self._seltickets()
        routeargs  = { 'projectname' : projectname, 'tckid' : tckid }
        self.tline_controller(
            h.r_projtcktline, routeargs, 'ticket',
            fromoff, logid, dir, c.ticket
        )
        c.title    = 'Ticket:%s:timeline' % tckid
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )

        c.rclose.append(render( '/derived/projects/tickettline.html' ))
        return c.rclose

    def feeds( self, environ, projectname ) :
        """Activities under project tickets or individual ticket
        URLS :
            /p/{projectname}/t/feed
        """
        from zeta.config.environment    import projcomp, tckcomp

        # Setup context for page generation
        title = '%s:tickets' % projectname
        link = h.urlroot(environ)
        descr = 'Timeline for tickets in project %s' % projectname
        c.projsummary = c.project.summary
        feed   = h.FeedGen( title, link, descr )
        routeargs  = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projtckstline, routeargs, ['ticket', 'project'],
            1, None, None, c.project
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, projectname, tckid ) :
        """Activities under project tickets or individual ticket
        URLS :
            /p/{projectname}/t/feed/{tckid}
        """
        from zeta.config.environment    import projcomp, tckcomp

        # Setup context for page generation
        title = '%s-ticket:(%s)' % ( projectname, tckid )
        link = h.urlroot(environ)
        descr = 'Timeline for ticket %s in project %s' % ( tckid, projectname )
        c.projsummary = c.project.summary
        feed   = h.FeedGen( title, link, descr )
        routeargs = { 'projectname' : projectname, 'tckid' : tckid }
        self.tline_controller(
            h.r_projtcktline, routeargs, 'ticket',
            1, None, None, c.ticket
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    _charts = {
        'chart21' : 'project-tickets',
        'chart22' : 'ticket-owners',
        'chart23' : 'ticket-components',
        'chart24' : 'ticket-milestones',
        'chart25' : 'ticket-versions',
        'chart26' : 'ticket-commenters',
    }

    @h.authorize( h.HasPermname([ 'TICKET_VIEW' ]))
    def charts( self, environ, projectname ) :
        """Charts and analytics for project tickets
        URLS : 
            /p/{projectname}/t/charts
            /p/{projectname}/t/charts?chartname=<name>
        """

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.chartname = c.chartname or 'chart21'
        c.selectedchart = (c.chartname, self._charts[c.chartname])
        fn =  lambda n, t : ( self.url_tckchart( projectname, n ), t )
        c.chartoptions = map( fn, self._charts.iteritems() )
        c.tcka = ca.get_analyticobj( 'tickets' )

        if c.chartname == 'chart21' :
            # Pie chart for types, severity and status
            c.chart21_data = getattr( c.tcka, 'chart21_data', {}
                                    ).get( c.project.id, [] )

        elif c.chartname == 'chart22' :
            # Pie chart of types, severity and status for project users
            allusers = getattr( c.tcka, 'chart22_data', {}
                              ).get( c.project.id, [] )
            c.chart22_usrs = getattr( c.tcka, 'chart22_usrs', {}
                                    ).get( c.project.id, [] )
            p = c.projectname
            fn = lambda u : ( self.url_tckchart( p, 'chart22', owner=u[0] ), u[0] )
            c.ticketowners = map( fn, c.chart22_usrs )
            c.forowner = c.forowner or (c.chart22_usrs and c.chart22_usrs[0][0])\
                         or ''
            c.selectedowner = c.forowner

            # Fetch chart data for requested user (owner)
            for u in allusers :
                if u[0] == c.forowner :
                    c.chart22_data = u[1:]
                    break
            else :
                c.chart22_data = []

        elif c.chartname == 'chart23' :
            # Pie chart of types, severity and status for project components
            allcomps = getattr( c.tcka, 'chart23_data', {}
                              ).get( c.project.id, [] )
            componentnames = sorted(map(lambda x : x[0], allcomps))
            p = c.projectname
            fn = lambda comp : ( self.url_tckchart( p, 'chart23', comp=comp ), comp )
            c.ticketcomps = map( fn, componentnames )
            c.forcomp = c.forcomp or (componentnames and componentnames[0]) or ''
            c.selectedcomp = c.forcomp

            # Fetch chart data for requested component
            for comp in allcomps :
                if comp[0] == c.forcomp :
                    c.chart23_data = comp[1:]
                    break
            else :
                c.chart23_data = []

        elif c.chartname == 'chart24' :
            # Pie chart of types, severity and status for project milestones
            allmstns = getattr( c.tcka, 'chart24_data', {}
                              ).get( c.project.id, [] )
            milestonenames = sorted(map(lambda x : x[0], allmstns))
            p = c.projectname
            fn = lambda m : ( self.url_tckchart( p, 'chart24', mstn=m ), m )
            c.ticketmstns = map( fn, milestonenames )
            c.formstn = c.formstn or (milestonenames and milestonenames[0]) or ''
            c.selectedmstn = c.formstn

            # Fetch chart data for requested milestone
            for mstn in allmstns :
                if mstn[0] == c.formstn :
                    c.chart24_data = mstn[1:]
                    break
            else :
                c.chart24_data = []

        elif c.chartname == 'chart25' :
            # Pie chart of types, severity and status for project versions
            allvers = getattr( c.tcka, 'chart25_data', {}
                             ).get( c.project.id, [] )
            versionnames = sorted(map(lambda x : x[0], allvers))
            p = c.projectname
            fn = lambda v : ( self.url_tckchart( p, 'chart25', ver=v ), v )
            c.ticketvers = map( fn, versionnames )
            c.forver = c.forver or (versionnames and versionnames[0]) or ''
            c.selectedver = c.forver

            # Fetch chart data for requested milestone
            for ver in allvers :
                if ver[0] == c.forver :
                    c.chart25_data = ver[1:]
                    break
            else :
                c.chart25_data = []

        elif c.chartname == 'chart26' :
            # Ticket commentors
            c.chart26_data = getattr( c.tcka, 'chart26_data', {}
                                    ).get( c.project.id, [] )
            c.chart26_usrs = getattr( c.tcka, 'chart26_usrs', {}
                                    ).get( c.project.id, [] )

        c.title    = 'TicketCharts'
        c.rclose.append(render( '/derived/projects/ticketcharts.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'TICKET_VIEW' ]))
    def attachs( self, environ, projectname ) :
        """Action to present attachment page for tickets under project 
        `projectname`
        URLS :
            /p/{projectname}/t/attachs
        """
        from zeta.config.environment    import vfcomp, tckcomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        attachments = tckcomp.attachments( c.project )
        c.attachments = self.attachments( attachments )
        c.editable = h.authorized( h.HasPermname( 'TICKET_CREATE' ))
        c.title    = 'TicketAttachs'
        c.rclose.append(render( '/derived/projects/tckattachs.html' ))
        return c.rclose

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers()
