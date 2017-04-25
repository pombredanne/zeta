# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on system tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
#   1. post-processing in functions that Create-Update-Delete database tables,
#           logging
#           cache-inavlidating
#           search-indexing
# Todo    : None


from   __future__               import with_statement
import os
from   os.path                  import abspath, dirname, isdir

from   sqlalchemy               import *
from   sqlalchemy.orm           import *

from   zeta.ccore               import Component
from   zeta.model               import meta
from   zeta.model.tables        import System, StaticWiki
from   zeta.lib.error           import ZetaTagError
from   zeta.lib.constants       import LEN_TAGNAME
import zeta.lib.helpers         as h
import zeta.lib.cache           as cache

pjoin = os.path.join

sysentries = [
    u'product_name',    u'product_version',     u'database_version',
    u'timezone',        u'unicode_encoding',    u'sitename',
    u'siteadmin',       u'envpath',
    u'userrel_types',   u'projteamtypes',       u'ticketstatus',
    u'tickettypes',     u'ticketseverity',      u'reviewnatures',
    u'reviewactions',   u'vcstypes',            u'wikitypes',
    u'ticketresolv',
    u'regrbyinvite', u'invitebyall', u'strictauth',
    u'def_wikitype', u'specialtags', u'welcomestring',
    u'userpanes', u'interzeta',

    u'replogs', u'mailacc_offsets', 
]

csvfields = [
    u'userrel_types',   u'projteamtypes',       u'ticketstatus',
    u'tickettypes',     u'ticketseverity',      u'reviewnatures',
    u'reviewactions',   u'vcstypes',            u'wikitypes',
    u'ticketresolv', u'specialtags',
]

