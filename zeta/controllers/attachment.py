# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to handle attachment related request."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None


import logging

from   pylons                  import request, response, session, tmpl_context as c

from   zeta.lib.base           import BaseController, render
from   zeta.lib.constants      import *
import zeta.lib.helpers        as h
import zeta.lib.analytics      as ca
from   zeta.lib.view           import metanav

log = logging.getLogger( __name__ )

class AttachmentController( BaseController ) :
    """Actions to handle user pages"""

    _charts = {
        'chart2': 'By Uploaders',
        'chart3': 'By download-count',
        'chart4': 'By tag',
        'chart5': 'By timestamp',
    }

    def __before__( self, environ=None ) :
        """Called before calling any actions under this controller"""

        # Collect the query values into 'context'
        c.fromid = request.params.get( 'fromid', None )
        c.all = request.params.get( 'all', None )

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

    @h.authorize( h.ValidUser() )
    def index( self, environ ) :
        """List of all attachments
        URLS :
            /attachment
            /attachment?fromid=<number>
            /attachment?all=1
            /attachment?form=submit&formname=attachssummary&view=js
            /attachment?form=submit&formname=attachstags&view=js
        """
        from zeta.config.environment    import attcomp, vfcomp

        c.rclose = h.ZResp()
        h.url_attachpages = self.url_attachpages()

        # Form handling
        def errhandler( errmsg ) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=errhandler,
            user=c.authuser, formnames=['attachssummary', 'attachstags']
        )

        try :
            fromid = c.fromid and int(c.fromid)
            fromid -= 1
        except :
            fromid = None
        c.title = 'Attachments'
        c.aa = ca.get_analyticobj( 'attachs' )
        c.ua = ca.get_analyticobj( 'users' )
        c.la = ca.get_analyticobj( 'license' )
        c.pa = ca.get_analyticobj( 'projects' )
        c.ta = ca.get_analyticobj( 'tickets' )
        c.ra = ca.get_analyticobj( 'reviews' )
        c.wa = ca.get_analyticobj( 'wiki' )

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.view == 'js' :
            html = ''
        else :
            limit = 100 if c.all == None else None
            attachments = attcomp.attachments( offset=fromid, limit=limit )
            attachs = [ [ aid ] + attachments[aid][:-1] + \
                        [ ', '.join(attachments[aid][-1]) ] + \
                        [ self.url_attachdownl( aid ) ]
                        for aid in attachments ]
            c.attachassc= attcomp.attachassc()
            c.attachments = { 'all-attachments' : attachs }
            c.editable = h.authorized( h.ValidUser( strict='True' ))

            html = render( '/derived/attachs/index.html' )

        c.rclose.append( html )
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ) )
    def add( self, environ ) :
        """Add a new attachment
        URLS :
            /attachment/add?form=request&formname=addattachs
            /attachment/add?form=submit&formname=addattachs
        """
        from zeta.config.environment    import vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler( errmsg ) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=errhandler,
            user=c.authuser, formnames=['addattachs']
        )

        # Setup context for page generation
        c.title = 'AddAttachs'

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        else :
            html = render( '/derived/attachs/add.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.ValidUser() )
    def attach( self, environ, id ) :
        """Provide the attachment's content
        URLS :
            /attachment/{id}
        """
        from zeta.config.environment    import attcomp

        attach = attcomp.get_attach( int(id) )
        if attach :
            return str(attcomp.content(attach))
        else : 
            response.status_int = 400
            return 'No attachment by id %s' % id

    @h.authorize( h.ValidUser() )
    def download( self, environ, id ) :
        """Prompt browser to download the attachment.
        URLS :
            /attachment/download/{id}
        """
        from zeta.config.environment    import attcomp

        attach, content = attcomp.downloadattach( int(id) )

        if attach :
            response.headers['Content-disposition'] = \
                str( 'attachment; filename="%s"' % attach.filename )

        else :
            response.status_int = 400
            return 'No attachment by id %s' % id

        return str(content)

    @h.authorize( h.ValidUser() )
    def charts( self, environ ) :
        """Attachment charts
        URLS :
            /attachment/charts
            /attachment/charts?chartname=<name>
        """
        # Setup context for page generation
        c.rclose = h.ZResp()
        c.chartname = c.chartname or 'chart2'
        c.selectedchart = ( c.chartname, self._charts[c.chartname] )
        c.chartoptions = [
            ( h.url_attachcharts( name ), text )
            for name, text in self._charts.iteritems()
        ]
        c.ta = ca.get_analyticobj( 'tags' )
        c.aa = ca.get_analyticobj( 'attachs' )

        if c.chartname == 'chart2' :    # user Vs attachments
            c.chart2_data = getattr( c.aa, 'chart2_data', [] )
            c.chart2_fcnt = getattr( c.aa, 'chart2_fcnt', 0 )
            c.chart2_payld= getattr( c.aa, 'chart2_payld', 0 )

        elif c.chartname == 'chart3' :  # attachment Vs download
            c.chart3_data = getattr( c.aa, 'chart3_data', [] )

        elif c.chartname == 'chart4' :  # attachment Vs tags
            c.chart4_data = getattr( c.ta, 'chart4_data', [] )
            c.chart4_tags = getattr( c.ta, 'chart4_tags', [] )

        elif c.chartname == 'chart5' :  # attachment Vs uploaded time
            c.chart5_data = getattr( c.aa, 'chart5_data', [] )
            date = c.chart5_data and c.chart5_data[0][0][3] or None
            c.chart5_frmdt= h.date2jsdate( date, [ '2000', '0', '1' ] )
            c.chart5_data = [ [ l[:3] for l in logs ] for logs in c.chart5_data ]

        c.title = "Attachment:Charts"

        # Html page generation
        c.rclose.append(render( '/derived/attachs/charts.html' ))
        return c.rclose

    @h.authorize( h.ValidUser() )
    def timeline( self, environ ) :
        """Timeline on attachments.
        URLS :
            /attachment/timeline
        """
        c.rclose = h.ZResp()

        # Action specific query parameters
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.links = [ '', '', '' ]
        self.tline_controller(
            h.r_attachtimeline, {}, 'attachment',
            fromoff, logid, dir, modelobj=None
        )
        c.title = 'AttachTimeline'
        c.timeline = True

        # Html page generation
        c.rclose.append(render( '/derived/attachs/tline.html' ))
        return c.rclose

    
    def feed( self, environ ) :
        """feed on attachments.
        URLS :
            /attachment/feeds
        """
        self.tline_controller(
            h.r_attachtimeline, {}, 'attachment',
            1, None, None, modelobj=None
        )
        title = 'AttachTimeline'
        link = h.urlroot(environ)
        descr = 'Timeline for Attachments'

        feed   = h.FeedGen( title, link, descr )
        for l in c.logs :
            summary, lnk, content = h.log2feed( l )
            feed.add_item(
                    summary, '%s%s' % (link,lnk), content,
                    pubdate=l.created_on, unique_id=str(l.id),
                    author_name=l.user.username
            )
        response.content_type = 'application/atom+xml'
        feedhtml = feed.writeString('utf-8')
        return feedhtml

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers() # Genering, app-level after-controller handler
