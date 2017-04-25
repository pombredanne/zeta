# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Mercurial binding for Zeta version control system"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None


import re
import os
from   os.path         import commonprefix, join
import time
import datetime        as dt
import difflib         as dl
from   pytz            import timezone

import mercurial
from mercurial import ui, hg
from mercurial.util import matchdate, Abort

mime_type = {
    'directory' : 'text/directory',
    'file'      : 'text/file'
}

changetypes = {
}

class Client( object ) :
    """Mercurial Client definition"""

    start_revno = 0

    def __init__( self, rooturl ) :
        self.rooturl = rooturl
        self.repo = hg.repository( ui.ui(), rooturl )
        try : 
            self.currevno = self.repo.changectx( revno or 'tip' ).rev()
        except :
            self.currevno = None

    def __del__( self ) :
        pass


    def info( self, url=None, revno=None ) :
        cctx = self.repo.changectx( 'tip' if revno == None else revno )
        idict = {}
        if cctx :
            d, delta = cctx.date()
            utcdt = self._datetime( d, delta )
            idict  = { 'l_revision' : cctx.rev(),
                       'l_author'   : cctx.user(),
                       'l_date'     : utcdt,
                     }

        relurl = self._relpath(url)
        f = None
        mime_type = 'text/text'
        if relurl :
            try :
                f = cctx.filectx( relurl )
            except :
                mime_type = 'text/directory'
                f = None

        ndict = {}
        if relurl :
            ndict = { 'mime_type'  : mime_type,
                      'size'       : f and f.size() or 0,
                      'repos_path' : relurl,
                    }

        idict.update(ndict)
        return idict


    def list( self, url, revno=None, recurse=False ) :
        relurl = self._relpath(url)
        try :
            cctx = self.repo.changectx( 'tip' if revno == None else revno )
        except :
            cctx = None

        ldir = []
        dirs = []
        cctx_cache = {}
        for f, node in cctx.manifest().items():
            if not f.startswith(relurl): continue
            frel= f[len(relurl):].strip(os.path.sep)
            if frel.count(os.path.sep) >= 1:
                d = frel.split(os.path.sep, 1)[0]
                if d in dirs : continue
                dirs.append(d)
                ldir.append([
                    cctx.rev(),
                    'text/directory',
                    join( self.rooturl, relurl, d ),
                    '',
                    '',
                    '',
                    join( relurl, d )
                ])
            else:
                fctx = cctx.filectx(f)
                lrev = fctx.linkrev()
                lrev_cctx = self.repo.changectx(lrev)
                d, delta = lrev_cctx.date()
                utcdt = self._datetime( d, delta )
                ldir.append([
                    fctx.linkrev(),
                    'text/file',
                    join( self.rooturl, f ),
                    lrev_cctx.user(),
                    fctx.size(),
                    utcdt.strftime( '%m/%d/%Y' ),
                    f
                ])

        return ldir


    def cat( self, url, revno=None, annotate=False ) :
        relurl = url and self._relpath( url ) 
        try :
            cctx = self.repo.changectx( 'tip' if revno == None else revno )
            f = cctx.filectx( relurl )
        except :
            raise
            cctx = None
            f = None

        annotations = []
        
        lineno = 1
        lines = []
        if f and cctx and annotate :
            for fctx, line in f.annotate() :
                lineno += 1
                d, delta = fctx.date()
                utcdt = self._datetime( d, delta )
                lines.append([ lineno,
                               line.strip('\r\n'),
                               fctx.rev(),
                               fctx.user(),
                               utcdt,
                            ])
        elif f and cctx :
            for line in f.data().splitlines() :
                lineno += 1
                lines.append([ lineno,
                               line.strip('\r\n'),
                               None,
                               None,
                               None,
                            ])
        return lines


    def diff( self, url, revno1, revno2, url2=None ) :
        revno1 = self.start_revno if revno1 == None else revno1
        revno2 = self.currevno if revno2 == None else revno2
        try :
            relurl1 = url and self._relpath( url )
            cctx1 = self.repo.changectx( revno1 )
            f1 = cctx1.filectx( relurl1 )
            text1 = f1.data().splitlines()
        except :
            text1 = []

        try :
            relurl2 = url2 and self._relpath( url2 ) or relurl1
            cctx2 = self.repo.changectx( revno2 )
            f2 = cctx2.filectx( relurl2 )
            text2 = f2.data().splitlines()
        except :
            text2 = []

        title1 = "%s (revision %s)" % (relurl1, revno1)
        title2 = "%s (revision %s)" % (relurl2, revno2)
        diffgen= dl.unified_diff( text1, text2,
                                  fromfile=title1,
                                  tofile=title2
                                )
        diff   = '\n'.join([ l.strip('\r\n') for l in diffgen ])
        return diff


    def logs( self, url=None, revstart=None, revend=None ) :
        revstart = self.start_revno if revstart == None else revstart
        revend = self.currevno if revend == None else revend
        relurl = url and self._relpath( url )
        logs = []
        if relurl :
            try :
                flog = self.repo.file( relurl )
                for idx in flog.index[:-1] :
                    cctx = self.repo.changectx( idx[4] )
                    d, delta = cctx.date()
                    utcdt = self._datetime( d, delta )
                    logs.append([
                        unicode( cctx.description(), 'utf8' ),
                        cctx.rev(),
                        cctx.user(),
                        utcdt    
                    ])
            except :
                raise
        else :
            try :
                for revno in range(revstart, revend+1) :
                    cctx = self.repo.changectx( revno )
                    d, delta = cctx.date()
                    utcdt = self._datetime( d, delta )
                    logs.append([
                        unicode( cctx.description(), 'utf8' ),
                        cctx.rev(),
                        cctx.user(),
                        utcdt    
                    ])
            except :
                raise
        return logs

    def changedfiles( self, url, revstart, revend ) :
        revstart = self.start_revno if  revstart == None else revstart
        revend = self.currevno if revend == None else revend
        changes = []
        try :
            cctx1 = self.repo.changectx( revstart )
            cctx2 = self.repo.changectx( revend )
            modified, added, removed = self.repo.status(
                                                cctx1.node(), cctx2.node()
                                       )[:3]

            for f in added :      # Added
                changes.append({
                    'repos_path' : f,
                    'changetype' : 'added',
                    'mime_type'  : 'text/file'
                })
            for f in removed :    # Deleted
                changes.append({
                    'repos_path' : f,
                    'changetype' : 'deleted',
                    'mime_type'  : 'text/file'
                })
            for f in modified :    # Modified
                changes.append({
                    'repos_path' : f,
                    'changetype' : 'modified',
                    'mime_type'  : 'text/file'
                })
        except :
            raise
        return changes

    def _datetime( self, timestamp, delta=0 ) :
        timestamp = timestamp + delta
        tz        = timezone('UTC')
        utcdt     = tz.localize( dt.datetime( *time.localtime( timestamp )[:6] ))
        return utcdt

    def _relpath( self, url ) :
        relpath = url and url.replace( self.rooturl, '' ).strip('/') or ''
        return relpath


def init( vcs ) :
    try :
        c = Client( vcs.rooturl )
    except :
        raise
    return c

def info( self, url=None, revno=None ) :
    return self.client.info( url=url, revno=revno )

def list( self, url_dir, revno=None, recurse=False ) :
    return self.client.list( url=url_dir, revno=revno, recurse=recurse )

def cat( self, url, revno=None, annotate=False ) :
    return self.client.cat( url=url, revno=revno, annotate=annotate )

def diff( self, url, revno1, revno2, url2=None ) :
    return self.client.diff( url=url, revno1=revno1, revno2=revno2, url2=url2 )

def logs( self, url, revstart=None, revend=None ) :
    return self.client.logs( url=url, revstart=revstart, revend=revend )

def changedfiles( self, url=None, revstart=None, revend=None ) :
    return self.client.changedfiles( url=url, revstart=revstart, revend=revend )


