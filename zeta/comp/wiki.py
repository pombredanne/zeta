# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on wiki tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
#   1. Can there by synchronisation issue in `create_wiki()` interface. Like,
#      when multiple users try to create a wiki page, the table-numbering can get
#      jumbled up ...
#   2. In getting the `wikipage[0-N]` tables, using metadata.sorted_tables()
#      or metadata.table_iterator() may not help, since metadata only
#      retrieves the mapped table. As you might know, we create table to
#      Object mapping dynamically for wiki pages.
#   3. Since WikiPage tables maintains a cache of table maps for wiki page
#      contents, it might get inconsistent with the actual mapping in the
#      database,
#        * when the wiki page creation succeeds but fails before completing
#          the rest of the database operation
# Notes   :
#   1. It is always better to specify the wiki-url in alphanumeric characters.
#      This can help is automatically detecting wiki pages and creating links.
#   2. post-processing in functions that Create-Update-Delete database tables,
#           logging
#           cache-inavlidating
#           search-indexing
# Todo    : 
#   1. wiki_redirect() function is not required. Since the method of
#      redirection is changed to confirm with the de-facto standard.
#   3. Is remove_wikicomment() method required ?? timeline logging is not done
#      for it.
#   4. Is remove_content() method required ?? timeline logging is not done
#      for it.
#   5. Search indexing is disabled for 'create_wiki()' method, because by then
#      no meaningful wiki content would have been generated and it may not be
#      associated with a project.

from   __future__              import with_statement

from   sqlalchemy              import *
from   sqlalchemy.orm          import mapper, relation, eagerload_all, eagerload

import zeta.lib.helpers        as h
from   zeta.ccore              import Component
from   zeta.model              import meta
from   zeta.model.schema       import t_wiki, t_wikipage, t_project, \
                                      t_wiki_comment, t_user, t_tag, \
                                      t_attachment, \
                                      at_wiki_replies, at_wiki_commentors, \
                                      at_wiki_projects, at_wiki_favorites, \
                                      at_wiki_attachments, at_attachment_tags, \
                                      at_attachment_uploaders, at_wiki_votes, \
                                      t_vote

from   zeta.model.tables       import User, Wiki, WikiType, WikiTable_Map, \
                                      WikiComment, wikipage_factory, Project

tbl_mappers = meta.tbl_mappers
metadata    = meta.metadata


