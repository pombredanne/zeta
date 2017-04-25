# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""SVN binding for Zeta version control system"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   1. `revstart` can be greater or lesser than `revend` for logs() api. Quite
#      flexible :-)
# Todo    : 
#   1. Add more mime types.
#   2. Test case for diff() method. Also re-verify all the test cases for this
#      module
#   3. Temporary file is used as /tmp/zeta try to put this under constants.py
#   4. client.list() has problems try to figure out the details.


import os
import time
import datetime as dt
import pysvn

mime_type = {
    pysvn.node_kind.dir  : 'text/directory',
    pysvn.node_kind.file : 'text/file'
}

changetypes = {
    pysvn.diff_summarize_kind.added    : 'added',
    pysvn.diff_summarize_kind.delete   : 'deleted',
    pysvn.diff_summarize_kind.modified : 'modified',
    pysvn.diff_summarize_kind.normal   : 'normal',
}

difftmp = "/tmp/zetasvn"

class Client( object ) :
    """SVN Client definition"""

    start_revno = 1

    def __init__( self, rooturl ) :
        self.rooturl = rooturl
        self.client = pysvn.Client()

    def info( self, url=None, revno=None ) :
        if getattr( revno, 'kind', None ) :
            r = revno
        else :
            r = revno and pysvn.Revision( pysvn.opt_revision_kind.number, revno ) or \
                pysvn.Revision( pysvn.opt_revision_kind.head )
        data = self.client.info2( url, revision=r, recurse=False )[0][1].data
        auth = data.get('last_changed_author', '')
        rev  = getattr( data.get('last_changed_rev', None ), 'number', 0 )
        mt   = data.get('kind', None ) and mime_type[data['kind']] or ''
        date = data.get('last_changed_date', None) and \
               dt.datetime.strptime( time.ctime( data['last_changed_date'] ),
                                     '%a %b %d %H:%M:%S %Y' ) \
               or None
        # Fetch the size by listing the file
        if mt == 'text/directory' :
            # ldata = self.client.list( url, revision=r, recurse=False )[0][0].data
            size  = 0
            repos_path = ''
        elif mt == 'text/file' :
            size = len(self.client.cat( url, revision=r ))
            repos_path = url.split( self.rooturl )[1]
        return { 'l_revision': rev , 'l_author': auth, 'l_date': date,
                 'mime_type': mt,    'size': size, 'repos_path': repos_path }

    def list( self, url, revno=None, recurse=False ) :
        if getattr( revno, 'kind', None ) :
            r = revno
        else :
            r = revno and pysvn.Revision( pysvn.opt_revision_kind.number, revno ) or \
                pysvn.Revision( pysvn.opt_revision_kind.head )
        entries = self.client.list( url, revision=r, recurse=recurse )
        listing = []
        for entry in entries :
            data = entry[0].data
            cr = data['created_rev'].number
            mt = mime_type[data['kind']]
            author = data['last_author']
            size = data['size']
            date = dt.datetime.strptime( time.ctime( data['time'] ),
                                         '%a %b %d %H:%M:%S %Y'
                                       ).strftime( '%m/%d/%Y' )
            listing.append( 
                [ cr, mt, data['path'], data['last_author'], data['size'], date,
                  data['repos_path'] ]
            )
        return listing[1:]

    def cat( self, url, revno=None, annotate=False ) :
        if getattr( revno, 'kind', None ) :
            r = revno
        else :
            r = revno and pysvn.Revision( pysvn.opt_revision_kind.number, revno ) or \
                pysvn.Revision( pysvn.opt_revision_kind.head )
        if annotate :
            lines   = self.client.annotate( url, revision_end=r )
            content = [ ( l['number'], l['line'], l['revision'].number, l['author'], 
                          dt.datetime.strptime( l['date'].split('.')[0], '%Y-%m-%dT%H:%M:%S' )
                        ) for l in lines ]
        else :
            text    = self.client.cat( url, revision=r )
            lines   = text.split('\n')
            content = [ ( i+1, lines[i], None, None, None )  
                        for i in range(len(lines)) ]
        return content


    def diff( self, url, revno1, revno2, url2=None ) :
        os.path.isdir( difftmp ) or os.makedirs( difftmp )
        if getattr( revno1, 'kind', None ) :
            r1 = revno1
        else :
            r1 = revno1 and \
                    pysvn.Revision( pysvn.opt_revision_kind.number, revno1 ) \
                 or pysvn.Revision( pysvn.opt_revision_kind.head )
        if getattr( revno2, 'kind', None ) :
            r2 = revno2
        else :
            r2 = revno2 and \
                    pysvn.Revision( pysvn.opt_revision_kind.number, revno2 ) \
                 or pysvn.Revision( pysvn.opt_revision_kind.number, 0 )

        d = self.client.diff( difftmp, url, revision1=r1, revision2=r2,
                              recurse=False )
        return d

    def logs( self, url, revstart=None, revend=None ) :
        if getattr( revstart, 'kind', None ) :
            r = revstart
        else :
            rs = revstart and \
                    pysvn.Revision( pysvn.opt_revision_kind.number, revstart ) \
                 or pysvn.Revision( pysvn.opt_revision_kind.number, 0 )
        if getattr( revend, 'kind', None ) :
            r = revend
        else :
            re   = revend and \
                      pysvn.Revision( pysvn.opt_revision_kind.number, revend ) \
                   or pysvn.Revision( pysvn.opt_revision_kind.head )
        try :
            logs = self.client.log( url, revision_start=rs, revision_end=re )
        except :
            logs = []

        listing = [ [ unicode( l['message'], 'utf8' ),
                      l['revision'].number,
                      l['author'],
                      dt.datetime.strptime( time.ctime( l['date'] ), 
                                            '%a %b %d %H:%M:%S %Y' ) 
                    ] for l in logs ]

        return listing

    def changedfiles( self, url=None, revstart=None, revend=None ) :
        if getattr( revstart, 'kind', None ) :
            r = revstart
        else :
            rs = revstart and \
                    pysvn.Revision( pysvn.opt_revision_kind.number, revstart )\
                 or pysvn.Revision( pysvn.opt_revision_kind.number, 1 )
        if getattr( revend, 'kind', None ) :
            r = revend
        else :
            re = revend and \
                    pysvn.Revision( pysvn.opt_revision_kind.number, revend )\
                 or pysvn.Revision( pysvn.opt_revision_kind.head )

        dslist = self.client.diff_summarize( url, revision1=rs, revision2=re )
        changestats = [ { 'repos_path': ds.data['path'],
                          'changetype': changetypes[ds.data['summarize_kind']],
                          'mime_type' : mime_type[ds.data['node_kind']]
                        } for ds in dslist ]
        return changestats

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
