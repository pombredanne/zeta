# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on tag tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None


from   __future__               import with_statement
import re

from   sqlalchemy               import *
from   sqlalchemy.orm           import *
from   sqlalchemy.sql           import *

from   zeta.ccore               import Component
from   zeta.model               import meta
from   zeta.model.schema        import t_tag, at_attachment_tags, \
                                       at_license_tags, at_project_tags, \
                                       at_ticket_tags, at_review_tags, \
                                       at_wiki_tags
from   zeta.model.tables        import Tag
from   zeta.lib.error           import ZetaTagError
from   zeta.lib.constants       import *

taggedcomps = [
    'attachment', 'license', 'project', 'ticket', 'review', 'wiki'
]
relatedas   = [
    'attachments', 'licenses', 'projects', 'tickets', 'reviews', 'wikipages'
]

class TagComponent( Component ) :
    """Component Tag."""
    def is_tagnamevalid( self, tagname ) :
        return re.match( RE_TNAME, tagname )

    def create_tag( self, tagname, byuser=None ) :
        """Create a new tag entry."""
        from zeta.config.environment import tlcomp

        tag      = None
        log      = ''
        msession = meta.Session()
        if self.is_tagnamevalid( tagname ) :
            with msession.begin( subtransactions=True ) :
                if not self.tag_exists( tagname ) :
                    tag = Tag( tagname )
                    msession.add( tag )
                    log = 'created new tag, `%s`' % tagname

                else :
                    raise ZetaTagError( 'Duplicate tag entry %s' % tagname )

        # Database Post processing
        log and tlcomp.log( byuser, log, tag=tag )

        return tag


    def get_tag( self, tag=None, attrload=[], attrload_all=[] ) :
        """Get tag identified by,
        `tag` which can be,
            `id` or `tagname` or `Tag` instance.
        if tag=None,
            all tag instances will be returned.

        Return,
            A list of Tag instance, or
            One Tag instance."""
        if isinstance( tag, Tag ) and attrload==[] and attrload_all==[] :
            return tag

        msession  = meta.Session()

        # Compose query based on `user` type
        if isinstance( tag, (int, long) ) :
            q = msession.query( Tag ).filter_by( id=tag )
        elif isinstance( tag,(str, unicode) ) :
            q = msession.query( Tag ).filter_by( tagname=tag )
        elif isinstance( tag, Tag ) :
            q = msession.query( Tag ).filter_by( id=tag.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            tag = q.first()

        elif tag == None :
            q = msession.query( Tag )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            tag = q.all()

        else :
            tag = None

        return tag

    def tag_exists( self, tag ) :
        """Check for the presence of tagname entry in the tag table."""
        return self.get_tag( tag ) and True or False

    def remove_tag( self, tag, byuser=None ) :
        """Remove existing tag entry."""
        from zeta.config.environment import tlcomp

        tag      = self.get_tag( tag )
        tagname  = tag and tag.tagname or ''
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            tag and msession.delete( tag )
        
        # Database Post processing
        tlcomp.log( byuser, 'deleted tag, `%s`' % tagname )


    def model_add_tags( self, tags, modelobj, byuser=None ) :
        """Add tags to the model instance `modelobj`.
        `tags` can be,
            list of `tagname` strings
            list of `Tag` instances
        Invalid tag names are SKIPPED !!"""
        msession = meta.Session()
        if isinstance( tags, (str, unicode) ) :
            tags = [ tags ]
        addedtags = []
        with msession.begin( subtransactions=True ) :
            for tag in tags[:] :
                if isinstance( tag, (str, unicode) ) :
                    if not self.is_tagnamevalid( tag ) :
                        continue
                    tagobj = self.get_tag( tag )
                    if not tagobj :
                        tagobj = self.create_tag( tag, byuser=byuser )
                        msession.flush()
                    modelobj.tags.append( tagobj )
                    addedtags.append( tagobj.tagname )
                elif isinstance( tag, Tag ) :
                    modelobj.tags.append( tag )
                    addedtags.append( tag.tagname )

        return addedtags

    def model_remove_tags( self, tags, modelobj, byuser=None ) :
        """Remove tags from model instance `modelobj`.
        `tags` can be,
            list of `tagname` strings
            list of `Tag` instances."""
        if isinstance( tags, (str, unicode) ) :
            tags  = [ tags ]
        removedtags = []
        msession    = meta.Session()
        with msession.begin( subtransactions=True ) :
            # Loop on copied list. Since the list might be the same as the
            # collection object of the model.
            for tag in tags[:] :
                if isinstance( tag, (str, unicode) ) :
                    tag = self.get_tag( tag )
                if isinstance( tag, Tag ) and tag in modelobj.tags :
                    removedtags.append( tag.tagname )
                    modelobj.tags.remove( tag )

        return removedtags

    # Data crunching methods on tag tables.
    def _tagnames( self ) :
        return [ t.tagname for t in self.get_tag() ]

    def _tagstats( self ) :
        """tag statistics"""
        tagstats = {}
        for t in self.get_tag( attrload=relatedas ) :
            compstats   = {}
            [ compstats.setdefault( attr, [] ).extend( getattr( t, attr ))
              for attr in relatedas ]
            tagstats[t.tagname] = compstats
        return tagstats

    def _tagpercentile( self ) :
        """Tag weightage from 0-100 as a percentile"""
        tagpercentile = {}

        oj = t_tag.outerjoin( at_attachment_tags 
                            ).outerjoin( at_license_tags
                            ).outerjoin( at_project_tags
                            ).outerjoin( at_ticket_tags
                            ).outerjoin( at_review_tags
                            ).outerjoin( at_wiki_tags )

        q  = select( [ t_tag.c.tagname, at_attachment_tags.c.attachmentid,
                       at_license_tags.c.licenseid, at_project_tags.c.projectid,
                       at_ticket_tags.c.ticketid, at_review_tags.c.reviewid, 
                       at_wiki_tags.c.wikiid
                     ],
                     bind=meta.engine
                   ).select_from( oj )

        # Identify tag relations
        [ tagpercentile.setdefault( tup[0], [] ).append( tup[1:] )
          for tup in q.execute().fetchall() if tup[0] ]

        # Count Number of time a tag is related
        tagpercentile = dict([
                            ( tag, 
                              sum([ len(filter( None, set(itemlist) ))
                                    for itemlist in zip(*tagpercentile[tag])
                                 ])
                            ) for tag in tagpercentile
                        ])

        # Calculate percentile
        maxt = max(tagpercentile.values())
        for t in tagpercentile :
            tagpercentile[t] = [ tagpercentile[t],
                                 int( (tagpercentile[t] / float(maxt)) * 100 )
                               ]
        return tagpercentile
            

    # Tag component properties
    tagnames      = property( _tagnames )
    tagstats      = property( _tagstats )
    tagpercentile = property( _tagpercentile )
