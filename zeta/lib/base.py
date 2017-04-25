# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""The base Controller API

Provides the BaseController class for subclassing.
"""

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Add special tags into the context `c` in beforecontrollers()

import time

from   pylons.controllers         import WSGIController
from   pylons                     import config
from   pylons.templating          import render_mako as render
from   pylons                     import request, response, session
try :
    from   pylons           import tmpl_context as c
except ImportError :
    import pylons
    pylons.tmpl_context = {}
    from   pylons           import tmpl_context as c

import zeta.lib.helpers          as h
from   zeta.lib.constants        import MAX_BREADCRUMBS
from   zeta.lib.error            import ZetaError
from   zeta.model                import meta
from   zeta.config.environment   import zetaversion, dbversion, zetacreators
import zeta.auth.perm            as permmod

class BaseController(WSGIController):

    ############################# Url constructors ############################

    def url_for_mform( self, *args, **kwargs ) :
        """Generate urls requesting / submitting multiple forms,
        ( with multiple, formname=* query parameters )"""
        formurl = ''
        if 'formname' in kwargs :
            formname = kwargs.pop( 'formname' )
            formurl = h.url_for( *args, **kwargs )
            formurl += '&' + '&'.join([ 'formname=' + fn for fn in formname ])
        return formurl

    def url_forproject( self, projname ) :
        """URL for project `projname` 's home page"""
        return h.url_for( h.r_projecthome, projectname=projname )

    def url_forresetp( self, digest, emailid ) :
        """URL for resetting password, this url will be sent to user's emailid"""
        return h.url_for(
                    h.r_accounts, action='resetpass', digest=digest,
                    form='request', formname='resetpass', emailid=emailid
               )

    def url_userreg( self, digest ) :
        return h.url_for(
                    h.r_accounts, action='newaccount', digest=digest,
                    form='request', formname='createuser'
               )

    def url_attachpages( self ) :
        """URL for index of attachment pages"""
        from zeta.config.environment import attcomp
        maxid = attcomp.latestattachs().id
        url = [
            ( i, h.url_for( h.r_attachments, fromid=i ) )
            for i in range(1, maxid, 100)
        ] if maxid else []
        return url

    def url_attach( self, aid ) :
        return h.url_for( h.r_attachment, id=id )

    def url_attachdownl( self, aid ) :
        return h.url_for( h.r_attachdownl, id=aid )

    def url_attachchart( self, name ) :
        return h.url_for( h.r_attachcharts, chartname=name )

    def url_swiki( self, swurl ) :
        return h.url_for( h.r_staticwiki, swurl=swurl )

    def url_editsw( self, swurl ) :
        url = h.url_for(
                h.r_staticwiki, swurl=swurl, editsw='1',
                form='request', formname='editsw'
              ) if h.authorized( h.HasPermname( 'STATICWIKI_CREATE' )) else ''
        return url

    def suburl_delsw( self, swurl ) :
        url = h.url_for(
                h.r_staticwiki, swurl=swurl,
                form='submit', formname='delsw', delsw='1'
              ) if h.authorized( h.HasPermname( 'STATICWIKI_CREATE' )) else ''
        return url

    def url_forlicense( self, licid ) :
        return h.url_for( h.r_licenseid, licid=licid )

    def url_licchart( self, name ) :
        return h.url_for( h.r_liccharts, chartname=name )

    def url_uplic( self, licid ) :
        url = h.url_for( 
                    h.r_licenseid, licid=licid,
                    form='request', formname='updatelic'
              )
        return url

    def suburl_rmlicid( self, licid ) :
        url = h.url_for(
                    h.r_licenseid, licid=licid, form='submit', formname='rmlic'
              )
        return url

    def url_projindex( self, alphaindex='a' ) :
        return h.url_for( h.r_projects, alphaindex=alphaindex )

    def url_projmountsname( self, p, name ) :
        return h.url_for( h.r_projmounts, projectname=p, name=name )

    def url_projmstn( self, p, mstnid ) :
        return h.url_for( h.r_projmstn, projectname=p, mstnid=mstnid )

    def url_forchmount( self, p, mid ) :
        return h.url_for( h.r_projmounts, projectname=p, changeid=mid )

    def url_mount( self, p, mid, murl ) :
        return h.url_for( h.r_projmount, projectname=p, mid=mid, murl=murl )

    def url_projchart( self, p, name ) :
        return h.url_for( h.r_projcharts, projectname=p, chartname=name )

    def url_ticket( self, p, tckid ) :
        return h.url_for( h.r_projticketid, projectname=p, tckid=tckid )

    def url_tcklist( self, p, **kw ) :
        return h.url_for( r_projtickets, projectname=p, **kw )

    def url_tckchart( self, p, name ) :
        return h.url_for( h.r_projtckcharts, projectname=p, chartname=name )

    def url_revwid( self, p, revwid ) :
        return h.url_for( h.r_projrevwid, projectname=p, revwid=revwid )

    def url_rsetid( self, p, rsetid ) :
        return h.url_for( h.r_projrevwset, projectname=p, rsetid=rsetid )

    def url_revwchart( self, p, name ) :
        return h.url_for( h.r_projrevwcharts, projectname=p, chartname=name )

    def url_revwfile( self, p, url, ver ) :
        url = h.url_for( h.r_projrevwcreate, projectname=p, rurl=url, ver=ver,
                         form='request', formname='createrev'
                       )
        return url

    def url_revwrev( self, p, vcsid, ver ) :
        url = h.url_for( h.r_projrevwcreate, projectname=p, vcsid=vcsid, ver=ver,
                         form='request', formname='createrev'
                       )
        return url 

    def url_vcsbrowse( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsbrowse, projectname=p, vcsid=vcsid, **kw )

    def url_vcsfiledown( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsfiledown, projectname=p, vcsid=vcsid, **kw )

    def url_vcsrev( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsrev, projectname=p, vcsid=vcsid, **kw )

    def url_vcsfile( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsfile, projectname=p, vcsid=vcsid, **kw )

    def url_vcsrevlist( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsrevlist, projectname=p, vcsid=vcsid, **kw )

    def url_vcsdiffdown( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsdiffdown, projectname=p, vcsid=vcsid, **kw )

    def url_vcsdiff( self, p, vcsid, **kw ) :
        return h.url_for( h.r_projvcsdiff, projectname=p, vcsid=vcsid, **kw )

    def url_wikiurl( self, p, wurl, **kw ) :
        return h.url_for( h.r_projwiki, projectname=p, wurl=wurl, **kw )

    def url_wikireview( self, p, url, ver ) :
        return h.url_for( h.r_projrevwcreate, projectname=p, rurl=url, ver=ver,
                          form='request', formname='createrev' )

    def url_wikichart( self, p, name ) :
        return h.url_for( h.r_projwikicharts, projectname=p, chartname=name )

    def url_tag( self, tgnm ) :
        return h.url_for( h.r_tag, tgnm=tgnm )

    def url_users( self, **kw ) :
        return h.url_for( h.r_usershome, **kw )

    def url_userschart( self, name ) :
        return h.url_for( h.r_userscharts, chartname=name )

    def url_user( self, u ) :
        return h.url_for( h.r_userhome, username=u )

    def url_usrtcks( self, **kw ) :
        kw.update({ 'jsonobj' : 'ticketlist', 'view' : 'js' })
        url = h.url_for( h.r_usertickets, **kwargs )
        return url


    ########################### Library methods ##############################

    def tline_controller( self, routename, routeargs, assc_tables, fromoff,
                          logid, dir, modelobj=None ) :
        from zeta.config.environment import tlcomp

        if routename != h.r_projtline :
            c.alllogs  = tlcomp.fetchlogs(
                                assc_tables, modelobj,
                                limit=TLCOUNT+2, id=logid, direction=dir
                         )

        c.logs = c.alllogs[:100]
        c.links = [ '', '', '' ]

        kwargs0 = { 'fromoff' : 1 }
        kwargs0.update( routeargs )
        kwargs1 = { 'logid' : c.logs[0].id,
                    'dir' : 'newer',
                    'fromoff' : (fromoff-TLCOUNT)
                  }
        kwargs1.update( routeargs )
        kwargs2 = { 'logid' : c.logs[-1].id,
                    'dir' : 'older',
                    'fromoff' : (fromoff+TLCOUNT)
                  }
        kwargs2.update( routeargs )

        if fromoff > TLCOUNT :        # Newest
            c.links[0] = h.url_for( routename, **kwargs0 )
            c.links[1] = h.url_for( routename, **kwargs1 )

        if len(c.alllogs) >= TLCOUNT : # Older
            c.links[2] = h.url_for( routename, **kwargs2 )

        c.fromoff = fromoff
        c.tooff = fromoff + len(c.logs)
        return

    def projecturls( self, projectnames ) :
        return dict([ ( p, self.url_forproject(p) ) for p in projectnames ])

    def shortentitle( self,  x ) :
        return (len(x) > 18) and (x[:9] + ".." + x[-7:]) or x

    def dourls( self, environ, projectname=None ) :
        cntlr = c.controllername
        self._staticurls( environ )
        self._userurls( environ )
        if projectname != None :
            self._projecturls( environ, projectname )
        getattr( self, '_url_'+cntlr )(environ)
        return

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()
        
    def returnerrmsg( self, environ ) :
        response.status_int = 400
        return c.errmsg

    def handlejson( self, environ ) :
        c.title = '-Skip-'
        func = getattr( self, '_json_' + c.jsonobj, None )
        return func() if func else ''

    def handletext( self, environ ) :
        c.title = '-Skip-'
        func = getattr( self, '_text_' + c.textobj, None )
        return func() if func else ''

    def modelattachments( self, model, attr='attachments' ) :
        """For JSON consumption.
        Massage the model's attachments, into a dictionary"""
        attachs = getattr( model, attr, [] )
        attachs = attachs if isinstance( attr, list ) else [ attachs ]
        adict   = dict([ ( a.id,
                           [ a.id, 
                             self.url_attachdownl( str(a.id) ),
                             a.filename,
                             a.summary
                           ]
                         ) for a in attachs ])
        return adict

    def modeltags( self, model ) :
        """For JSON consumption.
        Massage the model's tags, into a dictionary"""
        tags = getattr( model, 'tags', [] )
        return dict([ (t.tagname, t.tagname) for t in tags ])

    def attachments( self, attachs ) :
        attachs_ = {}
        for lkey, adict in attachs.iteritems() :
            x = [ [ aid ] + adict[aid][:-1] + [ ', '.join(adict[aid][-1]) ] + \
                  [ self.url_attachdownl( aid ) ]
                  for aid in adict
                ]
            attachs_[ lkey[1] ] = x
        return attachs_

    def feeds( self, link, f, logs ) :
        for l in logs :
            summary, lnk, content = h.log2feed( l )
            f.add_item( summary, '%s%s' % (link, lnk), content,
                        pubdate=l.created_on, unique_id=str(l.id),
                        author_name=l.user.username
                      )
        feedhtml = f.writeString('utf-8')
        return feedhtml

    def projusers( self, p ) :
        users = projcomp.projusernames(p) + [ p.admin.username ]
        users = sorted(list(set(users)))
        return users

    ##########################################################################

    def beforecontrollers( self, environ=None ) :
        """Generic function to be called before all controller actions are called.
        """
        from zeta.config.environment    import syscomp, userscomp

        # ---------- Debug code --------------
        self.starttime = time.time()
        # ---------- Debug code --------------

        c.sysentries = syscomp.get_sysentry()
        environ = environ or request.environ
        config['userscomp'] = userscomp

        self._check_badcookie( environ.get( 'multigate.cookie.error', False ))
        self._check_versionconsistency( c.sysentries )
        config.setdefault( 'c', c )
        c.authusername, c.authuser, c.myprojects, c.authorized = \
                                    self._do_usercontext( environ )

        # Routes map
        routes_map = config['routes.map']
        c.pathinfo = request.environ['PATH_INFO']
        c.routes_d, c.routesobj = routes_map.routematch( c.pathinfo )

        # Initialize context 
        c.zetalink = 'http://discoverzeta.com'

        c.title = config['zeta.sitename']
        c.sitelogo = config['zeta.sitelogo']
        c.sitename = config['zeta.sitename']
        c.siteadmin = config['zeta.siteadmin']
        c.zetalogo = config['zeta.zetalogo']

        c.welcomestring= c.sysentries.get( 'welcomestring', '' )
        c.zetaversion = zetaversion
        c.zetacreators = zetacreators

        c.form = request.params.get( 'form', None )
        c.formname = request.params.get( 'formname', None )
        c.view = request.params.get( 'view', None )
        c.jsonobj = request.params.get( 'jsonobj', None )
        c.textobj = request.params.get( 'textobj', None )
        c.chartname = request.params.get( 'chartname', None )
        c.stdfilter = request.params.get( 'stdfilter', '' )
        c.savfilter = request.params.get( 'savfilter', '' )
        c.savfilter = c.savfilter and int(c.savfilter)

        c.pathinfo = request.environ['PATH_INFO']
        c.projectname = c.routes_d.get( 'projectname', None )
        c.revwid = c.routes_d.get( 'revwid', '' )
        c.rsetid = c.routes_d.get( 'rsetid', '' )
        c.tckid  = c.routes_d.get( 'tckid', '' )
        c.vcsid  = c.routes_d.get( 'vcsid', '' )
        c.tgnm   = c.routes_d.get( 'tgnm', '' )
        c.wurl   = c.wikiurl = c.routes_d.get( 'wurl', None )
        c.cntlrobj = self
        c.project = None
        c.prjlogo = None
        c.textobj = None
        c.controllername = c.routesobj.defaults['controller']
        c.controlleraction = c.routesobj.defaults['action']

        # Initialize Pemission Mapping System.
        mapmod = eval_import( config['zeta.pmap.module'] )
        permmod.init_pms = eval_import( config['zeta.pmap.mapfunc'] )
        permmod.pms_root = permmod.init_pms( ctxt=c.sysentries )
        permmod.default_siteperms = mapmod.default_siteperms
        permmod.default_projperms = mapmod.default_projperms

        # Clean up breadcrumb, when the user is not authenticated.
        multigate_cookie = request.cookies.get( 'multigate', '' )
        if not multigate_cookie :
            session['breadcrumbs'] = []

        return

    def aftercontrollers( self ) :
        """Generic function to be called after all the controller actions are
        called."""
        # Manage breadcrumbs for session, if the c.title contains '-Skip-', then
        # the title will not be bread-crumbed.
        bd = session.get( 'breadcrumbs', [] )
        if ( c.view != 'js' ) and not c.jsonobj and c.title and c.title != '-Skip-' :
            title = self.shortentitle(c.title)
            bd = filter( lambda x : x[0] != title, bd )
            bd.insert( 0, ( title, request.url  ))
            session['breadcrumbs'] = bd[:MAX_BREADCRUMBS]
        session.save()
        if config['debug'] :
            print "************ %s" % request.url
            print time.time() - self.starttime
            print


    def _check_badcookie( self, cookie_error ) :              # Check for BAD COOKIE
        if cookie_error :
            errmsg = 'Cookie timeout'  \
                     if environ.get( 'multigate.cookie.timeout', False ) \
                     else 'Reason not known !'
            h.flash( '%sBad Cookie : %s' % ( ERROR_FLASH, errmsg ))
            h.redirect_to( h.r_accounts, action='signin' )


    def _check_versionconsistency( self, se ) :
        """Check whether application versions match with database versions"""
        if 'zeta.testmode' in config :
            return

        # Check for version consistency
        if se['product_version'] != zetaversion :
            errmsg = 'db : ( %s ), app : ( %s ), ' % \
                               ( se['product_version'], zetaversion )
            raise ZetaError( 'Inconsistent product version, ' + errmsg )

        if se['database_version'] != dbversion :
            errmsg = 'db : ( %s ), app : ( %s ), ' % \
                               ( se['database_version'], dbversion )
            raise ZetaError( 'Inconsistent database version, ' + errmsg )

    def _do_usercontext( self, environ ) :
        """Gather signed in user details and populate the context"""
        userscomp = config['userscomp']
        if 'REMOTE_USER' in environ :
            authusername = environ['REMOTE_USER']
            authuser = userscomp.get_user( authusername,
                                           attrload=[ 'userinfo' ] )
            myprojects = h.myprojects( authuser ) # user's projects
            authorized = True

        else :
            authusername = 'anonymous'
            authuser = userscomp.get_user( authusername )
            myprojects = []
            authorized = False
        return authusername, authuser, myprojects, authorized

    def _staticurls( self, environ ) :
        """Static urls that are created that are created just once."""

        if hasattr( h, 'url_sitehome' ) :
            return

        h.url_sitehome = h.urlroot(environ)
        h.suburl_searchzeta = h.url_for(
            h.r_searchpage
        )

        # Projects menu urls
        h.url_createprj = h.url_for(
            h.r_projcreate, form='request', formname='createprj'
        )
        h.url_projindex = h.url_for(
            h.r_projects
        )
        # Quick links menu urls
        h.url_usershome = h.url_for(
            h.r_usershome
        )
        h.url_inviteuser = h.url_for(
            h.r_usersinvite
        )
        # Other common urls
        h.url_attachments = h.url_for(
            h.r_attachments
        )
        h.url_titleindex = h.url_for(
            h.r_titleindex
        )

        # Url for `accounts` controller
        h.url_tos = h.url_for(
            h.r_staticwiki, swurl='tos'
        )
        h.url_signin = h.url_for(
            h.r_accounts, action='signin'
        )
        h.url_signout = h.url_for(
            h.r_accounts, action='signout'
        )
        h.url_register = h.url_for(
            h.r_accounts, action='newaccount',
            form='request', formname='createuser'
        )
        h.url_forgotpass = h.url_for(
            h.r_accounts, action='forgotpass',
            form='request', formname='forgotpass'
        )
        h.suburl_forgotpass = h.url_for(
            h.r_accounts, action='forgotpass',
            form='submit', formname='forgotpass'
        )

        # Url for `attachment` controller
        h.url_allattachments = h.url_for(
            h.r_attachments, all='1'
        )
        h.url_attachments = h.url_for(
            h.r_attachments
        )
        h.url_attachcharts = h.url_for(
            h.r_attachcharts
        )
        h.url_attachtline = h.url_for(
            h.r_attachtimeline
        )
        h.url_rssfeed = h.url_for(
            h.r_attachfeeds
        )
        h.url_addattachment = h.url_for(
            h.r_addattchments, form='request', formname='addattachs'
        )
        h.suburl_addattachs = h.url_for(
            h.r_addattchments, form='submit', formname='addattachs'
        )
        h.suburl_attachssummary = h.url_for(
            h.r_attachments, form='submit', formname='attachssummary', view='js'
        )
        h.suburl_attachstags = h.url_for(
            h.r_attachments, form='submit', formname='attachstags', view='js'
        )

        # Url for `staticwiki` controller
        h.url_aboutus = h.url_for(
            h.r_staticwiki, swurl='aboutus'
        )
        h.url_helppages = h.url_for(
            h.r_staticwiki, swurl='help/'
        )

        # Url for `license` controller
        h.url_license = h.url_for(
            h.r_license
        )
        h.url_crlic = h.url_for(
            h.r_liccreate
        )
        h.url_licattachs = h.url_for(
            h.r_licattachs
        )
        h.url_licensecharts = h.url_for(
            h.r_liccharts
        )
        h.suburl_crlic = h.url_for(
            h.r_liccreate, form='submit', formname='createlic'
        )
        h.suburl_rmlic = h.url_for(
            h.r_license, form='submit', formname='rmlic', view='js'
        )

        # Url for `tag` controller
        h.url_tagcloud = h.url_for(
            h.r_tags
        )

        # Url for `projects` controller
        h.suburl_createprj = h.url_for(
            h.r_projcreate, form='submit', formname='createprj'
        )

        # Url for `siteadmin` controller
        h.url_siteadmin = h.url_for(
            h.r_siteadmin, form='request'
        )
        h.url_uploadsitelogo = h.url_for(
            h.r_sitelogo, form='request', formname='sitelogo'
        )
        h.url_sitecharts = h.url_for(
            h.r_sitecharts
        )
        h.url_sitetline = h.url_for(
            h.r_sitetline
        )
        h.url_rssfeed = h.url_for(
            h.r_sitefeeds
        )

        h.suburl_sitelogo = h.url_for(
            h.r_sitelogo, form='submit', formname='sitelogo'
        )
        h.suburl_system = h.url_for(
            h.r_siteadmin, form='submit', formname='system', view='js'
        )
        h.suburl_enusers = h.url_for(
            h.r_siteadmin, form='submit', formname='userenb', view='js'
        )
        h.suburl_disusers = h.url_for(
            h.r_siteadmin, form='submit', formname='userdis', view='js'
        )
        h.suburl_enprojects = h.url_for(
            h.r_siteadmin, form='submit', formname='prjenb', view='js'
        )
        h.suburl_disprojects = h.url_for(
            h.r_siteadmin, form='submit', formname='prjdis', view='js'
        )
        h.suburl_adduserperms = h.url_for(
            h.r_siteadmin, form='submit', formname='adduserperms', view='js'
        )
        h.suburl_deluserperms = h.url_for(
            h.r_siteadmin, form='submit', formname='deluserperms', view='js'
        )
        h.suburl_createpg = h.url_for(
            h.r_siteadmin, form='submit', formname='createpg', view='js'
        )
        h.suburl_updatepg = h.url_for(
            h.r_siteadmin, form='submit', formname='updatepg', view='js'
        )
        h.suburl_addpntopg = h.url_for(
            h.r_siteadmin, form='submit', formname='addpntopg', view='js'
        )
        h.suburl_delpnfrompg = h.url_for(
            h.r_siteadmin, form='submit', formname='delpnfrompg', view='js'
        )

        # Url for `userpage` controller
        h.url_usersgmap = h.url_for(
            h.r_usersgmap
        )
        h.url_userscharts = h.url_for(
            h.r_userscharts
        )

    def _userurls( self, environ ) :
        """Urls that are generated in the context of authenticated user"""
        if c.authorized :
            h.url_userhome = h.url_for(
                h.r_userhome, username=c.authusername
            )
            h.url_mytickets = h.url_for(
                h.r_usertickets,
                username=c.authusername
            )
            h.url_userpref = h.url_for(
                h.r_userpref, username=c.authusername, form='request'
            )
        else :
            h.url_userhome = h.url_sitehome
            h.url_mytickets = h.url_sitehome
            h.url_userpref = h.url_sitehome

        h.quicklinks = [ [ 'users', h.url_usershome ],
                         [ 'invite', h.url_inviteuser ],
                         [ 'mytickets', h.url_mytickets ],
                         [ 'attachments', h.url_attachments ],
                         [ 'title-index', h.url_titleindex ],
                         [ 'mypage', h.url_userhome ],
                       ]
        h.quicklinks_special = []
        if h.authorized( h.HasPermname( 'SITE_ADMIN' )) :
            h.quicklinks_special.append(
                [ 'site-admin', h.url_for(h.r_siteadmin, form='request') ]
            )
        if h.authorized( h.HasPermname( 'LICENSE_VIEW' )) :
            h.quicklinks_special.append([ 'license', h.url_license ])

    def _projecturls( self, environ, projectname ) :
        """Urls that are generated in the context of project"""
        h.projectlinks = [
            [ p, self.url_forproject(p) ] for p in c.myprojects
        ]
        if projectname :
            h.url_projecthome = h.url_for(
                h.r_projecthome, projectname=projectname
            )
            h.url_projectwiki = h.url_for(
                h.r_projwikis, projectname=projectname
            )
            h.url_projectticket = h.url_for(
                h.r_projtickets, projectname=projectname
            )
            h.url_projectvcs = h.url_for(
                h.r_projvcs, projectname=projectname
            )
            h.url_projectreview = h.url_for(
                h.r_projrevw, projectname=projectname
            )
            h.url_projectadmin = h.url_for(
                h.r_projadmin, projectname=projectname, form='request'
            )
        else :
            h.url_projecthome = h.url_sitehome
            h.url_projectwiki = h.url_sitehome
            h.url_projectticket = h.url_sitehome
            h.url_projectvcs = h.url_sitehome
            h.url_projectreview = h.url_sitehome
            h.url_projectadmin = h.url_sitehome

    def _url_accounts( self, environ ) :
        digest = getattr( c, 'digest', None )
        kwargs = { 'digest' : digest } if digest else {}
        h.suburl_userreg = h.url_for(
            h.r_accounts, action='newaccount',
            form='submit', formname='createuser', **kwargs
        )
        h.suburl_resetpass = h.url_for(
            h.r_accounts, action='resetpass',
            emailid=getattr( c, 'emailid', '' ),
            form='submit', formname='resetpass'
        )

    def _url_home( self, environ ) :

        if getattr( c, 'swurl', None ) :
            h.url_swpage = h.url_for(
                h.r_staticwiki, swurl=c.swurl
            )
            h.url_refreshsw = h.url_for(
                h.r_staticwiki, swurl=c.swurl, refresh='1'
            )
            h.suburl_editsw = h.url_for(
                h.r_staticwiki, swurl=c.swurl,
                form='submit', formname='editsw', view='js'
            )
            h.url_editsw = h.url_for(
                h.r_staticwiki, swurl=c.swurl, editsw='1',
                form='request', formname='editsw'
            )
            h.url_swpreview = h.url_for(
                h.r_staticwiki, swurl=c.swurl, textobj='swpreview', view='text'
            )
            h.suburl_delsw = h.url_for(
                h.r_staticwiki, swurl=c.swurl,
                form='submit', formname='delsw', delsw='1'
            )

        h.suburl_search = h.url_for(
            h.r_searchpage, staticwiki='1'
        )

    def _url_attachment( self, environ ) :
        pass

    def _url_license( self, environ ) :
        licid = getattr( c, 'licid', '' )
        h.url_lictimeline = h.url_for(
            h.r_lictimeline, licid=c.licid
        ) if licid else h.url_for( h.r_lictimelines )

        h.url_rssfeed = h.url_for(
            h.r_licfeed, licid=c.licid
        ) if licid else h.url_for( h.r_licfeeds )

        h.url_uplic = h.url_for(
            h.r_licenseid, licid=licid, form='request', formname='updatelic'
        )
        h.url_licattachments = h.url_for(
            h.r_licenseid, licid=licid, jsonobj='licattach', view='js'
        )
        h.url_lictags = h.url_for(
            h.r_licenseid, licid=licid, jsonobj='lictag', view='js'
        )
        h.suburl_uplic = h.url_for(
            h.r_licenseid, licid=licid,
            form='submit', formname='updatelic', view='js'
        )
        h.suburl_rmlicid = h.url_for(
            h.r_licenseid, licid=licid, form='submit', formname='rmlic'
        )
        h.suburl_addlicattachs = h.url_for(
            h.r_licenseid, licid=licid,
            form='submit', formname='addlicattachs', view='js'
        )
        h.suburl_dellicattachs = h.url_for(
            h.r_licenseid, licid=licid,
            form='submit', formname='dellicattachs', view='js'
        )
        h.suburl_addlictags = h.url_for(
            h.r_licenseid, licid=licid,
            form='submit', formname='addlictags', view='js'
        )
        h.suburl_dellictags = h.url_for(
            h.r_licenseid, licid=licid,
            form='submit', formname='dellictags', view='js'
        )
        h.suburl_search = h.url_for(
            h.r_searchpage, license='1'
        )
        #h.suburl_attachssummary = h.url_for(
        #    h.r_licattachs,
        #    form='submit', formname='attachssummary', view='js'
        #)
        #h.suburl_attachstags = h.url_for(
        #    h.r_licattachs,
        #    form='submit', formname='attachstags', view='js'
        #)

    def _url_projcommon( self, environ ) :
        p = c.projectname
        h.url_projmounts = h.url_for(
            h.r_projmounts, projectname=p
        )
        h.url_projattachs = h.url_for(
            h.r_projattachs, projectname=p
        )
        h.url_projdownloads = h.url_for(
            h.r_projdownlds, projectname=p
        )
        h.url_projroadmap = h.url_for(
            h.r_projroadmap, projectname=p
        )
        h.url_projectcharts = h.url_for(
            h.r_projcharts, projectname=p
        )
        h.url_projtimeline = h.url_for(
            h.r_projtline, projectname=p
        )
        h.suburl_search = h.url_for(
            h.r_searchpage
        )

    def _url_projects( self, environ ) :
        self._url_projcommon( environ )
        p = c.projectname
        h.url_projadmtimeline = h.url_for(
            h.r_projadmtline, projectname=p
        )
        h.url_translatefp = h.url_for(
            h.r_projecthome, projectname=p, translate=1
        )

        h.url_prjlrefresh = h.url_for(
            h.r_projecthome, projectname=p, jsonobj='projectlogo', view='js'
        )
        h.url_prjirefresh = h.url_for(
            h.r_projecthome, projectname=p, jsonobj='projecticon', view='js'
        )
        h.url_pcomplist = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='pcomplist', view='js'
        )
        h.url_mstnlist = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='mstnlist', view='js'
        )
        h.url_verlist = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='verlist', view='js'
        )
        h.url_projectteams = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='projectteams', view='js'
        )
        h.url_teamperms = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='teamperms', view='js'
        )
        h.url_prjattachments = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='prjattach', view='js'
        )
        h.url_prjtags = h.url_for(
            h.r_projadmin, projectname=p, jsonobj='prjtag', view='js'
        )
        h.url_projmstns = h.url_for(
            h.r_projmstns, projectname=p
        )

        h.suburl_projectinfo = self.url_for_mform(
            h.r_projadmin, projectname=p,
            form='submit', formname=[ 'updateprj', 'prjexp', 'prjml', 'prjirc' ],
            view='js'
        )
        h.suburl_addprjlogo = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='addprjlogo', view='js'
        )
        h.suburl_delprjlogo = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='delprjlogo', view='js'
        )
        h.suburl_addprjicon = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='addprjicon', view='js'
        )
        h.suburl_delprjicon = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='delprjicon', view='js'
        )
        h.suburl_createpcomp = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='createpcomp', view='js'
        )
        h.suburl_updatepcomp = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='updatepcomp', view='js'
        )
        h.suburl_rmpcomp = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='rmpcomp', view='js'
        )
        h.suburl_createmstn = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='createmstn', view='js'
        )
        h.suburl_updatemstn = self.url_for_mform(
            h.r_projadmin, projectname=p,
            form='submit', formname=[ 'updatemstn', 'mstnclose' ], view='js'
        )
        h.suburl_rmmstn = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='rmmstn', view='js'
        )
        h.suburl_createver = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='createver', view='js' )
        h.suburl_updatever = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='updatever', view='js'
        )
        h.suburl_rmver = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='rmver', view='js'
        )
        h.suburl_addprjteam = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='addprjteam', view='js'
        )
        h.suburl_delprjteam = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='delprjteam', view='js'
        )
        h.suburl_addteamperms = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='addteamperms', view='js'
        )
        h.suburl_delteamperms = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='delteamperms', view='js'
        )
        h.suburl_addprjattachs = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='addprjattachs', view='js'
        )
        h.suburl_delprjattachs = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='delprjattachs', view='js'
        )
        h.suburl_addprjtags = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='addprjtags', view='js'
        )
        h.suburl_delprjtags = h.url_for(
            h.r_projadmin, projectname=p,
            form='submit', formname='delprjtags', view='js'
        )
        h.suburl_projfav = h.url_for(
            h.r_projecthome, projectname=p,
            form='submit', formname='projfav', view='js'
        )
        #h.suburl_attachssummary = h.url_for(
        #    h.r_projattachs, projectname=p,
        #    form='submit', formname='attachssummary', view='js'
        #)
        #h.suburl_attachstags = h.url_for(
        #    h.r_projattachs, projectname=p,
        #    form='submit', formname='attachstags', view='js'
        #)

    def _url_projmount( self, environ ) :
        p = c.projectname
        self._url_projcommon( environ )

        h.url_mountlist = h.url_for(
            h.r_projmounts, projectname=p, jsonobj='mountlist', view='js'
        )

        h.suburl_createmount = h.url_for(
            h.r_projmounts, projectname=p, form='submit', formname='createmount'
        )
        h.suburl_updatemount = h.url_for(
            h.r_projmounts, projectname=p, form='submit', formname='updatemount'
        )
        h.suburl_deletemount = h.url_for(
            h.r_projmounts, projectname=p, form='submit', formname='deletemount'
        )

    def _url_projticket( self, environ ) :
        p = c.projectname
        tckid = c.tckid
        h.url_tckattachs = h.url_for(
            h.r_projtckattachs, projectname=p
        )
        h.url_ticketgraph =  h.url_for(
            h.r_projtidgraph, projectname=p, tckid=tckid, file='graph.svg'
        )
        h.url_tickettree = h.url_for(
            h.r_projtidgraph, projectname=p, tckid=tckid, file='tree.svg'
        )
        h.url_ticketcharts = h.url_for(
            h.r_projtckcharts, projectname=p
        )
        h.url_ticketcreate = h.url_for(
            h.r_projtckcreate, projectname=p, action='createticket',
            form='request', formname='createtck'
        )

        h.url_ticketlist = h.url_for(
            h.r_projtickets, projectname=p,
            stdfilter=c.stdfilter, savfilter=c.savfilter,
            jsonobj='ticketlist', view='js'
        )
        h.url_tckattachments = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            jsonobj='tckattachs', view='js'
        )
        h.url_tcktags = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            jsonobj='tcktags', view='js'
        )
        h.url_tckcomments = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            jsonobj='tckcomments', view='js'
        )
        h.url_tckrcomments = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            jsonobj='tckrcomments', view='js'
        )

        h.suburl_createtck = h.url_for(
            h.r_projtckcreate, projectname=p, action='createticket',
            form='submit', formname='createtck'
        )
        h.suburl_configtck = h.url_for(
            h.r_projtickets, projectname=p,
            form='submit', formname='configtck', view='js'
        )
        h.suburl_configtckst = h.url_for(
            h.r_projtickets, projectname=p,
            form='submit', formname='configtstat', view='js'
        )
        h.suburl_changetckst = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='createtstat', view='js'
        )
        h.suburl_addtckattachs = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='addtckattachs', view='js'
        )
        h.suburl_deltckattachs = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='deltckattachs', view='js'
        )
        h.suburl_addtcktags = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='addtcktags', view='js'
        )
        h.suburl_deltcktags = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='deltcktags', view='js'
        )
        h.suburl_createtcmt = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='createtcmt', view='js'
        )
        h.suburl_updatetcmt = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='updatetcmt', view='js'
        )
        h.suburl_replytcmt = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='replytcmt', view='js'
        )
        h.suburl_tckfav = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='tckfav', view='js'
        )
        h.suburl_votetck = h.url_for(
            h.r_projticketid, projectname=p, tckid=tckid,
            form='submit', formname='votetck', view='js'
        )
        #h.suburl_attachssummary = h.url_for(
        #    h.r_projtckattachs, projectname=p,
        #    form='submit', formname='attachssummary', view='js'
        #)
        #h.suburl_attachstags = h.url_for(
        #    h.r_projtckattachs, projectname=p,
        #    form='submit', formname='attachstags', view='js'
        #)
        h.suburl_search = h.url_for(
            h.r_searchpage
        )
        h.suburl_addtckfilter = h.url_for(
            h.r_projtickets, projectname=p,
            form='submit', formname='addtckfilter', view='js'
        )
        h.suburl_deltckfilter = h.url_for(
            h.r_projtickets, projectname=p,
            form='submit', formname='deltckfilter', view='js'
        )

        h.url_tcktimeline = h.url_for(
            h.r_projtcktline, projectname=p, tckid=tckid
        ) if tckid else h.url_for(
            h.r_projtckstline, projectname=p
        )

        h.url_rssfeed = h.url_for(
            h.r_projtckfeed, projectname=p, tckid=tckid
        ) if tckid else h.url_for(
            h.r_projtcksfeed, projectname=p
        )

    def _url_projreview( self, environ ) :
        p = c.projectname
        revwid = getattr( c, 'revwid', '' )

        h.url_reviewsets = h.url_for(
            h.r_projrevwsets, projectname=p
        )
        h.url_revwattachs = h.url_for(
            h.r_projrevwattachs, projectname=p
        )
        h.url_revwcharts = h.url_for(
            h.r_projrevwcharts, projectname=p
        )
        h.url_revwcreate = h.url_for(
            h.r_projrevwcreate, projectname=p,
            form='request', formname='createrev'
        )

        h.url_revwlist = h.url_for(
            h.r_projrevw, projectname=p, jsonobj='revwlist', view='js'
        )
        h.url_revwattachments = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            jsonobj='revwattach', view='js'
        )
        h.url_revwtags = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            jsonobj='revwtag', view='js'
        )
        h.url_revwrcomments = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            jsonobj='revwrcomments', view='js'
        )

        h.suburl_createrset = h.url_for(
            h.r_projrevwsets, projectname=p,
            form='submit', formname='createrset', view='js'
        )
        h.suburl_updaterset = h.url_for(
            h.r_projrevwsets, projectname=p,
            form='submit', formname='updaterset', view='js'
        )
        h.suburl_addtorset = h.url_for(
            h.r_projrevwsets, projectname=p,
            form='submit', formname='addtorset', view='js'
        )
        h.suburl_delfromrset = h.url_for(
            h.r_projrevwsets, projectname=p,
            form='submit', formname='delfromrset', view='js'
        )
        h.suburl_createrev = h.url_for(
            h.r_projrevwcreate, projectname=p,
            form='submit', formname='createrev'
        )
        h.suburl_configrev = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='configrev', view='js'
        )
        h.suburl_revwauthor = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='revwauthor', view='js'
        )
        h.suburl_revwmoderator = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='revwmoderator', view='js'
        )
        h.suburl_closerev = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='closerev', view='js'
        )
        h.suburl_addparts = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='addparts', view='js'
        )
        h.suburl_delparts = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='delparts', view='js'
        )
        h.suburl_addrevattachs = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='addrevattachs', view='js'
        )
        h.suburl_delrevattachs = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='delrevattachs', view='js'
        )
        h.suburl_addrevtags = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='addrevtags', view='js'
        )
        h.suburl_delrevtags = h.url_for(
            h.r_projrevw, projectname=p,
            form='submit', formname='delrevtags', view='js'
        )
        h.suburl_creatercmt = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            form='submit', formname='creatercmt', view='js'
        )
        h.suburl_replyrcmt = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            form='submit', formname='replyrcmt', view='js'
        )
        h.suburl_processrcmt = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            form='submit', formname='processrcmt', view='js'
        )
        h.suburl_revwfav = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            form='submit', formname='revwfav', view='js'
        )
        h.suburl_closerev = h.url_for(
            h.r_projrevwid, projectname=p, revwid=revwid,
            form='submit', formname='closerev', view='js'
        )
        #h.suburl_attachssummary = h.url_for(
        #    h.r_projrevwattachs, projectname=p,
        #    form='submit', formname='attachssummary', view='js'
        #)
        #h.suburl_attachstags = h.url_for(
        #    h.r_projrevwattachs, projectname=p,
        #    form='submit', formname='attachstags', view='js'
        #)
        h.suburl_search = h.url_for(
            h.r_searchpage
        )

        if revwid :
            h.url_revwtimeline = h.url_for(
                h.r_projrevwtline, projectname=p, revwid=revwid
            )
            h.url_revwwithsource = h.url_for(
                h.r_projrevwid, projectname=p, revwid=revwid,
                withsource=1
            )
            h.url_review = h.url_for(
                h.r_projrevwid, projectname=p, revwid=revwid
            )
            h.url_rssfeed = h.url_for(
                h.r_projrevwfeed, projectname=p, revwid=revwid 
            )
        else :
            h.url_revwtimeline = h.url_for(
                h.r_projrevwtlines, projectname=p
            )
            h.url_rssfeed = h.url_for(
                h.r_projrevwfeeds, projectname=p
            )

    def _url_projvcs( self, environ ) :
        p = c.projectname
        vcsid = getattr( c.vcs, 'id', '' )
        h.url_vcsintegrate = h.url_for(
            h.r_projvcsintegrate, projectname=p,
            form='request', formname='integratevcs'
        )
        h.url_vcsbrowse = h.url_for(
            h.r_projvcsbrowse, projectname=p, vcsid=vcsid
        ) if c.vcsid else ''

        h.url_browseprev = h.url_for(
            h.r_projvcsbrowse, projectname=p, vcsid=vcsid, revno=c.revno_p
        ) if c.vcs and c.revno_p != None else ''
        h.url_browsenext = h.url_for(
            h.r_projvcsbrowse, projectname=p, vcsid=vcsid, revno=c.revno_n
        ) if c.vcs and c.revno_n else ''
        h.url_revprev = h.url_for(
            h.r_projvcsrev, projectname=p, vcsid=vcsid, revno=c.revno_p
        ) if c.vcs and c.revno_p != None else ''
        h.url_revnext = h.url_for(
            h.r_projvcsrev, projectname=p, vcsid=c.vcs.id, revno=c.revno_n
        ) if c.vcs and c.revno_n else ''

        h.url_vcstimeline = h.url_for(
            h.r_projvcstline, projectname=p, vcsid=vcsid
        ) if vcsid else h.url_for(
            h.r_projvcstlines, projectname=p
        )

        h.url_rssfeed = h.url_for(
            h.r_projvcsfeed, projectname=p, vcsid=vcsid
        ) if vcsid else h.url_for(
            h.r_projvcsfeeds, projectname=p
        )

        if c.vrep :
            revno = c.vrep.linfo['l_revision']
            revno = revno - (revno % 100) + 1
            h.url_revlist = h.url_for(
                h.r_projvcsrevlist, projectname=p, vcsid=vcsid, revno=revno
            )

        h.url_vcslist = h.url_for(
            h.r_projvcs, projectname=p, jsonobj='vcslist', view='js'
        )

        h.list_rootdir = h.url_for(
            h.r_projvcsbrowse, projectname=p,
            vcsid=vcsid, repopath=c.vcs.rooturl, revno=c.revno,
            jsonobj='dirlist', view='js'
        ) if c.vcs else ''

        h.suburl_createmount_e = h.url_for(
            h.r_projmounts, projectname=p,
            form='submit', formname='createmount', view='js'
        )
        h.suburl_deletemount_e = h.url_for(
            h.r_projmounts, projectname=p,
            form='submit', formname='deletemount', view='js'
        )
        h.suburl_integratevcs = h.url_for(
            h.r_projvcsintegrate, projectname=p,
            form='submit', formname='integratevcs'
        )
        h.suburl_configvcs = h.url_for(
            h.r_projvcs, projectname=p,
            form='submit', formname='configvcs', view='js'
        )
        h.suburl_vcsfile2wiki = h.url_for(
            h.r_projwikis, projectname=p,
            form='submit', formname='vcsfile2wiki', view='js'
        )
        h.suburl_search = h.url_for(
            h.r_searchpage
        )

    def _url_projwiki( self, environ ) :
        p = c.projectname
        wurl = c.wurl

        h.url_wikipage = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl
        )
        h.url_wikiedit = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, wikiedit='1'
        )
        h.url_wtalkpage = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, wikitalkpage='1'
        )
        h.url_whistory = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, wikihistory='1'
        )
        h.url_wikidiff = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, wikidiff='1'
        )
        h.url_translatewiki = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, translate=1
        )

        h.url_wikitimeline = h.url_for(
            h.r_projwikitline, projectname=p, wurl=wurl
        ) if wurl else h.url_for( h.r_projwikistline, projectname=p )

        h.url_rssfeed = h.url_for(
            h.r_projwikifeed, projectname=p, wurl=wurl
        ) if wurl else h.url_for( h.r_projwikisfeed, projectname=p )

        h.url_wikidownastext = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, downloadas='text'
        )
        h.url_wikidownasps = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, downloadas='ps'
        )
        h.url_wikidownaspdf = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, downloadas='pdf'
        )
        h.url_wikititleindex = h.url_for(
            h.r_projwtindex, projectname=p
        )
        h.url_wikicharts = h.url_for(
            h.r_projwikicharts, projectname=p
        )
        h.url_wikiattachs = h.url_for(
            h.r_projwikiattachs, projectname=p
        )

        h.url_wikilist = h.url_for(
            h.r_projwikis, projectname=p, jsonobj='wikilist', view='js'
        )
        h.url_wikicomments = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            jsonobj='wikicomments', view='js'
        )
        h.url_wikircomments = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            jsonobj='wikircomments', view='js'
        )
        h.url_wikiattachments = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            jsonobj='wikiattach', view='js'
        )
        h.url_wikitags = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, jsonobj='wikitag', view='js'
        )

        h.url_wikipreview = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            textobj='wikipreview', view='text'
        )

        h.suburl_configwiki = h.url_for(
            h.r_projwikis, projectname=p,
            form='submit', formname='configwiki', view='js'
        )
        h.suburl_addwikiattachs = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='addwikiattachs', view='js'
        )
        h.suburl_delwikiattachs = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='delwikiattachs', view='js'
        )
        h.suburl_addwikitags = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='addwikitags', view='js'
        )
        h.suburl_delwikitags = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='delwikitags', view='js'
        )
        h.suburl_wikiedit = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='wikicont', view='js'
        )
        h.suburl_createwcmt = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='createwcmt', view='js'
        )
        h.suburl_updatewcmt = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='updatewcmt', view='js'
        )
        h.suburl_replywcmt = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='replywcmt', view='js'
        )
        h.suburl_wikidiff = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl, wikidiff='1',
            form='submit', formname='wikidiff'
        )
        h.suburl_wikifav = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='wikifav', view='js'
        )
        h.suburl_votewiki = h.url_for(
            h.r_projwiki, projectname=p, wurl=wurl,
            form='submit', formname='votewiki', view='js'
        )
        #h.suburl_attachssummary = h.url_for(
        #    h.r_projwikiattachs, projectname=p,
        #    form='submit', formname='attachssummary', view='js'
        #)
        #h.suburl_attachstags = h.url_for(
        #    h.r_projwikiattachs, projectname=p,
        #    form='submit', formname='attachstags', view='js'
        #)

        h.suburl_search = h.url_for(
            h.r_searchpage
        )


    def _url_siteadmin( self, environ ) :
        pass

    def _url_tag( self, environ ) :
        h.url_tagcloud = h.url_for(
            h.r_tags
        )
        h.url_tagtimeline = h.url_for(
            h.r_tagtline, tgnm=tgnm
        ) if tgnm else h.url_for( h.r_tagstline )
        h.url_rssfeed = h.url_for(
            h.r_tagfeed, tgnm=tgnm
        ) if tgnm else h.url_for( h.r_tagsfeed )

    def _url_userpage( self, environ ) :
        uname = c.username

        h.url_userhome = h.url_for(
            h.r_userhome, username=uname
        )
        h.url_usercharts = h.url_for(
            h.r_usercharts, username=uname
        )

        h.url_usertline = h.url_for(
            h.r_usertline, username=uname,
        ) if uname else h.url_for( h.r_userstline )

        h.url_rssfeed = h.url_for(
            h.r_userfeed, username=uname
        ) if uname else h.url_for( h.r_usersfeed )

        h.url_userprefresh = h.url_for(
            h.r_userhome, username=uname, jsonobj='userphoto', view='js'
        )
        h.url_userirefresh = h.url_for(
            h.r_userhome, username=uname, jsonobj='usericon', view='js'
        )

        h.suburl_addtckfilter = h.url_for(
            h.r_usertickets, username=uname,
            form='submit', formname='addtckfilter', view='js'
        )
        h.suburl_deltckfilter = h.url_for(
            h.r_usertickets, username=uname,
            form='submit', formname='deltckfilter', view='js'
        )
        h.suburl_inviteuser = h.url_for(
            h.r_usersinvite, form='submit', formname='inviteuser'
        )
        h.suburl_accountinfo = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='updateuser', view='js'
        )
        h.suburl_updtpass = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='updtpass', view='js'
        )
        h.suburl_adduserphoto = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='userphoto', view='js'
        )
        h.suburl_deluserphoto = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='deluserphoto', view='js'
        )
        h.suburl_addusericon = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='usericon', view='js'
        )
        h.suburl_delusericon = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='delusericon', view='js'
        )
        h.suburl_adduserrels = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='adduserrels', view='js'
        )
        h.suburl_appruserrels = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='approveuserrels', view='js'
        )
        h.suburl_deluserrels = h.url_for(
            h.r_userpref, username=uname,
            form='submit', formname='deluserrels', view='js'
        )

    def _url_pasteradmin( self, environ ) :
        pass

    def _url_search( self, environ ) :
        pass

    def _url_xmlrpc( self, environ ) :
        pass

    def _url_error( self, environ ) :
        pass


#------------------- For Multigate -----------------------
def render_signin() :
    """This function will be called by AuthKit for user signin page"""
    from zeta.config.environment import userscomp

    basecntlr = BaseController()
    basecntlr.beforecontrollers()

    # Skip the google web-analytics block for signin page since Authkit
    # interprets the % character for text substitution.
    c.skipga = True

    # Logic to find invalid user/password or disabled user and flash messages
    claimeduser = request.POST.get( 'username', None )
    if claimeduser and getattr( c, 'signinflash', '' ) == '' :
        c.signinflash =  'Enter a correct username,  password'

    # Heuristics to detect Disabled user
    claimeduser = claimeduser and userscomp.get_user( claimeduser )
    if claimeduser and claimeduser.disabled :
        c.signinflash = 'User disabled, contact site-administrator'

    html = render( '/derived/accounts/signin.html' ).encode( 'utf-8' )
    return html
