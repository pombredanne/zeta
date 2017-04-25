# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage site search."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Captcha session management should be refined.
#   2. Implement `forgotpass` action.


from   __future__               import with_statement
import logging
import os

import xapian                   as xap
from   pylons                   import request, response  
from   pylons                   import config
from   pylons                   import session
from   pylons                   import tmpl_context as c

from   zeta.lib.error           import *
from   zeta.lib.base            import BaseController, render
from   zeta.lib.constants       import *
import zeta.lib.helpers         as h

log       = logging.getLogger(__name__)

ITEMSINPAGE = 10

class SearchController( BaseController ) :
    """Controller for faceted search using Xapian"""

    def sr_userurl( self, id ) :
        from zeta.config.environment import userscomp
        user = userscomp.get_user( id )
        return self.url_user( user.username )

    def sr_attachurl( self, id ) :
        from zeta.config.environment    import attcomp
        attach = attcomp.get_attach( id )
        return self.url_attach( attach.id )

    def sr_licenseurl( self, licid ) :
        from zeta.config.environment    import liccomp
        license = liccomp.get_license( licid )
        return self.url_forlicense( licid )

    def sr_swikiurl( self, path ) :
        from zeta.config.environment    import syscomp
        swiki = syscomp.get_staticwiki( unicode(path) )
        return self.url_swiki( path )

    def sr_projecturl( self, id ) :
        from zeta.config.environment    import projcomp
        project = projcomp.get_project( id )
        return self.url_forproject( project.projectname )

    def sr_ticketurl( self, projectname, id ) :
        from zeta.config.environment    import tckcomp
        ticket = tckcomp.get_ticket( id )
        return self.url_ticket( projectname, ticket.id )

    def sr_reviewurl( self, projectname, id ) :
        from zeta.config.environment    import revcomp
        review = revcomp.get_review( id )
        return self.url_revwid( projectname, review.id )

    def sr_wikiurl( self, projectname, id ) :
        from zeta.config.environment    import wikicomp
        wiki = wikicomp.get_wiki( id )
        return wiki.wikiurl


    def __before__( self, environ ) :
        from zeta.config.environment    import srchcomp

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

        c.querystring = request.params.get( 'querystring', '' )  
        c.frommatch   = int(request.params.get( 'frommatch', 0 ))
        c.all         = request.params.get( 'all', '' )
        projectface   = request.params.get( 'project', '' )

        c.allfaces = srchcomp.projectfaces.copy(
                     ) if projectface else srchcomp.searchfaces.copy()

        def filterfaces( attr ) :
            # Note an empty {key,value} pair is added.
            val = request.params.get( attr, None )
            return val and (attr, val) or ('', '')

        c.faces = dict( map( filterfaces, c.allfaces.keys() ))
        c.faces.pop( '', None ) # the empty {key,value} pair is pruned here.
        if (not c.faces) or c.all :
            c.faces = { 'all' : '1' }
            projectface and c.faces.update([ ('project', projectface) ])

        self.urlconstructor = {
            'user' : self.sr_userurl,
            'attach' : self.sr_attachurl,
            'license' : self.sr_licenseurl,
            'staticwiki' : self.sr_swikiurl,
            'project' : self.sr_projecturl,
            'ticket' : self.sr_ticketurl,
            'review' : self.sr_reviewurl,
            'wiki' : self.sr_wikiurl
        }


    @h.authorize( h.HasPermname( 'SEARCH_VIEW' ))
    def index( self, environ ) :
        """Search"""
        from zeta.config.environment    import srchcomp

        c.rclose = h.ZResp()

        q = c.querystring

        #------- Replace this with a query parser
        prefixes    = []
        for face in c.faces.keys() :
            if face == 'all' :
                break;
            elif face == 'project' :
                prefixes.append(( xap.Query.OP_AND, 'XPROJECT%s' % c.faces['project'].lower() ))
            elif face :
                prefixes.append(( xap.Query.OP_OR, 'XCLASS%s' % face ))
        #------- Replace this with a query parser

        matches   = srchcomp.query( q, prefixes, c.frommatch )
        c.matches = []
        c.total   = c.frommatch + len(matches)
        rem       = True
        count     = 0
        for m in matches :
            if count >= ITEMSINPAGE :
                break;
            count      += 1
            text, url  = srchcomp.urlfor_match( m, self.urlconstructor )
            c.matches.append(
              {
                'percent'   : m.percent,
                'rank'      : m.rank,
                'weight'    : m.weight,
                'data'      : m.document.get_data(),
                'url'       : url,
                'text'      : text,
              }
            )
        else :
            rem = False
                
        kwargs = {}
        kwargs.update( c.faces )
        c.querystring and kwargs.update({ 'querystring' : c.querystring })
        h.suburl_search     = \
            h.url_for( h.r_searchpage, **kwargs )
        h.suburl_searchprev = \
            c.frommatch and \
            h.url_for( h.r_searchpage, frommatch=(c.frommatch-ITEMSINPAGE), **kwargs ) \
            or ''
        h.suburl_searchnext = \
            rem and \
            h.url_for( h.r_searchpage, frommatch=(c.frommatch+ITEMSINPAGE), **kwargs ) \
            or ''

        c.terms = srchcomp.queryterms( q )
        c.title = 'Search'

        # Prune away the project face, since it is implicit and doesnt make
        # sense to give it as a selectable option.
        c.allfaces.pop( 'project' )
        c.rclose.append(render( '/derived/search/searchpage.html' ))
        return c.rclose

    def __after__( self ) :
        self.aftercontrollers()