class SystemComponent( Component ) :
    """Component System"""

    @cache.cache( '_sysentries', useargs=False )
    def _sysentries( self ) :
        msession   = meta.Session()
        entries = dict([ (s.field, s.value) 
                                 for s in msession.query(System).all() ])
        return entries

    def get_sysentry( self, field=None, default=None ) :
        """Return the value for 'field' in the system table"""
        entries = self._sysentries()
        return entries.get( field, default ) if field else entries

    @h.postproc()
    def set_sysentry( self, entries, doclose=None, byuser=None ) :
        """`entries` is a dictionary of 'field': 'value' which should be populated
        into the database."""
        from zeta.config.environment import tlcomp

        msession = meta.Session()

        # Sometimes, the caller might log the fact that sys-table is being
        # updated, so skip them here.
        #skiplog  = [ 'projteamtypes', 'tickettypes', 'ticketstatus', 
        #             'ticketseverity', 'reviewnatures', 'reviewactions',
        #             'wikitypes', 'vcstypes', 'specialtags' ]
        skiplog = []

        with msession.begin( subtransactions=True ) :
            dbentries = dict(map( lambda e : ( e.field, e ),
                                  msession.query(System).all()
                            ))
            loglines = []
            for k, v in entries.iteritems() :

                if not isinstance( entries[k], (str,unicode)) :
                    continue

                e = dbentries.get( k, None )
                if e == None :
                    msession.add( System( k, v ))
                    log = k not in skiplog

                elif k in csvfields and \
                  ( sorted(h.parse_csv(e.value)) != sorted(h.parse_csv(v)) ) :
                    dbentries[k].value = v
                    log = k not in skiplog

                elif (k not in csvfields) and (e.value != v) :
                    dbentries[k].value = v
                    log = k not in skiplog
                else :
                    log = False
                loglines.append( '%s : %s' % (k, v) ) if log else None

        log = loglines and 'system configuration,\n%s' % '\n'.join(loglines) or ''

        # Post processing, optional deferred handling
        cache.invalidate( self._sysentries )
        def onclose(tlcomp, byuser, log) :
            log and tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return None

    def get_interzeta( self, name=None ) :
        """Get the host mapping for interzeta `name`"""
        msession = meta.Session()
        d        = eval( self.get_sysentry( u'interzeta' ))
        return name and d.get( name, '' ) or d

    def set_interzeta( self, maps, byuser=None ) :
        """set the 'host' mapping for interzeta `name`"""
        d       = self.get_interzeta()
        d.update( maps )
        self.set_sysentry( { u'interzeta' : unicode(repr(d)) },
                           byuser=byuser )
        return maps

    def get_staticwiki( self, pathid=None, translate=False ) :
        """Get the static wiki page specified by 'pathid'
        Return StaticWiki"""
        msession  = meta.Session()
        if isinstance( pathid, (str, unicode) ) :
            q = msession.query( StaticWiki ).filter_by( path=pathid )
            q = q.options( eagerload( 'type' ) )
            sw = q.first()
            translate and sw.translate(wiki=sw, cache=True)
        elif isinstance( pathid, (int, long) ):
            q = msession.query( StaticWiki ).filter_by( id=pathid )
            q = q.options( eagerload( 'type' ) )
            sw = q.first()
            translate and sw.translate(wiki=sw, cache=True)
        else :
            q = msession.query( StaticWiki ).order_by( StaticWiki.path )
            q = q.options( eagerload( 'type' ) )
            swikis = q.all()
            translate and [ sw.translate(wiki=sw, cache=True) for sw in swikis ]
            sw = swikis
        return sw

    @h.postproc()
    def set_staticwiki( self, path, text, swtype=None, sourceurl=None,
                        doclose=None, byuser=None ) :
        """Set the static wiki page specified by 'path'"""
        from zeta.config.environment import tlcomp, srchcomp, wikicomp

        swtype = swtype and wikicomp.get_wikitype( swtype )
        swtype = swtype or wikicomp.get_wikitype(self.get_sysentry(u'def_wikitype'))
        sw       = self.get_staticwiki( path )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if sw :
                swtype and setattr( sw, 'type', swtype )
                if sourceurl != None :
                    sw.sourceurl = unicode(sourceurl)

                sw.text    = unicode(text)
                sw.texthtml= sw.translate(wiki=sw)    # To HTML

                log        = 'updated guest wiki page, %s' % path
                idxreplace = True

            else :
                sw         = StaticWiki( unicode(path), unicode(text) )
                swtype and setattr( sw, 'type', swtype )
                if sourceurl != None :
                    sw.sourceurl = unicode(sourceurl)
                sw.texthtml= sw.translate(wiki=sw)    # To HTML
                msession.add(sw)

                log        = 'created new guest wiki page, %s' % path
                idxreplace = False

        # Database Post processing

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, byuser, log, idxreplace) :
            tlcomp.log( byuser, log )
            srchcomp.indexstaticwiki( [sw], replace=idxreplace )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, byuser, log, idxreplace))
        return sw

    @h.postproc()
    def remove_staticwiki( self, paths=None, doclose=None, byuser=None ):
        """Remove the static wiki page identified by 'path'"""
        from zeta.config.environment import tlcomp, srchcomp

        if isinstance( paths, (str, unicode)) :
            paths = [ paths ]
        swikis   = self.get_staticwiki()
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if paths :
                [ msession.delete( sw ) for sw in swikis if sw.path in paths ]
            else :
                [ msession.delete( sw ) for sw in swikis ]
        
        log = 'deleted guest wiki pages,\n%s' % ', '.join(paths)

        # Post processing, optional deferred handling
        def onclose(tlcomp, byuser, log) :
            tlcomp.log( byuser, log )
        doclose( h.hitchfn( onclose, tlcomp, byuser, log ))
        return None

    def pull_staticwiki( self, todir ) :
        """Pull static wiki pages from database and form a directory tree
        relative to 'todir'
        
        Return the list of files retrieved from the database and stored into
        the dir-tree."""
        files = []
        for sw in self.get_staticwiki() :
            path = pjoin( todir, sw.path )
            if not isdir( dirname( path )) :
                os.makedirs( dirname( path ))
            open( path, 'w' ).write( sw.text )
            p = path.split( todir )[1]
            p = p[0] == os.sep and p[1:] or p
            files.append(p)
        return files

    def push_staticwiki( self, fromdir, byuser=None ) :
        """push static wiki pages into database by navigating the directory
        tree, 'fromdir'. Each file in the tree is considered a wiki page and
        the 'path' will be taken relative to 'fromdir'
        
        Return the list of files retrieved from the dir-tree and stored into
        the database."""
        swfiles = []
        skipped = []
        for wpath, dirs, files in os.walk( fromdir ) :
            for file in files :
                try :   # If incase, the file is not a valid unicode content.
                    path = unicode( pjoin( wpath.split( fromdir )[1], file ) )
                    path = path[0] == os.sep and path[1:] or path # prune /
                    text = unicode( open( pjoin( wpath, file )).read() )
                except :
                    skipped.append( path )
                else :
                    self.set_staticwiki( path, text, byuser=byuser )
                    swfiles.append( path )
        return ( swfiles, skipped )

    def updatecreatedon( self, byuser=None ) :
        """If `created_on` field is empty for any of the static wiki, update
        it to utcnow()"""
        import datetime     as dt

        updatedfor = []
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            for sw in self.get_staticwiki() :
                if sw.created_on : continue
                sw.created_on = dt.datetime.utcnow()
                updatedfor.append(sw)
        return updatedfor

    def upgradewiki( self, byuser=None ) :
        """Upgrade the database fields supporting wiki markup to the latest
        zwiki version"""
        from zeta.config.environment import tlcomp, srchcomp

        msession    = meta.Session()
        staticwikis = self.get_staticwiki()
        with msession.begin( subtransactions=True ) :
            for sw in staticwikis :
                sw.texthtml = sw.translate(wiki=sw)    # To HTML
        
        # Database Post processing
        tlcomp.log( byuser, "Upgraded static wiki pages" )

        return len(staticwikis)


    # Doc - metadata for 'staticwiki' table entries
    def documentof( self, swiki, search='xapian' ) :
        """Make a document for 'staticwiki' entry to create a searchable index
            [ metadata, attributes, document ], where

            metadata   : { key, value } pairs to be associated with document
            attributes : searchable { key, value } pairs to be associated with
                         document
            document   : [ list , of, ... ] document string, with increasing
                         weightage
        """
        swiki = self.get_staticwiki( swiki.path )
           
        metadata = \
            { 'doctype' : 'staticwiki', 'id' : swiki.path }
           
        attributes = \
            search == 'xapian' and \
                [ 'XID:staticwiki_%s' % swiki.id,           # id
                  'XCLASS:site', 'XCLASS:staticwiki',       # class
                ] \
            or \
                []

        attrs    = ' '.join( [ swiki.type.wiki_typename ] )
        sourceurl= swiki.sourceurl or u''

        document = [ swiki.text, ' '.join([ swiki.path, sourceurl ]), attrs ]

        return [ metadata, attributes, document ]
