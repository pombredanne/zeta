# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to handle home page."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None


import logging

from   pylons                  import request, response
from   pylons                  import config
from   pylons                  import tmpl_context as c

from   multigate               import NotAuthorizedError

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
import zeta.lib.analytics      as ca
from   zeta.lib.constants      import *

# Sometimes absent public files (under defenv/public/) will be treated as
# guest-wiki pages. Make sure to skip them.
PUBLICFILES = [ 'sitelogo' ]

log = logging.getLogger(__name__)

class HomeController( BaseController ) :
    """All the pages returned by this controller are static wiki pages"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Collect the query values into 'context'
        c.editsw = request.params.get( 'editsw', None )
        c.delsw = request.params.get( 'delsw', None )
        c.refresh = request.params.get( 'refresh', None )
        c.previewtype = request.params.get( 'previewtype', None )

        # Common logic for this controller
        c.searchfaces = [('staticwiki', '1')]

        # Initialize context
        c.swurl = None
        c.swiki = None
        c.swhtml = ''

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        c.swurl = c.routes_d.get( 'swurl', '' )
        if c.controlleraction == 'index' :
            c.swurl = u'frontpage'
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

    def formpermission( self ) :
        return c.form in [ 'submit', 'request' ] and \
               not h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))

    def listswdir( self ) :
        swentry = lambda x : x[1] and ( x[0], x[2], self.url_editsw(x[2]),
                                        self.suburl_delsw(x[2]) )
        l = [ [sw.id] + h.checksuburl(sw.path, c.swurl)
              for sw in syscomp.get_staticwiki() ]
        c.swikis = filter( None, map( swentry, l ))

    @h.authorize( h.HasPermname( 'STATICWIKI_CREATE' ))
    def _text_swpreview( self ) :                           # TEXT
        """Translate wiki markup text into HTML and send back to browser"""
        o = h.Preview()
        text = request.POST.get('text', '')
        setattr(o, 'text', text)
        o.translate = h.hitch( o, h.Preview, h.translate, cacheattr='text' )
        html = o.translate( wtype=c.previewtype, wiki=c.swiki )
        return html

    def _publicfile( self, url ) :
        """Check for public file, which are not present and so gets redirected
        here"""
        return True if url in PUBLICFILES else False

    @h.authorize( h.ValidUser() )
    def index( self, environ ) :
        """Static Wiki - Home page.
        URLS :
            /
        """
        from zeta.config.environment    import syscomp

        c.rclose = h.ZResp()
        # Setup context for page generation
        c.sweditable = h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))
        c.swiki = syscomp.get_staticwiki( u'frontpage' )
        c.title = config['zeta.sitename']
        c.swhtml = c.swiki and c.swiki.texthtml or ''

        c.rclose.append(render( '/derived/home/guestwiki.html' ))
        return c.rclose

    def tos( self, environ ) :
        """Static Wiki - Terms of Service
        .... Deprecated ....
        """
        from zeta.config.environment    import syscomp

        c.rclose = h.ZResp()
        c.sweditable = h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))
        c.swiki  = syscomp.get_staticwiki( u'tos' )
        c.swhtml = c.swiki and c.swiki.texthtml or ''

        c.rclose.append(render( '/derived/home/guestwiki.html' ))
        return c.rclose

    @h.authorize( h.ValidUser() )
    def titleindex( self, environ ) :
        """Static Wiki - titleindex
        URLS :
            /titleindex
            /TitleIndex
        """
        from zeta.config.environment    import syscomp

        c.rclose = h.ZResp()
        c.sweditable = h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))
        c.swikis = [ ( sw.id, sw.path, self.url_editsw(sw.path),
                       self.suburl_delsw(sw.path)
                     ) for sw in syscomp.get_staticwiki()
                   ]
        c.swikis = sorted( c.swikis, key=lambda sw : sw[1] )
        c.swa = ca.get_analyticobj( 'staticwiki' )
        c.swsnippets = getattr( c.swa, 'pagesnippets', {} )
        c.title = 'TitleIndex'
        c.rclose.append(render( '/derived/home/titleindex.html' ))
        return c.rclose

    @h.authorize( h.ValidUser() )
    def staticwiki( self, environ, swurl ) :
        """Static Wiki - every thing else
        URLS :
            /tos
            /aboutus
            /help/
            /(swurl)
            /(swurl)?refresh=1
            /(swurl)?textobj=swpreview&view=text
            /(swurl)?editsw=1&form=request&formname=editsw
            /(swurl)?form=submit&formname=editsw&view=js
            /(swurl)?form=submit&formname=delsw&delsw=1
        """
        from zeta.config.environment    import vfcomp, syscomp, wikicomp

        c.rclose = h.ZResp()
        c.sweditable = h.authorized( h.HasPermname( 'STATICWIKI_CREATE' ))

        # Form handling
        if self.formpermission() :
           c.errmsg = 'Do not have STATICWIKI_CREATE permission !!'

        def errhandler(errmsg) :
            c.errmsg = errmsg
        kwargs = { 'pathurl' : swurl } if c.formname == 'delsw' else {}
        kwargs['user'] = c.authuser
        vfcomp.process(
            request, c,
            defer=True, errhandler=h.hitchfn(errhandler),
            formnames=['editsw', 'delsw'], **kwargs
        )

        if [c.form, c.formname] == ['submit', 'delsw'] and c.delsw :
            h.redirect_url( h.url_titleindex )

        # Setup context for page generation
        c.urldir = swurl and swurl[-1] == '/'
        c.swurl = swurl
        c.swiki = syscomp.get_staticwiki( swurl )
        c.title = c.swurl.split('/')[-1]
        
        html = ''
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.jsonobj and c.view == 'js' :     # Ajax request <JSON>
            html = self.handlejson(environ)

        elif c.textobj and c.view == 'text' :   # Ajax request <TEXT>
            html = self.handletext(environ)

        elif self._publicfile( c.swurl ) :      # Check for public file
            html = ''

        elif c.view == 'js' :                   # Ajax view, so empty html
            html = ''

        elif c.editsw and c.swiki :             # Page-logic, edit static wiki
            c.wikitypenames = wikicomp.typenames
            c.title = '%s:edit' % c.title
            html = render( '/derived/home/guestwiki.html' )

        elif c.swiki and (c.swiki.type.wiki_typename == h.WIKITYPE_REDIRECT) \
                and c.swiki.sourceurl :         # Page redirect
            h.redirect_url( c.swiki.sourceurl )

        elif c.urldir :                         # List static wiki directory
            c.swikis = self.listswdir()
            c.swa = ca.get_analyticobj( 'staticwiki' )
            c.swsnippets = getattr( c.swa, 'pagesnippets', {} )
            html = render( '/derived/home/guestwiki.html' )

        elif c.swiki :                          # Page-logic, show static wiki
            if not c.swiki.texthtml :
                c.swhtml = c.swiki.translate(wiki=c.swiki, cache=True)
            elif c.refresh :
                c.swhtml = c.swiki.translate(wiki=c.swiki, cache=True)
            else :
                c.swhtml = c.swiki.texthtml
            html = render( '/derived/home/guestwiki.html' )

        elif h.authorized( h.HasPermname( 'STATICWIKI_CREATE' )) :
            # Assume this as a new static wiki url and create it.
            c.wikitypenames = wikicomp.typenames
            c.swiki  = syscomp.set_staticwiki( unicode(swurl), u'', byuser=c.authuser )
            c.editsw = 1
            html = render( '/derived/home/guestwiki.html' )

        else :
            raise NotAuthorizedError( 'You are allowed to create this resource.' )

        c.rclose.append(html)
        return c.rclose

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers() # Genering, app-level after-controller handler
