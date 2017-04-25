# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage license pages."""

# -*- coding: utf-8 -*-

# Gotchas :
#   1. Sometimes form submition request could change the content of `c.*`
#      variables, in which case all the `c.*` should be moved down.
# Notes : None
# Todo  : None


import logging

from   pylons                  import request, response, session, tmpl_context as c
import simplejson              as json

from   zeta.lib.base           import BaseController, render
from   zeta.lib.constants      import *
import zeta.lib.helpers        as h
import zeta.lib.analytics      as ca

log = logging.getLogger( __name__ )

class LicenseController( BaseController ) :
    """License pages"""

    _charts = {
        'chart6': 'By projects',
        'chart7': 'Tagged license',
    }

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        c.licid = c.routes_d.get( 'licid', '' )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

        try :
            c.licid_i = int(licid)
            c.license = liccomp.get_license(
                            c.licid_i, attrload=[ 'attachments', 'tags' ]
                        )
        except :
            c.licid_i = None
            c.license = None
        c.searchfaces = [('license', '1')]

    def _lictable( self, licfields ) :
        """Create a list of license to be displayed as a table"""
        l = []
        f = sorted( licfields, key=lambda x : x[0] )
        for licid, licname, projects in f :
            l.append( 
                [ licid, licname
                ] + [
                  self.url_forlicense( str(licid) ),    # View
                  self.url_uplic( str(licid) ),         # Edit
                  self.suburl_rmlicid( str(licid) ),    # Remov
                ] + [
                  [ p[1], self.url_forproject( p[1] ) ] for p in projects
                ]
            )
        return l

    def _selectoptions( self ) :
        """Compose the select-option list for all the licenses in DB"""
        from zeta.config.environment    import liccomp

        f = liccomp.licensefields()
        n = l = []
        for licid, licname, projects in f :
            n.append( licname )
            l.append(( self.url_forlicense(licid), licname))
        return sorted(n), l, f

    @h.authorize( h.HasPermname( 'LICENSE_VIEW' ))
    def _json_licattach( self ) :                           # JSON
        """JSON: { id : [ id, url, filename, summary ], ... }"""
        return json.dumps( self.modelattachments( c.license ) )

    @h.authorize( h.HasPermname( 'LICENSE_VIEW' ))
    def _json_lictag( self ) :                              # JSON
        """JSON: { tagname : tagname, ... }"""
        return json.dumps( self.modeltags( c.license ) )


    @h.authorize( h.HasPermname([ 'LICENSE_CREATE' ]))
    def liccreate( self, environ ) :
        """Create a new license to be hosted on this site.
        URLS :
            /license/create
            /license/create?form=submit&formname=createlic
        """
        from zeta.config.environment    import vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=['createlic'], user=c.authuser
        )

        # Setup context for page generation
        c.licensenames, c.licenselist, licfields = self._selectoptions()
        c.title = (c.form == 'request' and '-Skip-') or 'CreateLicense'

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        else :
            html = render( '/derived/license/liccreate.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'LICENSE_VIEW' ]))
    def licenses( self, environ ) :
        """Action for all license pages.
        URLS :
            /license
            /license?form=submit&formname=rmlic&view=js
        """
        from zeta.config.environment    import liccomp, vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        c.liceditable = h.authorized( h.HasPermname(['LICENSE_CREATE']) )
        c.att_editable = c.liceditable
        c.tag_editable = c.liceditable
        if c.form == 'submit' and c.liceditable :
            vfcomp.process(
                request, c,
                defer=True, errhandler=h.hitchfn(errhandler),
                formnames=['rmlic'], user=c.authuser
            )
        else :
            c.errmsg = 'Need `LICENSE_CREATE` to access the page'

        # Setup context for page generation
        c.licprojects = c.licensetable = []
        c.licensenames, c.licenselist, licfields = self._selectoptions()
        c.licensetable = self._lictable( licfields )
        c.attachs = {}
        c.tags = {}
        c.title = 'LicenseTable'

        # Html page generation
        c.rclose.append(render( '/derived/license/license.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'LICENSE_VIEW' ]))
    def license( self, environ, licid ) :
        """Action for all license pages.
        URLS :
            /license/<licid>
            /license/<licid>?jsonobj=licattach&view=js
            /license/<licid>?jsonobj=lictag&view=js
            /license/<licid>?form=request&formname=updatelic
            /license/<licid>?form=submit&formname=updatelic&view=js
            /license/<licid>?form=submit&formname=rmlic
            /license/<licid>?form=submit&formname=addlicattachs&view=js
            /license/<licid>?form=submit&formname=dellicattachs&view=js
            /license/<licid>?form=submit&formname=addlictags&view=js
            /license/<licid>?form=submit&formname=dellictags&view=js
        """
        from zeta.config.environment    import liccomp, vfcomp

        c.rclose = h.ZResp()

        # Setting up urls to be stuffed into the page
        def errhandler(errmsg) :
            c.errmsg = errmsg
        c.liceditable = h.authorized( h.HasPermname(['LICENSE_CREATE']) )
        c.att_editable = c.liceditable
        c.tag_editable = c.liceditable
        if c.form == 'submit' and c.liceditable :
            vfcomp.process(
                request, c,
                defer=True, errhandler=h.hitchfn(errhandler),
                formnames=['updatelic', 'rmlic', 'addlictags', 'dellictags',
                           'addlicattachs', 'dellicattachs' ],
                licid=c.licid_i, user=c.authuser
            )
        else :
            c.errmsg = 'Need `LICENSE_CREATE` to access the page'

        # Setup context for page generation
        c.licprojects = c.licensetable = []
        c.licensenames, c.licenselist, licfields = self._selectoptions()
        c.uplic = (c.form == 'request') and (c.formname == 'updatelic')

        if c.license and c.uplic :              # Edit license
            c.title = '%s:edit' % c.license.licensename
        elif c.license :                        # License page
            lprjs = liccomp.licprojects(c.license.id)
            c.licprojects = [ (p, self.url_forproject(p))
                              for p in lprjs[c.license.id] if p
                            ]
            c.attachs = self.modelattachments( c.license )
            c.tags = self.modeltags( c.license )
            c.title = c.license.licensename

        # Html page generation
        html = ''
        if c.view == 'js' and c.formname in [ 'addlicattachs' ] :
            html = IFRAME_RET

        elif c.view == 'js' and c.jsonobj and c.license :
            html = self.handlejson(environ)

        elif c.formname == 'rmlic' and c.licid :   
            # when removing the displayed license, redirect to first license
            remaining = [ i for i, _, projects in licfields if licid_i != int(i) ]
            h.redirect_url( self.url_forlicense(remaining[0])
            ) if remaining else h.redirec( h.url_crlic )

        elif (c.form == 'submit') and (c.formname == 'updatelic') :
            h.redirect_url( self.url_forlicense(licid) )

        elif c.view != 'js' :
            html = render( '/derived/license/license.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'LICENSE_VIEW' ]))
    def charts( self, environ ) :
        """License analytics chart
        URLS :
            /license/charts
            /license/charts?chartname=<name>
        """
        from zeta.config.environment    import liccomp

        c.rclose = h.ZResp()
        c.chartname = c.chartname or 'chart6'
        c.selectedchart = (c.chartname, self._charts[c.chartname])
        c.chartoptions = [ (self.url_licchart(name), text)
                           for name, text in self._charts.iteritems() ]

        c.la = ca.get_analyticobj( 'license' )
        c.ta = ca.get_analyticobj( 'tags' )

        if c.chartname == 'chart6' :            # Projects Vs license
            c.chart6_data = getattr( c.la, 'chart6_data', [] )
        elif c.chartname == 'chart7' :          # Tagged license
            c.chart7_data = getattr( c.ta, 'chart7_data', [] )
            c.chart7_tags = getattr( c.ta, 'chart7_tags', [] )

        c.title    = 'License:Charts'

        # Html page generation
        c.rclose.append(render( '/derived/license/charts.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'LICENSE_VIEW' ]))
    def attachs( self, environ ) :
        """Action to present attachment page for all license
        URLS : 
            /license/attachs
        """
        from zeta.config.environment    import liccomp, vfcomp

        c.rclose = h.ZResp()
        c.editable = h.authorized( h.HasPermname( 'LICENSE_CREATE' ))
        c.attachments = self.attachments( liccomp.attachments() )
        c.title = 'LicenseAttachs'

        # Html page generation
        c.rclose.append(render( '/derived/license/licattachs.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'LICENSE_VIEW' ]))
    def timelines( self, environ ) :
        """Timeline log of activities on all license pages
        URLS :
            /license/timeline
        """
        from zeta.config.environment    import liccomp

        c.rclose = h.ZResp()

        # Action specific query parameters
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.licensenames, c.licenselist, licfields = self._selectoptions()
        c.links = [ '', '', '' ]
        c.license = None
        c.timeline = True
        self.tline_controller( h.r_lictimelines, {}, 'license',
                               fromoff, logid, dir, c.license
                             )
        c.title = 'LicenseTimeline'
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )

        # Html page generation
        c.rclose.append(render( '/derived/license/lictline.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'LICENSE_VIEW' ]))
    def timeline( self, environ, licid ) :
        """Action for all license pages.
        URLS :
            /license/timeline/<licid>
        """
        from zeta.config.environment    import liccomp

        c.rclose = h.ZResp()

        # Action specific query parameters
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.licensenames, c.licenselist, licfields = self._selectoptions()
        c.links        = [ '', '', '' ]
        c.license      = None
        c.timeline = True
        licid = [ _i for _i, _, p in licfields if _i == c.licid_i ][0]
        c.license = liccomp.get_license( licid )
        self.tline_controller(
            h.r_lictimeline, { 'id' : licid_i }, [ 'license' ],
            fromoff, logid, dir, c.license
        )
        c.title = '%s:timeline' % c.license.licensename
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )

        # Html page generation
        c.rclose.append(render( '/derived/license/lictline.html' ))
        return c.rclose

    def feeds( self, environ ) :
        """Feed of activity log for all license pages
        URLS : 
            /license/feed
        """
        from zeta.config.environment    import liccomp

        title = 'LicenseTimeline'
        link = h.urlroot(environ)
        descr = 'Timeline for License'
        feed = h.FeedGen( title, link, descr )
        self.tline_controller(
            h.r_lictimelines, {}, 'license', 1, None, None, c.license
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, licid='' ) :
        """Action for all license pages.
        URLS : 
            /license/feed/<licid>
        """
        from zeta.config.environment    import liccomp

        title = '%s(%s):timeline' % ( c.license.licensename, licid_i )
        link = h.urlroot(environ)
        descr = 'Timeline for license %s' % c.license.licensename
        feed = h.FeedGen( title, link, descr )
        self.tline_controller(
            h.r_lictimeline, {}, 'license', 1, None, None, c.license
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers() # Genering, app-level after-controller handler
