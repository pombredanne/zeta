# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to handler tag related request.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

import logging

from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
import zeta.lib.analytics      as ca

log = logging.getLogger( __name__ )

class TagController( BaseController ) :

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

    def tagcloud( self, environ ) :
        """Tag cloud"""
        from zeta.config.environment    import syscomp, tagcomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.specialtags = h.parse_csv( syscomp.get_sysentry( 'specialtags' ))
        c.tagpercentile = tagcomp.tagpercentile
        c.title = 'TagCloud'

        # Html page generation
        c.rclose.append(render( '/derived/tag/tagcloud.html' ))
        return c.rclose

    def tagname( self, environ, tgnm ) :
        """Show tag details"""
        from zeta.config.environment    import tagcomp, projcomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.tag = tagcomp.get_tag(
                        tgnm,
                        attrload=[
                            'attachments', 'licenses', 'projects',
                            'tickets', 'reviews', 'wikipages'
                        ],
                        attrload_all=[
                            'tickets.project', 'reviews.project',
                            'wikipages.project'
                        ]
                )
        c.projecturls = self.projecturls( projcomp.projectnames )

        # Pie Chart for tagged resource type
        ta  = ca.get_analyticobj( 'tags' )
        c.chart1_rtags= getattr( ta, 'chart1_rtags', {} ).get( tgnm, [] )
        c.chart1_data = getattr( ta, 'chart1_data', {} ).get( tgnm, [] )
        c.title       = tgnm

        # Html page generation
        c.rclose.append(render( '/derived/tag/tag.html' ))
        return c.rclose

    def timelines( self, environ ) :
        """Action for all timeline pages."""
        from zeta.config.environment    import tagcomp

        c.rclose = h.ZResp()
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.links = [ '', '', '' ]
        self.tline_controller(
            h.r_tagstline, {}, 'tag', fromoff, logid, dir, c.tag
        )
        c.title = 'Tags:timeline'
        c.rclose.append(render( '/derived/tag/tagtline.html' ))
        return c.rclose

    def timeline( self, environ, tgnm ) :
        """Action for all timeline pages."""
        from zeta.config.environment    import tagcomp

        c.rclose = h.ZResp()
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.tag = tagcomp.get_tag( tgnm )
        c.links = [ '', '', '' ]
        self.tline_controller(
            h.r_tagtline, {}, 'tag', fromoff, logid, dir, c.tag
        )
        c.title = '%s:timeline' % tgnm
        c.rclose.append(render( '/derived/tag/tagtline.html' ))
        return c.rclose

    def feeds( self, environ ) :
        """Action for all timeline pages."""
        from zeta.config.environment    import tagcomp

        # Setup context for page generation
        title = 'tags'
        link = h.urlroot(environ)
        descr = 'Timeline for tags'
        feed   = h.FeedGen( title, link, descr )
        self.tline_controller(
            h.r_tagstline, {}, 'tag', 1, None, None, c.tag
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, tgnm ) :
        """Action for all timeline pages."""
        from zeta.config.environment    import tagcomp

        # Setup context for page generation
        title = 'tag:%s' % tgnm
        link = h.urlroot(environ)
        descr = 'Timeline for tag %s' % tgnm
        c.tag = tagcomp.get_tag( tgnm )
        feed   = h.FeedGen( title, link, descr )
        self.tline_controller(
            h.r_tagtline, {}, 'tag', 1, None, None, c.tag
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def __after__( self ) :
        self.aftercontrollers()
