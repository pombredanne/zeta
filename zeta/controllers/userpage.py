# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to handler user related request."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Captcha session management should be refined.
#   2. Implement `forgotpass` action.
#   3. User-Relationship feature is now redefined as Organisation feature.


import logging

from   pylons                    import request, response, session, tmpl_context as c
import simplejson                as json

from   zeta.lib.base             import BaseController, render
from   zeta.config.environment   import tckfilters
from   zeta.lib.constants        import *
import zeta.lib.helpers          as h
import zeta.lib.analytics        as ca

log = logging.getLogger( __name__ )

class UserpageController( BaseController ) :
    """Actions to handle user pages"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

        # Collect the query values into 'context'
        c.stdfilter = request.params.get( 'stdfilter', None )
        c.alphaindex = request.params.get( 'alphaindex', None )
        c.savfilter = request.params.get( 'savfilter', None )
        c.savfilter = c.savfilter and int(c.savfilter)

    def _userphoto( self, u ) :
        return self.modelattachments( u, 'photofile') if u.photofile else {}

    def _usericon( self, u ) :
        return self.modelattachments( u, 'iconfile') if u.iconfile else {}

    def _json_usernames( self, users=[] ) :                 # JSON
        """JSON: { id   : '',
                   label: '',
                   items: [ { usernames: usernames } ]
                 }"""
        from zeta.config.environment import userscomp

        usernames = [ u.username for u in users
                    ] if users else sorted( userscomp.usernames )
        return h.todojoreadstore( [ usernames ], lambda v : { 'usernames': v } )

    @h.authorize( h.ValidUser( strict='True' ))
    def _json_userphoto( self ) :                           # JSON
        """JSON: { id : [ id, url, filename, summary } """
        return json.dumps( self._userphoto( c.authuser ) )


    @h.authorize( h.ValidUser( strict='True' ))
    def _json_usericon( self ) :
        """JSON: { id : [ id, url, filename, summary } """
        return json.dumps( self._usericon( c.authuser ) )


    @h.authorize( h.ValidUser( strict='True' ))
    def _json_userperms( self ) :                           # JSON
        """JSON: { id   : 'username',
                   label: 'username',
                   items: [ { username: username,
                              permissions: permissions,
                              x_permissions: ^permissions },
                            ... ]
                 }"""
        from zeta.config.environment import userscomp

        fn = lambda k, v : { 'username'      : k,   'permissions'   : v[0],
                             'x_permissions' : v[1] },
        x = userscomp.userpermission_map()
        return h.todojoreadstore( x, fn, id='username', label='username' )

    @h.authorize( h.SiteAdmin() )
    def _json_userstatus( self ) :                          # JSON
        """JSON: { id   : 'status',
                   label: 'status',
                   items: [ { status: status, usernames: usernames },
                            ... ]
                 }"""
        from zeta.config.environment import userscomp
        fn = lambda k, v : { 'status' : k, 'usernames' : v }
        x = userscomp.userstatus
        return h.todojoreadstore( x, fn, id='status', label='status' )

    @h.authorize( h.ValidUser( strict='True' ))
    def _json_userconns( self ) :                           # JSON
        """JSON: { id   : '',
                   label: '',
                   items: [ touserrels, fromuserrels, potrels ]
                 }
             touserrels  : { type : [ (tousr, rel.id, approved), ... ], ... }
             fromuserrels: { type : [ (fromsr, rel.id, approved), ... ], ... }
             potrels     : { type : [ [ username, ...], ... }"""
        from zeta.config.environment import userscomp

        json = []
        touserrels, fromuserrels, potrels = userscomp.get_connections( c.authuser
               ) if c.authusername != 'anonymous' else ( [], [], [] )
        fn = lambda rt, val : ( rt, sorted( val, key=lambda x : x[0] ) )

        touserrels = dict( map( fn, touserrels.iteritems() ))
        fromuserrels = dict( map( fn, fromuserrels.iteritems() ))
        potrels = dict([ ( rt, sorted( potrels[rt] ) ) for rt in potrels ])

        return h.todojoreadstore( [ [ touserrels, fromuserrels, potrels ] ],
                                  lambda v : { 'rels' : v } )


    @h.authorize( h.ValidUser( strict='True' ))
    def _json_ticketlist( self ) :                          # JSON-GRID
        """Fetch the json object with caching, under `username`
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
                          age            : age },
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
                'ticketurl'       : self.url_ticket( tup[1], tup[0] ),
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
        filters      = savfilters.get( c.savfilter, {} )
        tcklist      = sorted( tckcomp.ticketlist(
                                            user=c.authuser, filters=filters
                               ).values(),
                               key=lambda l : l[0], reverse=True
                             )
        _tl =  h.todojoreadstore( tcklist,
                                  format_item,
                                  id='id',
                                  label='ticket_id'
                                )
        return _tl


    @h.authorize( h.ValidUser( strict='True' ))
    def index( self, environ ) :
        """Index of all registered users
        URLS :
            /u
            /u?alphaindex=<a>
        """
        from zeta.config.environment import userscomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.users = userscomp.get_user( attrload=[ 'userinfo', 'photofile' ] )
        byindex = {}
        [ byindex.setdefault( u.username[0], [] ).append(u) for u in c.users ]
        c.indexlist = sorted( byindex.keys() )
        if (c.alphaindex == None) and (len(c.users) > h.MAX2SWITCH_ALPHAINDEX) :
            c.alphaindex = c.indexlist[0]
        if c.alphaindex :
            c.users = byindex[c.alphaindex]
        c.urlusersphoto = dict([
            ( u.id, h.url_attach( u.photofile.id ) )
            for u in c.users if u.photofile
        ])
        c.title = 'Users'

        # Html page generation
        if c.jsonobj and c.view == 'js' :
            html = self.handlejson(environ)
        else :
            html = render( '/derived/userpage/usersindex.html' )
        c.rclose.append(html)
        return c.rclose


    @h.authorize( h.ValidUser( strict='True' ))
    def gmap( self, environ ) :
        """all registered users on google map
        URLS :
            /u/gmap
        """
        from zeta.config.environment import userscomp

        c.rclose = h.ZResp()
        # Setup context for page rendering
        c.useraddrs = [ [ u.username, h.useraddress( u.userinfo ) ]
                        for u in userscomp.get_user(attrload=['userinfo'])
                      ]
        c.googlemaps= h.gmapkey( c.sysentries )
        c.title = 'UsersOnGooglemap'

        # Html page generation
        c.rclose.append(render( '/derived/userpage/usersgmap.html' ))
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ))
    def inviteuser( self, environ ) :
        """Invite a new user to join the site
        URLS : 
            /u/inviteuser
            /u/inviteuser?form=submit&formname=inviteuser
        """
        from zeta.config.environment    import vfcomp

        c.rclose = h.ZResp()

        # Authorize: This context attribute should be set before calling the
        # viewcontext() method.
        regrbyinvite = h.str2bool( c.sysentries['regrbyinvite'] )
        invitebyall  = h.str2bool( c.sysentries['invitebyall'] )

        c.usercaninvite = \
               ( regrbyinvite and invitebyall and \
                        h.authorized( h.ValidUser( strict='True' ))  \
               ) or \
               ( regrbyinvite and h.authorized( h.SiteAdmin() ) )

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if c.usercaninvite :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=['inviteuser'], user=c.authuser, environ=environ
            )

        c.title = 'InviteUser'

        # Html page generation
        if c.usercaninvite :
            html = render( '/derived/userpage/inviteuser.html' )
        else :
            html = render( '/derived/userpage/inviteuser.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ))
    def userhome( self, environ, username ) :
        """User Home page
        URLS :
            /u/{username}
            /u/{username}?jsonobj=userphoto&view=js
            /u/{username}?jsonobj=usericon&view=js
        """
        from zeta.config.environment import \
                userscomp, attcomp, projcomp, tckcomp, wikicomp, revcomp, \
                votecomp, tlcomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.username = username
        c.user  = userscomp.get_user( username, 
                                      attrload=[ 'userinfo' ],
                                      attrload_all=[ 'owncomponents.project' ]
                                    )
        votes   = votecomp.uservotes( c.user )
        c.statistics = {
            'uploadedfiles' : len(attcomp.uploadedbyuser( c.user )),
            'votes'         : dict([ ( votedas, len(votes[votedas]) )
                                     for votedas in votes ]),
            'adminprojects' : projcomp.adminprojects( c.user ),
            'inprojects'    : projcomp.userprojects( c.user ),
            'tickets'       : len(tckcomp.usertickets( c.user ).keys()),
            'tckcomments'   : len(tckcomp.usercomments( c.user )),
            'wikicomments'  : len(wikicomp.usercomments( c.user )),
            'authoredrevw'  : len(revcomp.userasauthor( c.user )),
            'modertrevw'    : len(revcomp.userasmoderator( c.user )),
            'particprevw'   : len(revcomp.userasparticipant( c.user )),
            'revwcomments'  : len(revcomp.usercomments( c.user )),
        }
        c.googlemaps = h.gmapkey( c.sysentries )
        c.logs = tlcomp.fetchlogs( 'user', c.user, limit=20 )
        c.useraddr= [ [ username, h.useraddress( c.user.userinfo ) ] ]
        photofile = c.user.photofile
        h.url_userphoto = photofile and self.url_attach(photofile.id)
        c.projecturls = self.projecturls( projcomp.projectnames )
        c.title = username

        # Html page generation
        if c.jsonobj and c.view == 'js' :
            html = self.handlejson(environ)
        else :
            html = render( '/derived/userpage/userhome.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ))
    def preference( self, environ, username, **kwargs ) :
        """Handle user preference
        URLS :
            /u/{username}/preference?form=request
            /u/{username}/preference?form=submit&formname=updateuser&view=js
            /u/{username}/preference?form=submit&formname=updtpass&view=js
            /u/{username}/preference?form=submit&formname=userphoto&view=js
            /u/{username}/preference?form=submit&formname=deluserphoto&view=js
            /u/{username}/preference?form=submit&formname=usericon&view=js
            /u/{username}/preference?form=submit&formname=delusericon&view=js
            /u/{username}/preference?form=submit&formname=adduserrels&view=js
            /u/{username}/preference?form=submit&formname=approveuserrels&view=js
            /u/{username}/preference?form=submit&formname=deluserrels&view=js
        """
        from zeta.config.environment    import vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if c.usercaninvite :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'updateuser', 'updtpass', 'userphoto',
                'deluserphoto', 'usericon', 'delusericon', 'adduserrels',
                'approveuserrels', 'deluserrels' ], user=c.authuser
            )

        # Setup context for page rendering
        uinfo            = c.authuser.userinfo
        c.title          = 'Preference'
        c.photo_editable = c.icon_editable = h.authorized( h.ValidUser( strict='True' ))
        c.photoattach    = self._userphoto( c.authuser )
        c.iconattach     = self._usericon( c.authuser )
        c.googlemaps     = h.gmapkey( c.sysentries )
        c.fulladdress    = h.useraddress( uinfo )

        # Html page generation
        if c.view == 'js' and c.formname in [ 'userphoto', 'usericon' ] :
            html = IFRAME_RET
        else :
            html = render( '/derived/userpage/preference.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ))
    def tickets( self, environ, username ) :
        """List tickets belonging to user (attributed as owner and/or
        promptuser
        URLS :
            /u/{username}/t
            /u/{username}/t?stdfilter=<name>
            /u/{username}/t?savfilter=<name>
            /u/{username}/t?form=submit&formname=addtckfilter&view=js
            /u/{username}/t?form=submit&formname=deltckfilter&view=js
        """
        from zeta.config.environment    import projcomp, tckcomp, vfcomp

        c.rclose = h.ZResp()

        # Setting up urls to be stuffed into the page
        kwargs = { 'username' : username }
        c.stdfilter and kwargs.update({ 'stdfilter' : c.stdfilter })
        c.savfilter and kwargs.update({ 'savfilter' : c.savfilter })
        h.url_ticketlist = self.url_usrtcks( **kwargs )

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if c.form in [ 'request', 'submit' ] and \
           c.formname in [ 'addtckfilter', 'deltckfilter' ] and \
           h.authorized( h.UserIn([ username ]) ) :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'addtckfilter', 'deltckfilter' ], user=c.authuser
            )

        # Setup context for both html page and AJAX request.
        c.tckfilters = h.compile_tckfilters( tckfilters )
        c.title = '%s:tickets' % c.authuser.username

        # HTML page generation
        if c.jsonobj and c.view == 'js' :
            html = self.handlejson(environ)

        elif c.view != 'js' and not (c.stdfilter or c.savfilter) and c.tckfilters :
            kw = { 'username' : username, 'stdfilter' : c.tckfilters[0][0] }
            h.redirect_url( self.url_usrtcks( **kw ))

        elif c.view != 'js' :
            # Setup context for html page
            c.tckeditable = False
            c.tckccodes = h.tckccodes
            c.tstat_resolv = h.parse_csv( c.sysentries.get( u'ticketresolv', '' ))

            c.tck_typenames = tckcomp.tcktypenames
            c.tck_statusnames = tckcomp.tckstatusnames
            c.tck_severitynames = tckcomp.tckseveritynames
            c.projectnames = projcomp.projectnames

            userfilters     = tckcomp.get_ticketfilter( user=c.authuser )
            fn = lambda tf : ( tf.id, [ tf.name, tf.filterbyjson ] )
            c.savfilterlist = dict( map( fn, userfilters ))
            c.savfilterval = c.savfilterlist.get( c.savfilter, ['', ''] )
            c.savfiltername = c.savfilterval[0]
            fn = lambda k, v = [ self.url_usrtcks(**{'username' : username, 'savfilter' : k })
                                 v[0] ]
            c.savfilterlist = map( fn, c.savfilterlist.iteritems() )
            html = render( '/derived/userpage/ticket.html' )

        else :
            html =''

        c.rclose.append(html)
        return c.rclose

    _userscharts = {
        'chart8'  : 'user activity',
        'chart9'  : 'user-site-permissions',
        'chart10' : 'project-administrators',
        'chart11' : 'component-owners',
    }

    @h.authorize( h.ValidUser( strict='True' ))
    def charts( self, environ ) :
        """Charts for combined users
        URLS :
            /u/charts
            /u/charts?chartname=<name>
        """
        from zeta.config.environment import userscomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.chartname = c.chartname or 'chart8'
        c.selectedchart = (c.chartname, self._userscharts[c.chartname])
        c.chartoptions = [ (self.url_userschart(name), text)
                           for name, text in self._userscharts.iteritems() ]

        c.ua     = ca.get_analyticobj( 'users' )

        if c.chartname == 'chart8' :    # User activity
            c.chart8_data  = getattr( c.ua, 'chart8_data', [] )
        elif c.chartname == 'chart9' :  # User site-permission
            c.chart9_data  = getattr( c.ua, 'chart9_data', [] )
        elif c.chartname == 'chart10' : # project administrators
            c.chart10_data = getattr( c.ua, 'chart10_data', [] )
        elif c.chartname == 'chart11' : # Component owners
            c.chart11_data = getattr( c.ua, 'chart11_data', [] )
            c.chart11_ccnt = getattr( c.ua, 'chart11_ccnt', [] )

        c.title = 'Users:Charts'

        # Html page generation
        c.rclose.append(render( '/derived/userpage/userscharts.html' ))
        return c.rclose

    _usercharts = {
        'chart12'  : 'project activities',
    }

    @h.authorize( h.ValidUser( strict='True' ))
    def usercharts( self, environ, username='' ) :
        """User charts
        URLS :
            /u/{username}/charts
            /u/{username}/charts?chartname=<name>
        """
        from zeta.config.environment import userscomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.chartname = c.chartname or 'chart12'
        c.selectedchart = (c.chartname, self._usercharts[c.chartname])
        c.chartoptions = [ (self.url_userschart(name), text)
                           for name, text in self._usercharts.iteritems() ]

        c.user = userscomp.get_user( unicode(username) )
        c.ua   = ca.get_analyticobj( 'users' )

        data   = getattr( c.ua, 'chart12_data', {} ).get(
                          c.user.id, [ c.user.id, c.user.username, [] ] )
        c.chart12_data = data
        c.title   = '%s:Charts' % username

        # Html page generation
        c.rclose.append(render( '/derived/userpage/usercharts.html' ))
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ))
    def timelines( self, environ ) :
        """User timelines
        URLS :
            /u/timeline
        """
        from zeta.config.environment import userscomp

        c.rclose = h.ZResp()

        # Action specific query parameters
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.user = None
        self.tline_controller(
            h.r_userstline, {}, 'user', fromoff, logid, dir, c.user
        )
        c.title = 'Users:timeline'
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.timeline = True

        # Html page generation
        c.rclose.append(render( '/derived/userpage/usertline.html' ))
        return c.rclose

    @h.authorize( h.ValidUser( strict='True' ))
    def timeline( self, environ, username ) :
        """User timeline
        URLS :
            /u/timeline/{username}
        """
        from zeta.config.environment import userscomp

        c.rclose = h.ZResp()

        # Action specific query parameters
        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        c.user = userscomp.get_user( username )
        self.tline_controller(
            h.r_usertline, { 'username' : username }, [ 'user' ],
            fromoff, logid, dir, c.user
        )
        c.title   = '%s:timeline' % username
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )
        c.timeline = True

        # Html page generation
        c.rclose.append(render( '/derived/userpage/usertline.html' ))
        return c.rclose

    def feeds( self, environ ) :
        """Feed for user timeline
        URLS :
            /u/feed
        """
        from zeta.config.environment import userscomp

        title = 'UsersTimeline'
        link = h.urlroot(environ)
        descr = 'Timeline for all users'
        c.user = None
        feed   = h.FeedGen( title, link, descr )
        self.tline_controller( h.r_userstline, {}, 'user', 1, None, None, c.user )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, username ) :
        """Feed for user timeline
        URLS :
            /u/feed/{username}
        """
        from zeta.config.environment import userscomp

        title = '%s:timeline' % c.user.username
        link = h.urlroot(environ)
        descr = 'Timeline for user %s' % c.user.username
        c.user = userscomp.get_user( username )
        feed   = h.FeedGen( title, link, descr )
        self.tline_controller( 
            h.r_usertline, { 'username': username },
            'user', 1, None, None, c.user
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers() # Genering, app-level after-controller handler
