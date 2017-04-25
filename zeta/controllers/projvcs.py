# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage project source control pages."""

# -*- coding: utf-8 -*-

# Gotchas : None
#   1. When entering the 'rooturl' for VCS/SVN a trailing '/' must be present
#      to indicate a directory.
# Notes   : None
# Todo    : None


import logging
from   os.path                 import basename, join, splitext

from   pylons                  import request, response, session, tmpl_context as c
from   pylons                  import config
import simplejson              as json

from   zeta.lib.base           import BaseController, render
import zeta.lib.helpers        as h
import zeta.lib.vcsadaptor     as va
from   zeta.lib.constants      import *

log = logging.getLogger( __name__ )

vcsperm  = {}
vcsperm.update(
    dict([ ( formname, h.HasPermname( 'VCS_CREATE' ))
           for formname in [ 'integratevcs', 'configvcs', 'deletevcs' ]
        ])
)
vcsperm.update(
    dict([ ( formname, h.HasPermname( 'WIKI_CREATE' ))
           for formname in [ 'vcsfile2wiki' ]
        ])
)

class ProjvcsController( BaseController ) :
    """Class to handle project page request"""

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""
        from zeta.config.environment    import vcscomp

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )
        c.mainnavs = mainnav( c.projectname, c.controllername )

        # Collect the query values into 'context'
        c.revno    = request.params.get( 'revno', None )
        c.rev1     = request.params.get( 'rev1', None )
        c.rev2     = request.params.get( 'rev2', None )
        c.repopath = request.params.get( 'repopath', None )
        c.wikifile = request.params.get( 'wikifile', None )
        c.cnttype  = request.params.get( 'cnttype', MNT_TEXTCONTENT )
        c.vcseditable = None

        c.vcs  = vcscomp.get_vcs( int(vcs_id), attrload=[ 'type' ]
                 ) if c.vcsid else None
        c.project = projcomp.get_project(
                            c.projectname, attrload=[ 'logofile' ],
                            attrload_all=[ 'vcslist.type' ]
                    )
        c.prjlogo = c.project and c.project.logofile and \
                    self.url_attach( c.project.logofile.id )

        # More specific initialisations.
        c.revno = int(c.revno) if c.revno else None
        c.rev1 = int(c.rev1) if c.rev1 else None
        c.rev2 = int(c.rev2) if c.rev2 else None
        fn = lambda v : [ self.url_vcsbrowse( c.projectname, v.id ), v.name ]
        c.vcslist = map( fn, c.project.vcslist )
        c.vrep = None
        if c.vcs :
            c.vrep = va.open_repository( c.vcs )
            c.revno_l  = c.vrep.linfo['l_revision']
            c.revno= c.revno_l if c.revno == None else c.revno 
            strvno = c.vrep.client.start_revno
            c.revno_p = (c.revno-1) if ((c.revno-1) >= strvno) else None
            c.revno_n = (c.revno+1) if ((c.revno+1) <= c.revno_l) else None

    def formpermission( self ) :
        return ( c.form == 'submit'
               ) and ( c.formname in vcsperm 
               ) and ( not h.authorized( vcsperm[c.formname] ) )

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def _json_vcslist( self ) :                             # JSON
        """JSON: { id   : 'id',
                   label: 'vcs_id',
                   items: [ { 'id'          : v.id,
                              'name'        : v.name,
                              'rooturl'     : v.rooturl,
                              'href'        : href,
                              'vcs_typename': v.type.vcs_typename },
                            ... ]
                 }"""
        def format_item( v ) :
            href = self.url_vcsbrowse( c.project.projectname, str(v.id) )
            d = {
                'id'           : v.id,
                'name'         : v.name,
                'rooturl'      : v.rooturl,
                'href'         : href,
                'vcs_typename' : v.type.vcs_typename,
            }
            return d
        return h.todojoreadstore( c.project.vcslist,
                                  format_item,
                                  id='id',
                                  label='vcs_id'
                                )

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def _json_dirlist( self ) :                                # JSON
        """JSON : { id: 'dirlist',
                    label: 'dirlist',
                    items: [{ 'dirlist': '',
                              'dirs' : [ [ dirname, listurl, repos_path ], ... ],
                              'files': [ [ created_revision, mime_type, path,
                                           author, size, timestamp, repos_path,
                                           basename, url ],
                                         ... ]
                            }]"""
        c.vrep = va.open_repository( c.vcs )
        listing = {}
        fn = lambda f : listing.setdefault( f[1], [] ).append(f)
        map( fn, c.vrep.list( c.repopath, revno=c.revno ) )
        fn = lambda f : [
                basename( f[2] ), 
                self.url_vcsbrowse(
                    c.project.projectname, c.vcs.id, repopath=f[2],
                    revno=c.revno, jsonobj='dirlist', view='js'
                ),
                f[6][2:] if f[6][:2] == './' else f[6].lstrip('/')
             ]

        listing['text/directory'] = map( fn, listing.get('text/directory', []) )
        fn = lambda f : f + [
                basename( f[2] ),
                self.url_vcsbrowse( 
                    c.project.projectname, c.vcs.id, filepath=f[6].lstrip('/'),
                    revno=c.revno
                )
             ]
        listing['text/file'] = map( fn, listing.get( 'text/file', [] ) )
        return h.todojoreadstore(
                        [{ 'dirlist' : 0,
                           'dirs' : listing['text/directory'],
                           'files': listing['text/file']
                        }],
                        lambda v :  v,
                        id='dirlist',
                        label='dirlist'
               )

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def vcsindex( self, environ, projectname ) :
        """Project source control
        URLS :
            /p/{projectname}/s
            /p/{projectname}/s?jsonobj=vcslist&view=js
            /p/{projectname}/s?form=submit&formname=configvcs&view=js
        """
        from zeta.config.environment    import vfcomp, projcomp, vcscomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        if self.formpermission() :
            c.errmsg = 'Do not have %s permission !!' % tckperm[c.formname]
        else :
            vfcomp.process(
                request, c, defer=True, errhandler=h.hitchfn(errhandler),
                formnames=[ 'configvcs' ], 
            )

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.vcs_typenames = vcscomp.vcstypenames
        c.vcseditable = h.authorized( h.HasPermname( 'VCS_CREATE' ))
        c.title = '%s:source' % projectname

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.view == 'js' and c.jsonobj :
            html = self.handlejson(environ)
        elif c.view != 'js' :
            html = render( '/derived/projects/vcsindex.html' )
        else :
            html = ''

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'VCS_CREATE' ))
    def integratevcs( self, environ, projectname ) :
        """Integrate / config / delete VCS entries
        URLS :
            /p/{projectname}/s/integratevcs?form=request&formname=integratevcs
            /p/{projectname}/s/integratevcs?form=submit&formname=integratevcs
        """
        from zeta.config.environment    import vfcomp, projcomp, vcscomp

        c.rclose = h.ZResp()

        # Handle forms
        def errhandler(errmsg) :
            c.errmsg = errmsg
        vfcomp.process(
            request, c, defer=True, errhandler=h.hitchfn(errhandler),
            formnames=[ 'Integratevcs' ], user=c.authuser
        )

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.vcs_typenames = vcscomp.vcstypenames
        c.title = 'IntegrateSource'

        # HTML page generation
        if c.errmsg :
            html = self.returnerrmsg(environ)
        elif c.form == 'submit' :
            # Skip breadcrumbing, if it is a form submit
            c.title = '-Skip-'
            h.redirect_url( h.url_vcsintegrate )
        else :
            html = render( '/derived/projects/vcsintegrate.html' )
        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def vcs_browse( self, environ, projectname, vcsid ) :
        """Browse repository
        URLS :
            /p/{projectname}/s/{vcsid}/browse
            /p/{projectname}/s/{vcsid}/browse?revno=<num>
            /p/{projectname}/s/{vcsid}/browse?repospath=<rooturl>&revno=<num>
                                             &jsonobj=dirlist&view=js
            /p/{projectname}/s/{vcsid}/browse?filepath=<path>&revno=<num>
        """
        from zeta.config.environment    import projcomp, vcscomp

        c.rclose = h.ZResp()

        # Setup context for page generation
        c.projsummary = c.project.summary
        c.rootdir = basename( c.vcs.rooturl.rstrip('/') )
        c.vcseditable = h.authorized( h.HasPermname( 'VCS_CREATE' ))
        c.contents = vcscomp.mountcontents
        c.title = '%s:browse' % c.vcs.name
    
        # HTML page generation
        if c.jsonobj and c.view == 'js' :
            html = self.handlejson(environ)

        else :
            c.pmounts = vcscomp.projmounts( c.project )
            fn = lambda mnt : [
                    mnt[0], h.fix2repospath( mnt[3], [ mnt[7] ] ).lstrip('/')
                 ]
            c.mountdirs = map( fn, c.pmounts )
            html = render( '/derived/projects/vcsbrowse.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def vcs_file( self, environ, projectname, vcsid, filepath ) :
        """Create / config / delete VCS entries
        URLS :
            /p/{projectname}/s/{vcsid}/*(filepath)?revno=<num>
        """
        from zeta.config.environment    import projcomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.projsummary = c.project.summary
        fileurl = join( c.vcs.rooturl, filepath )
        c.fileerror = ''
        c.vfile = c.vrep.file( fileurl, revno=c.revno )
        c.sourceurl = c.pathinfo + '?wikifile=1'

        try :
            c.fileinfo  = c.vfile.info( revno=c.revno )
            c.filelines = c.vfile.cat( revno=c.revno, annotate=True )
            h.url_filedownl = self.url_vcsfiledown(
                                    projectname, vcsid, repopath=filepath,
                                    revno=c.revno
                               )
        except :
            c.fileinfo  = {}
            c.filelines = []
            c.fileerror = "Unable to obtain file %s at revision %s" % \
                          ( fileurl, c.revno )

        if c.wikifile :
            text = '\n'.join(map(lambda l : l[1], c.filelines ))
            o = h.Preview()
            setattr( o, 'text', text )
            o.translate  = h.hitch( o, h.Preview, h.translate, cacheattr='text' )
            html = o.translate(
                        wtype=h.CNTTYPE2WIKITYPE.get(c.cnttype, MNT_TEXTCONTENT)
                   )

        else :
            try :
                c.filelogs = c.vrep.logs( fileurl )
                c.filelogs = sorted( c.filelogs, key=lambda x : x[1], reverse=True )
                # Create revision url for each log.
                fn = lambda l : l.append( self.url_vcsrev( projectname, vcsid, revno=l[1] ))
                map( fn, c.filelogs )
                # Create file-url for each revision where the file was modified.
                fn = lambda l : [
                        self.url_vcsfile(
                            projectname, vcsid, filepath=filepath.lstrip('/'),
                            revno=l[1]
                        ),
                        str(l[1])
                     ]
                c.sel_frevs = map( fn, c.filelogs )

            except :
                c.fileerror = ( "Unable to obtain the history for file %s " +\
                                "at revision %s") % ( fileurl, c.revno )
                c.sel_frevs = []
                c.filelogs  = []

            h.url_reviewvfile = self.url_revwfile( projectname, fileurl, c.vfile.revno )
            c.vcseditable = h.authorized( h.HasPermname( 'VCS_CREATE' ))
            c.title = '%s:r%s' % ( basename(filepath), c.revno )

            # Html page generation
            html = render( '/derived/projects/vcsfile.html' )

        c.rclose.append(html)
        return c.rclose

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def vcs_revlist( self, environ, projectname, vcsid ) :
        """Browse repository
        URLS :
            /p/{projectname}/s/{vcsid}/revlist?revno=<num>
        """
        from zeta.config.environment    import projcomp

        c.rclose = h.ZResp()

        # Setup context for page rendering
        c.projsummary = c.project.summary
        c.replogs = c.vrep.logs( c.vcs.rooturl,
                                 revstart=c.vrep.finfo['l_revision'],
                                 revend=c.vrep.linfo['l_revision']
                               )

        # Create revision url for each log.
        c.revpages = [[ c.replogs[i][1],
                        self.url_vcsrevlist( projectname, vcsid, revno=c.replogs[i][1] )
                      ] for i in range(0, len(c.replogs), 100) ]
        c.revpages.reverse()

        adj = c.vrep.client.start_revno
        c.revlist = [ log + [
                            self.url_vcsrev( projectname, vcsid, revno=log[1] ),
                      ] for log in c.replogs[ (c.revno-adj) : c.revno+100-adj ] ]
        c.revlist.reverse()
        c.vcseditable = h.authorized( h.HasPermname( 'VCS_CREATE' ))
        c.title = '%s:revlist' % c.vcs.name

        # Html page generation
        c.rclose.append(render( '/derived/projects/vcsrevlist.html' ))
        return c.rclose

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def vcs_revision( self, environ, projectname, vcsid ) :
        """View repository revision details and log message
        URLS :
            /p/{projectname}/s/{vcsid}/revision?revno=<num>
        """
        from zeta.config.environment    import projcomp

        c.rclose = h.ZResp()

        # Compose the revision details
        c.projsummary = c.project.summary
        c.revision = c.vrep.logs(c.vcs.rooturl, revstart=c.revno, revend=c.revno)
        c.revision = c.revision and c.revision[0] or [ '', '', '', '' ]
        c.changedfiles = c.vrep.changedfiles( c.vcs.rooturl, 
                                              revstart=c.revno-1,
                                              revend=c.revno
                                            )
        c.revision.append(
            self.url_vcsdiffdown( projectname, vcsid, rev1=c.revno-1, rev2=c.revno )
        )

        for cf in c.changedfiles :
            cf['fileurl'] = self.url_vcsfile(
                                projectname, vcsid, revno=c.revno,
                                filepath=cf['repos_path'].lstrip('/'),
                            )

            if cf['changetype'] == 'modified' :
                cf['diffurl'] = self.url_vcsdiff(
                    projectname, vcsid, repopath=cf['repos_path'],
                    rev1=c.revno-1, rev2=c.revno, view='text', textobj='filediff'
                )
                #cf['diff'] = c.vrep.diff( join(c.vcs.rooturl, cf['repos_path']),
                #                          c.revno_p and c.revno-1, c.revno )
                cf['diffdownlurl'] = self.url_vcsdiffdown(
                    projectname, vcsid, repopath=cf['repos_path'],
                    rev1=c.revno-1, rev2=c.revno
                )

            else :
                cf['diffurl'] = ''
                cf['diff']    = ''

        h.url_reviewrev = self.url_revwrev( projectname, c.vcs.id, c.revision[1] )
        c.vcseditable = h.authorized( h.HasPermname( 'VCS_CREATE' ))
        c.vcsrevision = True
        c.title = '%s:r%s' % ( c.vcs.name, c.revno )

        # Html page generation
        c.rclose.append(render( '/derived/projects/vcsrevision.html' ))
        return c.rclose

    @h.authorize( h.HasPermname( 'VCS_VIEW' ))
    def vcs_diff( self, environ, projectname, vcsid ) :
        """View repository revision details and log message
        URLS :
            /p/{projectname}/s/{vcsid}/diff?repopath=<path>&rev1=<num>
                                           &rev2=<num>&view=text&textobj=filediff
        """
        from zeta.config.environment    import projcomp

        # Setup context for page rendering
        c.projsummary = c.project.summary
        diff = ''

        if c.repopath and (c.rev1 != None) and (c.rev2 != None) :
            diff = c.vrep.diff( join( c.vcs.rooturl, c.repopath ),
                                c.rev1, c.rev2 )
            cfdiff = diff.strip()
            cfdiff = diff.strip('\r\n\t')
            if cfdiff :
                cfdiff = h.syntaxhl( cfdiff, lexname='diff', linenos=True )
                cfdiff = '<code class="wsprewrap">%s</code>' % cfdiff
            else :
                cfdiff = '<em>Empty difference</em>'
        return cfdiff

    @h.authorize( h.HasPermname([ 'VCS_VIEW' ]))
    def diffdownload( self, environ, projectname, vcsid='' ) :
        """Provide downloadable diff for individual files between revisions or
        for the entire revision, the revision difference will be for rev2.
        URLS : 
            /p/{projectname}/s/{vcsid}/diffdownl?rev1=<num>&rev2=<num>
            /p/{projectname}/s/{vcsid}/diffdownl?repospath=<path>&rev1=<num>
                                                &rev2=<num>
        """
        from zeta.config.environment    import projcomp

        # Setup context for page rendering
        c.projsummary = c.project.summary
        diff      = ''

        filename = '%s-r%s' % (c.vcs.name, c.rev2)
        if c.repopath and (c.rev1 != None) and (c.rev2 != None) :
            diff = c.vrep.diff( join( c.vcs.rooturl, c.repopath ),
                                c.rev1, c.rev2 )
            filename = '%s:%s-r%s' % (
                            c.vcs.name, basename(c.repopath), c.rev2 )

        elif (c.rev1 != None) and (c.rev2 != None) :
            changedfiles = c.vrep.changedfiles( c.vcs.rooturl,
                                                revstart=c.rev1, revend=c.rev2 )
            for cf in changedfiles :
                if cf['changetype'] in ['modified'] :
                    fdiff = c.vrep.diff(
                                join( c.vcs.rooturl, cf['repos_path'] ),
                                c.rev1, c.rev2
                            ) + '\n\n'
                    diff += fdiff

        response.headers['Content-disposition'] = \
                        str( 'attachment; filename="%s.diff"' % filename )
        return diff

    @h.authorize( h.HasPermname([ 'VCS_VIEW' ]))
    def filedownload( self, environ, projectname, vcsid='' ) :
        """Download entire file for the specified revision
        URLS :
            /p/{projectname}/s/{vcsid}/filedownl?repopath=<path>&revno=<num>
        """
        from zeta.config.environment    import projcomp

        # Setup context for page rendering
        c.projsummary = c.project.summary
        vfile = c.vrep.file( join( c.vcs.rooturl, c.repopath ),
                                 revno=c.revno )
        file = ''
        if c.repopath and c.revno != None :
            file = '\n'.join( 
                        [ ltup[1] 
                          for ltup in vfile.cat( revno=c.revno, annotate=False )
                        ])
            fname, ext  = splitext( basename(c.repopath) )

        filename = '%s.r%s%s' % ( fname, c.revno, ext )
        response.headers['Content-disposition'] = \
                         str( 'attachment; filename="%s"' % filename )
        return file

    @h.authorize( h.HasPermname([ 'VCS_VIEW' ]))
    def timelines( self, environ, projectname ) :
        """Aggregate activities under project vcs or individual vcs
        URLS :
            /p/{projectname}/s/timeline
        """
        from zeta.config.environment    import projcomp, vcscomp

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
            h.r_projvcstlines, routeargs, ['vcs', 'project'],
            fromoff, logid, dir, c.project
        )
        c.title    = 'Source:timeline'

        c.rclose.append(render( '/derived/projects/vcstline.html' ))
        return c.rclose

    @h.authorize( h.HasPermname([ 'VCS_VIEW' ]))
    def timeline( self, environ, projectname, vcsid ) :
        """Aggregate activities under project vcs or individual vcs
        URLS :
            /p/{projectname}/s/timeline/{vcsid}
        """
        from zeta.config.environment    import projcomp, vcscomp

        c.rclose = h.ZResp()

        logid   = request.params.get( 'logid', None )
        dir     = request.params.get( 'dir', None )
        fromoff = request.params.get( 'fromoff', 1 )
        logid   = logid and int(logid)
        fromoff = int(fromoff)
        
        # Setup context for page generation
        c.projsummary = c.project.summary
        routeargs  = { 'projectname' : projectname, 'vcsid' : vcsid }
        self.tline_controller(
            h.r_projvcstline, routeargs, 'vcs', fromoff, logid, dir, c.vcs
        )
        c.title    = '%s:timeline' % c.vcs.name
        c.rclose.append(render( '/derived/projects/vcstline.html' ))
        return c.rclose

    def feeds( self, environ, projectname ) :
        """Aggregate activities under project vcs or individual vcs
        URLS :
            /p/{projectname}/s/feed
        """
        from zeta.config.environment    import projcomp, vcscomp

        host   = environ['HTTP_HOST']
        script = environ['SCRIPT_NAME']

        # Setup context for page generation
        c.projsummary = c.project.summary
        title = '%s:vcs' % projectname 
        link = h.urlroot(environ)
        descr = 'Timeline for vcs, in project %s' % projectname
        feed = h.FeedGen( title, link, descr )
        routeargs  = { 'projectname' : projectname }
        self.tline_controller(
            h.r_projvcstlines, routeargs, ['vcs', 'project'],
            1, None, None, c.project
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def feed( self, environ, projectname, vcsid ) :
        """Aggregate activities under project vcs or individual vcs
        URLS : 
            /p/{projectname}/s/feed/{vcsid}
        """
        from zeta.config.environment    import projcomp, vcscomp

        c.projsummary = c.project.summary
        title = '%s-vcs:%s' % ( projectname, c.vcs.name )
        link = h.urlroot(environ)
        descr = 'Timeline for vcs, %s in project %s' % (c.vcs.name, projectname)
        feed = h.FeedGen( title, link, descr )
        routeargs  = { 'projectname' : projectname, 'vcsid' : vcsid }
        self.tline_controller(
            h.r_projvcstline, routeargs, 'vcs', 1, None, None, c.vcs
        )
        feedhtml = self.feeds( environ, link, feed, c.logs )
        response.content_type = 'application/atom+xml'
        return feedhtml

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers()
