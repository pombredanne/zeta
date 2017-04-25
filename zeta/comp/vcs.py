# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on vcs tables."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None


from   __future__               import with_statement

from   sqlalchemy               import *
from   sqlalchemy.orm           import *

from   zeta.ccore               import Component
import zeta.lib.helpers         as h
from   zeta.model               import meta
from   zeta.model.tables        import Project, VcsType, Vcs, VcsMount
from   zeta.model.schema        import t_vcsmount, t_project, t_vcs, \
                                       at_vcs_projects

class VcsComponent( Component ) :
    """Component Version Control System."""

    def get_vcstype( self, vcs_type=None ) :
        """Get VcsType instance for the type identified by,
        vcs_type, which can be,
            `id` or `vcs_typename` or `VcsType` instance.

        Return,     
            VcsType instance.
            A list of VcsType instances."""

        msession  = meta.Session()

        if isinstance( vcs_type, (int,long) ) :
            vcs_type = msession.query( VcsType
                            ).filter_by( id=vcs_type ).first()

        elif isinstance( vcs_type, (str, unicode) ) :
            vcs_type = msession.query( VcsType 
                            ).filter_by( vcs_typename=vcs_type ).first()

        elif vcs_type == None :
            vcs_type = msession.query( VcsType ).all()

        elif isinstance( vcs_type, VcsType ) :
            pass

        else :
            vcs_type = None

        return vcs_type

    def create_vcstype( self, vcs_typenames, byuser=None ):
        """Create vcs_typename  entries for the vcs_typenames specified by,
        `vcs_typenames`
            which can be, a string specifying the vcs_typename name or a list of
            such strings"""
        from zeta.config.environment import tlcomp

        if isinstance( vcs_typenames, (str,unicode) ) :
            vcs_typenames = [ vcs_typenames ]

        logs     = []
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ msession.add( VcsType( unicode(t) )) for t in vcs_typenames ]

        # Database Post processing
        tlcomp.log( byuser,
                    'added version control types, `%s`' % \
                            ', '.join(vcs_typenames)
                  )

    @h.postproc()
    def integrate_vcs( self, project, vcsdetail, doclose=None, byuser=None ) :
        """Create a new vcs based on,
        `project` can be,
            `id` or `projectname` or `Project` instance
        `vcsdetail` which is a tuple of,
            ( type, name, rooturl, loginname, password )
            type can be `id` or `vcs_typename`
        Return,
            Vcs instance."""
        from zeta.config.environment import userscomp, prjcomp, tlcomp

        project   = prjcomp.get_project( project )
        vcs_type  = self.get_vcstype( vcsdetail[0] )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            type, name, rooturl, loginname, password = vcsdetail
            vcs = Vcs( name, rooturl, loginname, password )
            vcs_type and setattr( vcs, 'type', vcs_type )
            project.vcslist.append( vcs )
            msession.add( vcs )
            msession.flush()

        log = 'added project repository, `%s`' % vcs.name

        # Post processing, optional deferred handling
        def onclose(tlcomp, vcs, byuser, log) :
            tlcomp.log( byuser, log, vcs=vcs )
        doclose( h.hitchfn( onclose, tlcomp, vcs, byuser, log ))
        return vcs


    @h.postproc()
    def delete_vcs( self, vcs, doclose=None, byuser=None ) :
        """Delete the vcs entry identified by,
        `vcs` which can be,
            `id` or `Vcs` instance"""
        from zeta.config.environment import userscomp, prjcomp, tlcomp

        vcs       = self.get_vcs( vcs )
        project   = vcs.project
        name      = vcs.name
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            log = 'deleted project repository, `%s`' % vcs.name
            msession.delete( vcs )


        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser, log) :
            tlcomp.log( byuser, log, project=project )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, log ))
        return None

    @h.postproc()
    def config_vcs( self, vcs, name=None, type=None, rooturl=None,
                    loginname=None, password=None, doclose=None,
                    byuser=None ) :
        """For the vcs identified by,
        `vcs` which can be,
            `id` or `Vcs` instance
        """
        from zeta.config.environment import userscomp, prjcomp, tlcomp

        attrs      = [ 'name', 'type', 'rooturl', 'loginname', 'password' ]
        vcs        = self.get_vcs( vcs, attrload=[ 'project' ] )

        # Construct log based on changing attributes
        loglines   = [ ( 'name', vcs.name, name ),
                       ( 'type', vcs.type.vcs_typename, type ),
                       ( 'rooturl', vcs.rooturl, rooturl )
                     ]
        log = h.logfor( loglines )
        if log :
            log = 'changed attributes,\n%s' % log
        # Logging ends here

        # Find the changing attributes
        localvars  = locals()
        type       = type and self.get_vcstype( type ) or None
        msession   = meta.Session()
        localvars  = locals()   # locals() where changed.
        with msession.begin( subtransactions=True ) :
            [ setattr( vcs, attr, localvars[attr] )
              for attr in attrs if localvars[attr] ]

        # Post processing, optional deferred handling
        def onclose(tlcomp, vcs, byuser, log) :
            log and tlcomp.log( byuser, log, vcs=vcs )
        doclose( h.hitchfn( onclose, tlcomp, vcs, byuser, log ))
        return None


    def get_vcs( self, vcs=None, attrload=[], attrload_all=[] ) :
        """Get the Vcs instance corresponding to the vcs entry identified by,
        `vcs` can be,
            `id` or `Vcs` instance

        Return,
            A Vcs instance. or
            List of Vcs instances."""

        msession  = meta.Session()

        if isinstance( vcs, Vcs ) and attrload==[] and attrload_all==[] :
            return vcs

        # Compose query based on `vcs` type
        if isinstance( vcs, (int,long) ) :
            q = msession.query( Vcs ).filter_by( id=vcs )
        elif isinstance( vcs, Vcs ) :
            q = msession.query( Vcs ).filter_by( id=vcs.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            vcs = q.first()

        elif vcs == None :
            q = msession.query( Vcs )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            vcs = q.all()

        else :
            vcs = None

        return vcs

    def get_mount( self, mount=None, attrload=[], attrload_all=[] ) :
        """Get the VcsMount instance corresponding to the mount entry identified
        by,
        `mount` which can be,
            `id` or `VcsMount` instance

        Return,
            A VcsMount instance. or
            List of VcsMount instances."""

        msession  = meta.Session()

        if isinstance( mount, VcsMount ) and attrload==[] and attrload_all==[] :
            return mount

        # Compose query based on `mount` type
        if isinstance( mount, (int,long) ) :
            q = msession.query( VcsMount ).filter_by( id=mount )
        elif isinstance( mount, VcsMount ) :
            q = msession.query( VcsMount ).filter_by( id=mount.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            mount = q.first()

        elif mount == None :
            q = msession.query( VcsMount )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            mount = q.all()

        else :
            mount = None

        return mount
    
    @h.postproc()
    def create_mount( self, vcs, name, repospath, content=h.MNT_TEXTCONTENT,
                      doclose=None, byuser=None ) :
        """Create a mount point for repository directory"""
        from zeta.config.environment import tlcomp

        vcs      = self.get_vcs( vcs, attrload=[ 'project' ] )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            vmount = VcsMount( name, repospath, content )
            vmount.vcs = vcs
            msession.add( vmount )
            msession.flush()

        log = 'Mounted directory `%s` onto mount point %s' % (repospath, name)

        # Post processing, optional deferred handling
        def onclose(tlcomp, vcs, byuser, log) :
            tlcomp.log( byuser, log, project=vcs.project )
        doclose( h.hitchfn( onclose, tlcomp, vcs, byuser, log ))
        return vmount

    @h.postproc()
    def update_mount( self, mount, name=None, repospath=None, content=None,
                      doclose=None, byuser=None ) :
        """Update already created mount"""
        from zeta.config.environment import tlcomp

        mount    = self.get_mount( mount, attrload_all=[ 'vcs.project' ] ) 
        logs     = []
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if name :
                mount.name = name
                logs.append( 'name : %s' % name )
            if repospath :
                mount.repospath = repospath
                logs.append( 'repospath : %s' % repospath )
            if content :
                mount.content = content
                logs.append( 'content : %s' % content )

        log = ''
        if logs and mount :
            log = '\n'.join(
                    ['Updated repository mount, %s' % mount.name] + logs )

        # Post processing, optional deferred handling
        def onclose(tlcomp, mount, byuser, log) :
            log and tlcomp.log( byuser, log, project=mount.vcs.project )
        doclose( h.hitchfn( onclose, tlcomp, mount, byuser, log ))
        return None

    @h.postproc()
    def delete_mount( self, mount, doclose=None, byuser=None ) :
        """Delete mount point identified by,
        `mount` which can be,
            `id` or `VcsMount` instance"""
        from zeta.config.environment import tlcomp

        mount    = self.get_mount( mount, attrload_all=[ 'vcs.project' ] )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if mount :
                project = mount.vcs.project
                name    = mount.name
                msession.delete( mount )

        log = mount and 'Deleted mount point %s' % name or ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, project, byuser, log) :
            tlcomp.log( byuser, log, project=project )
        doclose( h.hitchfn( onclose, tlcomp, project, byuser, log ))
        return None

    def projmounts( self, project ) :
        """Collect all the mount definitions for `project`"""

        oj = t_vcsmount.outerjoin( t_vcs 
                      ).outerjoin(
                            at_vcs_projects,
                            t_vcs.c.id==at_vcs_projects.c.vscid
                      ).outerjoin(
                            t_project,
                            t_project.c.id==at_vcs_projects.c.projectid
                      )
        q  = select( [ t_vcsmount.c.id, t_vcsmount.c.name, t_vcsmount.c.content,
                       t_vcsmount.c.repospath, t_vcsmount.c.created_on,
                       t_vcs.c.id, t_vcs.c.name, t_vcs.c.rooturl
                     ],
                     bind=meta.engine
                   ).select_from( oj )

        if isinstance( project, (int, long)) :
            q   = q.where( t_project.c.id == project )

        elif isinstance( project, (str, unicode)) :
            q   = q.where( t_project.c.projectname == project )

        elif isinstance( project, Project ) :
            q   = q.where( t_project.c.id == project.id)

        return filter( lambda x : x[0], q.execute().fetchall() )
    
    # Data Crunching methods on ticket database.

    def _vcstypenames( self ) :
        return [ vt.vcs_typename for vt in self.get_vcstype() ]

    # vcs component properties
    vcstypenames     = property( _vcstypenames )
    mountcontents    = [ h.MNT_HTMLCONTENT, h.MNT_TEXTCONTENT,
                         h.MNT_ZWIKICONTENT ]
