# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage project mount points with repository"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None


import logging
from   os.path                 import basename, join, splitext, commonprefix

from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config
import simplejson              as json

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
import zeta.lib.vcsadaptor     as va
from   zeta.lib.constants      import *

log = logging.getLogger( __name__ )

mountperm = dict([
    ( formname, h.HasPermname( 'VCS_CREATE' ))
    for formname in [ 'createmount', 'updatemount', 'deletemount' ]
])

class ProjmountController( BaseController ) :
    """Class to handle project page request"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )
        c.mainnavs = mainnav( c.projectname, c.controllername )

        # Collect the query values into 'context'
        c.changeid = request.params.get( 'changeid', None )
        c.project = projcomp.get_project(
                        c.projectname, attrload=[ 'logofile', 'vcslist' ],
                    ) if c.projectname else None
        c.prjlogo = c.project and c.project.logofile and \
                       self.url_attach( c.project.logofile.id )

    def formpermission( self ) :
        return ( c.form == 'submit'
               ) and ( c.formname in mountperm 
               ) and ( not h.authorized( mountperm[c.formname] ) )

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def _json_mountlist( self ) :                             # JSON
        """JSON: { id   : 'id',
                   label: 'mount_id',
                   items: [ { 'id'          : m.id,
                              'name'        : m.name,
                              'content'     : m.content,
                              'repospath'   : m.repospath,
                              'href'        : href,
                              'createdon'   : m.created_on },
                            ... ]
                 }"""
        from zeta.config.environment    import vcscomp

        def format_item( m ) :
            href = self.url_projmountsname( c.project.projectname, m[0] )
            d = {
                'id'         : m[0],
                'name'       : m[1],
                'content'    : m[2],
                'repospath'  : m[3],
                'href'       : href,
                'created_on' : m[4],
            }
            return d

        return h.todojoreadstore( vcscomp.projmounts( c.project ),
                                  format_item,
                                  id='id',
                                  label='mount_id'
                                )

    @h.authorize( h.HasPermname([ 'VCS_VIEW' ]))
    def mounts( self, environ, projectname ) :
        """List of Repository mount points
        URLS :
            /p/<projectname>/mnt
            /p/<projectname>/mnt?name=<name>
            /p/<projectname>/mnt?changeid=<mountid>
            /p/<projectname>/mnt?jsonobj=mountlist&view=js
            /p/<projectname>/mnt?form=submit&formname=createmount
            /p/<projectname>/mnt?form=submit&formname=updatemount
            /p/<projectname>/mnt?form=submit&formname=deletemount
            /p/<projectname>/mnt?form=submit&formname=createmount&view=js
            /p/<projectname>/mnt?form=submit&formname=deletemount&view=js
        """
        from zeta.config.environment    import vfcomp, projcomp, vcscomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % mountperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'createmount', 'updatemount', 'deletemount' ]
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.mnt = vcscomp.get_mount( int(c.changeid), attrload=['vcs']
                ) if c.changeid else None
        c.title = '-Skip-' if c.form else '%s:mounts' % projectname

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)

        elif c.form == 'submit' and (c.view != 'js') and \
           c.formname in [ 'createmount', 'updatemount' ]:
            h.redirect_url( h.url_projmounts )

        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)

        elif c.form and c.view == 'js' :
            html = ''

        else :
            c.contents = vcscomp.mountcontents
            c.vcslist = [ (v.id, v.name) for v in c.project.vcslist ]
            c.pmounts = [ list(vals[:3]) +
                          [ h.fix2repospath( vals[3], [vals[7]] ).lstrip('/') ] +
                          list(vals[4:])
                          for vals in vcscomp.projmounts(c.project)
                        ]
            html = render( '/derived/projects/projmounts.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname([ 'VCS_VIEW' ]))
    def mount( self, environ, projectname, mid, murl='' ) :
        """Repository mount point
        URLS :
            /p/<projectname>/mnt/<mid>/*(murl)
        """
        from zeta.config.environment    import projcomp, vcscomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.repospath = murl.lstrip( '/' )
        c.projsummary = c.project.summary
        c.mnt = vcscomp.get_mount( int(mid), attrload=[ 'vcs' ] ) if mid else None
        c.id = mid
        c.title = 'mount:%s' % getattr( c.mnt, 'name', '' )

        try :
            cprefix = commonprefix([ c.repospath, c.mnt.vcs.rooturl ]) 
            c.vrep = va.open_repository( getattr( c.mnt, 'vcs', None ))
            c.repurl = c.repospath and \
                       ( c.repospath if cprefix == c.mnt.vcs.rooturl
                                   else join( c.mnt.vcs.rooturl, c.repospath ) ) \
                       or c.mnt.vcs.rooturl
            c.vfile = c.vrep.file( c.repurl )
        except :
            c.vfile = None

        if c.vfile == None :
            c.content = '<b>Error in reading path</b>'
            c.rendertype = c.mnt.content if c.mnt else h.MNT_TEXTCONTENT

        elif c.vfile.mimetype == 'text/directory' :
            listing = {}
            dlist   = c.vrep.list( c.repurl )
            [ listing.setdefault( f[1], [] ).append(f) for f in dlist ]
            fn = lambda f : [ self.url_mount( projectname, mid, f[6] ),
                              basename( f[2] ),
                            ]
            dirs  = map( fn, listing.get( 'text/directory', [] ) )
            files = map( fn, listing.get( 'text/file', [] ) )
            c.content = [ '<li><a href="%s">%s</a></li>' % tuple(d) 
                          for d in dirs ] + \
                        [ '<li><a href="%s">%s</a></li>' % tuple(f)
                          for f in files ]
            c.content = '\n'.join( c.content )
            c.rendertype = 'dir'
        else :
            c.content    = '\n'.join([ l[1] for l in c.vfile.cat() ])
            c.rendertype = c.mnt.content
            try :
                o = h.Preview()
                setattr( o, 'text', c.content )
                o.translate = h.hitch( o, h.Preview, h.translate, cacheattr='text' )
                c.content   = o.translate( wtype=h.CNTTYPE2WIKITYPE[c.rendertype] )
            except :
                c.content = u''

        try :
            c.content = unicode(c.content)
        except:
            c.content = u'Unicoded file content'
        
        c.rclose.append(render( '/derived/projects/projmount.html' ))
        return c.rclose

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers()

