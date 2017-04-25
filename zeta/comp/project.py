# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on project tables.
"""

# -*- coding: utf-8 -*-

# Gotchas :
#   1. Team name and username cannot be same. Doing so, could mangle
#      authentication mechanism 
# Notes   :
#   1. Calculation of permission name mapping have a glitch.
#      While retrieving the permission groups from `ptp` and `pup`, make sure
#      that the permission names get automatically computed from
#      `permission_maps`. That way it is easy to compute the missing
#      permission names more consistently (without redundancy)
#   2. post-processing function can be subscribed to onclose event and can
#      thus be delayed until the request is completed.
# Todo    : 
#   1. Detailed log might be required for create_project() method ??
#   2. Add timeline logging for approve_project_user() method
#   3. userpermissions() method is deprecated. Confirm and remove !!
#   4. projectuserperms() method is deprecated. Confirm and remove !!
#   5. `noquery` kwarg does not have any meaning. Remove them.

from   __future__               import with_statement

from   sqlalchemy               import *
from   sqlalchemy.sql           import *
from   sqlalchemy.orm           import *

from   zeta.ccore               import Component
from   zeta.model               import meta
from   zeta.model.schema        import t_user, at_project_favorites, t_project,\
                                       t_ticket, t_component, t_milestone, \
                                       t_version, t_ticket_status, \
                                       t_attachment, t_tag, \
                                       t_ticket_severity, t_ticket_type, \
                                       t_ticket_status_history, t_project_team, \
                                       t_projectteam_type, t_projectteam_perm, \
                                       t_permission_group, t_permission_name, \
                                       at_ticket_milestones, at_project_attachments, \
                                       at_attachment_tags, at_ticketstatus_owners, \
                                       at_attachment_uploaders, \
                                       at_project_admins, at_permission_maps

from   zeta.model.tables        import User, PermissionGroup, Attachment, \
                                       ProjectTeam_Type, \
                                       Project,  ProjectInfo, MailingList, \
                                       IRCChannel, PrjComponent, Milestone, \
                                       Version, ProjectPerm, ProjectTeam_Perm, \
                                       ProjectTeam, Ticket, TicketType, \
                                       TicketSeverity
import zeta.lib.helpers         as h
import zeta.lib.cache           as cache
from   zeta.lib.error           import ZetaProjectError

class ProjectComponent( Component ) :
    """Project Component."""
    def _last_entry( self, list, attr ) :
        """Sort the `list` based on attr and return the last element."""
        models = sorted( list, key=lambda o : getattr(o, attr) )
        last   = ( models and models[-1] ) or None
        return last

    def create_projteamtype( self, team_types, byuser=None ) :
        """Create project team_type entries for the teamtypes specified by,
        `team_types`
            which can be, a string specifying the team_type name or a list of
            such strings"""
        from zeta.config.environment import tlcomp

        if isinstance( team_types, (str,unicode) ) :
            team_types = [ team_types ]

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ msession.add( ProjectTeam_Type( unicode(t) )) 
              for t in team_types if t ]

        # Database Post processing
        tlcomp.log( byuser, 'created project team type, %s' % ', '.join(team_types) )

    @h.postproc()
    def create_project( self, prjdetail=None, prjidetail=None, update=False,
                        doclose=None, byuser=None ) :
        """Create entries in project and projectinfo table for a new project
        defined by,
            prjdetail  ( prjid, projectname, summary, admin_email, license, admin )
                license can be `id` or `License` instance.
                admin   can be `id` or `User` instance.
            prjidetail ( description )
        if update=True,
            Update an existing project identified by `prjid` (prjdetail[0])
            and projectinfo entry.

        Return,
            Project instance."""
        from zeta.config.environment import userscomp, liccomp, tlcomp, srchcomp

        if prjidetail and not prjidetail[0] :
            prjidetail = ( 'No Description', ) 

        log = ''

        if update and prjdetail[0] :
            project = self.get_project(
                            prjdetail[0],
                            attrload=['project_info', 'license', 'admin' ]
                      )
        else :
            project = None

        license = prjdetail[4] and liccomp.get_license( prjdetail[4] )
        admin = prjdetail[5] and userscomp.get_user( prjdetail[5] )

        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            if (update and project) or project :
                # Generate the log message based on the changing attributes
                loglines = [
                    ('summary', project.summary, prjdetail[2] ),
                    ('admin_email', project.admin_email, prjdetail[3]),
                ]
                loglines.append(
                    ('license', project.license.licensename, license.licensename)
                )
                loglines.append(
                    ('project-admin', project.admin.username, admin.username)
                )
                loglines.append(
                    ('', project.project_info.description, prjidetail[0])
                )

                log = h.logfor( loglines )
                if log :
                    log = 'updated project information,\n%s' % log
                # Logging logic till here

                project.projectname = prjdetail[1]
                project.summary = prjdetail[2]
                project.admin_email = prjdetail[3]
                if prjidetail :
                    pinfo  = project.project_info
                    pinfo.description     = prjidetail[0]
                    pinfo.descriptionhtml = pinfo.translate()
                license and setattr( project, 'license', license )
                admin and setattr( project, 'admin', admin )

                idxreplace = True                   # Replace the search index

            else :
                project_info = ProjectInfo( *prjidetail )
                project = Project( *prjdetail[1:4] )
                project_info.descriptionhtml = project_info.translate()
                license and setattr( project, 'license', license )
                admin and setattr( project, 'admin', admin )
                project.project_info = project_info
                project_info.project = project
                msession.add( project )
                log = 'created a new project `%s`\nsummary : %s' % \
                                (project.projectname, project.summary)
                idxreplace = False

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_teamperms )
        cache.invalidate( self.mapfor_projadmins )

        def onclose(tlcomp, srchcomp, project, byuser, log, idxreplace) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=idxreplace )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log,
                            idxreplace ))
        return project

    @h.postproc()
    def config_project( self, project, doclose=None, byuser=None, **kwargs ) :
        """Configure project identified by,
        `project` which can be,
            `id` or `projectname` or `Project` instance
        with config options,
            disable=Bool, Disable or enable the specified project.
            expose=Bool, Expose the specified project.
            logo=attach, if None, then remove the attachment
            icon=attach, if None, then remove the attachment
            license=`id` or `licensename` or `License` instance
            admin=`id` or `username` or `User` instance
            uploader=<user who is uploading the logo and icon attachment>
                Where attach is `id` or `resource_url` or `Attachment` instance.
        """
        from zeta.config.environment import \
                    userscomp, attcomp, liccomp, tlcomp, srchcomp

        project   = self.get_project( project )
        lic = kwargs.get( 'license', None )
        lic = lic and liccomp.get_license( lic )
        adm = kwargs.get( 'admin', None )
        adm = adm and userscomp.get_user( adm )
        logo = kwargs.get( 'logo', False )
        logo = logo and attcomp.get_attach( logo )
        icon = kwargs.get( 'icon', False )
        icon = icon and attcomp.get_attach( icon )
        uploader = kwargs.get( 'uploader', None )
        uploader = uploader and userscomp.get_user( uploader )
        msession = meta.Session()

        # Construct log based on attributes that have changed
        loglines = []
        disabled = kwargs.get( 'disable', None )
        exposed  = kwargs.get( 'expose', None )
        disabled != None and \
            loglines.append(( 'disabled', project.disabled, disabled ))
        exposed != None and \
            loglines.append(( 'exposed', project.exposed, exposed ))
        lic and \
            loglines.append(
                  ( 'license', getattr(project.license, 'licensename', ''),
                               lic.licensename )
            )
        adm and \
            loglines.append(
                ( 'project-admin', project.admin.username, adm.username )
            )
        if logo == None :
            loglines.append(( 'project-logo', '', '-' ))
        elif logo :
            loglines.append(( 'project-logo', '', logo.filename ))
        if icon == None :
            loglines.append(( 'project-icon', '', '-' ))
        elif icon :
            loglines.append(( 'project-icon', '', icon.filename ))
        # Ends here

        with msession.begin( subtransactions=True ) :
            if (logo or (logo == None)) and project.logofile :
                msession.delete( project.logofile )
            if (icon or (icon == None)) and project.iconfile :
                msession.delete( project.iconfile )

        with msession.begin( subtransactions=True ) :
            if 'disable' in kwargs :
                project.disabled = kwargs['disable']
            if 'expose' in kwargs :
                project.exposed  = kwargs['expose']
            lic and setattr( project, 'license', lic )
            adm and setattr( project, 'admin', adm )

            if (logo or (logo == None)) and project.logofile :
                msession.delete( project.logofile )
                project.logofile = None
            if (icon or (icon == None)) and project.iconfile :
                msession.delete( project.iconfile )
                project.iconfile = None

            if logo :
                project.logofile = logo
                if uploader :
                    project.logofile.uploader = uploader

            if icon :
                project.iconfile = icon
                if uploader :
                    project.iconfile.uploader = uploader

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_projadmins )
        log = "updated project attributes,\n%s" % h.logfor(loglines) \
              if loglines else ''

        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return project

    @h.postproc()
    def addfavorites( self, project, favusers, doclose=None, byuser=None ) :
        """Add the project as favorite for users identified by
        `favusers`, which can be (also can be an array of)
            `id` or `username` or `User` instance.
        to `project` which can be,
            `id` or `projectname` or `Project` instance"""
        from zeta.config.environment import userscomp, tlcomp

        if not isinstance( favusers, list ) :
            favusers = [ favusers ]

        favusers  = [ userscomp.get_user( u ) for u in favusers ]
        project   = self.get_project( project )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            project.favoriteof.extend( favusers )

        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser) :
            tlcomp.log(byuser, 'added project as favorite', project=project)
        doclose( h.hitchfn( onclose, tlcomp, project, byuser ))
        return None

    @h.postproc()
    def delfavorites( self, project, favusers, doclose=None, byuser=None ) :
        """Delete the project as favorite for users identified by
        `favusers`, which can be (also can be an array of)
            `id` or `username` or `User` instance.
        to `project` which can be,
            `id` or `projectname` or `Project` instance"""
        from zeta.config.environment import userscomp, tlcomp

        if not isinstance( favusers, list ) :
            favusers = [ favusers ]

        favusers  = [ userscomp.get_user( u ) for u in favusers ]
        project   = self.get_project( project )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ project.favoriteof.remove(u)
              for u in favusers if u in project.favoriteof ]

        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser ) :
            tlcomp.log(byuser, 'removed project from favorite', project=project)
        doclose( h.hitchfn( onclose, tlcomp, project, byuser ))
        return None

    def get_project( self, project=None, attrload=[], attrload_all=[],
                     astuple=False ) :
        """Get project identified by,
        `project` which can be,
            `id` or `projectname` or `Project` instance
        if project=None
            Get the list of all Project instances.
        if astuple == True
            `attrload` and `attrload_all` contain the attributes as tuples

        Return,
            Requested Project instance.
            A list of Project instances."""
        if isinstance( project, Project ) and attrload==[] and attrload_all==[]:
            return project

        msession = meta.Session()

        # Compose query based on `user` type
        if isinstance( project, (int, long) ) :
            q = msession.query( Project ).filter_by( id=project)
        elif isinstance( project, (str,unicode) ) :
            q = msession.query( Project ).filter_by( projectname=project )
        elif isinstance( project, Project ) :
            q = msession.query( Project ).filter_by( id=project.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None and astuple :
            q = q.options( *[ eagerload_all( *e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( *e ) for e in attrload ] )
            project = q.first()

        elif q != None:
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            project = q.first()

        elif project == None :
            q = msession.query( Project )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            project = q.all()

        else :
            project = None

        return project

    def get_teamtype( self, teamtype=None ) :
        """Get the team type identified by,
        `teamtype` which can be,
            `id` or `team_type` or ProjectTeam_Type instance.
        if teamtype==None,
            return a list of ProjectTeam_Type instances."""
        msession = meta.Session()
        if isinstance( teamtype, (int, long) ) :
            teamtype = msession.query( ProjectTeam_Type 
                       ).filter_by( id=teamtype ).first()
        elif isinstance( teamtype, (str, unicode) ) :
            teamtype = msession.query( ProjectTeam_Type 
                       ).filter_by( team_type=teamtype ).first()
        elif teamtype == None :
            teamtype = msession.query( ProjectTeam_Type ).all()
        elif isinstance( teamtype, ProjectTeam_Type ) :
            pass
        else :
            teamtype = None
        return teamtype

    def get_component( self, component=None, project=None, attrload=[],
                       attrload_all=[] ) :
        """Get the Component instance for component identified by,
        `component` which can be,
            `id` or `PrjComponent` instance
        if component=None 
            Return all the components.
        if project != None and component is a number then,
            Then `component` will be treated as `comp_number` and the
            PrjComponent instance with `project.id` and `comp_number` will be returned.
        Return
            List of PrjComponent instances or
            One PrjComponent instance."""
        if isinstance( component, PrjComponent ) and attrload==[] and \
           attrload_all==[] :
               return component

        msession = meta.Session()

        # Compose query based on 'project' and 'component' parameters
        if isinstance( project, (str, unicode)) and component :
            q = msession.query( PrjComponent 
                    ).filter_by( comp_number=component
                    ).join( 'project'
                    ).filter_by( projectname=project )

        elif isinstance( project, (str, unicode)) :
            q = msession.query( PrjComponent ).join( 'project' 
                    ).filter_by( projectname=project )

        elif isinstance( project, (int, long)) and component :
            q = msession.query( PrjComponent 
                    ).filter_by( comp_number=component
                    ).join( 'project'
                    ).filter_by( id=project )

        elif isinstance( project, (int, long)) :
            q = msession.query( PrjComponent ).join( 'project'
                    ).filter_by( id=project )

        elif isinstance( project, Project ) and component :
            q = msession.query( PrjComponent 
                    ).filter_by( comp_number=component
                    ).join( 'project'
                    ).filter_by( id=project.id )

        elif isinstance( project, Project ) :
            q = msession.query( PrjComponent ).join( 'project'
                    ).filter_by( id=project.id )

        elif isinstance( component, (int, long)) :
            q = msession.query( PrjComponent ).filter_by( id=component )

        elif isinstance( component, PrjComponent ) :
            q = msession.query( PrjComponent ).filter_by( id=component.id )

        elif project == None and component == None :
            q = msession.query( PrjComponent )

        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )

        if q != None and component==None :
            component = q.all()
        elif q != None :
            component = q.first()
        else :
            component = None

        return component

    def get_milestone( self, milestone=None, project=None, attrload=[],
                       attrload_all=[] ) :
        """Get the Milestone instance for milestone identified by,
        `milestone` can be,
            `id` or `Milestone` instance
        if milestone=None 
            Return all the milestones.
        if project != None and milestone is a number then,
            Then `milestone` will be treated as `mstn_number` and the
            Milestone instance with `project.id` and `mstn_number` will be
            returned

        Return
            List of Milestone instances or
            One Milestone instance."""
        if isinstance( milestone, Milestone ) and attrload==[] and \
           attrload_all==[] :
               return milestone

        msession = meta.Session()

        # Compose query based on 'project' and 'milestone' parameters
        if isinstance( project, (str, unicode)) and milestone :
            q = msession.query( Milestone 
                    ).filter_by( mstn_number=milestone
                    ).join( 'project'
                    ).filter_by( projectname=project )

        elif isinstance( project, (str, unicode)) :
            q = msession.query( Milestone ).join( 'project' 
                    ).filter_by( projectname=project )

        elif isinstance( project, (int, long)) and milestone :
            q = msession.query( Milestone 
                    ).filter_by( mstn_number=milestone
                    ).join( 'project'
                    ).filter_by( id=project )

        elif isinstance( project, (int, long)) :
            q = msession.query( Milestone ).join( 'project'
                    ).filter_by( id=project )

        elif isinstance( project, Project ) and milestone :
            q = msession.query( Milestone
                    ).filter_by( mstn_number=milestone
                    ).join( 'project'
                    ).filter_by( id=project.id )

        elif isinstance( project, Project ) :
            q = msession.query( Milestone ).join( 'project'
                    ).filter_by( id=project.id )

        elif isinstance( milestone, (int, long)) :
            q = msession.query( Milestone ).filter_by( id=milestone )

        elif isinstance( milestone, Milestone ) :
            q = msession.query( Milestone ).filter_by( id=milestone.id )

        elif project == None and milestone == None :
            q = msession.query( Milestone )

        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )

        if q != None and milestone==None :
            milestone = q.all()
        elif q != None :
            milestone = q.first()
        else :
            milestone = None

        return milestone

    def get_version( self, version=None, project=None, attrload=[],
                     attrload_all=[] ) :
        """Get the Version instance for version identified by,
        `version` can be,
            `id` or `Version` instance
        if version=None 
            Return all the versions.
        if project != None and version is a number then,
            Then `version` will be treated as `ver_number` and the
            Version instance with `project.id` and `ver_number` will be
            returned

        Return
            List of Version instances or
            One Version instance."""
        if isinstance( version, Version ) and attrload==[] and \
           attrload_all==[] :
               return version

        msession = meta.Session()

        # Compose query based on 'project' and 'version' parameters
        if isinstance( project, (str, unicode)) and version :
            q = msession.query( Version 
                    ).filter_by( ver_number=version
                    ).join( 'project'
                    ).filter_by( projectname=project )

        elif isinstance( project, (str, unicode)) :
            q = msession.query( Version ).join( 'project' 
                    ).filter_by( projectname=project )

        elif isinstance( project, (int, long)) and version :
            q = msession.query( Version 
                    ).filter_by( ver_number=version
                    ).join( 'project'
                    ).filter_by( id=project )

        elif isinstance( project, (int, long)) :
            q = msession.query( Version ).join( 'project'
                    ).filter_by( id=project )

        elif isinstance( project, Project ) and version :
            q = msession.query( Version
                    ).filter_by( ver_number=version
                    ).join( 'project'
                    ).filter_by( id=project.id )

        elif isinstance( project, Project ) :
            q = msession.query( Version ).join( 'project'
                    ).filter_by( id=project.id )

        elif isinstance( version, (int, long)) :
            q = msession.query( Version ).filter_by( id=version )

        elif isinstance( version, Version ) :
            q = msession.query( Version ).filter_by( id=version.id )

        elif project == None and version == None :
            q = msession.query( Version )

        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )

        if q != None and version==None :
            version = q.all()
        elif q != None :
            version = q.first()
        else :
            version = None

        return version

    def get_projectperm( self, projectperm=None,
                         user=None, project=None, permgroup=None ) :
        """Get the ProjectPerm entry identified by,
        `projectperm` which can be,
            `id` or `ProjectPerm` instance.
        (or)
        `user` which can be,
            `id` or `username` or `User` instance.
        (or)
        `project` which can be,
            `id` or `projectname` or `Project` instance.
        (or)
        `permgroup` which can be,
            `id` or `perm_group` or `PermissionGroup` instance.
        if all the arguments are None.
            return a list of ProjectPerm instances."""
        from zeta.config.environment import userscomp

        user        = user and userscomp.get_user( user )
        permgroup   = permgroup and userscomp.get_permgroup( permgroup )
        project     = project and self.get_project( project )
        msession    = meta.Session()
        if projectperm :
            if isinstance( projectperm, (int,long) ) :
                projectperm = msession.query( ProjectPerm 
                                    ).filter_by( id=projectperm 
                                    ).options(
                                        eagerload( 'user' ),
                                        eagerload( 'project' ),
                                        eagerload( 'permgroup' )
                                    ).first()

            elif isinstance( projectperm, ProjectPerm ) :
                pass

            else :
                projectperm = None

        else :
            q = msession.query( ProjectPerm )
            q = user      and q.filter_by( user_id=user.id ) or q
            q = project   and q.filter_by( project_id=project.id ) or q
            q = permgroup and q.filter_by( perm_group_id=permgroup.id ) or q
            projectperm = q.all()

        return projectperm

    def get_projectteamperm( self, projectteamperm=None,
                             project=None, teamtype=None, permgroup=None ) :
        """Get the projectteamperm entry identified by,
        `projectteamperm` which can be,
            `id` or `ProjectTeam_Perm` instance.
        (or)
        `project` which can be,
            `id` or `projectname` or `Project` instance.
        (or)
        `teamtype` which can be,
            `id` or `team_type` or ProjectTeam_Type instance.
        (or)
        `permgroup` which can be,
            `id` or `perm_group` or `PermissionGroup` instance.
        if all the arguments are None.
            return a list of ProjectTeam_Perm instances."""
        from zeta.config.environment import userscomp

        project   = project and self.get_project( project )
        teamtype  = teamtype and self.get_teamtype( teamtype )
        permgroup = permgroup and userscomp.get_permgroup( permgroup )
        msession  = meta.Session()
        if projectteamperm :
            if isinstance( projectteamperm, (int,long) ) :
                projectteamperm = msession.query( ProjectTeam_Perm
                                    ).filter_by( id=projectteamperm 
                                    ).options(
                                        eagerload( 'teamtype' ),
                                        eagerload( 'project' ),
                                        eagerload( 'permgroup' )
                                    ).first()

            elif isinstance( projectteamperm, ProjectTeam_Perm ) :
                pass

            else :
                projectteamperm = None

        else :
            q = msession.query( ProjectTeam_Perm )
            q = project   and q.filter_by( project_id=project.id ) or q
            q = teamtype  and q.filter_by( teamtype_id=teamtype.id ) or q
            q = permgroup and q.filter_by( perm_group_id=permgroup.id ) or q
            projectteamperm = q.all()

        return projectteamperm

    def get_projectteam( self, projectteam=None,
                         user=None, project=None, teamtype=None ) :
        """Get the ProjectTeam entry identified by,
        `projectteam` which can be,
            `id` or `ProjectTeam` instance.
        (or)
        `user` which can be,
            `id` or `username` or `User` instance.
        (or)
        `project` which can be,
            `id` or `projectname` or `Project` instance.
        (or)
        `teamtype` which can be,
            `id` or `team_type` or `ProjectTeam_Type` instance.
        if all the arguments are None.
            return a list of ProjectTeam instances."""
        from zeta.config.environment import userscomp

        user      = user and userscomp.get_user( user )
        project   = project and self.get_project( project )
        teamtype  = teamtype and self.get_teamtype( teamtype )
        msession  = meta.Session()
        if projectteam :
            if isinstance( projectteam, (int,long) ) :
                projectteam = msession.query( ProjectTeam 
                                    ).filter_by( id=projectteam 
                                    ).options(
                                        eagerload( 'teamtype' ),
                                        eagerload( 'project' ),
                                        eagerload( 'user' )
                                    ).first()

            elif isinstance( projectteam, ProjectTeam ) :
                pass

            else :
                projectteam = None

        else :
            q = msession.query( ProjectTeam )
            q = user     and q.filter_by( user_id=user.id ) or q
            q = project  and q.filter_by( project_id=project.id ) or q
            q = teamtype and q.filter_by( teamtype_id=teamtype.id ) or q
            projectteam = q.all()

        return projectteam

    @h.postproc()
    def set_mailinglists( self, project, mailinglists=None, append=False,
                          doclose=None, byuser=None ) :
        """Set the specified `mailinglists` for the project identified by,
        `project` which can be, 
            `id` or `projectname` or `Project` instance
        if append=True,
            Specified mailing lists will be added to project's existing 
            mailing lists.
        if append=False,
            Existing mailing lists will be cleared and replaced by the
            specified mailing lists.
        if mailinglists == None,
            Delete project's all mailing-lists."""
        from zeta.config.environment import tlcomp, srchcomp

        mlistobj = lambda ml : ( isinstance( ml, MailingList ) and ml ) \
                               or \
                               ( isinstance( ml, (str, unicode) ) and \
                                 MailingList(ml) )

        project  = self.get_project( project )
        if mailinglists and not isinstance(mailinglists, list) :
            mailinglists = [ mailinglists ]

        # Construct log based on mailing lists that have changed
        loglines = [
            ( 'mailing-lists',
              ', '.join([ ml.mailing_list for ml in project.mailinglists ]),
              ', '.join(filter( None,
                                [ mlistobj( ml ).mailing_list
                                  for ml in (mailinglists or []) ]
                              )),
            )
        ]
        log = h.logfor( loglines )
        # End here

        msession = meta.Session()
        mlists = []
        with msession.begin( subtransactions=True ) :
            if append == False :
                project.mailinglists = []
            if mailinglists :
                mlists = [ mlistobj( ml ) for  ml in mailinglists ]
                if append :
                    project.mailinglists.extend( mlists )
                else :
                    project.mailinglists = mlists

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return mlists

    @h.postproc()
    def set_ircchannels( self, project, ircchannels=None, append=False,
                         doclose=None, byuser=None ) :
        """Set the specified `ircchannels` for the project identified by,
        `project` which can be, 
            `id` or `projectname` or `Project` instance
        if append=True,
            Specified ircchannels will be added to project's existing 
            ircchannel list.
        if append=False,
            Existing ircchannels will be cleared and replaced by the
            specified ircchannels.
        if ircchannels == None,
            Delete project's all ircchannels."""
        from zeta.config.environment    import tlcomp, srchcomp

        ircobj = lambda ir : ( isinstance( ir, IRCChannel ) and ir ) \
                             or \
                             ( isinstance( ir, (str, unicode) ) and \
                               IRCChannel(ir) )

        project  = self.get_project( project )

        if ircchannels and not isinstance( ircchannels, list ) :
            ircchannels = [ ircchannels ]

        # Construct log based on mailing lists that have changed
        log      = ''
        loglines = [
            ( 'irc-channels',
              ', '.join([ irc.ircchannel for irc in project.ircchannels ]),
              ', '.join(filter( None,
                                [ ircobj( irc ).ircchannel
                                  for irc in (ircchannels or []) ]
                              )),
            )
        ]
        log = h.logfor( loglines )
        # End here

        irclists = []
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if append == False :
                project.ircchannels = []
            if ircchannels :
                irclists = [ ircobj( ir ) for ir in ircchannels ]
                if append :
                    project.ircchannels.extend( irclists )
                else :
                    project.ircchannels = irclists

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return irclists

    @h.postproc()
    def create_component( self, project, compdetail, update=False,
                          doclose=None, byuser=None ) :
        """Create project component for project identified by,
        `project` which can be, 
            `id` or `projectname` or `Project` instance.
        `compdetail` is a tuple of,
            ( compid, componentname, description, owner)
                `owner` can be `id` or `username` or `User` instance.
        if update=True,
            `compid` identifies `id` of PrjComponent.
            An existing project component identified by compid will be updated.
        else,
            `compid` can be None,

        Return,
            PrjComponent instance."""
        from zeta.config.environment    import userscomp, tlcomp, srchcomp

        log       = ''
        project   = self.get_project( project )
        component = (update and self.get_component( compdetail[0] )) or None
        owner     = compdetail[3] and userscomp.get_user( compdetail[3] )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            if (update and component) or component :
                # Construct log based on changing attributes
                loglines = [
                    ('component-name', component.componentname, compdetail[1])
                ]
                owner and loglines.append(
                            ( 'owner', getattr(component.owner, 'username', ''),
                              owner.username )
                          )
                loglines.append(('', component.description, compdetail[2]))
                log = h.logfor( loglines )
                if log :
                    log = "updated project component, `%s`\n%s" % \
                                ( component.componentname, log )
                # Ends here

                component.componentname   = compdetail[1]
                component.description     = compdetail[2]
                component.descriptionhtml = component.translate()
                owner and setattr( component, 'owner', owner )

            else :
                lastcomp = self._last_entry(project.components, 'comp_number')
                nextcompnum = (lastcomp and (lastcomp.comp_number + 1)) or 1
                component = PrjComponent(compdetail[1], nextcompnum, compdetail[2])
                owner and setattr(component, 'owner', owner)
                project.components.append(component)
                component.descriptionhtml = component.translate()

                # Construct log
                loglines = [ 'created new project component, `%s`' % compdetail[1],
                             'owner : %s' % getattr( owner, 'username', '-' ),
                           ]
                compdetail[2] and loglines.append( compdetail[2] )
                log = '\n'.join( loglines )
                # Logging ends here

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return component

                
    @h.postproc()
    def remove_component(self, project, component, doclose=None, byuser=None) :
        """Remove the component identified by,
        `component` which can be,
            `id` or `PrjComponent` instance.
        belonging to the project identified by,
        `project`, which can be,
            `id` or `projectname`."""
        from zeta.config.environment    import tlcomp, srchcomp

        log = ''
        project = self.get_project( project )
        component = self.get_component( component )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if isinstance( component, PrjComponent ) and \
               isinstance( project, Project ) :
                log = "deleted project component `%s`" % component.componentname
                project.components.remove( component )

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log) :
            log and tlcomp.log( byuser, log, project=project )
            log and srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return None


    @h.postproc()
    def create_milestone( self, project, mstndetail, update=False,
                          doclose=None, byuser=None ) :
        """Create project milestone for project identified by,
        `project` which can be, 
            `id` or `projectname` or `Project` instance.
        `mstndetail` is a tuple of,
            (mstnid, milestonename, description, due_date)
        if update=True,
            `mstnid` identifies `id` of Milestone.
            An existing project milestone identified by mstnid will be updated.
        else,
            `mstnid` can be None.

        Return,
            Milestone instance."""
        from zeta.config.environment    import tlcomp, srchcomp

        log = ''
        project = self.get_project( project )
        milestone = (update and self.get_milestone( mstndetail[0] )) or None
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if ( update and milestone ) or milestone :
                # Construct log based on changing attributes
                loglines = [
                    ('milestone-name', milestone.milestone_name, mstndetail[1])
                ]
                mstndetail[3] != None and loglines.append( 
                                ('due_date', milestone.due_date, mstndetail[3])
                             )
                loglines.append(('', milestone.description, mstndetail[2]))
                log = h.logfor( loglines )
                if log :
                    log = "updated project milestone `%s`\n%s" % \
                                ( milestone.milestone_name, log )
                # Logging logic till here

                milestone.milestone_name = mstndetail[1]
                milestone.description    = mstndetail[2]
                if milestone.description :
                    milestone.descriptionhtml= milestone.translate()
                if mstndetail[3] :
                    milestone.due_date = mstndetail[3]
                elif mstndetail[3] != None :
                    milestone.due_date = None

            else :
                lastmstn    = self._last_entry( project.milestones, 'mstn_number' )
                nextmstnnum = (lastmstn and (lastmstn.mstn_number + 1)) or 1
                milestone   = Milestone( mstndetail[1], nextmstnnum, mstndetail[2])
                mstndetail[3] and setattr( milestone, 'due_date', mstndetail[3] )
                if milestone.description :
                    milestone.descriptionhtml = milestone.translate()
                project.milestones.append( milestone )

                # Construct log based on changing attributes
                loglines = [ 'created new project milestone, `%s`' % mstndetail[1],
                             'due_date : %s' % (mstndetail[3] or '-'),
                           ]
                mstndetail[2] and loglines.append( "%s" % mstndetail[2] )
                log = '\n'.join( loglines )
                # Loggind ends here

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return milestone


    @h.postproc()
    def close_milestone( self, milestone, closing_remark=None,
                         status='completed', doclose=None, byuser=None ) :
        """Close milestone identified by,
        `milestone` which can be,
            `id` or `Milestone` instance.
        default status for closing milestone is
            status='completed', status can also be 'cancelled'"""
        from zeta.config.environment import tlcomp, srchcomp

        log = ''
        msession = meta.Session()
        milestone = self.get_milestone( milestone, attrload=[ 'project' ] )
        with msession.begin( subtransactions=True ) :
            if milestone :
                milestone.closing_remark     = closing_remark
                if milestone.closing_remark :
                    milestone.closing_remarkhtml = milestone.crtranslate()
                setattr( milestone, 'completed', False )
                setattr( milestone, 'cancelled', False )
                setattr( milestone, status, True )

                # Construct log based on changing attributes
                loglines = [
                             'Closing milestone, `%s`' % milestone.milestone_name,
                             'status : %s' % status,
                           ]
                closing_remark and loglines.append( closing_remark )
                log = '\n'.join( loglines )
                # Loggind ends here

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, milestone, byuser, log ) :
            log and tlcomp.log( byuser, log, project=milestone.project )
            srchcomp.indexproject( [milestone.project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, milestone, byuser, log ))
        return None

    @h.postproc()
    def open_milestone( self, milestone, closing_remark=None, doclose=None,
                        byuser=None ) :
        """Open milestone identified by,
        `milestone` which can be,
            `id` or `Milestone` instance."""
        from zeta.config.environment import tlcomp, srchcomp

        log       = ''
        msession  = meta.Session()
        milestone = self.get_milestone( milestone, attrload=[ 'project' ] )
        index     = False
        with msession.begin( subtransactions=True ) :
            if milestone and (milestone.completed or milestone.cancelled) :
                setattr( milestone, 'completed', False )
                setattr( milestone, 'cancelled', False )

                # Construct log message
                loglines = [ 'Re-opened milestone, `%s`' % milestone.milestone_name
                           ]

                if (closing_remark != None) and \
                   (closing_remark != milestone.closing_remark) :
                    milestone.closing_remark = closing_remark
                    milestone.closing_remarkhtml = milestone.crtranslate()
                    loglines.append( closing_remark )
                    index = True

                log = '\n'.join( loglines )

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, milestone, byuser, log ) :
            log and tlcomp.log( byuser, log, project=milestone.project )
            srchcomp.indexproject( [milestone.project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, milestone, byuser, log ))
        return None


    @h.postproc()
    def remove_milestone( self, project, milestone, doclose=None, byuser=None ) :
        """Remove the milestone identified by,
        `milestone` which can be,
            `id` or `milestone_name` or `Milestone` instance.
        belonging to the project identified by,
        `project`, which can be,
            `id` or `projectname`."""
        from zeta.config.environment    import tlcomp, srchcomp

        log       = ''
        project   = self.get_project( project )
        milestone = self.get_milestone( milestone )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            if isinstance( milestone, Milestone ) and \
               isinstance( project, Project ) :
                log = "deleted project milestone `%s`" % milestone.milestone_name
                project.milestones.remove( milestone )

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            log and tlcomp.log( byuser, log, project=project )
            log and srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return None

    @h.postproc()
    def create_version( self, project, verdetail, update=False,
                        doclose=None, byuser=None ) :
        """Create project version for project identified by,
        `project` which can be, 
            `id` or `projectname` or `Project` instance.
        `verdetail` is a tuple of,
            (verid, version_name, description)
        if update=True,
            `verid` identifies the `id` of Version.
            An existing project milestone identified by `verid` will be updated.

        Return,
            Version instance."""
        from zeta.config.environment    import tlcomp, srchcomp

        log      = ''
        msession = meta.Session()
        project  = self.get_project( project )
        version  = (update and self.get_version( verdetail[0] )) or None
        with msession.begin( subtransactions=True ) :
            if (update and version) or version :
                # Construct log based on changing attributes
                loglines = [
                    ( 'version-name', version.version_name, verdetail[1] ),
                    ( '', version.description, verdetail[2] )
                ]
                log = h.logfor( loglines )
                if log :
                    log = "updated project version, `%s`\n%s" % \
                                ( version.version_name, log )
                # Logging logic till here

                version.version_name = verdetail[1]
                version.description  = verdetail[2]
                if version.description :
                    version.descriptionhtml = version.translate()

            else :
                lastver    = self._last_entry( project.versions, 'ver_number' )
                nextvernum = (lastver and (lastver.ver_number + 1)) or 1
                version    = Version( verdetail[1], nextvernum, verdetail[2])
                if version.description :
                    version.descriptionhtml = version.translate()
                project.versions.append( version )

                # Construct log based on changing attributes
                loglines = [ 'created new project version, `%s`' % verdetail[1] ]
                verdetail[2] and loglines.append( "%s" % verdetail[2] )
                log = '\n'.join( loglines )
                # Loggind ends here

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return version


    @h.postproc()
    def remove_version( self, project, version, doclose=None, byuser=None ) :
        """Remove the version identified by,
        `version` which can be,
            `id` or `version_name` or `Version` instance.
        belonging to the project identified by,
        `project`, which can be,
            `id` or `projectname`."""
        from zeta.config.environment    import tlcomp, srchcomp

        log      = ''
        project  = self.get_project( project )
        version  = self.get_version( version )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if isinstance( version, Version ) and \
               isinstance( project, Project ) :
                log = "deleted project version `%s`" % version.version_name
                project.versions.remove( version )

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log) :
            log and tlcomp.log( byuser, log, project=project )
            log and srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return None


    @h.postproc()
    def add_project_permission( self, project, touser, perm_group, doclose=None,
                                byuser=None ) :
        """Add the permission `perm_group` to user specified by `touser`
        for project identified by,
        `project` which can be,
            `id` or `projectname` or `Project` instance.
        `touser` can be,
            `id` or `username` or `User` instance.
        `perm_group` can be,
            `id` or `perm_group` or `PermissionGroup` instance.
        """
        from zeta.config.environment    import userscomp, tlcomp

        touser    = userscomp.get_user( touser )
        perm_group= userscomp.get_permgroup( perm_group )
        pp        = None
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            pp           = ProjectPerm()
            pp.project   = self.get_project( project )
            pp.user      = touser
            pp.permgroup = perm_group
            msession.add( pp )

        log = 'added permission `%s` to user `%s`' % \
                        ( perm_group.perm_group, touser.username )

        # Post processing, optional deferred handling
        def onclose(tlcomp, pp, byuser, log ) :
            tlcomp.log( byuser, log, project=pp.project )
        doclose( h.hitchfn( onclose, tlcomp, pp, byuser, log ))
        return pp


    @h.postproc()
    def remove_project_permission( self, prjuserperms, doclose=None,
                                   byuser=None ) :
        """Remove project permissions identified by 
        `prjuserperms` which can be,
            `id` or `ProjectPerm` instance or
            list of `id` or `ProjectPerm` instances."""
        from zeta.config.environment    import tlcomp

        if not isinstance( prjuserperms, list ) :
            prjuserperms = [ prjuserperms ]

        prjuserperms = [ self.get_projectperm( pp ) for pp in prjuserperms ]
        logs = []
        pp = None
        msession     = meta.Session()
        with msession.begin( subtransactions=True ) :
            for pp in prjuserperms :
                if pp :
                    logs.append(
                        'deleted permissions `%s` from user `%s` in project `%s`' % \
                            ( pp.permgroup.perm_group, pp.user.username, 
                              pp.project.projectname )
                    )
                    msession.delete( pp )
            project = pp and pp.project or None

        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser, logs ) :
            kwargs = {}
            project and kwargs.setdefault( 'project', project )
            logs and tlcomp.log( byuser, '\n'.join(logs), **kwargs )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, logs ))
        return None


    @h.postproc()
    def add_projectteam_perm( self, project, teamtype, perm_groups,
                              doclose=None, byuser=None ) :
        """Add the permission `perm_groups` to the project team specified by
        `project` which can be,
            `id` or `projectname` or `Project` instance.
        `teamtype` for project identified by,
            `id` or `team_type` or `ProjectTeam_Type` instance.
        `perm_groups` can be a list of,
            `id` or `perm_group` or `PermissionGroup` instance."""
        from zeta.config.environment    import userscomp, tlcomp

        if not isinstance( perm_groups, list ) :
            perm_groups = [ perm_groups ]

        teamtype   = self.get_teamtype( teamtype )
        project    = self.get_project( project )
        perm_groups= [ userscomp.get_permgroup(
                            perm_group, attrload=['perm_names']
                       ) for perm_group in perm_groups ]
        msession   = meta.Session()
        ptps = []
        with msession.begin( subtransactions=True ) :
            for perm_group in perm_groups :
                perm_names = [ p.perm_name for p in perm_group.perm_names ]
                # If the permission name to be added is in global context
                # (site-level) then flag an exception.
                sitepnames = list(set(userscomp.site_permnames
                                     ).intersection(set(perm_names)))
                if sitepnames :
                    raise ZetaProjectError(
                        "Cannot add site level permission names %s to project teams !!"\
                                % sitepnames )

                else :
                    ptp           = ProjectTeam_Perm()
                    ptp.teamtype  = teamtype
                    ptp.permgroup = perm_group
                    ptp.project   = project
                    msession.add( ptp )
                    ptps.append( ptp )

        log = ''
        if perm_groups :
            log = 'added permissions, `%s` to team `%s`' % (
                        ', '.join([ pg.perm_group for pg in perm_groups ]),
                        teamtype.team_type
                  )

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_teamperms )
        def onclose(tlcomp, project, byuser, log ) :
            log and tlcomp.log( byuser, log, project=project )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, log ))
        return ptps


    @h.postproc()
    def remove_projectteam_perm(self, prjteamperms, doclose=None, byuser=None):
        """Remove project team permissions identified by,
        `prjteamperms` which can be,
            `id` or `ProjectTeam_Perm` instance or
            list of `id` or `ProjectTeam_Perm` instances."""
        from zeta.config.environment    import tlcomp

        if not isinstance( prjteamperms, list ) :
            prjteamperms = [ prjteamperms ]

        prjteamperms = [ self.get_projectteamperm( ptp ) for ptp in prjteamperms ]
        msession     = meta.Session()
        pgforlog     = {}
        with msession.begin( subtransactions=True ) :
            for ptp in prjteamperms :
                if ptp :
                    pgforlog.setdefault( ptp.teamtype.team_type, [] 
                                       ).append( ptp.permgroup.perm_group )
                    project = ptp.project
                    msession.delete( ptp )

        log = ''
        if pgforlog :
            log = '\n'.join(
                    [ 'deleted permission, `%s`, from team `%s`' % (
                            ', '.join( pgforlog[tt] ), tt
                      ) for tt in pgforlog ]
                  )
        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_teamperms )
        def onclose(tlcomp, project, byuser, log ) :
            tlcomp.log( byuser, log, project=project )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, log ))
        return None


    @h.postproc()
    def add_project_user( self, project, teamtype, addusers, doclose=None,
                          byuser=None ) :
        """Add user to project identified by,
        `project` which can be,
            `id` or `projectname` or `Project` instance.
        under the team identified by,
        `teamtype`, which can be,
            `id` or `team_type` or ProjectTeam_Type instance.
        `addusers` can be a list of one or more,
            `id` or `username` or `User` instance."""
        from zeta.config.environment    import userscomp, tlcomp, srchcomp

        if not isinstance( addusers, list ) :
            addusers = [ addusers ]

        project   = self.get_project( project )
        teamtype  = self.get_teamtype( teamtype )
        addusers  = [ userscomp.get_user(u) for u in addusers ]
        msession  = meta.Session()
        pts = []
        with msession.begin( subtransactions=True ) :
            for adduser in addusers :
                pt          = ProjectTeam()
                pt.user     = adduser
                pt.project  = project
                pt.teamtype = teamtype
                msession.add( pt )
                pts.append( pt )

        log = ''
        if addusers :
            log = 'added users, `%s` to team `%s`' % ( 
                        ', '.join([ u.username for u in addusers ]),
                        teamtype.team_type 
                  )
        project = addusers and pts[-1].project

        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_teamperms )
        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            log and tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return pts

    @h.postproc()
    def approve_project_user( self, project=None, user=None, teamtype=None,
                              projectteam=None, approve=True, doclose=None ) :
        """Approve the projectteam entry identified by,
        `projectteam` which can be,
        `id` or `ProjectTeam` instance.
        (or)
        for all the entries identified by
        `project` which can be,
           `id` or `projectname` or `Project` instance.
        (or)
        for all the entries identified by
        `user` which can be,
            `id` or `username` or `User` instance.
        (or)
        for all the entries identified by
        `teamtype` which can be,
            `id` or `team_type` or ProjectTeam_Type instance."""
        from zeta.config.environment    import userscomp

        projectteam = self.get_projectteam( projectteam=projectteam,
                                            project=project,
                                            teamtype=teamtype,
                                            user=user
                                          )
        msession    = meta.Session() 
        with msession.begin( subtransactions=True ) :
            if isinstance( projectteam, ProjectTeam ) :
                projectteam.approved = approve
            else :
                [ setattr( pt, 'approved', approve ) for pt in projectteam ]

        # Database Post processing
        cache.invalidate( self.mapfor_teamperms )

                
    @h.postproc()
    def remove_project_users( self, projectteams, doclose=None, byuser=None ) :
        """Remove project team identified by,
        `projectteams` which can be,
            `id` or `ProjectTeam` instance or
            list of `id` or `ProjectTeam` instances."""
        from zeta.config.environment    import tlcomp, srchcomp

        if not isinstance( projectteams, list ) :
            projectteams = [ projectteams ]

        projectteams = [ self.get_projectteam( pt ) for pt in projectteams ]
        usrforlog    = {}
        msession     = meta.Session()
        with msession.begin( subtransactions=True ) :
            for pt in projectteams :
                if pt :
                    usrforlog.setdefault( pt.teamtype.team_type, [] 
                                        ).append( pt.user.username )
                    project = pt.project
                    msession.delete( pt )

        log = ''
        if usrforlog :
            log = '\n'.join(
                    [ 'deleted users, `%s`, from team `%s`' % (
                            ', '.join( usrforlog[tt] ), tt
                      ) for tt in usrforlog ]
                  )
        # Post processing, optional deferred handling
        cache.invalidate( self.mapfor_teamperms )
        def onclose(tlcomp, pt, byuser, log ) :
            tlcomp.log( byuser, log, project=pt.project )
            srchcomp.indexproject( [pt.project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, pt, byuser, log ))
        return None
                                      

    @h.postproc()
    def add_tags( self, project, entity=None, id=None, tags=[], doclose=None,
                  byuser=None ) :
        """Get tags for project, project-component, project-milestone,
        project-version.
        `project` can be,
            id` or `projectname` or `Project` instance.
        if entity='component'
            id can be `id` or `Component` instance.
        if entity='milestone'
            id can be `id` or `Milestone` instance.
        if entity='version'
            id can be `id` or `Version` instance.
        if entity=None
            id is not considered and the tags are added to the project.
        add tags specified by `tagnames`."""
        from zeta.config.environment    import tlcomp, srchcomp, tagcomp

        project  = self.get_project( project )
        if entity == 'component' :
            modelobj = self.get_component( id )
            log      = 'to component `%s`' % modelobj.componentname

        elif entity == 'milestone' :
            modelobj = self.get_milestone( id )
            log      = 'to milestone `%s`' % modelobj.milestone_name

        elif entity == 'version' :
            modelobj = self.get_version( id )
            log      = 'to version `%s`' % modelobj.version_name

        elif entity == None :
            modelobj = project
            log      = 'to project'

        if modelobj :
            addtags = tagcomp.model_add_tags( tags, modelobj, byuser=byuser )
            log     = "%s, added tags, `%s`" % (log, ', '.join( addtags ))

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return None

    @h.postproc()
    def remove_tags( self, project, entity=None, id=None, tags=[],
                     doclose=None, byuser=None ) :
        """Remove Tags for project, project-component, project-milestone,
        project-version.
        `project` can be,
            `id` or `projectname` or `Project` instance.
        if entity='component'
            id can be `id` or `componentname` or `Component` instance.
        if entity='milestone'
            id can be `id` or `milestone_name` or `Milestone` instance.
        if entity='version'
            id can be `id` or `version_name` or `Version` instance.
        if entity=None
            id is not considered and the tags are removed from project."""
        from zeta.config.environment    import tlcomp, srchcomp, tagcomp

        project  = self.get_project( project )
        if entity == 'component' :
            modelobj = self.get_component( id )
            log      = 'from component `%s`' % modelobj.componentname

        elif entity == 'milestone' :
            modelobj = self.get_milestone( id )
            log      = 'from milestone `%s`' % modelobj.milestone_name

        elif entity == 'version' :
            modelobj = self.get_version( id )
            log      = 'from version `%s`' % modelobj.version_name

        elif entity == None :
            modelobj = project
            log      = 'from project'

        if modelobj :
            rmtags = tagcomp.model_remove_tags( tags, modelobj, byuser=byuser )
            log    = "%s, deleted tags, `%s`" % (log, ', '.join( rmtags ))

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, project, byuser, log ) :
            tlcomp.log( byuser, log, project=project )
            srchcomp.indexproject( [project], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, project, byuser, log ))
        return None


    @h.postproc()
    def add_attach( self, project, attach, doclose=None, byuser=None ) :
        """Add attachment to the project identified by,
        `project` can be,
            `id` or `projectname` or `Project` instance.
        `attach` can be
            `id` or `resource_url` or `Attachment` instance."""
        from zeta.config.environment    import tlcomp, attachcomp

        project    = self.get_project( project )
        attach     = attachcomp.get_attach( attach )
        project and attachcomp.model_add_attach( attach, project, byuser=byuser)

        log = 'uploaded attachment `%s`' % attach.filename

        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser, log ) :
            tlcomp.log( byuser, log, project=project )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, log ))
        return None

    @h.postproc()
    def remove_attach( self, project, attach, doclose=None, byuser=None ) :
        """Remove attachment to the project identified by,
        `project` can be,
            `id` or `projectname` or `Project` instance.
        `attach` can be
            `id` or `resource_url` or `Attachment` instance."""
        from zeta.config.environment    import tlcomp, attachcomp

        project    = self.get_project( project )
        attach     = attachcomp.get_attach( attach )
        project and attachcomp.model_remove_attach( attach, project,
                                                    byuser=byuser )

        log = 'deleted attachment `%s`' % attach.filename

        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser, log ) :
            tlcomp.log( byuser, log, project=project )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, log ))
        return None


    @h.postproc()
    def upgradewiki( self, doclose=None, byuser=None ) :
        """Upgrade the database fields supporting wiki markup to latest
        zwiki version"""
        from zeta.config.environment    import tlcomp

        projects   = self.get_project( attrload=['project_info'] )
        components = self.get_component()
        milestones = self.get_milestone()
        versions   = self.get_version()
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            for project in projects :
                pinfo                 = project.project_info
                pinfo.descriptionhtml = pinfo.translate()
                for comp in components :
                    comp.descriptionhtml = comp.translate()
                for mstn in milestones :
                    mstn.descriptionhtml    = mstn.translate()
                    mstn.closing_remarkhtml = mstn.crtranslate()
                for ver in versions :
                    ver.descriptionhtml  = ver.translate()
        
        log = "Upgraded project wiki fields to latest wiki version"

        # Post processing, optional deferred handling
        def onclose(tlcomp, byuser, log ) :
            tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return ( len(projects), len(components), len(milestones), len(versions) )


    # Doc - metadata for 'project' table entries
    def documentof( self, project, search='xapian' ) :
        """Make a document for 'project' entry to create a searchable index
            [ metadata, attributes, document ], where

            metadata   : { key, value } pairs to be associated with document
            attributes : searchable { key, value } pairs to be associated with
                         document
            document   : [ list , of, ... ] document string, with increasing
                         weightage
        """
        project   = self.get_project(
                            project,
                            attrload=[
                                'project_info', 'tags', 'license',
                                'mailinglists', 'ircchannels', 'milestones',
                                'components', 'versions',
                            ]
                    )
        projusers = self.projusernames( project )
        tagnames  = [ t.tagname for t in project.tags ]
        license   = project.license and project.license.licensename or ''

        metadata = { 'doctype'     : 'project',
                     'id'          : project.id,
                     'projectname' : project.projectname
                   }
           
        attributes = \
            search == 'xapian' and \
                [ 'XID:project_%s'  % project.id,                   # id
                  'XPROJECT:%s'     % project.projectname,          # project
                  'XLICENSE:%s'     % license,                      # license
                  'XEMAIL:%s'       % project.admin_email,          # email
                ] + \
                [ 'XUSER:%s'        % u                             # user
                  for u in projusers ] + \
                [ 'XTAG:%s'         % t                             # tag
                  for t in tagnames ] \
            or \
                []

        attrs = ' '.join(
                    [ project.projectname, license, project.admin_email ] +\
                    projusers                                             +\
                    tagnames
                )
        document = [
                ' '.join([
                    project.project_info.description,
                    ' '.join([ co.description for co in project.components ]),
                    ' '.join([ '%s %s' % ( m.description, m.closing_remark )
                               for m in project.milestones ]),
                    ' '.join([ v.description for v in project.versions ]),
                ]),
                ' '.join([
                    project.summary,
                    ' '.join([ co.componentname for co in project.components ]),
                    ' '.join([ m.milestone_name for m in project.milestones ]),
                    ' '.join([ v.version_name for v in project.versions ]),
                    ' '.join([ m.mailing_list for m in project.mailinglists ]),
                    ' '.join([ i.ircchannel for i in project.ircchannels ]),
                ]),
                attrs
        ]

        return [ metadata, attributes, document ]

    # Data Crunching methods on project database.

    def _projectnames( self ) :
        stmt = select([ t_project.c.projectname ], bind=meta.engine)
        return [ tup[0] for tup in stmt.execute().fetchall() if tup[0] ]

    def _projectstatus( self, projects=[] ) :
        """UnSorted dictionary of disabled and enabled `projectnames`"""
        d       = { 'enabled' : [], 'disabled' : [] }
        lookup  = [ 'enabled', 'disabled' ]

        if projects :
            [ d[ lookup[ p.disabled ] ].append( p.projectname )
              for p in projects ]

        else :
            stmt   = select( [ t_project.c.projectname, t_project.c.disabled ],
                             bind=meta.engine
                           )
            [ d[ lookup[ tup[1] ] ].append( tup[0] )
              for tup in stmt.execute().fetchall() if tup[0] ]

        return d

    def _disabledprojs( self ) :
        msession = meta.Session()
        projects = msession.query( Project ).filter_by(
                        disabled=True ).order_by( Project.projectname ).all()
        return [ p.projectname for p in projects ]
        # return [ prj.projectname for prj in self.get_project() if prj.disabled ]

    def _enabledprojs( self ) :
        msession = meta.Session()
        projects = msession.query( Project ).filter_by(
                        disabled=False ).order_by( Project.projectname ).all()
        return [ p.projectname for p in projects ]
        # return [ prj.projectname for prj in self.get_project() if not prj.disabled ]

    def _exposedprojs( self ) :
        msession = meta.Session()
        projects = msession.query( Project ).filter_by(
                        exposed=True ).order_by( Project.projectname ).all()
        return [ p.projectname for p in projects ]
        # return [ prj.projectname for prj in self.get_project() if prj.exposed ]

    def _privateprojs( self ) :
        msession = meta.Session()
        projects = msession.query( Project ).filter_by(
                        exposed=False ).order_by( Project.projectname ).all()
        return [ p.projectname for p in projects ]
        # return [ prj.projectname for prj in self.get_project() if not prj.exposed ]

    def _compnames( self ) :
        return [ comp.componentname for comp in self.get_component() ]

    def _mstnnames( self ) :
        return [ m.milestone_name for m in self.get_milestone() ]

    def _vernames( self ) :
        return [ v.version_name for v in self.get_version() ]

    def _teams( self ) :
        return [ t.team_type for t in self.get_teamtype() ]

    def pstatus( self, projects ) :
        """Alternate API to crunch projectstatus by passing a prefetched list of
        projects from DB"""
        return self._projectstatus( projects=projects )

    def projectteams( self, project, teamnames=[], usernames=[], noquery=False ) :
        """Get a consolidated team for project identified by.
        `project` which can be
            `id` or `projectname` or `Project` instance."""
        from zeta.config.environment    import userscomp

        users = set( usernames or userscomp.usernames )
        project = self.get_project( project )
        teams = dict([ ( tt, [] ) for tt in (teamnames or self.teams) ])

        oj = t_project.outerjoin(
                        t_project_team,
                        t_project.c.id == t_project_team.c.project_id
                     ).outerjoin(
                        t_projectteam_type,
                        t_project_team.c.teamtype_id == t_projectteam_type.c.id
                     ).outerjoin(
                        t_user,
                        t_project_team.c.user_id == t_user.c.id
                     )

        q  = select( [ t_project_team.c.id, t_projectteam_type.c.team_type,
                       t_user.c.username ],
                     bind=meta.engine
                   ).select_from( oj
                   ).where( t_project.c.id == project.id )

        tups = q.execute().fetchall()

        [ teams[ team_type ].append(( pt_id, username ))
          for pt_id, team_type, username in tups if pt_id ]

        teams_ = {}
        for tt in teams :
            usersids = list( set( teams[tt] ))
            usersids = sorted( teams[tt], key=lambda x : x[1] )
            x_users = users.difference( set( map( lambda x : x[1], usersids )) )
            x_users = sorted( list( x_users ))
            teams_[tt] = [ usersids, x_users ]
        return teams_

    def teamperms( self, project, teamnames=[], noquery=False ) :
        """Get a consolidated permissions for project teams identified by,
        `project` which can be,
            `id` or `projectname` or `Project` instance."""
        from zeta.config.environment    import userscomp

        project = self.get_project( project )
        teams = dict([ ( tt, [] ) for tt in (teamnames or self.teams) ])
        pnames = dict([ ( tt, [] ) for tt in (teamnames or self.teams) ])

        oj = t_project.outerjoin(
                        t_projectteam_perm,
                        t_project.c.id == t_projectteam_perm.c.project_id
                     ).outerjoin(
                        t_projectteam_type,
                        t_projectteam_perm.c.teamtype_id == t_projectteam_type.c.id
                     ).outerjoin(
                        t_permission_group,
                        t_projectteam_perm.c.perm_group_id == t_permission_group.c.id
                     ).outerjoin(
                        at_permission_maps,
                        t_projectteam_perm.c.perm_group_id == at_permission_maps.c.groupid
                     ).outerjoin(
                        t_permission_name,
                        at_permission_maps.c.permid == t_permission_name.c.id
                     )

        q  = select( [ t_projectteam_perm.c.id, t_projectteam_type.c.team_type,
                       t_permission_group.c.perm_group,
                       t_permission_name.c.perm_name ],
                     bind=meta.engine
                   ).select_from( oj
                   ).where( t_project.c.id == project.id )

        tups = q.execute().fetchall()
        
        # Expand permission groups into permission names
        [ teams[ team_type ].append(
               ( ptp_id, userscomp.normalize_perms( perm_group ) )
          ) for ptp_id, team_type, perm_group, perm_name in tups if ptp_id ]
        [ pnames[ team_type ].append( perm_name )
          for ptp_id, team_type, perm_group, perm_name in tups if ptp_id ]

        prjpnames = userscomp.mixedpnames
        prjpnames_ = set(prjpnames)
        [ prjpnames_.remove(pn) for pn in userscomp.site_permnames ]
        teams_ = {}
        for tt in teams :
            teams[tt] = list(set( teams[tt] ))
            permsids = sorted( teams[tt], key=lambda x : x[1] )
            # When a permission name is part of a permission group that
            # the user has, then that permission name is removed from the
            # list of addable-permissions.
            x_perms = prjpnames_.difference(
                            set( map( lambda x : x[1], teams[tt] ))
                      )
            [ x_perms.remove( p ) for p in set(pnames[tt]) if p in x_perms  ]
            x_perms = sorted(list( x_perms ))
            teams_[tt] = [ permsids, x_perms ] 
        return teams_

    @cache.cache( 'mapfor_teamperms', useargs=False )
    def mapfor_teamperms( self ) :
        """Generate the permission map for project teams"""
        from zeta.config.environment    import userscomp

        maps = {}
        teams = self.teams
        projects = self.get_project(
                        attrload_all=[
                            'projteamperms.permgroup.perm_names',
                            'projteamperms.teamtype'
                        ]
                   )
        for proj in projects :
            ptmap = dict([ ( (proj.projectname, t), [] ) for t in teams ])
            for ptp in proj.projteamperms :
                pnames = [ pn.perm_name for pn in ptp.permgroup.perm_names ]
                ptmap[(proj.projectname, ptp.teamtype.team_type)].extend(
                        pnames 
                )
            maps.update( ptmap )
        return maps

    @cache.cache( 'mapfor_projadmins', useargs=False )
    def mapfor_projadmins( self ) :
        """Generate the permission map for project administrators"""
        from zeta.config.environment    import userscomp

        perms = [ 'PMS_PROJECT_ADMIN' ] + userscomp.proj_permnames

        oj = t_project.outerjoin(
                        at_project_admins,
                        t_project.c.id == at_project_admins.c.projectid
                     ).outerjoin(
                        t_user,
                        at_project_admins.c.adminid == t_user.c.id
                     )
        q = select( [ t_project.c.projectname, t_user.c.username ],
                    bind=meta.engine
                  ).select_from( oj )
        
        tups = q.execute().fetchall() 
        res = set([ (tup[0], tup[1]) for tup in tups if tup[0] and tup[1] ])

        maps = dict( map( lambda x : (x, perms), res ))
        return maps

    # TODO : Deprecated
    def projectuserperms( self, project ) :
        """Get a consolidated permissions for project users identified by,
        `project` which can be,
            `id` or `projectname` or `Project` instance."""
        from zeta.config.environment    import userscomp

        project   = self.get_project( project )

        projusers = sorted(list(set( 
                        [ pt.user.username for pt in project.team ]
                    )))

        uperms = dict([ ( u, [] ) for u in projusers ])
        # Expand permission groups into permission names
        pnames = dict([ ( u, [] ) for u in projusers ])
        [( uperms.setdefault( pup.user.username, [] ).append(
                [ pup.id,
                  userscomp.normalize_perms( pup.permgroup.perm_group )
                ]
           ),
           pnames.setdefault( pup.user.username, [] ).extend(
               [ p.perm_name for p in pup.permgroup.perm_names ]
           )
         ) for pup in project.projectperms ]
        for projuser in uperms :
            permsids = sorted( uperms[projuser], key=lambda x : x[1] )
            x_permissions = sorted(list(
                                set( userscomp.mixedpnames ).difference(
                                    set(map(lambda x : x[1], uperms[projuser]))
                                )
                            ))
            # When a permission name is part of a permission group that
            # the user has, then that permission name is removed from the
            # list of addable-permissions.
            [ x_permissions.remove( p )
              for p in pnames[projuser] if p in x_permissions  ]
            uperms[projuser] = [ permsids, x_permissions ]
        return uperms

    # TODO : Deprecated
    def userpermissions( self, user, project ) :
        """Calculate the list of permission names for the user, based on the
        following algorithm,

        The permission name should be present at,
            site level user pemission,
            Project team permission to which the user belongs to,
            Project level user permission"""
        from zeta.config.environment    import userscomp

        user      = userscomp.get_user( user )
        project   = self.get_project( project )
        spnames   = set(userscomp.user_permnames( user ))
        msession  = meta.Session()

        pteams  = msession.query( ProjectTeam ).filter(
                        and_( ProjectTeam.user_id == user.id,
                              ProjectTeam.project_id == project.id )
                  )
        teams   = [ pt.teamtype for pt in pteams.all() ]
        tpnames = []
        for team in teams :
            ptperms  = msession.query( ProjectTeam_Perm ).filter(
                           and_( ProjectTeam_Perm.teamtype_id == team.id,
                                 ProjectTeam_Perm.project_id == project.id )
                       )
            tpnames.extend([ pn.perm_name for ptp in ptperms
                                         for pn in ptp.permgroup.perm_names ])
        tpnames = set( tpnames )

        puperms = msession.query( ProjectPerm ).filter(
                        and_( ProjectPerm.user_id == user.id,
                              ProjectPerm.project_id == project.id )
                  )
        upnames = set([ pn.perm_name for pup in puperms
                                    for pn in pup.permgroup.perm_names ])

        permnames = list(
                        spnames.intersection( tpnames ).intersection( upnames )
                    )
        return permnames

    def prjcompnames( self, p ) :
        return [ comp.componentname for comp in self.get_component( project=p ) ] 

    def prjmstnnames( self, p ) :
        return [ m.milestone_name for m in self.get_milestone( project=p ) ] 

    def prjvernames( self, p  ) :
        return [ v.version_name for v in self.get_version( project=p ) ] 

    def projusernames( self, p, noquery=False ) :
        """All users (usernames) member of this project"""

        oj = t_project.outerjoin( t_project_team 
                     ).outerjoin(
                        t_user,
                        t_project_team.c.user_id == t_user.c.id
                     )
        res = []
        if isinstance( p, (int, long)) :
            q = select( [ t_user.c.username ], bind=meta.engine
                      ).select_from( oj 
                      ).where( t_project.c.id == p )
            res = list(set([ tup[0] for tup in q.execute().fetchall() if tup[0] ]))

        elif isinstance( p, (str, unicode)) :
            q = select( [ t_user.c.username ], bind=meta.engine
                      ).select_from( oj 
                      ).where( t_project.c.projectname == p )
            res = list(set([ tup[0] for tup in q.execute().fetchall() if tup[0] ]))

        elif isinstance( p, Project ) :
            q = select( [ t_user.c.username ], bind=meta.engine
                      ).select_from( oj 
                      ).where( t_project.c.id == p.id )
            res = list(set([ tup[0] for tup in q.execute().fetchall() if tup[0] ]))

        return filter( None, res )

    def project_exists( self, projectname ) :
        return bool( self.get_project( projectname ))

    def userinteams( self, project, username ) :
        teams  = self.projectteams( project )
        uteams = [ t for t in teams for u in teams[t][0] if u[1] == username ]
        return uteams

    def projticketlist( self, project ) :
        return project

    def checkfavorite( self, pid, uid ) :
        """Check whether the project `pid` is a favorite of user `uid`"""
        oj = t_user.join( at_project_favorites ).join( t_project )
        q  = select( [ t_user.c.id, t_project.c.id ],
                         bind=meta.engine
                       ).select_from( oj 
                       ).where( t_project.c.id == pid 
                       ).where( t_user.c.id == uid )
        return bool( q.execute().fetchone() )

    def projectdetails( self, project ) :
        """Obtain 
            [ { <compid> : <componentname>, ... },
              { <mstnid> : <milestonename>, ... },
              { <verid>  : <versionname>, ...   },
              [ username, ... ]
            ]
        """
        oj = t_project.outerjoin( t_component,
                     ).outerjoin( t_milestone,
                     ).outerjoin( t_version,
                     ).outerjoin( t_project_team,
                     ).outerjoin( t_user )

        q  = select( [ t_project.c.id,
                       t_component.c.id, t_component.c.componentname,
                       t_milestone.c.id, t_milestone.c.milestone_name,
                       t_version.c.id,   t_version.c.version_name,
                       t_project_team.c.id, t_user.c.username
                     ],
                     bind=meta.engine
                   ).select_from( oj )
        qw = None
        if isinstance( project, (int, long) ) :
            qw = q.where( t_project.c.id == project )
        elif isinstance( project, (str, unicode) ) :
            qw = q.where( t_project.c.projectname == project )
        elif isinstance( project, Project ) :
            qw = q.where( t_project.c.id == project.id )
        
        d = [{}, {}, {}, [] ]   # components, milestones, versions, pusers
        if qw != None :
            comps = {}; mstns = {}; vers = {}; pusers = {}
            entries = qw.execute().fetchall() 
            for tup in entries :
                if not tup[0] : continue
                tup[1] and comps.setdefault( tup[1], tup[2] )
                tup[3] and mstns.setdefault( tup[3], tup[4] )
                tup[5] and vers.setdefault( tup[5], tup[6] )
                tup[7] and pusers.setdefault( tup[7], tup[8] )
            d = [ comps, mstns, vers, list(set(pusers.values())) ]

        return d
        
    def attachments( self, project ) :
        """Collect attachment list for project,
        Return attachments"""

        oj = t_project.outerjoin( at_project_attachments
                     ).outerjoin( t_attachment
                     ).outerjoin(
                         at_attachment_tags,
                         at_attachment_tags.c.attachmentid == t_attachment.c.id
                     ).outerjoin(
                         t_tag,
                         at_attachment_tags.c.tagid == t_tag.c.id
                     ).outerjoin(
                        at_attachment_uploaders,
                        at_attachment_uploaders.c.attachmentid == t_attachment.c.id
                     ).outerjoin(
                        t_user,
                        at_attachment_uploaders.c.uploaderid == t_user.c.id
                     )

        q  = select( [ t_project.c.id, t_project.c.projectname,
                       t_attachment.c.id, t_attachment.c.filename,
                       t_attachment.c.size, t_attachment.c.summary,
                       t_attachment.c.download_count,
                       t_attachment.c.created_on, t_user.c.username,
                       t_tag.c.tagname,
                     ],
                     bind=meta.engine
                   ).select_from( oj 
                   ).where( t_project.c.id == project.id )

        entries = q.execute().fetchall()
        result  = {}
        for tup in entries :
            if tup[2] == None : continue
            forproj = result.get( tup[0:2], {} )
            foratt  = forproj.get( tup[2], [] )
            if foratt :
                tup[9] and foratt[-1].append( tup[9] )
            else :
                foratt = list( tup[3:9] )
                foratt.append( tup[9] and [ tup[9] ] or [] )
            forproj[ tup[2] ]  = foratt
            result[ tup[0:2] ] = forproj

        return result

    def adminprojects( self, user ) :
        """Get the list of all projects administered by `user`."""

        oj = at_project_admins.outerjoin( t_project
                             ).outerjoin(
                                    t_user,
                                    at_project_admins.c.adminid == t_user.c.id 
                             )

        q  = select( [ t_project.c.projectname ],
                     bind=meta.engine
                   ).select_from( oj
                   ).where( t_user.c.id == user.id )

        projects = list(set(
                        [ tup[0] for tup in q.execute().fetchall() if tup[0] ]
                   ))
        return projects

    def userprojects( self, user ) :
        """Get the list of all projects in which `user` is associated"""

        oj = t_project_team.outerjoin( t_project
                          ).outerjoin(
                                  t_user,
                                  t_project_team.c.user_id == t_user.c.id 
                          ).outerjoin( t_projectteam_type )

        q  = select( [ t_project.c.projectname, t_projectteam_type.c.team_type ],
                     bind=meta.engine
                   ).select_from( oj
                   ).where( t_user.c.id == user.id )

        pt = {}
        [ pt.setdefault( tup[0], [] ).append( tup[1] )
               for tup in q.execute().fetchall() if tup[0] ]
        return pt

    # Project component properties
    projectnames  = property( _projectnames )
    projectstatus = property( _projectstatus )
    disabledprojs = property( _disabledprojs )
    enabledprojs  = property( _enabledprojs )
    exposedprojs  = property( _exposedprojs )
    privateprojs  = property( _privateprojs )
    compnames     = property( _compnames )
    mstnnames     = property( _mstnnames )
    vernames      = property( _vernames )
    teams         = property( _teams )
    team_nomember = 'non-members'