class WikiComponent( Component ) :
    """Component to manage the wiki subsystem."""

    def _create_wikitable( self, table_pagenum, engine ) :
        """Create the `wikipage[0-N]` table."""
        if table_pagenum not in meta.wiki_tables :
            meta.wiki_tables[table_pagenum] = t_wikipage( table_pagenum )
            meta.wiki_tables[table_pagenum].create( bind=engine, checkfirst=True )

        return meta.wiki_tables[table_pagenum]

    def _map_wikipage( self, table_pagenum ) :
        """Dynamically map wiki page table to WikiPage Object."""
        global tbl_mappers

        WikiPage    = wikipage_factory( table_pagenum )
        if WikiPage not in tbl_mappers :
            tbl_mappers[WikiPage] = \
                    mapper( WikiPage,
                            self._create_wikitable( table_pagenum, meta.engine )
                          )
                            
        return WikiPage

    def _wikipagetables( self ) :
        """Return the list of `wikipage` tables from database."""
        # Refer Gotchas above !!
        # return [ t for t in meta.metadata.table_iterator()
        #           if t.name[:8] == 'wikipage' ]
        tables = meta.engine.text( 'SHOW TABLES' ).execute()
        return [ t[0] for t in tables if t[0][:8] == 'wikipage' ]

    def _nexttablenumber( self ) :
        """Return next numerically largest table_pagenum."""
        global metadata

        nl = sorted([ int(tname[8:]) for tname in self._wikipagetables() ])
        if nl :
            return nl[-1] + 1
        else :
            return 1

    def _latestversion( self, WikiPage ) :
        """Return the latest version of WikiPage."""
        msession  = meta.Session()
        latest   = sorted([ wp.id for wp in msession.query( WikiPage).all() ])
        latest   = latest and latest[-1]
        if latest :
            wikipage = msession.query( WikiPage ).filter_by( id=latest ).first()
        else :
            wikipage = None
        return wikipage

    def get_wikitype( self, wikitype=None ) :
        """Get the WikiType instance identified by,
        `wikitype`, which can be,
            `id` or `wiki_typename` or  `WikiType` instance.
        if wikitype==None
            Return the list of all WikiType instances.

        Return,
            List of WikiType instances or
            WikiType instance."""

        msession  = meta.Session()

        if isinstance( wikitype, (int,long) ) :
            wikitype = msession.query( WikiType 
                                ).filter_by( id=wikitype ).first()

        elif isinstance( wikitype, (str, unicode) ) :
            wikitype = msession.query( WikiType 
                                ).filter_by( wiki_typename=wikitype ).first()

        elif wikitype == None :
            wikitype = msession.query( WikiType ).all()

        elif isinstance( wikitype, WikiType ) :
            pass

        else :
            wikitype = None

        return wikitype

    def create_wikitype( self, wiki_typenames, byuser=None ) :
        """Create wiki_typename  entries for the wiki_typenames specified by,
        `wiki_typenames`
            which can be, a string specifying the wiki_typename name or a list of
            such strings"""
        from zeta.config.environment import tlcomp, srchcomp

        if isinstance( wiki_typenames, (str,unicode) ) :
            wiki_typenames = [ wiki_typenames ]

        logs     = []
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ msession.add( WikiType( unicode(wt) )) for wt in wiki_typenames ]

        # Database Post processing
        tlcomp.log( byuser,
                    'added wiki type names, `%s`' % ', '.join(wiki_typenames) )

    @h.postproc()
    def create_wiki( self, wikiurl, wtype=None, summary=u'', sourceurl=u'',
                     creator=None, doclose=None ) :
        """Create a new Wiki entry."""
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        wtype     = wtype and self.get_wikitype( wtype )
        creator   = creator and userscomp.get_user( creator )
        msession  = meta.Session()
        if summary == None :
            summary = u''
        if sourceurl == None :
            sourceurl = u''
        summary   = summary.replace( '\n', ' ' ).replace( '\r', ' ' )
        with msession.begin( subtransactions=True ) :
            wiki = Wiki( wikiurl, summary, 0 )
            wiki.sourceurl = sourceurl
            wtype and setattr( wiki, 'type', wtype )
            creator and setattr( wiki, 'creator', creator )
            msession.add( wiki )
            wiki.tablemap = WikiTable_Map( self._nexttablenumber() )
            self._map_wikipage( wiki.tablemap.table_pagenum )

        log = 'created the wiki page'

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, creator, log) :
            tlcomp.log( creator, log, wiki=wiki )
            srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, creator, log ))
        return wiki

    @h.postproc()
    def config_wiki( self, wiki, wtype=None, summary=None, sourceurl=None,
                     project=None, doclose=None, byuser=None ) :
        """For the wiki page identified by
        `wiki`, which can be,
            `id` or `wikiurl` or `Wiki` instance.
        Set the wiki wtype.
        `wtype`, can be
            `id` or `wiki_typename` or `WikiType` instance.
        Add the project to which the wiki belongs to.
        `project` can be,
            `id` or `projectname` or `Project` instance
            if project can also be a string."""
        from zeta.config.environment import projcomp, tlcomp, srchcomp

        wiki     = self.get_wiki( wiki )
        wtype    = wtype and self.get_wikitype( wtype )
        project  = project and projcomp.get_project( project )
        msession = meta.Session()
        summary  = summary and summary.replace( '\n', ' ' ).replace( '\r', ' ' )
        with msession.begin( subtransactions=True ) :
            # Construct log based on attributes that have changed
            loglines = []
            wtype and loglines.append(( 'type', wiki.type.wiki_typename, wtype.wiki_typename ))
            summary and loglines.append(( 'summary', wiki.summary, summary ))
            sourceurl and loglines.append(( 'sourceurl', wiki.sourceurl, sourceurl ))
            log = h.logfor( loglines )
            if log :
                log  = 'Changed,\n%s' % log
            # Logging ends here

            if wtype :
                wiki.type = wtype

            if summary != None :
                wiki.summary = unicode(summary)

            if sourceurl != None :
                wiki.sourceurl = unicode(sourceurl)

            if project != None :
                wiki.project = project

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, byuser, log) :
            log and tlcomp.log( byuser, log, wiki=wiki )
            srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def addfavorites( self, wiki, favusers, doclose=None, byuser=None ):
        """Add the wiki as favorite for users identified by
        `favusers`, which can be (also can be an array of)
            `id` or `username` or `User` instance.
        to `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance."""
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        if not isinstance( favusers, list ) :
            favusers = [ favusers ]

        favusers  = [ userscomp.get_user( u ) for u in favusers ]
        wiki      = self.get_wiki( wiki )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ wiki.favoriteof.append( u ) for u in favusers ]

        log = 'added wiki page as favorite'

        # Post processing, optional deferred handling
        def onclose(tlcomp, wiki, byuser, log) :
            tlcomp.log( byuser, log, wiki=wiki )
        doclose( h.hitchfn( onclose, tlcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def delfavorites( self, wiki, favusers, doclose=None, byuser=None ) :
        """Delete the wiki as favorite for users identified by
        `favusers`, which can be (also can be an array of)
            `id` or `username` or `User` instance.
        to `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance."""
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        if not isinstance( favusers, list ) :
            favusers = [ favusers ]

        favusers  = [ userscomp.get_user( u ) for u in favusers ]
        wiki      = self.get_wiki( wiki )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            [ wiki.favoriteof.remove( u ) 
              for u in favusers if u in wiki.favoriteof ]

        log = 'removed wiki page from favorite'

        # Post processing, optional deferred handling
        def onclose(tlcomp, wiki, byuser, log) :
            tlcomp.log( byuser, log, wiki=wiki )
        doclose( h.hitchfn( onclose, tlcomp, wiki, byuser, log ))
        return None

    def get_wiki( self, wiki=None, attrload=[], attrload_all=[] ) :
        """Get the Wiki instance identified by,
        `wiki`, which can be,
            `id` or `wikiurl` or `Wiki` instance.

        Return
            List of Wiki instances or
            Wiki instance."""
        msession  = meta.Session()

        if isinstance( wiki, Wiki ) and attrload==[] and attrload==[] :
            return wiki

        # Compose query based on `wiki` type
        if isinstance( wiki, (int,long) ) :
            q = msession.query( Wiki ).filter_by( id=wiki )

        elif isinstance( wiki, (str, unicode) ) :
            q = msession.query( Wiki ).filter_by( wikiurl=wiki )

        elif isinstance( wiki, Wiki ) :
            q = msession.query( Wiki ).filter_by( id=wiki.id )

        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            wiki = q.first()

        elif wiki == None :
            q = msession.query( Wiki )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            wiki = q.all()

        else :
            wiki = None

        return wiki

    def wiki_redirect( self, wiki, target ) :
        """For the Wiki identified by,
        `wiki`, which can be,
            `id` or `wikiurl` or `Wiki` instance.
        create a mapping to wikipage table in wikitable_map, using,
        `target, which can be,
            `id` or `wikiurl` or `Wiki` instance or `WikiTable_Map`."""
        msession = meta.Session()

        wiki     = self.get_wiki( wiki )

        if isinstance( target, WikiTable_Map ) :
            target = target.table_pagenum
        else :
            target = self.get_wiki( target )

        if isinstance( target, Wiki ) :
            target = target.tablemap.table_pagenum

        with msession.begin( subtransactions=True ) :
            wiki.tablemap = WikiTable_Map( target )
            msession.add( wiki.tablemap )

    @h.postproc()
    def create_content( self, wiki, author, text, version=None, doclose=None ) :
        """For the Wiki page identified by 
        `wiki`, which can be,
            `id` or `wikiurl` or `Wiki` instance.
        add wiki content as the next version to wikipage table. if version is
        specified and matches a wikipage.id, then update the entry."""
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        log       = ''
        wiki      = self.get_wiki( wiki )
        author    = userscomp.get_user( author )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            WikiPage = self._map_wikipage( wiki.tablemap.table_pagenum )
            if version :
                wikipage = msession.query( WikiPage ).filter_by( id=version ).first()
                wikipage and author and setattr( wikipage, 'author', author.username ) 
                if wikipage and text :
                    wikipage.text     = text
                    wikipage.translate( wiki=wiki, cache=True ) # To HTML, maybe cached, maybe not !
                log = 'updated existing wiki version %s' % version
            else :
                wikipage = WikiPage( text )
                wikipage and author and setattr( wikipage, 'author', author.username ) 
                if wikipage and text :
                    wikipage.text     = text
                    wikipage.translate( wiki=wiki, cache=True ) # To HTML, maybe cached, maybe not !
                msession.add( wikipage )
                msession.flush()
                wiki.latest_version = wikipage.id
                log = 'updated wiki content to version %s' % wiki.latest_version

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, author, log) :
            tlcomp.log( author, log, wiki=wiki )
            srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, author, log ))
        return wikipage


    def get_content( self, wiki, version=None, all=False, translate=False ) :
        """For the Wiki page identified by 
        `wiki`, which can be,
            `id` or `WikiPage` instance.
        Get the latest `wikipage` entry if version==None.
        else, get the entry wikipage.id==version.
        if all==True
            return all the versions of the wiki page.

        Return,
            WikiPage instance."""
        wiki     = self.get_wiki( wiki )
        WikiPage = self._map_wikipage( wiki.tablemap.table_pagenum )
        msession = meta.Session()
        if isinstance( version, (int, long) ) :
            wikipage = msession.query( WikiPage ).filter_by( id=version ).first()
        elif all :
            wikipage = msession.query( WikiPage ).all()
        elif version == None :
            wikipage = msession.query( WikiPage ).filter_by( id=wiki.latest_version ).first()
        else :
            wikipage = None

        if translate and wikipage :
            with msession.begin( subtransactions=True ) :
                wikipage.translate( wiki=wiki, cache=True )

        return wikipage

    @h.postproc()
    def remove_content( self, wiki, version, doclose=None, byuser=None ) :
        """For the Wiki page identified by 
        `wiki`, which can be,
            `id` or `wikiurl` or `Wiki` instance.
        Remove the version,
        `version` which should be a valid `wikipage.id`."""
        from zeta.config.environment import tlcomp, srchcomp

        wiki = self.get_wiki( wiki )
        msession = meta.Session()

        with msession.begin( subtransactions=True ) :
            WikiPage   = self._map_wikipage( wiki.tablemap.table_pagenum )
            wikipage   = msession.query( WikiPage ).filter_by( id=version ).first()
            removed_id = wikipage.id
            msession.delete( wikipage )

        with msession.begin( subtransactions=True ) :
            if wiki.latest_version == removed_id :
                wikipage            = self._latestversion( WikiPage )
                if wikipage :
                    wiki.latest_version = wikipage.id
                else :
                    wiki.latest_version = 0

        log = 'removed wiki page version %s' % version

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, byuser, log) :
            tlcomp.log( byuser, log, wiki=wiki )
            srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def create_wikicomment( self, wiki, wcmtdetail, update=False,
                            doclose=None, byuser=None ):
        """For the Wiki instance identified by,
        `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance.
        `wcmtdetail` can be,
            (id, commentby, version_id, text)
        if update==True,
            then wcmtdetail[0] must be valid, in which an older comment
            will be updated.
        """
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        log       = ''
        wiki      = self.get_wiki( wiki )
        wikicmt   = (update and self.get_wikicomment( wcmtdetail[0] )) or None
        commentby = userscomp.get_user( wcmtdetail[1] )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            if ( update and wikicmt ) or wikicmt :
                wikicmt.commentby  = commentby
                wikicmt.version_id = wcmtdetail[2]
                wikicmt.text       = wcmtdetail[3]
                wikicmt.texthtml   = wikicmt.translate() # To HTML
                log = 'updated comment,\n%s' % wikicmt.text

            else :
                wikicmt           = WikiComment( wcmtdetail[2], wcmtdetail[3] )
                wikicmt.commentby = commentby
                wikicmt.wiki      = wiki
                wikicmt.texthtml  = wikicmt.translate() # To HTML
                wiki.comments.append( wikicmt )
                msession.add( wikicmt )
                log = 'commented as,\n%s' % wikicmt.text

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, byuser, log) :
            tlcomp.log( byuser, log, wiki=wiki )
            srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, byuser, log ))
        return wikicmt


    def get_wikicomment( self, wikicomment=None, attrload=[], attrload_all=[] ) :
        """Get the wiki comment identified by,
        `wikicomment` which can be,
            `id` or `WikiComment` instance.
        if wikicomment==None,
            return all the comments for `wiki`.

        Return,
            List of WikiComment instances or
            WikiComment instance."""
        if isinstance( wikicomment, WikiComment ) and attrload==[] and \
           attrload_all==[] :
            wikicmt = wikicomment

        msession = meta.Session()

        # Compose query based on `wikicmt` type
        if isinstance( wikicomment, (int,long) ) :
            q = msession.query( WikiComment ).filter_by( id=wikicomment )
        elif isinstance( wikicomment, WikiComment ) :
            q = msession.query( WikiComment ).filter_by( id=wikicomment.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            wikicmt = q.first()

        elif wikicomment == None :
            q = msession.query( WikiComment )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            wikicmt = q.all()

        else :
            wikicmt = None

        return wikicmt

    def remove_wikicomment( self, wikicomment ) :
        """Remove the WikiComment identified by,
        `wikicomment` which can be,
            `id` or `WikiComment` instance"""
        wikicomment = self.get_wikicomment( wikicomment )
        msession    = meta.Session()
        with msession.begin( subtransactions=True ) :
            wikicomment and msession.delete( wikicomment )
        return wikicomment

    def comment_reply( self, wikicomment, replytocomment ) :
        """Make `wikicomment` a reply to `replytocomment` where,
        `wikicomment` and `replytocomment` can be,
            `id` or `WikiComment` instance"""
        msession       = meta.Session()
        wikicomment    = wikicomment and \
                            self.get_wikicomment( wikicomment )
        replytocomment = replytocomment and \
                            self.get_wikicomment( replytocomment, attrload=['replies'] )

        if wikicomment and replytocomment :
            with msession.begin( subtransactions=True ) :
                replytocomment.replies.append( wikicomment )

    @h.postproc()
    def add_tags( self, wiki, tags=[], doclose=None, byuser=None ) :
        """For the wiki entry identified by,
        `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance.
        add tags specified by `tags`."""
        from zeta.config.environment import tagcomp, tlcomp, srchcomp

        wiki    = self.get_wiki( wiki )
        if wiki and tags :
            addtags = tagcomp.model_add_tags( tags, wiki, byuser=byuser )
        else :
            addtags = []

        log = ''
        if wiki and addtags :
            log = 'added tags, `%s`' % ', '.join(addtags)

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, byuser, log) :
            log and tlcomp.log( byuser, log, wiki=wiki )
            log and srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def remove_tags( self, wiki, tags=[], doclose=None, byuser=None ) :
        """For the wiki entry identified by,
        `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance.
        remove tags specified by `tags`."""
        from zeta.config.environment import tagcomp, tlcomp, srchcomp

        wiki    = self.get_wiki( wiki )
        if wiki and tags :
            rmtags = tagcomp.model_remove_tags( tags, wiki, byuser=byuser )
        else :
            rmtags = []

        log = ''
        if wiki and rmtags :
            log = 'deleted tags, `%s`' % ', '.join(rmtags)

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, wiki, byuser, log) :
            log and tlcomp.log( byuser, log, wiki=wiki )
            log and srchcomp.indexwiki( [wiki], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def add_attach( self, wiki, attach, doclose=None, byuser=None ) :
        """Add attachment to the wiki identified by,
        `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance.
        `attach` can be
            `id` or `resource_url` or `Attachment` instance."""
        from zeta.config.environment import attachcomp, tlcomp, srchcomp

        wiki = self.get_wiki( wiki )
        attach = attachcomp.get_attach( attach )
        wiki and attachcomp.model_add_attach( attach, wiki, byuser=byuser )

        log = ''
        if wiki :
            log = 'uploaded attachment, `%s`' % attach.filename

        # Post processing, optional deferred handling
        def onclose(tlcomp, wiki, byuser, log) :
            log and tlcomp.log( byuser, log, wiki=wiki )
        doclose( h.hitchfn( onclose, tlcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def remove_attach( self, wiki, attach, doclose=None, byuser=None ) :
        """Remove attachment to the wiki identified by,
        `wiki` which can be,
            `id` or `wikiurl` or `Wiki` instance.
        `attach` can be
            `id` or `resource_url` or `Attachment` instance."""
        from zeta.config.environment import attachcomp, tlcomp, srchcomp

        log = ''
        wiki = self.get_wiki( wiki )
        attach = attachcomp.get_attach( attach )
        if wiki :
            attachcomp.model_remove_attach( attach, wiki, byuser=byuser )
            log = 'deleted attachment, `%s`' % attach.filename

        # Post processing, optional deferred handling
        def onclose(tlcomp, wiki, byuser, log) :
            tlcomp.log( byuser, log, wiki=wiki )
        doclose( h.hitchfn( onclose, tlcomp, wiki, byuser, log ))
        return None

    @h.postproc()
    def voteup( self, wiki, user, doclose=None ) :
        """Increase popularity for the wiki page"""
        from zeta.config.environment import userscomp, votecomp, tlcomp, srchcomp

        log       = ''
        user      = userscomp.get_user( user )
        wiki      = self.get_wiki( wiki )
        vote      = votecomp.get_wikivote( user, wiki )
        if vote :
            votecomp.recast_vote( vote, u'up' );
            log = 're-casted vote'

        else :
            vote = votecomp.cast_vote( user, wiki, u'up' )
            log = 'casted vote'

        # Post processing, optional deferred handling
        def onclose(tlcomp, wiki, user, log) :
            tlcomp.log( user, log, wiki=wiki )
        doclose( h.hitchfn( onclose, tlcomp, wiki, user, log ))
        return vote

    @h.postproc()
    def votedown( self, wiki, user, doclose=None ) :
        """Decrease popularity for the wiki page"""
        from zeta.config.environment import userscomp, votecomp, tlcomp, srchcomp

        log       = ''
        user      = userscomp.get_user( user )
        wiki      = self.get_wiki( wiki )
        vote      = votecomp.get_wikivote( user, wiki )
        if vote :
            votecomp.recast_vote( vote, u'down' );
            log = 're-casted vote'

        else :
            vote = votecomp.cast_vote( user, wiki, u'down' )
            log = 'casted vote'

        # Post processing, optional deferred handling
        def onclose(tlcomp, wiki, user, log) :
            tlcomp.log( user, log, wiki=wiki )
        doclose( h.hitchfn( onclose, tlcomp, wiki, user, log ))
        return vote


    # Doc - metadata for 'wiki' table entries
    def documentof( self, wiki, search='xapian' ) :
        """Make a document for 'wiki' entry to create a searchable index
            [ metadata, attributes, document ], where

            metadata   : { key, value } pairs to be associated with document
            attributes : searchable { key, value } pairs to be associated with
                         document
            document   : [ list , of, ... ] document string, with increasing
                         weightage
        """
        wiki  = self.get_wiki( wiki, attrload=[ 'type', 'project', 'creator',
                                                'tags' ] )
        wcnts = self.get_content( wiki, all=True )

        q  = select( [ t_user.c.username, t_wiki_comment.c.text ],
                     bind=meta.engine
                   ).select_from(
                           t_wiki.outerjoin( t_wiki_comment 
                                ).outerjoin( at_wiki_commentors
                                ).outerjoin(
                                    t_user,
                                    at_wiki_commentors.c.commentorid == t_user.c.id
                                )
                   ).where( t_wiki.c.id == wiki.id )
        cmtusers = []
        cmttexts = []
        for tup in q.execute().fetchall() :
            tup[0] and cmtusers.append( tup[0] )
            tup[1] and cmttexts.append( tup[1] )

        wikiusers = [ wiki.creator.username ] + \
                    [ wcnt.author for wcnt in wcnts ] + cmtusers
        tagnames  = [ t.tagname for t in wiki.tags ]
        url       = h.wiki_parseurl( wiki.wikiurl )
        projname  = getattr( wiki.project, 'projectname', '' )
           
        metadata = { 'doctype'     : 'wiki', 
                     'id'          : wiki.id,
                     'projectname' : projname,
                   }
           
        attributes = \
            search == 'xapian' and \
                [ 'XID:wiki_%s'     % wiki.id,                      # id
                  'XCLASS:wiki',                                    # class
                  'XPROJECT:%s'     % projname,                     # project
                ] + \
                [ 'XUSER:%s'        % u                             # user
                  for u in wikiusers ] + \
                [ 'XTAG:%s'        % t                              # tag
                  for t in tagnames ] \
            or \
                []

        attrs    = ' '.join( [ projname, wiki.type.wiki_typename ] +\
                             wikiusers + tagnames )
        sourceurl= wiki.sourceurl or u''
        document = [
                ' '.join( [ wcnt.text for wcnt in wcnts ] + cmttexts ),
                ' '.join([ url, wiki.summary, sourceurl ]),
                attrs
        ]

        return [ metadata, attributes, document ]

    # Data Crunching methods on project database.

    def upgradewiki( self, byuser=u'admin' ) :
        """Upgrade the database fields supporting wiki markup to the latest
        zwiki version"""
        from zeta.config.environment import tlcomp, srchcomp

        msession = meta.Session()
        wikis    = self.get_wiki()
        wcmts    = self.get_wikicomment()
        cnt_wcmt = len(wcmts)
        cnt_wcnt = 0
        while wikis :
            with msession.begin( subtransactions=True ) :
                w        = wikis.pop(0)
                wcnts    = self.get_content( w, all=True )
                cnt_wcnt += len(wcnts)
                for wcnt in wcnts :
                    wcnt.texthtml = wcnt.translate(wiki=w, cache=True) # To HTML
        while wcmts :
            with msession.begin( subtransactions=True ) :
                wcmt = wcmts.pop(0)
                wcmt.texthtml = wcmt.translate()                       # To HTML
                
        # Database Post processing
        tlcomp.log(byuser, "Upgraded wiki contents and comments to latest wiki")

        return (cnt_wcnt, cnt_wcmt )


    def _typenames( self ) :
        return [ wt.wiki_typename for wt in self.get_wikitype() ]

    def countvotes( self, wiki=None, votes=[] ) :
        """Count votes and map it to dictionary
            { u'up' : count, u'down' : count }"""
        d  = { 'up': 0, 'down': 0 }
        if wiki :
            d  = { 'up' : [], 'down' : [] }

            oj = t_wiki.outerjoin( at_wiki_votes
                        ).outerjoin( t_vote )
            q  = select( [ t_vote.c.votedas ], bind=meta.engine 
                       ).select_from( oj
                       ).where( t_wiki.c.id == wiki.id )

            [ d[ tup[0] ].append(1) 
              for tup in q.execute().fetchall() if tup[0] ]

            d['up']   = len( d['up'] )
            d['down'] = len( d['down'] )

        elif votes :
            for vote in votes :
                d[vote.votedas] += 1
        return d

    def wikiurls( self, project ) :
        """Fetch all the wiki url for the `project`"""

        oj = t_project.outerjoin( at_wiki_projects ).outerjoin( t_wiki )

        q  = None
        if isinstance( project, (int, long) ) :
            q  = select( [ t_wiki.c.id, t_wiki.c.wikiurl ], bind=meta.engine
                       ).select_from( oj 
                       ).where( t_project.c.id == project )
        elif isinstance( project, (str, unicode) ) :
            q  = select( [ t_wiki.c.id, t_wiki.c.wikiurl ], bind=meta.engine
                       ).select_from( oj 
                       ).where( t_project.c.projectname == project )
        elif isinstance( project, Project ) :
            q  = select( [ t_wiki.c.id, t_wiki.c.wikiurl ], bind=meta.engine
                       ).select_from( oj 
                       ).where( t_project.c.id == project.id )

        return q != None and [tuple(tup) for tup in q.execute().fetchall()] or []

    def wikisproject( self ) :
        """Fetch a mapping of wiki id and project to which the wiki
        belongs to"""

        oj = t_wiki.outerjoin( at_wiki_projects ).outerjoin( t_project )
        q  = select( [ t_wiki.c.id, t_wiki.c.wikiurl,
                       t_project.c.id, t_project.c.projectname ],
                     order_by=[desc(t_wiki.c.id)],
                     bind=meta.engine
                   ).select_from( oj 
                   )
        res = [ tup for tup in q.execute().fetchall() if tup[0] and tup[2] ]
        return res

    def isfavorite( self, userid, wikiid ) :
        """Select whether the wiki page is favorite for user"""
        q  = select( [ at_wiki_favorites.c.wikiid, at_wiki_favorites.c.userid ],
                     bind=meta.engine
                   ).where(
                      and_( at_wiki_favorites.c.wikiid == wikiid,
                            at_wiki_favorites.c.userid == userid )
                   )
        return filter( lambda x : x[0], q.execute().fetchall() )

    def wikicomments( self, wikiid ) :
        """Collect wiki comments"""
        oj = t_wiki.outerjoin( t_wiki_comment 
                  ).outerjoin( at_wiki_commentors 
                  ).outerjoin( t_user )

        q  = select( [ t_wiki_comment.c.id, t_wiki_comment.c.version_id,
                       t_wiki_comment.c.text, t_wiki_comment.c.texthtml,
                       t_wiki_comment.c.created_on, t_user.c.username
                     ],
                     bind=meta.engine
                   ).select_from( oj 
                   ).where( t_wiki_comment.c.wiki_id == wikiid )

        # return the result as a list of tuple, instead of dict
        return [ tup for tup in q.execute().fetchall() if tup[0] ]

    def wikircomments( self, wikiid ) :
        """Collect wiki comments, in threaded mode"""
        oj = t_wiki.outerjoin( t_wiki_comment
                  ).outerjoin( at_wiki_commentors
                  ).outerjoin(
                         at_wiki_replies,
                         t_wiki_comment.c.id==at_wiki_replies.c.wikicommentid
                  ).outerjoin( t_user )

        q  = select( [ t_wiki_comment.c.id, t_wiki_comment.c.version_id,
                       t_wiki_comment.c.text, t_wiki_comment.c.texthtml,
                       t_wiki_comment.c.created_on, t_user.c.username,
                       at_wiki_replies.c.replytoid
                     ],
                     bind=meta.engine
                   ).select_from( oj
                   ).where( t_wiki_comment.c.wiki_id == wikiid )
 
        # Compute the comment replies and append the replies at the end of the
        # list.
        entries = [ tup for tup in q.execute().fetchall() if tup[0] ]
        res     = dict([ (tup[0], list(tup)+[ [] ]) for tup in entries ])

        # Detect reply hierarchy
        [ res[ res[id][6] ][-1].append( res[id] ) for id in res if res[id][6] ]

        # Compose it into a single level thread
        def threaded( cmt, replies ) :
            for rcmt in cmt[-1] :
                replies.append( rcmt )
                threaded( rcmt, replies )
        for id in res.keys() :
            if id in res :
                replies = []
                threaded( res[id], replies )
                res[id][-1] = replies
                [ res.pop( r[0], None ) for r in replies ]

        # return the result as a list of tuple, instead of dict
        return res.values()

    def wikicontents( self, wiki ) :
        """Fetch all the wiki content versions for `wiki`"""
        # To be completed, as an alternative to get_content with all=True
        pass

    def attachments( self, project ) :
        """Collect attachment list for all wiki pages,
        Return attachments"""

        oj = at_wiki_attachments.outerjoin( t_wiki
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
                               ).outerjoin(
                                  at_wiki_projects,
                                  at_wiki_projects.c.wikiid == t_wiki.c.id
                               ).outerjoin(
                                  t_project,
                                  at_wiki_projects.c.projectid == t_project.c.id
                               )

        q  = select( [ t_wiki.c.id, t_wiki.c.wikiurl,
                       t_attachment.c.id, t_attachment.c.filename,
                       t_attachment.c.size, t_attachment.c.summary,
                       t_attachment.c.download_count, t_attachment.c.created_on,
                       t_user.c.username, t_tag.c.tagname,
                     ],
                     bind=meta.engine
                   ).select_from( oj 
                   ).where( t_project.c.id == project.id )

        entries = q.execute().fetchall()
        result  = {}
        for tup in entries :
            if tup[2] == None : continue
            forwiki = result.get( tup[0:2], {} )
            foratt  = forwiki.get( tup[2], [] )
            if foratt :
                tup[9] and foratt[-1].append( tup[9] )
            else :
                foratt = list( tup[3:9] )
                foratt.append( tup[9] and [ tup[9] ] or [] )
            forwiki[ tup[2] ]  = foratt
            result[ tup[0:2] ] = forwiki

        return result

    def usercomments( self, user ) :
        """List of comments by user"""

        oj = at_wiki_commentors.outerjoin( t_wiki_comment )

        q  = select( [ t_wiki_comment.c.id ], bind=meta.engine 
                   ).select_from( oj 
                   ).where( at_wiki_commentors.c.commentorid == user.id )

        wcmts = [ tup[0] for tup in q.execute().fetchall() if tup[0] ]
        return wcmts


    # Project component properties
    typenames  = property( _typenames )
