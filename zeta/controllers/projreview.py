# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage project reviews"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

import logging
import datetime                as dt
from   os.path                 import basename, join, splitext

from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config
import simplejson              as json

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
import zeta.lib.analytics      as ca
from   zeta.lib.constants      import *
import zeta.lib.vcsadaptor     as va

log       = logging.getLogger(__name__)

revwperm  = dict([
    ( formname, h.HasPermname( 'REVIEW_CREATE' ) )
    for formname in [ 'createrev', 'configrev', 'revwauthor', 'revwmoderator',
                      'addparts', 'delparts', 'closerev', 'addrevtags',
                      'delrevtags', 'addrevattachs', 'delrevattachs' ]
])

resurlname = lambda parts : '/'.join( (['...'] if parts[-5:-4] else []) \
                                      + parts[-4:] )


class ProjreviewController(BaseController):
    """Class to handle review page request"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )
        c.mainnavs = mainnav( c.projectname, c.controllername )

        # Collect the query values into 'context'
        c.withsource = request.params.get( 'withsource', None )
        c.position = request.params.get( 'position', None )
        c.project = projcomp.get_project(
                            c.projectname,
                            attrload=[ 'admin', 'logofile', 'reviewsets' ]
                    )
        c.revwopts = revcomp.reviewopts( c.project )
        c.revwlist = [[ self.url_revwid( c.project.projectname, rid ),
                        resurlname( resource_url.split('/') )
                      ] for rid, resource_url in c.revwopts ]
        c.rsetlist = [[ self.url_rsetid( c.project.projectname, rs.id ),
                        rs.name
                      ] for rs in c.project.reviewsets ]
        c.prjlogo = c.project and c.project.logofile and \
                    self.url_attach( c.project.logofile.id )
        c.review = revcomp.get_review( 
                        int(c.revwid),
                        attrload=[ 'tags', 'attachments',
                                    'author', 'moderator', 'participants',
                                 ]
                   ) if c.revwid else None

        c.searchproject = [( 'project', c.projectname )]
        c.searchfaces = [ ( 'project', c.projectname ), ( 'review', '1' ) ]

    def formpermission( self ) :
        return ( c.form == 'submit'
               ) and ( c.formname in revwperm 
               ) and ( not h.authorized( revwperm[c.formname] ) )

    def _revwattachs( self, review ) :
        """For JSON consumption.
        Massage the review attachments"""
        return self.modelattachments( review )

    def _revwtags( self, review ) :
        """For JSON consumption.
        Massage the review tags"""
        return self.modeltags( review )

    def _revwrcomments( self ) :
        """JSON: { review_comment_id : 'review_comment_id',
                   review_comment_id : 'review_comment_id',
                   items: [ { review_comment_id : rcmt.id,
                              position          : rcmt.position,
                              text              : rcmt.text,
                              html              : rcmt.texthtml,
                              commentby         : rcmt.commentby.username ,
                              commentbyurl      : userurl,
                              nature            : rcmt.nature.naturename,
                              action            : rcmt.action.actionname,
                              approved          : rcmt.approved
                              replies           : []
                              datestr           : rcmt.created_on },
                            ... ]
                 }"""
        from zeta.config.environment    import revcomp

        def format_item( tup ) :
            d = {
                'review_comment_id' : tup[0],
                'position'          : tup[1],
                'text'              : tup[2],
                'html'              : tup[3],
                'commentby'         : tup[6],
                'commentbyurl'      : self.url_user( tup[6] ),
                'nature'            : tup[7] or '',
                'action'            : tup[8] or '',
                'approved'          : tup[4],
                'datestr'           : h.utc_2_usertz(
                                         tup[5], c.authuser.timezone
                                      ).strftime( '%d %b %Y'),
            }
            return d

        c.position = int(c.position) if c.position else None
        rcomments = revcomp.reviewrcomments( c.review ).values()
        items = []
        while rcomments :
            rcomment = rcomments.pop( 0 )
            d_rcmt = format_item( rcomment )
            d_rcmt.setdefault(
                'replies',
                [ format_item( rrcomment ) for rrcomment in rcomment[-1] ]
            )
            if c.position != None and d_rcmt['position'] != c.position :
                continue
            items.append(d_rcmt)

        json = h.todojoreadstore(
                            items,
                            lambda v : v,
                            id='review_comment_id',
                            label='review_comment'
               )
        return json, items

    @h.authorize( h.HasPermname( 'REVIEW_VIEW' ))
    def _json_revwlist( self ) :                             # JSON
        """JSON: { id   : 'id',
                   label: 'review_id',
                   items: [ { 'id'           : r.id,
                              'href'         : href,
                              'resource_url' : r.resource_url,
                              'reviewset'    : r.reviewset.name,
                              'rshref'       : href,
                              'version'      : r.version,
                              'author'       : r.author.username,
                              'moderator'    : r.moderator.username,
                              'comments'     : comments,
                              'olderby'      : olderby }
                            ... ]
                 }"""
        from zeta.config.environment    import revcomp

        def format_item( tup ) :
            p = c.project.projectname
            olderby = dt.datetime.utcnow().toordinal() - tup[7].toordinal()
            d = {
                'id'            : tup[0],
                'href'          : self.url_revwid( p, tup[0] ),
                'resource_url'  : tup[1],
                'reviewset'     : tup[2] or '',
                'rshref'        : self.url_rsetid( p, tup[3] ) if tup[3] else '',
                'version'       : tup[4],
                'author'        : tup[5],
                'moderator'     : tup[6],
                'comments'      : revcomp.countcomments( tup[0] ),
                'olderby'       : h.olderby( olderby ),
            }
            return d

        return h.todojoreadstore( revcomp.reviewlist( c.project ).values(),
                                  format_item,
                                  id='id',
                                  label='vcs_id'
                                )

    @h.authorize( h.HasPermname( 'REVIEW_VIEW' ))
    def _json_revwattach( self ) :                          # JSON
        """JSON: { id : [ id, url, filename, summary ], ... } """
        return json.dumps( self._revwattachs(c.review) )

    @h.authorize( h.HasPermname( 'REVIEW_VIEW' ))
    def _json_revwtag( self ) :                             # JSON
        """JSON: { tagname : tagname, ... } """
        return json.dumps( self._revwtags(c.review) )

    @h.authorize( h.HasPermname( 'REVIEW_VIEW' ))
    def _json_revwrcomments( self ) :                       # JSON
        """JSON: { review_comment_id : 'review_comment_id',
                   review_comment_id : 'review_comment_id',
                   items: [ { review_comment_id : rcmt.id,
                              position          : rcmt.position,
                              text              : rcmt.text,
                              html              : rcmt.texthtml,
                              commentby         : rcmt.commentby.username ,
                              commentbyurl      : userurl,
                              nature            : rcmt.nature.naturename,
                              action            : rcmt.action.actionname,
                              approved          : rcmt.approved
                              replies           : []
                              datestr           : rcmt.created_on },
                            ... ]
                 }"""
        _json, items = self._revwrcomments()
        return _json

    @h.authorize( h.HasPermname( 'REVIEW_VIEW' ))
    def index( self, environ, projectname ):
        """List all project review
        URLS :
            /p/{projectname}/r
            /p/{projectname}/r?jsonobj=revwlist&view=js
            /p/{projectname}/r?form=submit&formname=configrev&view=js
            /p/{projectname}/r?form=submit&formname=revwauthor&view=js
            /p/{projectname}/r?form=submit&formname=revwmoderator&view=js
            /p/{projectname}/r?form=submit&formname=closerev&view=js
            /p/{projectname}/r?form=submit&formname=addparts&view=js
            /p/{projectname}/r?form=submit&formname=delparts&view=js
            /p/{projectname}/r?form=submit&formname=addrevattachs&view=js
            /p/{projectname}/r?form=submit&formname=delrevattachs&view=js
            /p/{projectname}/r?form=submit&formname=addrevtags&view=js
            /p/{projectname}/r?form=submit&formname=delrevtags&view=js
        """
        from zeta.config.environment    import projcomp, vfcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % revwperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'configrev', 'revwauthor', 'revwmoderator',
                            'addparts', 'delparts', 'closerev',
                            'addrevattachs', 'delrevattachs', 'addrevtags',
                            'delrevtags' ], 
                user=c.authuser
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.revweditable = h.authorized( h.HasPermname( 'REVIEW_CREATE' ))
        c.title = '-Skip-' if c.form == 'submit' else 'Review:list' 

        # HTML page generation
        html = ''
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.view == 'js' and c.formname in [ 'addrevattachs' ] :
            html = IFRAME_RET

        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)

        elif c.view != 'js' :
            c.projusers = self.projusers(c.project)
            html = render( '/derived/projects/reviewindex.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'REVIEW_CREATE' ))
    def create( self, environ, projectname ) :
        """Create a new project review
        URLS : 
            /p/{projectname}/r/createrevw?form=request&formname=createrev
            /p/{projectname}/r/createrevw?form=submit&formname=createrev
        """
        from zeta.config.environment import projcomp, userscomp, vcscomp, vfcomp

        cfok = lambda cf : ( cf['mime_type'] != 'text/directory' ) and \
                           ( cf['changetype'] != 'deleted' )

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=[ 'createrev' ], user=c.authuser
        )

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.projusers = self.projusers( c.project )
        c.usernames = sorted( userscomp.usernames )
        c.rsets = [ [ rs.id, rs.name ] for rs in c.project.reviewsets ]
        c.forsrc = request.params.getall( 'rurl' )
        c.forversion = request.params.get( 'ver', None )
        c.forversion = int(c.forversion) if c.forversion != None else None
        vcsid = request.params.get( 'vcsid', None )
        c.vcs = vcsid and vcscomp.get_vcs( int(vcsid) )
        c.vrep = c.vcs and va.open_repository( c.vcs )
        c.title        = 'CreateReview'
        if c.vrep :
            c.changedfiles = c.vrep.changedfiles(
                                    c.vcs.rooturl, revstart=c.forversion-1,
                                    revend=c.forversion
                             )
            c.forsrc = [
                join( c.vcs.rooturl, cf['repos_path'].lstrip('/') )
                for cf in c.changedfiles if cfok(cf) 
            ]


        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.form == 'submit' and c.formname == 'createrev' :
            # Skip breadcrumbing, if it is a form submit
            c.title = '-Skip-'
            h.redirect_url( h.url_revwcreate )

        else :
            html = render( '/derived/projects/reviewcreate.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'REVIEW_VIEW' ))
    def review( self, environ, projectname, revwid ) :
        """Create a new project review
        URLS : 
            /p/{projectname}/r/{rewid}
            /p/{projectname}/r/{rewid}?withsource=1
            /p/{projectname}/r/{rewid}?jsonobj=revwattach&view=js
            /p/{projectname}/r/{rewid}?jsonobj=revwtag&view=js
            /p/{projectname}/r/{rewid}?jsonobj=revwrcomments&view=js
            /p/{projectname}/r/{rewid}?form=submit&formname=creatercmt&view=js
            /p/{projectname}/r/{rewid}?form=submit&formname=replyrcmt&view=js
            /p/{projectname}/r/{rewid}?form=submit&formname=processrcmt&view=js
            /p/{projectname}/r/{rewid}?form=submit&formname=revwfav&view=js
            /p/{projectname}/r/{rewid}?form=submit&formname=closerev&view=js
        """
        from zeta.config.environment import userscomp, projcomp, revcomp, vfcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % revwperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'creatercmt', 'replyrcmt', 'processrcmt',
                            'revwfav', 'closerev' ], 
                user=c.authuser
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        if not c.jsonobj :
            c.projusers = self.projusers( c.project )
            c.usernames = userscomp.usernames
            c.naturenames = revcomp.naturenames
            c.actionnames = revcomp.actionnames
            c.revweditable = c.att_editable = c.tag_editable = h.authorized(
                    h.HasPermname( 'REVIEW_CREATE' )
            )
            commentors = [ c.review.participants ] + [ c.review.author, c.review.moderator ]
            c.revwcmtable = c.authuser in commentors
            c.revwmoderated = c.authuser == c.review.moderator
            c.revwauthored = c.authuser == c.review.author
            c.title = 'Review:%s' % revwid
            c.isuserfavorite = revcomp.isfavorite( c.authuser.id, c.review.id )

        c.revwsource = None
        if c.withsource :
            c.revwsource, c.sourcediff = revcomp.guess_revwsource( c.review )
            c.diffsec = c.sourcediff and c.sourcediff.pop(0)
            c.diffpri = c.sourcediff and c.sourcediff.pop(0)

        c.attachs = self._revwattachs( c.review )
        c.tags = self._revwtags( c.review )

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.jsonobj and c.view == 'js' :
            html = self.returnerrmsg(environ)

        elif c.view != 'js' :
            c.items_revwrcomments, items = self._revwrcomments()
            c.cnt_comments = len(items)
            c.cnt_pending = len( filter( lambda x : not x['approved'], items ))
            if c.revwsource :
                c.cmtsatpos = [ d['position'] for d in items ]
                html = render( '/derived/projects/reviewsource.html' )
            else :
                html = render( '/derived/projects/review.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'REVIEW_VIEW' ]))
    def reviewsets( self, environ, projectname ) :
        """Review set
        URLS :
            /p/{projectname}/rset
            /p/{projectname}/rset?form=submit&formname=createrset&view=js
            /p/{projectname}/rset?form=submit&formname=updaterset&view=js
            /p/{projectname}/rset?form=submit&formname=addtorset&view=js
            /p/{projectname}/rset?form=submit&formname=delfromrset&view=js
        """
        from zeta.config.environment    import userscomp, revcomp, vfcomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % revwperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'createrset', 'updaterset', 'addtorset', 'delfromrset' ], 
                user=c.authuser
            )

        c.projsummary = c.project.summary
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.view == 'js' :
            html = ''

        else :
            c.reviewsets = c.project.reviewsets
            c.title = '%s:reviewsets' % projectname
            html = render( '/derived/projects/reviewset.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'REVIEW_VIEW' ]))
    def reviewset( self, environ, projectname, rsetid='' ) :
        """Review set
        URLS :
            /p/{projectname}/rset/{rsetid}
        """
        from zeta.config.environment    import userscomp, revcomp, vfcomp

        c.rclose = h.ZResp()

        c.projsummary = c.project.summary
        c.reviewset = revcomp.get_reviewset(
                                int(rsetid),
                                attrload=[ 'reviews' ],
                                attrload_all=[ 'reviews.author',
                                               'reviews.moderator',
                                               'reviews.participants',
                                               'reviews.comments',
                                             ]
                      )
        c.reviews = revcomp.addabletorset(c.project, c.reviewset)
        c.revwloner = [ [ r[0], resurlname( r[1].split('/') ) ]
                        for r in c.reviews ]
        c.revwinrset = [ [ r.id, resurlname( r.resource_url.split('/') ) ]
                         for r in c.reviewset.reviews ]
        c.title = 'reviewset:%s' % c.reviewset.name
        c.rclose.append(render( '/derived/projects/reviewset.html' ))
        return c.rclose


    _charts = {
        'chart27' : 'reviewers',
    }

    @h.authorize( h.HasPermname([ 'REVIEW_VIEW' ]))
    def charts( self, environ, projectname ) :
        """Charts and analytics for project tickets
        URLS : 
            /p/{projectname}/r/charts
        """

        c.rclose = h.ZResp()

        # Setup context for html page
        c.projsummary = c.project.summary
        c.chartname = c.chartname or 'chart27'
        c.selectedchart = (c.chartname, self._charts[c.chartname])
        fn = lambda n, t : ( self.url_revwchart(projectname, n), t)
        c.chartoptions = map( fn, self._charts.iteritems() )
        c.ra  = ca.get_analyticobj( 'reviews' )

        if c.chartname == 'chart27' :
            # Pie chart of reviewers
            c.chart27_data = getattr( c.ra, 'chart27_data', {}
                                    ).get( c.project.id, [] )
            c.chart27_usrs = getattr( c.ra, 'chart27_usrs', {}
                                    ).get( c.project.id, [] )

        c.title    = 'ReviewCharts'
        c.rclose.append(render( '/derived/projects/reviewcharts.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'REVIEW_VIEW' ]))
    def attachs( self, environ, projectname ) :
        """Action to present attachment page for reviews under project 
        `projectname`
        URLS :
            /p/{projectname}/r/attachs
        """
        from zeta.config.environment    import revcomp, vfcomp

        c.rclose = h.ZResp()

        # Setup context for html page
        c.projsummary = c.project.summary
        attachments  = revcomp.attachments( c.project )
        c.attachments = self.attachments( attachments )
        c.editable = h.authorized( h.HasPermname( 'REVIEW_CREATE' ))
        c.title = 'ReviewAttachs'
        c.rclose.append(render( '/derived/projects/revwattachs.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'REVIEW_VIEW' ]))
    def timelines( self, environ, projectname ) :
        """Aggregate activities under project review or individual review
        URLS :
            /p/{projectname}/r/timeline
        """
        from zeta.config.environment    import projcomp, revcomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        c.revweditable = h.authorized( h.HasPermname( 'REVIEW_CREATE' ))
        routeargs = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projrevwtlines, routeargs, ['review', 'project'],
            fromoff, logid, dir, c.project
        )
        c.title = 'Review:timeline'
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.rclose.append(render( '/derived/projects/reviewtline.html' ))
        return c.rclose


    @h.authorize( h.HasPermname([ 'REVIEW_VIEW' ]))
    def timeline( self, environ, projectname, revwid='' ) :
        """Aggregate activities under project review or individual review
        URLS :
            /p/{projectname}/r/timeline/{revwid}
        """
        from zeta.config.environment    import projcomp, revcomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        c.review = revwid and revcomp.get_review( int(revwid) ) or None
        c.revweditable = h.authorized( h.HasPermname( 'REVIEW_CREATE' ))
        routeargs = { 'projectname' : projectname,  'revwid' : revwid }
        self.tline_controller(
            h.r_projrevwtline, routeargs, 'review',
            fromoff, logid, dir, c.review
        )
        c.title = 'Review:%s:timeline' % c.review.id
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.rclose.append(render( '/derived/projects/reviewtline.html' ))
        return c.rclose

    def feeds( self, environ, projectname ) :
        """Aggregate activities under project review or individual review
        URLS :
            /p/{projectname}/r/feed
        """

        title = '%s:review' % projectname
        link = h.urlroot(environ)
        descr = 'Timeline for review, in project %s' % projectname
        c.projsummary = c.project.summary
        feed = h.FeedGen( title, link, descr )
        routeargs = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projrevwtlines, routeargs, ['review', 'project'],
            1, None, None, c.project
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml
    
    def feed( self, environ, projectname, revwid='' ) :
        """Aggregate activities under project review or individual review
        URLS :
            /p/{projectname}/r/feed/{revwid}
        """
        from zeta.config.environment    import revcomp

        title = '%s-revw:%s' % ( projectname, revwid )
        link = h.urlroot(environ)
        descr = 'Timeline for review, %s in project %s' % (
                        c.review.resource_url, projectname )
        c.projsummary = c.project.summary
        c.review = revcomp.get_review( int(revwid) ) if revwid else None
        feed   = h.FeedGen( title, link, descr )
        routeargs = { 'projectname' : projectname, 'revwid' : revwid }
        self.tline_controller(
            h.r_projrevwtline, routeargs, 'review', 1, None, None, c.review
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml
    
    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers()
