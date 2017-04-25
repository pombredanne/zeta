# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage pages that are accessible only to the
site administrator
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Remove editurl for licenselist

import logging

from   pylons                   import request, response, session, tmpl_context as c
from   pylons                   import config

from   zeta.lib.base            import BaseController, render
import zeta.lib.helpers         as h

log = logging.getLogger( __name__ )

class SiteadminController( BaseController ) :
    """Site administration via web"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

        # Collect the query values into 'context'
        c.form      = request.params.get( 'form', None )
        c.formname  = request.params.get( 'formname', None )
        c.view      = request.params.get( 'view', None )
        c.jsonobj   = request.params.get( 'jsonobj', None )

    def _licenselist( self ) :
        from zeta.config.environment    import liccomp

        h.url_licenses = {}
        licenselist  = []
        licfields  = sorted( liccomp.licensefields(), key=lambda x : x[1] )
        for licid, licname, projects in licfields :
            licurl = self.url_forlicense( str(licid) ),     # View
            editurl = self.url_uplic( str(licid) ),         # Edit
            rmurl = self.suburl_rmlicid( str(licid) ),      # Remov
            h.url_licenses.setdefault( licid, [ licurl, editurl, rmurl ] )

        licenselist = [ [ licid, licname ] + h.url_licenses[licid] +
                          [ [p[1], self.url_forproject( p[1] )] for p in projects ]
                          for licid, licname, projects in licfields ]
        return licenselist

    def _json_pgmap( self ) :                                   # JSON
        """JSON : [ { id   : 'pg_id', 
                      label: 'perm_group',
                      items: [ { pg_id      : id,
                                 perm_group : perm_group,
                                 permnames  : permnames,
                                 x_permnames: ^permnames }
                               ... ]
                    }"""
        from zeta.config.environment import userscomp
        fn = lambda k, v : { 'pg_id'     : k,    'perm_group'  : v[0],
                             'permnames' : v[1], 'x_permnames' : v[2] }
        return h.todojoreadstore( userscomp.pgmap, fn id='pg_id', label='perm_group' )

    @h.authorize( h.HasPermname( 'SITE_ADMIN' ))
    def index( self, environ ) :
        """Action to handle siteadministration"""
        from zeta.config.environment    import projcomp, vfcomp, userscomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg

        vfcomp.process(
                request, c,
                defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'system', 'userenb', 'userdis', 'prjenb', 'prjdis',
                            'adduserperms', 'deluserperms', 'createpg',
                            'updatepg', 'addpntopg', 'delpnfrompg' ]
        )

        # Setup context for page rendering
        if c.jsonobj not in [ 'pgmap' ] :
            c.licenselist = self._licenselist()
            c.permnames = sorted( userscomp.perm_names )
            c.usernames, userperms, c.userstatus = userscomp.siteadmin()
            defuser = sorted(userperms.keys())[0]
            c.defuserperms = [ defuser, sorted(userperms[defuser][0]),
                               userperms[defuser][1] ]
            c.projectstatus = projcomp.projectstatus

        c.liceditable = True
        c.title = 'SiteAdmin'

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)
        elif c.view != 'js' :
            html = render( '/derived/siteadmin/siteadmin.html' )
        else :
            html = ''
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'SITE_ADMIN' ))
    def uploadlogo( self, environ ) :
        """Action to upload site logo file"""
        from zeta.config.environment    import vfcomp, userscomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True,
            errhandler=h.hitchfn(errhandler), formnames=[ 'sitelogo']
        )

        c.title = 'SiteLogo'

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.form == 'submit' :
            h.redirect_url( h.url_siteadmin )
        else :
            html = render( '/derived/siteadmin/sitelogo.html' )

        c.rclose.append(html)
        return html

    @h.authorize( h.HasPermname( 'SITE_ADMIN' ))
    def timeline( self, environ ) :
        """Complete timeline history"""

        c.rclose = h.ZResp()

        # Action specific query parameters
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.links = [ '', '', '' ]
        self.tline_controller(
                h.r_sitetline, {}, [], fromoff, logid, dir
        )
        c.title = 'SiteTimeline'
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.rclose.append(render( '/derived/siteadmin/tline.html' ))
        return c.rclose

    def feed( self, environ ) :
        """feed for site"""
        title = 'SiteTimeline'
        link = h.urlroot(environ)
        descr = 'Timeline for Site'
        feed = h.FeedGen( title, link, descr )
        self.tline_controller(
                h.r_sitetline, {}, [], 1, None, None, modelobj=None 
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    @h.authorize( h.HasPermname( 'SITE_ADMIN' ))
    def charts( self, environ ) :
        """Charts for site"""
        pass

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers() # Genering, app-level after-controller handler
