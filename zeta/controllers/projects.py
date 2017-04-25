# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage project pages."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : 
#   1. `url_for` API should be moved to base class (BaseController)


import logging

from   pytz                    import timezone, all_timezones, utc
from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config
import simplejson              as json

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
from   zeta.lib.constants      import *
import zeta.lib.analytics      as ca

log = logging.getLogger( __name__ )

class ProjectsController( BaseController ) :
    """Class to handle project page request"""

    _charts = {
        'chart14' : 'project-activity',
        'chart15' : 'roadmap',
    }

    def _optimized_fetch( self, controllername, projname ) :
        """Fetch the project object (details) from the database in an optimized
        manner based on the action and json request"""
        from zeta.config.environment    import projcomp, tckcomp

        attrload, attrload_all = ( ['logofile'], [] )
        if c.jsonobj == 'pcomplist' :
            attrload_all.extend([ 'components.owner' ])
        elif c.jsonobj == 'mstnlist' :
            attrload.extend([ 'milestones' ])
        elif c.jsonobj == 'verlist' :
            attrload.extend([ 'versions' ])
        elif controllername == 'projadmin' :
            attrload.extend([ 'iconfile', 'license', 'project_info',
                              'mailinglists', 'ircchannels', 'admin', 
                           ])
        elif controllername == 'projectmilestone' :
            attrload.extend([ 'milestones' ])
            c.mstntickets= tckcomp.mstntickets( c.project )
        elif controllername == 'projectroadmap' :
            attrload.extend([ 'milestones' ])
            c.mstntickets= tckcomp.mstntickets( c.project )
        elif controllername == 'projectcharts' :
            attrload.extend([ 'milestones', 'versions', 'components' ])
            c.mstntickets= tckcomp.mstntickets( c.project )
        elif controllername == 'projecthome' :
            attrload.extend([ 'mailinglists', 'ircchannels', 'license', 'tags',
                              'admin' ])
            attrload_all.extend([ 'team.user' ])

        c.project = projcomp.get_project(
                        projname, attrload=attrload, attrload_all=attrload_all
                    ) if projname else None

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )
        c.mainnavs = mainnav( c.projectname, c.controllername )

        # Collect the query values into 'context'
        c.id = request.params.get( 'id', None )
        c.translate = request.params.get( 'translate', False ) and True
        c.alphaindex = request.params.get( 'alphaindex', None )
        c.searchproject = [( 'project', c.projectname )]
        c.prjlogo = self.url_attach( c.project.logofile.id ) \
                    if c.project and c.project.logofile else None

        self._optimized_fetch( c.routesobj.name, c.projectname )

    def _prjattachs( self, project ) :
        """For JSON consumption. Massage the project attachments"""
        return self.modelattachments( project )

    def _prjtags( self, project ) :
        """For JSON consumption. Massage the project tags"""
        return self.modeltags( project )

    def _projlogo( self, p ) :
        return self.modelattachments( p, 'logofile') if p.logofile else {}

    def _projicon( self, p ) :
        return self.modelattachments( p, 'iconfile') if p.iconfile else {}

    @h.authorize( h.ValidUser( strict='True' ))
    def _json_myprojects( self, environ ) :                          # JSON
        """JSON : { id    : ''
                    label : ''
                    item  : [ { projectnames : myprojectnames } ]
                  }"""
        fn  = lambda v : { 'projectnames': v }
        return h.todojoreadstore( [ h.myprojects(c.authuser) ], fn )

    @h.authorize( h.ValidUser() )
    def _json_projectnames( self, environ ) :                        # JSON
        """JSON : { id    : ''
                    label : ''
                    item  : [ { projectnames : projectnames } ]
                  }"""
        from zeta.config.environment    import projcomp
        fn = lambda v : { 'projectnames': v }
        return h.todojoreadstore( [ projcomp.projectnames ], fn )

    @h.authorize( h.SiteAdmin() )
    def _json_projectstatus( self, environ ) :                       # JSON
        """JSON: { id   : 'status',
                   label: 'status',
                   items: [ { status: status, projectnames: projectnames },
                            ... ]
                 }"""
        from zeta.config.environment    import projcomp
        fn = lambda k, v : { 'status' : k, 'projectnames' : v }
        return h.todojoreadstore(
                        projcomp.projectstatus, fn, id='status', label='status'
               )

    @h.authorize( h.HasPermname( ['PROJECT_VIEW'] ))
    def _json_projectlogo( self, environ ) :                         # JSON
        """JSON: { id : [ id, url, filename, summary } """
        return json.dumps( self._projlogo( c.project ) )

    @h.authorize( h.HasPermname( ['PROJECT_VIEW'] ))
    def _json_projecticon( self, environ ) :                         # JSON
        """JSON: { id : [ id, url, filename, summary } """
        return json.dumps( self._projicon( c.project ) )

    @h.authorize( h.HasPermname( 'PROJECT_VIEW' ))
    def _json_prjattach( self, environ ) :                          # JSON
        """JSON: { id : [ id, url, filename, summary ], ... } """
        return json.dumps( self._prjattachs( c.project ) )

    @h.authorize( h.HasPermname( 'PROJECT_VIEW' ))
    def _json_prjtag( self, environ ) :                             # JSON
        """JSON: { tagname : tagname, ... } """
        return json.dumps( self._prjtags( c.project ) )

    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def _json_pcomplist( self, environ ) :                           # JSON
        """JSON: { id   : 'id',
                   label: 'id',
                   items: [ { id           : component.id,
                              componentname: component.componentname,
                              owner        : component.owner 
                              description  : component.description },
                            ... ]
                 }"""
        pcomps = [ [ pcomp.id, pcomp.componentname, pcomp.owner.username,
                     pcomp.description
                   ] for pcomp in getattr( c.project, 'components', [] ) ]
        fn = lambda v : { 'id'    : v[0], 'componentname' : v[1],
                          'owner' : v[2], 'description'   : v[3],
                        }
        return h.todojoreadstore( pcomps, fn id='id', label='id' )

    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def _json_pcomptag( self, environ ) :                            # JSON
        """JSON: [ tagname, ... ] """
        from zeta.config.environment    import projcomp
        comp = projcomp.get_component( int(c.id) ) if c.id else None
        return json.dumps([ t.tagname for t in getattr( comp, 'tags', [] ) ])

    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def _json_mstnlist( self, environ ) :                            # JSON
        """JSON: { id   : 'id',
                   label: 'id',
                   items: [ { id            : milestone.id,
                              milestone_name: milestone.milestone_name,
                              due_date      : milestone.due_date ,
                              description   : milestone.description,
                              status        : milestone.status,
                              closing_remark: milestone.closing_remark },
                            ... ]
                 }"""
        mstns = []
        for mstn in getattr( c.project, 'milestones', [] ) :
            status = ( mstn.completed and 'completed' ) or \
                     ( mstn.cancelled and 'cancelled' ) or ''
            dd = []
            if mstn.due_date :
                due_date = mstn.due_date.astimezone(
                                    h.timezone( c.authuser.timezone ))
                dd = [ due_date.year, due_date.month, due_date.day ]
            mstns.append([
                mstn.id, mstn.milestone_name, dd,
                mstn.description, status, mstn.closing_remark
            ])

        fn = lambda v : { 'id'       : v[0], 'milestone_name' : v[1],
                          'due_date' : v[2], 'description'    : v[3],
                          'status'   : v[4], 'closing_remark' : v[5]
                        }
        return h.todojoreadstore( mstns, fn, id='id', label='id' )

    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def _json_mstntag( self, environ ) :                             # JSON
        """JSON: [ tagname, ... ] """
        from zeta.config.environment    import projcomp
        mstn = projcomp.get_milestone( int( c.id )) if c.id else None
        return json.dumps([ t.tagname for t in getattr( mstn, 'tags', [] ) ])

    @h.authorize( h.HasPermname( ['PROJECT_VIEW'] ))
    def _json_verlist( self, environ ) :                             # JSON
        """JSON: { id   : 'id',
                   label: 'id',
                   items: [ { id          : version.id,
                              version_name: version.version_name,
                              description : version.description },
                            ... ]
                 }"""
        vers = [ [ ver.id, ver.version_name, ver.description ]
                 for ver in getattr( c.project, 'versions', [] )
               ]
        fn = lambda v : { 'id'          : v[0], 'version_name' : v[1],
                          'description' : v[2]
                        }
        return h.todojoreadstore( vers, fn, id='id', label='id' )

    @h.authorize( h.HasPermname( ['PROJECT_VIEW'] ))
    def _json_vertag( self, environ ) :                              # JSON
        """JSON: [ tagname, ... ] """
        from zeta.config.environment    import projcomp
        ver = projcomp.get_version( int( c.id )) if c.id else None
        return json.dumps([ t.tagname for t in getattr( ver, 'tags', [] ) ])

    @h.authorize( h.ProjectAdmin() )
    def _json_projectteams( self, environ ) :               # JSON
        """JSON: { id   : 'team',
                   label: 'team',
                   items: [ { team        : team_typename,
                              usersids    : [[ pt.id, pt.user.username ], ... ],
                              x_usernames : [ username, ... ] },
                            ... ]
                 }"""
        from zeta.config.environment    import projcomp

        teams = projcomp.projectteams( project=c.project )
        teams.pop( projcomp.team_nomember )  # Prune nomember team
        fn = lambda k, v : { 'team'        : k,   'usersids' : v[0],
                             'x_usernames' : v[1]
                           }
        return h.todojoreadstore( teams, fn, id='team', label='team' )

    @h.authorize( h.ProjectAdmin() )
    def _json_teamperms( self, environ ) :                           # JSON
        """JSON: { id   : 'team',
                   label: 'team',
                   items: [ { team        : team_typename,
                              permsids    : [[ ptp.id, permgroup ] ... ],
                              x_permission: [ permission, ... ] },
                            ... ]
                 }"""
        from zeta.config.environment    import projcomp

        teamperms = projcomp.teamperms( project=c.project )
        fn = lambda k, v : { 'team'          : k,   'permsids' : v[0],
                             'x_permissions' : v[1]
                           }
        return h.todojoreadstore( teamperms, fn, id='team', label='team' )

    @h.authorize( h.ProjectAdmin() )
    def _json_prjperms( self, environ ) :                            # JSON
        """JSON: { id   : 'username',
                   label: 'username',
                   items: [ { username    : projuser,
                              permsids    : [[ pup.id, permgroup ] ... ],
                              x_permission: [ permission, ... ] },
                            ... ]
                 }"""
        from zeta.config.environment    import projcomp
        fn = lambda k, v : { 'username'      : k,   'permsids' : v[0],
                             'x_permissions' : v[1]
                           }
        x = projcomp.projectuserperms( project=c.project )
        return h.todojoreadstore( x, fn, id='username', label='username' )

    @h.authorize( h.ValidUser( strict='True' ))
    def create( self, environ ) :
        """Create and host a new project
        URLS :
            /p/newproject?form=request&formname=createprj
            /p/newproject?form=submit&formname=createprj
        """
        from zeta.config.environment    import liccomp, projcomp, vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=['createprj'], user=c.authuser
        )

        # Setup context for page generation
        c.licensenames = sorted([ l[1] for l in liccomp.licensefields() ])
        c.projectnames = projcomp.projectnames
        c.liceditable  = h.authorized( h.HasPermname(['LICENSE_CREATE']) )
        c.title = 'CreateProject'

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.form == 'submit' :
            h.redirect_url( h.url_createprj )
        else :
            html = render( '/derived/projects/create.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.ValidUser() )
    def index( self, environ ) :
        """List all the projects.
        URLS :
            /p
            /p?alphaindex=<alphaindex>
        """
        from zeta.config.environment    import projcomp, vfcomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        x = projcomp.get_project( attrload=['admin', 'project_info'] )
        c.projects = x
        c.urlprojects = dict([ ( p.id, self.url_forproject( p.projectname )) for p in x ])
        c.title = 'ProjectIndex'

        byindex = {}
        [ byindex.setdefault( p.projectname[0], [] ).append(p) for p in x ]
        c.indexlist = sorted( byindex.keys() )
        if (c.alphaindex == None) and (len(c.projects) > h.MAX2SWITCH_ALPHAINDEX) :
            c.alphaindex = c.indexlist[0]
        if c.alphaindex :
            c.projects = byindex[c.alphaindex]

        # Html page generation
        c.rclose.append(render( '/derived/projects/index.html' ))
        return c.rclose

    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def projecthome( self, environ, projectname ) :
        """Project main-page for `projectname`
        URLS :
            /p/<projectname>
            /p/<projectname>?translate=1
            /p/<projectname>?jsonobj=projectlogo&view=js
            /p/<projectname>?jsonobj=projecticon&view=js
            /p/<projectname>?form=submit&formname=projfav&view=js
        """
        from zeta.config.environment    import projcomp, wikicomp, vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=['projfav'], user=c.authuser
        )

        # Setup context for page generation
        c.projsummary = c.project.summary
        pt = {}
        [ pt.setdefault( t.teamtype.team_type, [] ).append( t.user.username )
          for t in c.project.team ]
        c.projectteams = pt
        c.att_editable = h.authorized( h.ProjectAdmin() )
        c.tag_editable = c.att_editable
        c.isfavorite = projcomp.checkfavorite( c.project.id, c.authuser.id )
        c.tags = self._prjtags( c.project )
        c.title = c.projectname

        fpurl = unicode( self.url_wikiurl( c.projectname, PROJHOMEPAGE ))
        w = wikicomp.get_wiki( fpurl, attrload=[ 'tablemap' ] )
        c.fpwcnt = wikicomp.get_content( w, translate=True ) if w else None
        c.fphtml = wikipage2html( c.fpwcnt, c.translate )

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.jsonobj and c.view == 'js' :
            html = self.handlejson(environ)
        elif c.view != 'js' :
            html = render( '/derived/projects/project.html' )
        c.rclose.append(html)
        return c.rclose


    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def roadmap( self, environ, projectname ) :
        """Milestones and report cards for project, `projectname`
        URLS :
            /p/<projectname>/roadmap
        """
        from zeta.config.environment    import projcomp, tckcomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.tck_typenames = tckcomp.tcktypenames
        c.tck_statusnames = tckcomp.tckstatusnames
        c.tck_severitynames = tckcomp.tckseveritynames
        c.title = projectname + ':roadmap'

        c.chart13_data = []
        c.mstnresolved = {}
        fn = lambda k, v : { 'name' : k, 'y' : v }
        for m in c.project.milestones :
            bystatus, bytypes, byseverity, byowner, c.mstnresolved[m.id] = \
                    h.chartify_mstn( c.mstntickets[m.id] )
            c.chart13_data.append(
                [ m.id,
                  map( fn, bytypes.iteritems() ),
                  map( fn, byseverity.iteritems() ),
                  map( fn, bystatus.iteritems() ),
                  map( fn, byowner.iteritems() ),
                ]
            )
        c.rclose.append(render( '/derived/projects/projroadmap.html' ))
        return c.rclose

    @h.authorize( h.HasPermname( ['PROJECT_VIEW' ] ))
    def milestone( self, environ, projectname, mstnid=None ) :
        """Individual milestone for project, `projectname`
        URLS :
            /p/<projectname>/m
            /p/<projectname>/m/<mstnid>
        """
        from zeta.config.environment    import projcomp, tckcomp

        h.redirect_url( h.url_projroadmap ) if not mstnid else None

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.milestone = projcomp.get_milestone( int(mstnid) )
        m = c.milestone
        h.redirect_url( h.url_projroadmap
        ) if m and m.project_id != c.project.id else None

        c.tck_typenames = tckcomp.tcktypenames
        c.tck_statusnames = tckcomp.tckstatusnames
        c.tck_severitynames = tckcomp.tckseveritynames
        c.title = c.milestone.milestone_name

        c.chart13_data      = []
        bystatus, bytypes, byseverity, byowner, c.mstnresolved = \
                                h.chartify_mstn( c.mstntickets[m.id] )
        c.chart13_data = [
              m.id,
              map( fn, bytypes.iteritems() ),
              map( fn, byseverity.iteritems() ),
              map( fn, bystatus.iteritems() ),
              map( fn, byowner.iteritems() ),
        ]
        c.rclose.append(render( '/derived/projects/projmilestone.html' ))
        return c.rclose

    @h.authorize( h.ProjectAdmin() )
    def admin( self, environ, projectname ) :
        """Project administration page
        URLS :
            /p/<projectname>/admin?jsonobj=pcomplist&view=js
            /p/<projectname>/admin?jsonobj=mstnlist&view=js
            /p/<projectname>/admin?jsonobj=verlist&view=js
            /p/<projectname>/admin?jsonobj=projectteams&view=js
            /p/<projectname>/admin?jsonobj=teamperms&view=js
            /p/<projectname>/admin?jsonobj=prjattach&view=js
            /p/<projectname>/admin?jsonobj=prjtag&view=js
            /p/<projectname>/admin?jsonobj=prjtag&view=js
            /p/<projectname>/admin?form=request
            /p/<projectname>/admin?form=submit&formname=updateprj&view=js
            /p/<projectname>/admin?form=submit&formname=prjexp&view=js
            /p/<projectname>/admin?form=submit&formname=prjml&view=js
            /p/<projectname>/admin?form=submit&formname=prjirc&view=js
            /p/<projectname>/admin?form=submit&formname=addprjlogo&view=js
            /p/<projectname>/admin?form=submit&formname=delprjlogo&view=js
            /p/<projectname>/admin?form=submit&formname=addprjicon&view=js
            /p/<projectname>/admin?form=submit&formname=delprjicon&view=js
            /p/<projectname>/admin?form=submit&formname=createpcomp&view=js
            /p/<projectname>/admin?form=submit&formname=updatepcomp&view=js
            /p/<projectname>/admin?form=submit&formname=rmpcomp&view=js
            /p/<projectname>/admin?form=submit&formname=createmstn&view=js
            /p/<projectname>/admin?form=submit&formname=updatemstn&view=js
            /p/<projectname>/admin?form=submit&formname=mstnclose&view=js
            /p/<projectname>/admin?form=submit&formname=rmmstn&view=js
            /p/<projectname>/admin?form=submit&formname=createver&view=js
            /p/<projectname>/admin?form=submit&formname=updatever&view=js
            /p/<projectname>/admin?form=submit&formname=rmver&view=js
            /p/<projectname>/admin?form=submit&formname=addprjteam&view=js
            /p/<projectname>/admin?form=submit&formname=delprjteam&view=js
            /p/<projectname>/admin?form=submit&formname=addteamperms&view=js
            /p/<projectname>/admin?form=submit&formname=delteamperms&view=js
            /p/<projectname>/admin?form=submit&formname=addprjattachs&view=js
            /p/<projectname>/admin?form=submit&formname=delprjattachs&view=js
            /p/<projectname>/admin?form=submit&formname=addprjtags&view=js
            /p/<projectname>/admin?form=submit&formname=delprjtags&view=js
        """
        from zeta.config.environment import userscomp, liccomp, projcomp, vfcomp
    
        formnames = [ 'updateprj', 'prjexp', 'prjml', 'prjirc', 'addprjlogo',
                      'delprjlogo', 'addprjicon', 'delprjicon', 'createpcomp',
                      'updatepcomp', 'rmpcomp', 'createmstn', 'updatemstn',
                      'mstnclose', 'rmmstn', 'createver', 'updatever', 'rmver',
                      'addprjteam', 'delprjteam', 'addteamperms',
                      'delteamperms', 'addprjattachs', 'delprjattachs',
                      'addprjtags', 'delprjtags', ]

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=formnames, user=c.authuser, project=c.project
        )

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.logo_editable= c.icon_editable= c.tag_editable = True
        c.pcomplist = c.mstnlist = c.verlist = []
        c.title = projectname+':admin'
        if c.view != 'js' :
            c.licensenames = sorted(liccomp.licensenames)
            c.projusers    = sorted(
                                projcomp.projusernames( c.project ) + \
                                [ c.project.admin.username ]
                             )
            c.usernames = userscomp.usernames
            c.teamtypes_p  = projcomp.teams
            c.teamtypes = c.teamtypes_p[:]
            c.teamtypes.remove( projcomp.team_nomember )
            c.logoattach = self._projlogo( c.project )
            c.iconattach = self._projicon( c.project )

        # Html page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.view == 'js' and \
           c.formname in [ 'addprjlogo', 'addprjicon', 'addprjattachs' ] :
            html = IFRAME_RET

        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)

        elif c.view == 'js' :
            html = ''

        else :
            # Context specific to project admin form
            c.projectteams = projcomp.projectteams(
                                project=c.project, teamnames=c.teamtypes_p,
                                usernames=c.usernames,
                             )
            c.isfavorite = projcomp.checkfavorite( c.project.id, c.authuser.id )

            deftt = sorted(c.projectteams.keys())[0]
            c.defteamtype= deftt
            c.teamusers = map( lambda pr : pr[1], c.projectteams[deftt][0] )
            c.x_teamusers = c.projectteams[deftt][1]

            c.teamperms = projcomp.teamperms(
                                project=c.project, teamnames=c.teamtypes_p,
                          )
            c.teampgroups = map( lambda pr : pr[1], c.teamperms[deftt][0] )
            c.x_teampgroups= c.teamperms[deftt][1]

            html = render( '/derived/projects/admin.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'PROJECT_VIEW' ]))
    def timeline( self, environ, projectname ) :
        """Aggregate all the activities under the project
        URLS :
            /p/<projectname>/timeline
        """
        from zeta.config.environment    import projcomp, tlcomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.project = c.project or projcomp.get_project( projectname )
        c.projectname = c.project.projectname
        c.projsummary = c.project.summary
        c.title = projectname + ':timeline'
        c.alllogs = tlcomp.fetchprojlogs(
                        c.project, limit=h.TLCOUNT+2, id=logid, direction=dir
                    )
        routeargs = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projtline, routeargs, [], fromoff, logid, dir, c.project
        )
        h.url_rssfeed = h.url_for( h.r_projfeed, projectname=projectname )
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )

        c.rclose.append(render( '/derived/projects/projtline.html' ))
        return c.rclose

    @h.authorize( h.ProjectAdmin() )
    def timelineadmin( self, environ, projectname ) :
        """Aggregate all the activities under the project
        URLS :
            /p/<projectname>/timeline/admin"""
        from zeta.config.environment    import projcomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        routeargs  = { 'projectname' : projectname }
        self.tline_controller(
                h.r_projadmtline, routeargs, 'project',
                fromoff, logid, dir, c.project
        )
        c.title = projectname + ':admintimeline'
        h.url_rssfeed = h.url_for( h.r_projadmfeed, projectname=projectname )
        c.datatline, c.startdt = h.tlineplot( c.logs[:] )

        c.rclose.append(render( '/derived/projects/admintline.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'PROJECT_VIEW' ]))
    def downloads( self, environ, projectname ) :
        """Action to present project downloads
        URLS : 
            /p/<projectname>/downloads
        """
        from zeta.config.environment    import projcomp

        c.rclose = h.ZResp()

        # Setup context for html page
        c.projsummary = c.project.summary
        c.title = 'ProjectDownloads'
        attachments = projcomp.attachments( c.project )
        c.attachments = {}
        for pkey, adict in attachments.iteritems() :
            attachs = []
            for aid, a in adict.iteritems() :
                if 'download' not in a[-1] : continue
                a[-1].remove( 'download' )
                attachs.append( 
                    [ aid ] + adict[aid][:-1] + [ ', '.join(a[-1]) ] + \
                    [ self.url_attachdownl( aid ) ]
                )
            c.attachments[ pkey[1] ] = attachs

        # Html page generation
        c.rclose.append(render( '/derived/projects/projdownloads.html' ))
        return c.rclose


    @h.authorize( h.HasPermname([ 'PROJECT_VIEW' ]))
    def attachs( self, environ, projectname ) :
        """Action to present attachment page for `projectname`
        URLS :
            /p/<projectname>/attachs
        """
        from zeta.config.environment    import projcomp, vfcomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.editable = c.att_editable = h.authorized( h.ProjectAdmin() )
        c.title    = 'ProjectAttachs'
        c.projsummary = c.project.summary
        attachments  = projcomp.attachments( c.project )
        c.attachments = self.attachments( attachments )
        c.attachs = self._prjattachs( c.project )
        c.isfavorite = projcomp.checkfavorite( c.project.id, c.authuser.id )

        # Html page generation
        c.rclose.append(render( '/derived/projects/projattachs.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'PROJECT_VIEW' ]))
    def charts( self, environ, projectname ) :
        """Chart analytics for project `projectname`
        URLS :
            /p/<projectname>/charts
            /p/<projectname>/charts?chartname=<name>
        """

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.projectname = c.project.projectname
        c.projsummary = c.project.summary
        c.chartname = c.chartname or 'chart14'
        c.selectedchart = (c.chartname, self._charts[c.chartname])
        c.chartoptions = [ ( self.url_projchart( projectname, name), text
                           ) for name, text in self._charts.iteritems() ]
        c.pa = ca.get_analyticobj( 'projects' )
        c.title = '%s:Charts' % projectname

        # Html page generation
        if c.chartname == 'chart14' :
            c.chart14_data = getattr( c.pa, 'chart14_data', {}
                                    ).get( projectname, {} ).items()
        elif c.chartname == 'chart15' :
            dates    = []
            mstns    = []
            for m in c.project.milestones :
                created_on = timezone('UTC').localize(m.created_on)
                dates.extend([ created_on, m.due_date ])
                mstns.append(( m, created_on, m.due_date ))
            mstns    = sorted( mstns, key=lambda x: x[1] )
            dates    = sorted(filter( None, dates ))

            c.chart15_data = []
            for mstn in mstns :
                m      = mstn[0]
                mrange = mstn[1:3]
                # stacked bar : open, cancelled, completed
                if not mrange[1] :
                    days = (dates[-1]-mrange[0]).days
                elif mrange[1] > mrange[0] :
                    days = (mrange[1]-mrange[0]).days
                elif mrange[1] <= mrange[0] :
                    days = 0

                bar = [ (mrange[0]-dates[0]).days ]
                if m.completed :
                    bar.extend( [0, 0, days] )
                elif m.cancelled :
                    bar.extend( [0, days, 0] )
                else :
                    bar.extend( [days, 0, 0] )
                c.chart15_data.append( [m.milestone_name] + bar )

            date            = dates and dates[0] or None
            c.chart15_frmdt = h.date2jsdate( date, [ '2000', '0', '1' ] )

        c.rclose.append(render( '/derived/projects/projcharts.html' ))
        return c.rclose

    def feedadmin( self, environ, projectname ) :
        """Aggregate all the activities under the project
        URLS :
            /p/<projectname>/feed/admin
        """
        from zeta.config.environment    import projcomp

        # Setup context for page generation
        c.projsummary = c.project.summary
        title = projectname + ':admintimeline'
        link = h.urlroot(environ)
        descr = 'Timeline for project administration, %s' % projectname
        feed = h.FeedGen( title, link, descr )
        routeargs  = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projadmtline, routeargs, 'project', 1, None, None, c.project
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, projectname ) :
        """Aggregate all the activities under the project, and provide them as
        feed
        URLS :
            /p/<projectname>/feed
        """
        from zeta.config.environment    import tlcomp

        # Setup context for page generation
        c.projsummary = c.project.summary
        title = projectname + ':timeline'
        link = h.urlroot(environ)
        descr = 'Timeline for project, %s' % projectname
        c.alllogs = tlcomp.fetchprojlogs( c.project, limit=h.TLCOUNT+1, id=None)
        c.logs = c.alllogs[:100]
        feed = h.FeedGen( title, link, descr )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers()
