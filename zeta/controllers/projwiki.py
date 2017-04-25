# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage project wiki pages."""

# -*- coding: utf-8 -*-

# Gotchas :
#   1. Eagerloading wiki-comment replies does not seem to work. Is it to do
#      with many-many relationship between same table ?
# Notes   : None
# Todo    : None

import logging

from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config
import simplejson              as json
from   multigate               import NotAuthorizedError

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
import zeta.lib.analytics      as ca
from   zeta.lib.constants      import *

log = logging.getLogger( __name__ )

# Permission maps for forms
wikiperm = {}
wikiperm.update(
    dict([ ( formname, h.HasPermname( 'WIKI_CREATE' ))
           for formname in [ 'createwiki', 'configwiki', 'wikitype',
                             'wikisummary', 'wikisourceurl', 'wikicont',
                             'rmwikicont', 'addwikiattachs', 'delwikiattachs',
                             'addwikitags', 'delwikitags', 'vcsfile2wiki' ]
         ])
)
wikiperm.update(
    dict([ ( formname, h.HasPermname( 'WIKICOMMENT_CREATE' ))
           for formname in [ 'createwcmt', 'updatewcmt', 'replywcmt' ]
         ])
)

class ProjwikiController( BaseController ) :
    """Class to handle project wiki page request"""

    def _optimized_fetch( self, controllername, projectname ) :
        """Fetch the project object and wiki object from the database in
        an optimized manner based on the action and json request"""
        from zeta.config.environment    import projcomp, wikicomp

        # For Ajax request
        if c.jsonobj == 'wikicomments' :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo) )

        elif c.jsonobj == 'wikircomments' :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo) )

        elif c.jsonobj == 'wikilist' :
            l = [ 'logofile', 'wikis', 'wikis.tablemap', 'wikis.votes', 'wikis.type' ]
            c.project = projcomp.get_project( c.projectname, attrload=l )

        elif c.textobj == 'wikipreview' :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo) )

        elif controllername == 'wiki' and c.wikiedit :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo), attrload=[ 'tablemap' ] )

        elif controllername == 'wiki' and c.wtalkpage :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo), attrload=[ 'tablemap' ] )

        elif controllername == 'wiki' and c.whistory :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo), attrload=[ 'tablemap' ] )

        elif controllername == 'wiki' and c.wikidiff :
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo), attrload=[ 'tablemap' ] )

        elif controllername == 'wiki' :
            l = [ 'creator', 'type', 'attachments', 'tags', 'tablemap', 'votes' ]
            c.wiki = wikicomp.get_wiki( unicode(c.pathinfo), attrload=l )

        l = [ 'logofile' ]
        c.project = c.project or projcomp.get_project( projectname, attrload=l )


    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )
        c.mainnavs = mainnav( c.projectname, c.controllername )

        # Collect the query values into 'context'
        c.wikipage   = request.params.get( 'wikipage', None )
        c.wikipreview= request.params.get( 'wikipreview', None )
        c.wikiedit   = request.params.get( 'wikiedit', None )
        c.wikidiff   = request.params.get( 'wikidiff', None )
        c.wtalkpage  = request.params.get( 'wikitalkpage', None )
        c.whistory   = request.params.get( 'wikihistory', None )
        c.translate  = request.params.get( 'translate', False ) and True
        c.downloadas = request.params.get( 'downloadas', None )
        c.previewtype= request.params.get( 'previewtype', None )
        c.oldver     = request.POST.get( 'oldver', None )
        c.newver     = request.POST.get( 'newver', None )
        c.oldver     = c.oldver and int(c.oldver)
        c.newver     = c.newver and int(c.newver)
        c.wiki       = None

        self._optimized_fetch( c.controllername, projectname )
        c.prjlogo = c.project and c.project.logofile and \
                    self.url_attach( c.project.logofile.id )
        c.searchfaces = [ ( 'project', projectname ), 
                          ( 'wiki', '1' )
                        ]

    def formpermission( self ) :
        return ( c.form == 'submit'
               ) and ( c.formname in wikiperm 
               ) and ( not h.authorized( wikiperm[c.formname] ) )

    def wikipagenames( self, wikiurls ) :
        fn = lambda wu : [ wu[1], h.wiki_parseurl( wu[1] ) ]
        pagenames = map( fn, wikiurls )
        return pagenames

    def _wikiattachs( self, wiki ) :
        """For JSON consumption.
        Massage the wiki attachments"""
        return self.modelattachments( wiki )

    def _wikitags( self, wiki ) :
        """For JSON consumption.
        Massage the wiki tags"""
        return self.modeltags( wiki )

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def _json_wikilist( self ) :                            # JSON-GRID
        """JSON: { id   : 'id',
                   label: 'wiki_id',
                   items: [ { id             : wiki.id,
                              wikiurl        : wiki.wikiurl ,
                              pagename       : wurl,
                              summary        : wiki.summary ,
                              sourceurl      : wiki.sourceurl,
                              wiki_typename  : wiki.type.wiki_typename ,
                              latest_version : wiki.latest_version ,
                              last_modified  : wcnt.created_on ,
                              author         : wcnt.author,
                              upvotes        : upvotes ,
                              downvotes      : downvotes }
                            ... ]
                 }"""
        from zeta.config.environment    import wikicomp
        def format_item( w ) :
            wcnt    = wikicomp.get_content( w )
            votes   = wikicomp.countvotes( votes=w.votes )
            lastmod = h.utc_2_usertz( wcnt.created_on, c.authuser.timezone
                      ).strftime( '%d %b %Y' ) if wcnt else 'N/A'
            author  = wcnt.author if wcnt else 'N/A'
            d = {
                'id'             : w.id,
                'wikiurl'        : w.wikiurl,
                'pagename'       : c.wurl,
                'summary'        : w.summary,
                'sourceurl'      : w.sourceurl,
                'wiki_typename'  : w.type.wiki_typename,
                'latest_version' : str(w.latest_version),
                'last_modified'  : lastmod,
                'author'         : author,
                'upvotes'        : votes.get('up', 0 ),
                'downvotes'      : votes.get('down', 0 )
            }
            return d
        return h.todojoreadstore(
                         c.project.wikis,
                         format_item,
                         id='id',
                         label='wiki_id'
                 )

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def _json_wikiattach( self ) :                          # JSON
        """JSON: { id : [ id, url, filename, summary ], ... } """
        return json.dumps( self._wikiattachs( c.wiki ) )

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def _json_wikitag( self ) :                             # JSON
        """JSON: { tagname : tagname, ... } """
        return json.dumps( self._wikitags( c.wiki ) )

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def _json_wikicomments( self ) :                        # JSON
        """JSON: { wiki_comment_id : 'wiki_comment_id',
                   wiki_comment_id : 'wiki_comment_id',
                   items: [ { wiki_comment_id : wcmt.id,
                              version_id      : wcmt.version_id,
                              commentby       : wcmt.commentby.username ,
                              text            : wcmt.text,
                              html            : wcmt.texthtml,
                              commentbyicon   : usericon,
                              commentbyurl    : userurl,
                              datestr         : wcmt.created_on },
                            ... ]
                 }"""
        from zeta.config.environment    import wikicomp

        def format_item( qres ) :
            s = h.utc_2_usertz( qres[4], c.authuser.timezone
                              ).strftime( '%d %b %Y, %r' )
            d = {
                'wiki_comment_id' : qres[0],
                'version_id'      : qres[1],
                'commentby'       : qres[5],
                'text'            : qres[2],
                'html'            : qres[3],
                'commentbyicon'   : '',
                'commentbyurl'    : self.url_user( qres[5] ),
                'datestr'         : s
            }
            return d

        return h.todojoreadstore(
                        wikicomp.wikicomments( c.wiki.id ),
                        format_item,
                        id='wiki_comment_id',
                        label='wiki_comment_id'
                )

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def _json_wikircomments( self ) :                       # JSON
        """JSON: { wiki_comment_id : 'wiki_comment_id',
                   wiki_comment_id : 'wiki_comment_id',
                   items: [ { wiki_comment_id : wcmt.id,
                              version_id      : wcmt.version_id,
                              commentby       : wcmt.commentby.username ,
                              text            : wcmt.text,
                              html            : wcmt.texthtml,
                              commentbyicon   : usericon,
                              commentbyurl    : userurl,
                              datestr         : wcmt.created_on },
                            ... ]
                 }"""
        from zeta.config.environment    import wikicomp

        def format_item( qres ) :
            s = h.utc_2_usertz( qres[4], c.authuser.timezone
                              ).strftime( '%d %b %Y, %r' )
            d = {
                'wiki_comment_id' : qres[0],
                'version_id'      : qres[1],
                'commentby'       : qres[5],
                'text'            : qres[2],
                'html'            : qres[3],
                'commentbyicon'   : '',
                'commentbyurl'    : self.url_user( qres[5] ),
                'datestr'         : s
            }
            return d
        wcomments = wikicomp.wikircomments( c.wiki.id )
        items = []
        while wcomments :
            wcomment = wcomments.pop( 0 )
            d_wcmt   = format_item( wcomment )
            d_wcmt.setdefault(
                'replies',
                [ format_item( rwcomment ) for rwcomment in wcomment[-1] ]
            )
            items.append( d_wcmt )
        return h.todojoreadstore(
                        items,
                        lambda v : v,
                        id='wiki_comment_id',
                        label='wiki_comment_id'
                 )

    @h.authorize( h.HasPermname( 'WIKI_CREATE' ))
    def _text_wikipreview( self ) :                     # TEXT
        """ TEXT : HTML content of wiki markup text"""
        o = h.Preview()
        text = request.POST.get( 'text', '' )
        setattr( o, 'text', text)
        o.translate  = h.hitch( o, h.Preview, h.translate, cacheattr='text' )
        html = o.translate( wtype=c.previewtype, wiki=c.wiki )
        return html

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def wikiindex( self, environ, projectname ) :
        """Project wiki pages.
        URLS :
            /p/{projectname}/wiki
            /p/{projectname}/wiki?jsonobj=wikilist&view=js
            /p/{projectname}/wiki?form=submit&formname=vcsfile2wiki&view=js
            /p/{projectname}/wiki?form=submit&formname=configwiki&view=js
        """
        from zeta.config.environment    import projcomp, wikicomp, vfcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % tckperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'vcsfile2wiki', 'configwiki' ], 
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        if not c.jsonobj and c.formname != 'vcsfile2wiki' :
            c.wikitypenames = wikicomp.typenames
            c.wikipagenames = self.wikipagename( wikicomp.wikiurls( c.project ))
            c.wikipagename = None
            c.wikieditable = h.authorized( h.HasPermname( 'WIKI_CREATE' ))
            c.title = '%s:wiki' % projectname

        # HTML page generation
        html = ''
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)
        elif c.view != 'js' :
            html = render( '/derived/projects/wikiindex.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def titleindex( self, environ, projectname ) :
        """Title index of all Project wiki pages.
        URLS :
            /p/{projectname}/wiki/titleindex
            /p/{projectname}/wiki/TitleIndex
        """
        from zeta.config.environment    import projcomp, wikicomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        wikiurls = wikicomp.wikiurls( c.project )
        c.wikipagenames = self.wikipagename( wikiurls )
        fn = lambda wu : ( wu[0], h.wiki_parseurl(wu[1]) )
        c.titlepages = sorted( map( fn, wikiurls ), key=lambda x : x[1] )
        c.wikipagename = None
        c.wa = ca.get_analyticobj( 'wiki' )
        c.wsnippets = getattr(c.wa, 'pagesnippets', {}).get(c.project.id, {})
        c.title = '%s:titleindex' % projectname

        # HTML page generation
        c.rclose.append(render( '/derived/projects/wikitindex.html' ))
        return c.rclose


    @h.authorize( h.HasPermname( 'WIKI_VIEW' ))
    def wiki( self, environ, projectname, wurl=None ) :
        """Project wiki pages.
        URLS :
            /p/{projectname}/wiki/*(wurl)
            /p/{projectname}/wiki/*(wurl)?ver=<num>
            /p/{projectname}/wiki/*(wurl)?wikiedit=1
            /p/{projectname}/wiki/*(wurl)?wikitalkpage=1
            /p/{projectname}/wiki/*(wurl)?wikihistory=1
            /p/{projectname}/wiki/*(wurl)?wikidiff=1
            /p/{projectname}/wiki/*(wurl)?translate=1
            /p/{projectname}/wiki/*(wurl)?downloadas=text
            /p/{projectname}/wiki/*(wurl)?downloadas=ps
            /p/{projectname}/wiki/*(wurl)?downloadas=pdf
            /p/{projectname}/wiki/*(wurl)?jsonobj=wikicomments&view=js
            /p/{projectname}/wiki/*(wurl)?jsonobj=wikircomments&view=js
            /p/{projectname}/wiki/*(wurl)?jsonobj=wikiattach&view=js
            /p/{projectname}/wiki/*(wurl)?jsonobj=wikitag&view=js
            /p/{projectname}/wiki/*(wurl)?textobj=wikipreview&view=text
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=addwikiattachs&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=delwikiattachs&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=addwikitags&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=delwikitags&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=wikicont&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=createwcmt&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=updatewcmt&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=replywcmt&view=js
            /p/{projectname}/wiki/*(wurl)?wikidiff=1&form=submit&formname=wikidiff
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=wikifav&view=js
            /p/{projectname}/wiki/*(wurl)?form=submit&formname=votewiki&view=js
        """
        from zeta.config.environment import projcomp, wikicomp, votcomp, vfcomp

        version = request.params.get( 'ver', None )
        wurl = wurl.rstrip('/')
        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % tckperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'addwikiattachs', 'delwikiattachs', 'addwikitags',
                            'delwikitags', 'wikicont', 'createwcmt',
                            'updatewcmt', 'replywcmt', 'wikidiff', 'wikifav',
                            'votewiki'
                          ],
                user=c.authuser
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        if not c.jsonobj :
            c.wikipagenames = self.wikipagename( wikicomp.wikiurls( c.project ))
            c.wikipagename = wurl
            c.wikieditable = h.authorized( h.HasPermname( 'WIKI_CREATE' ))
            c.wiki = c.wiki or wikicomp.get_wiki( unicode(c.pathinfo) )

        # If there is no wiki page by that name then create the wiki and
        # show the edit page.
        if not c.wiki and c.wikieditable :
            c.wiki = wikicomp.create_wiki(
                                unicode(c.pathinfo),
                                wtype=c.sysentries.get('def_wikitype', None),
                                creator=c.authusername
                     )
            c.project and wikicomp.config_wiki( c.wiki, project=c.project )
            c.wikiedit = '1'

        elif not c.wiki :
            raise NotAuthorizedError(
                    'Do not have permission to create wiki page, WIKI_CREATE' )


        # If the wiki page is empty (ie) no wiki content ever created, then
        # show the edit page.
        if not c.wiki.latest_version and c.wikieditable :
            h.flash( MESSAGE_FLASH + 'Empty page, write some text ...' )
            c.wikiedit = '1'

        elif not c.wiki.latest_version :
            raise NotAuthorizedError(
                    'Do not have permission to create wiki page, WIKI_CREATE' )

        if c.wiki :
            c.isuserfavorite = wikicomp.isfavorite( c.authuser.id, c.wiki.id )

        c.title   = wurl

        # HTML page generation
        html = ''
        typename = c.wiki.type.wiki_typename
        if c.errmsg :
            html = self.returnerrmsg(environ)

        if c.view == 'js' and c.formname in [ 'addwikiattachs' ] :
            html = IFRAME_RET

        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)

        elif c.view == 'text' and c.textobj :
            html = self.handletext(environ)

        elif typename == h.WIKITYPE_REDIRECT and c.wiki.sourceurl : # Page redirect
            h.redirect_url( c.wiki.sourceurl )

        elif c.wikiedit :
            c.wcnt = wikicomp.get_content( c.wiki );
            c.wikitypenames = wikicomp.typenames
            c.title += ':edit'
            html = render( '/derived/projects/wiki.html' )

        elif c.wtalkpage :
            c.items_wikicomments = self._json_wikicomments()
            c.title += ':talkpage'
            html = render( '/derived/projects/wiki.html' )

        elif c.whistory :
            c.wikicontents = wikicomp.get_content( c.wiki, all=True )
            c.title += ':history'
            html = render( '/derived/projects/wiki.html' )

        elif c.wikidiff :
            v = c.oldver or 1
            c.wcnt_oldver = wikicomp.get_content( c.wiki, version=v )
            c.wcnt_newver = wikicomp.get_content( c.wiki, version=c.newver )
            c.oldver = c.wcnt_oldver.id
            c.newver = c.wcnt_newver.id
            c.title += ':diff'
            html = render( '/derived/projects/wiki.html' )

        elif c.downloadas :
            c.wcnt  = wikicomp.get_content( c.wiki )
            wikihtml = c.wcnt.translate( wiki=c.wiki, cache=True
                       ) if not c.wcnt.texthtml else c.wcnt.texthtml
            fmtobj = h.Html2Doc( wikihtml, format=c.downloadas )
            c.title = '-Skip-'
            html = fmtobj.convert()

            response.headers['Content-disposition'] = \
                str( 'attachment; filename="%s.%s"' % (c.wiki.wikiurl, c.downloadas) )

        elif c.view != 'js' :
            # Refetch the wiki entry from DB with prepared query
            c.attachs = self._wikiattachs( c.wiki )
            c.tags = self._wikitags( c.wiki )
            c.att_editable = c.tag_editable = c.wikieditable
            c.wcnts = wikicomp.get_content( c.wiki, all=True )
            c.wikiauthors = h.computecount( c.wcnts, lambda x : x.author )
            c.wcnt = ( version and c.wcnts[int(version)-1] or c.wcnts[-1]
                     ) if c.wcnts else None
            c.wikitypenames = wikicomp.typenames

            c.wikihtml = ''
            if c.wcnt :
                if not c.wcnt.texthtml :
                    c.wikihtml = c.wcnt.translate(wiki=c.wiki, cache=True)
                elif c.translate :
                    c.wikihtml = c.wcnt.translate(wiki=c.wiki, cache=True)
                else :
                    c.wikihtml = c.wcnt.texthtml

            lastver = c.wiki.latest_version
            fn = lambda v : [ self.url_wikiurl( projectname, wurl, ver=str(v) ),
                              str(v) ]
            c.wversions = map( fn, range( 1, lastver+1 ) )
            c.wdownload = [ [ h.url_wikidownastext, 'as text' ],
                            [ h.url_wikidownasps, 'as post-script' ],
                            [ h.url_wikidownaspdf, 'as pdf' ],
                          ]
            uservote = votcomp.get_wikivote( c.authuser, c.wiki ) 
            votes = wikicomp.countvotes( votes=c.wiki.votes )
            c.upvotes = votes.get( 'up', 0 )
            c.downvotes = votes.get( 'down', 0 )
            c.currvote= uservote and uservote.votedas or ''
            h.url_reviewwiki = self.url_wikireview(
                                    projectname, c.wiki.wikiurl, c.wcnt.id )
            html = render( '/derived/projects/wiki.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'WIKI_VIEW' ]))
    def timelines( self, environ, projectname ) :
        """Aggregate activities under project wiki or individual wiki
        URLS :
            /p/{projectname}/wiki/timeline
        """
        from zeta.config.environment    import projcomp, wikicomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        c.wikipagenames = self.wikipagename( wikicomp.wikiurls( c.project ))
        routeargs  = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projwikistline, routeargs, ['wiki', 'project'],
            fromoff, logid, dir, c.project
        )
        c.title = 'Wiki:timeline'
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.rclose.append(render( '/derived/projects/wikitline.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'WIKI_VIEW' ]))
    def timeline( self, environ, projectname, wurl ) :
        """Aggregate activities under project wiki or individual wiki
        URLS :
            /p/{projectname}/wiki/timeline/*(wurl)
        """
        from zeta.config.environment    import projcomp, wikicomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        wikiurl = self.url_wikiurl( projectname, wurl )
        c.wiki = wikicomp.get_wiki( unicode(wikiurl) )
        c.wikipagenames = self.wikipagename( wikicomp.wikiurls( c.project ))
        c.wikipagename = wurl
        routeargs  = { 'projectname' : projectname, 'wurl' : wurl }
        self.tline_controller(
            h.r_projwikitline, routeargs, 'wiki',
            fromoff, logid, dir, c.wiki
        )
        c.title = '%s:timeline' % wurl
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.rclose.append(render( '/derived/projects/wikitline.html' ))
        return c.rclose

    def feeds( self, environ, projectname ) :
        """Aggregate activities under project wiki or individual wiki
        URLS : 
            /p/{projectname}/wiki/feed
        """
        from zeta.config.environment    import projcomp, wikicomp

        # Setup context for page generation
        title = '%s:wikis' % projectname 
        link = h.urlroot(environ)
        descr = 'Timeline for wikipages, in project %s' % projectname
        c.projsummary = c.project.summary
        feed   = h.FeedGen( title, link, descr )
        routeargs = { 'projectname' : projectname }
        self.tline_controller( 
            h.r_projwikistline, routeargs, ['wiki', 'project'],
            1, None, None, c.project
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, projectname, wurl ) :
        """Aggregate activities under project wiki or individual wiki
        URLS :
            /p/{projectname}/wiki/feed/*(wurl)
        """
        from zeta.config.environment    import projcomp, wikicomp

        # Setup context for page generation
        title = '%s-wiki:%s' % ( projectname, wurl )
        link = h.urlroot(environ)
        descr = 'Timeline for wikipage, %s in project %s' % (wurl, projectname)
        c.projsummary = c.project.summary
        wikiurl = self.url_wikiurl( projectname, wurl )
        c.wiki = wikicomp.get_wiki( unicode(wikiurl) )
        routeargs = { 'projectname' : projectname, 'wurl' : wurl }
        feed   = h.FeedGen( title, link, descr )
        self.tline_controller(
            h.r_projwikitline, routeargs, 'wiki',
            1, None, None, c.wiki
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    _charts = {
        'chart16' : 'wiki-edits',
        'chart17' : 'wiki-votes',
        'chart18' : 'wiki-authors',
        'chart19' : 'wiki-commenters',
        'chart20' : 'wiki-tags',
    }

    @h.authorize( h.HasPermname([ 'WIKI_VIEW' ]))
    def charts( self, environ, projectname ) :
        """Charts and analytics for project wiki
        URLS :
            /p/{projectname}/wiki/charts
            /p/{projectname}/wiki/charts?chartname=<name>
        """
        from zeta.config.environment    import wikicomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.selectedchart = (c.chartname, self._charts[c.chartname])
        c.chartoptions = [ (self.url_wikichart( projectname, name ),
                            text) for name, text in self._charts.iteritems() ]

        c.ta         = ca.get_analyticobj( 'tags' )
        c.wa         = ca.get_analyticobj( 'wiki' )

        if c.chartname == 'chart16' :       # Wiki comments and versions
            c.chart16_data = getattr( c.wa, 'chart16_data', {} 
                                    ).get( c.project.id, [] )
            c.chart16_wiki = getattr( c.wa, 'chart16_wiki', {} 
                                    ).get( c.project.id, [] )

        elif c.chartname == 'chart17' :     # Wiki votes
            c.chart17_data = getattr( c.wa, 'chart17_data', {}
                                    ).get( c.project.id, [] )

        elif c.chartname == 'chart18' :     # Wiki authors
            c.chart18_data = getattr( c.wa, 'chart18_data', {}
                                    ).get( c.project.id, [] )
            c.chart18_usrs = getattr( c.wa, 'chart18_usrs', {}
                                    ).get( c.project.id, [] )

        elif c.chartname == 'chart19' :     # Wiki commentors
            c.chart19_data = getattr( c.wa, 'chart19_data', {}
                                    ).get( c.project.id, [] )
            c.chart19_usrs = getattr( c.wa, 'chart19_usrs', {}
                                    ).get( c.project.id, [] )
        elif c.chartname == 'chart20' :     # Tagged wiki pages
            c.chart20_data = getattr( c.ta, 'chart20_data', {}
                                    ).get( c.project.id, [] )
            c.chart20_tags = getattr( c.ta, 'chart20_tags', {},
                                    ).get( c.project.id, [] )

        c.title = 'WikiCharts'
        c.rclose.append(render( '/derived/projects/wikicharts.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'WIKI_VIEW' ]))
    def attachs( self, environ, projectname ) :
        """Action to present attachment page for wiki pages under project 
        `projectname`
        URLS : 
            p/{projectname}/wiki/attachs
        """
        from zeta.config.environment    import wikicomp, vfcomp

        c.rclose = h.ZResp()
        c.projsummary = c.project.summary
        c.wikipagenames = self.wikipagename( wikicomp.wikiurls( c.project ))
        attachments = wikicomp.attachments( c.project )
        c.attachments = self.attachments( attachments )
        c.editable  = h.authorized( h.HasPermname( 'WIKI_CREATE' ))
        c.title    = 'WikiAttachs'
        c.rclose.append(render( '/derived/projects/wikiattachs.html' ))
        return c.rclose

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers()
