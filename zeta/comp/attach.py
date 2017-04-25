# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on attachment tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   1. post-processing function can be subscribed to onclose event and can
#      thus be delayed until the request is completed.
# Todo    :  None

from   __future__               import with_statement
import os
from   os.path                  import isfile, isdir

from   sqlalchemy               import *
from   sqlalchemy.orm           import *

from   zeta.ccore               import Component
from   zeta.model               import meta
from   zeta.model.tables        import Attachment
from   zeta.model.schema        import t_attachment, t_tag, t_user, \
                                       at_user_icons, at_user_photos, \
                                       at_project_icons, at_project_logos, \
                                       at_project_attachments, \
                                       at_ticket_attachments, \
                                       at_license_attachments, \
                                       at_review_attachments, \
                                       at_wiki_attachments, \
                                       at_attachment_tags, \
                                       at_attachment_uploaders
from   zeta.lib.constants       import ATTACH_DIR
import zeta.lib.helpers         as h

class AttachComponent( Component ) :
    """Component to handle all attachments."""

    def _contentfile(self, attach) :
        """Compose the filepath for every attachment"""
        attdir  = os.path.join(h.fromconfig( 'zeta.envpath' ), ATTACH_DIR)
        isdir(attdir) or os.makedirs(attdir)
        filename = attach.filename + '_' + str(attach.id)
        return os.path.join(attdir, filename)

    def _store_fileupload( self, content, attach ) :
        """Store attachment `content` into attachment directory under
        `envpath`"""
        filename = self._contentfile(attach)
        open( filename, 'wb').write(content)
        return None

    def _read_content( self, attach ) :
        """Fetch the content of attachment"""
        filename = self._contentfile(attach)
        content = isfile(filename) and open(filename, 'rb').read() or ''
        return content

    def _remove_content( self, attach ) :
        """Fetch the content of attachment"""
        filename = self._contentfile(attach)
        isfile(filename) and os.remove(filename)
        return

    def db2file( self, attach ) :
        """Migrate attachment content from database to file"""
        attach = self.get_attach( attach=attach )
        filename = self._contentfile(attach)
        open(filename, 'wb').write( str(attach.content) )
        return

    def content( self, attach ) :
        """Get the content of attachment for,
        `attach`, which can be,
            `id` or `Attachment` instance."""
        attach = self.get_attach( attach=attach )
        return self._read_content(attach)

    def updatesize(self, attach) :
        """Update the `size` field in the attachment table from disk-file
        having the attachment content"""
        attach = self.get_attach( attach=attach )
        msession = meta.Session()
        if attach :
            with msession.begin( subtransactions=True ) :
                attach.size = len(self.content(attach))

    def downloadattach( self, attach ) :
        """Get the attachment entry specified by,
        `attach`, which can be,
            `id` or `Attachment` instance.
        and send the file for downloading."""
        attach = self.get_attach( attach=attach )
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            attach.download_count += 1
        content = self._read_content(attach)
        return (attach, content)

    def get_attach( self, attach=None, attrload=[], attrload_all=[] ) :
        """Get the attachment entry identified by,
        `attach` which can be
            `id` or `Attachment` instance.

        Return,
            Attachment Instance(s)."""
        if isinstance( attach, Attachment ) and attrload==[] and \
           attrload_all==[] :
            return attach

        msession = meta.Session()

        # Compose query based on `attach` type
        if isinstance( attach, (int, long) ) :
            q = msession.query( Attachment ).filter_by( id=attach )
        elif isinstance( attach, Attachment ) :
            q = msession.query( Attachment ).filter_by( id=attach.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            attach = q.first()

        elif attach == None :
            q = msession.query( Attachment )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            attach = q.all()

        return attach

    @h.postproc()
    def create_attach( self, filename, fdfile=None, uploader=None,
                       summary=None, log=False, doclose=None ) :
        """Create an attachment for `filename`,
        Return,
            Attachment instance."""
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        uploader = uploader and userscomp.get_user( uploader )
        content = fdfile and fdfile.read() or ''
        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            attach = Attachment( filename, 0 )
            summary and setattr( attach, 'summary', summary )
            uploader and setattr( attach, 'uploader', uploader )
            attach.size = len(content)
            msession.add(attach)

        self._store_fileupload(content, attach)
        fdfile and fdfile.close()

        log = log and 'Uploaded attachment, %s' % filename or ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, attach, uploader, log) :
            srchcomp.indexattach( [attach] )
            log and tlcomp.log( uploader, log, attach=attach )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, attach, uploader, log ))
        return attach

    @h.postproc()
    def edit_summary( self, attach, summary='', doclose=None, byuser=None ) :
        """Edit the summary text for already created attachment, specified by,
        `attach` which can be,
            `id` or `Attachment` instance."""
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        attach    = self.get_attach( attach )
        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            attach.summary = summary
            log = 'Updated summary, `%s`' % summary

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, attach, log, byuser) :
            srchcomp.indexattach( [attach], replace=True )
            attach and tlcomp.log( byuser, log, attach=attach )
        doclose( h.hitchfn(onclose, tlcomp, srchcomp, attach, log, byuser))
        return attach

    @h.postproc()
    def remove_attach(self, attach=None, log=False, doclose=None, byuser=None) :
        """Remove the attachment entry identified by,
        `attach` which can be
            `id` or `Attachment` instance.
        """
        from zeta.config.environment import userscomp, tlcomp, srchcomp

        attach = self.get_attach( attach=attach )
        msession = meta.Session()
        attach and self._remove_content(attach)
        filename = attach.filename
        with msession.begin( subtransactions=True ) :
            attach and msession.delete( attach )
            msession.flush()

        log = log and 'deleted attachment, %s' % filename or ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, attach, log, byuser) :
            # TODO : Delete this attachment.
            #srchcomp.indexattach( [attach], replace=True )
            log and tlcomp.log( byuser, log )
        doclose( h.hitchfn(onclose, tlcomp, srchcomp, attach, log, byuser))
        return attach

    @h.postproc()
    def add_tags( self, attach, tags=[], doclose=None, byuser=None ) :
        """Add tags for the attachment entry identified by,
        `attach` which can be
            `id` or `Attachment` instance.
        `tags` can be,
            list of `tagname` strings
            list of `Tag` instances"""
        from zeta.config.environment import tagcomp, tlcomp, srchcomp

        attach  = self.get_attach( attach=attach )
        if attach and tags :
            addtags = tagcomp.model_add_tags( tags, attach, byuser=byuser )
            log = addtags and 'added tags, `%s`' % ', '.join(addtags) or ''
        else :
            addtags = []
            log = ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, attach, log, byuser) :
            srchcomp.indexattach( [attach], replace=True )
            log and tlcomp.log( byuser, log, attach=attach )
        doclose( h.hitchfn(onclose, tlcomp, srchcomp, attach, log, byuser))
        return attach

    @h.postproc()
    def remove_tags( self, attach, tags=[], doclose=None, byuser=None ) :
        """Remove tags for the attachment entry identified by,
        `attach` which can be
            `id` or `Attachment` instance.
        `tags` can be,
            list of `tagname` strings
            list of `Tag` instances"""
        from zeta.config.environment import tagcomp, tlcomp, srchcomp

        attach = self.get_attach( attach=attach )
        if attach and tags :
            rmtags = tagcomp.model_remove_tags( tags, attach, byuser=byuser )
            log = rmtags and 'deleted tags , `%s`' % ', '.join(rmtags) or ''
        else :
            rmtags = []
            log = ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, attach, log, byuser) :
            srchcomp.indexattach( [attach], replace=True )
            log and tlcomp.log( byuser, log, attach=attach )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, attach, log, byuser ))
        return attach

    def model_add_attach( self, attach, modelobj, byuser=None ) :
        """Add attachment to the model instance `modelobj`.
        `attach` which can be
            `id` or `Attachment` instance."""
        attach = self.get_attach( attach=attach )

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            attach and modelobj.attachments.append( attach )

    def model_remove_attach( self, attach, modelobj, byuser=None ) :
        """Remove attachment from model instance `modelobj`.
        `attach` which can be
            `id` or `Attachment` instance."""
        attach   = self.get_attach( attach=attach )

        msession = meta.Session()
        with msession.begin( subtransactions=True ) :
            if attach :
                msession.delete( attach )

    # Data Crunching methods on attachment database.

    def attachments( self, offset=None, limit=None ) :
        """Collect all attachments.
        Return attachments"""

        oj = t_attachment.outerjoin(
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

        q  = select( [ t_attachment.c.id, t_attachment.c.filename,
                       t_attachment.c.size, t_attachment.c.summary,
                       t_attachment.c.download_count, t_attachment.c.created_on,
                       t_user.c.username, t_tag.c.tagname,
                     ],
                     bind=meta.engine
                   ).select_from( oj )
        
        if offset :
            q = q.offset( offset )
        if limit :
            q = q.limit( limit )

        entries = q.execute().fetchall()
        result  = {}
        for tup in entries :
            if tup[0] == None : continue
            foratt  = result.get( tup[0], [] )
            if foratt :
                tup[7] and foratt[-1].append( tup[7] )
            else :
                foratt = list( tup[1:7] )
                foratt.append( tup[7] and [ tup[7] ] or [] )
            result[ tup[0] ] = foratt

        return result

    def latestattachs( self ) :
        """Fetch the latest attachment"""
        msession = meta.Session()
        q = msession.query( Attachment ).order_by( Attachment.id.desc()).limit(1)
        attachs = q.all()
        attach = attachs and attachs[0] or None
        return attach

    def attachassc( self ) :
        """Fetch all the entries for user, project, license, ticket, wiki,
        review etc... that have associated attachments"""
        attachs = {}
        q = select( [ at_user_icons.c.attachid, at_user_icons.c.userid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('user', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_user_photos.c.attachid, at_user_photos.c.userid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('user', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_license_attachments.c.attachmentid,
                      at_license_attachments.c.licenseid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('license', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_project_icons.c.attachid,
                      at_project_icons.c.projectid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('project', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_project_logos.c.attachid,
                      at_project_logos.c.projectid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('project', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_project_attachments.c.attachmentid,
                      at_project_attachments.c.projectid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('project', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_ticket_attachments.c.attachmentid,
                      at_ticket_attachments.c.ticketid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('ticket', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_review_attachments.c.attachmentid,
                      at_review_attachments.c.reviewid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('review', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        q = select( [ at_wiki_attachments.c.attachmentid,
                      at_wiki_attachments.c.wikiid ],
                    bind=meta.engine )
        [ attachs.setdefault( aid, [] ).append( ('wiki', uid) )
          for aid, uid in q.execute().fetchall() if aid ]

        return attachs


    def uploadedbyuser( self, user ) :
        """Find all the attachments uploaded by `user`"""
        oj = at_attachment_uploaders.outerjoin( t_attachment 
                                   ).outerjoin(
                                        at_attachment_tags,
                                        at_attachment_tags.c.attachmentid == t_attachment.c.id
                                   ).outerjoin(
                                        t_tag,
                                        at_attachment_tags.c.tagid == t_tag.c.id
                                   )

        q  = select( [ t_attachment.c.id, t_attachment.c.filename,
                       t_attachment.c.size, t_attachment.c.summary,
                       t_attachment.c.download_count, t_attachment.c.created_on,
                       t_tag.c.tagname,
                     ],
                     bind=meta.engine
                   ).select_from( oj 
                   ).where( at_attachment_uploaders.c.uploaderid == user.id )

        entries = q.execute().fetchall()
        attachs = {}
        for tup in entries :
            if tup[0] == None : continue
            foratt  = attachs.get( tup[0], [] )
            if foratt :
                tup[5] and foratt[-1].append( tup[5] )
            else :
                foratt = list( tup[1:5] )
                foratt.append( tup[5] and [ tup[5] ] or [] )
            attachs[ tup[0] ] = foratt

        return attachs

    # Doc - metadata for 'attach' table entries
    def documentof( self, attach, search='xapian' ) :
        """Make a document for 'attach' entry to create a searchable index
            [ metadata, attributes, document ], where

            metadata   : { key, value } pairs to be associated with document
            attributes : searchable { key, value } pairs to be associated with
                         document
            document   : [ list , of, ... ] document string, with increasing
                         weightage
        """
        attach   = self.get_attach( attach, attrload=[ 'tags', 'uploader' ] )
        tagnames = [ t.tagname for t in attach.tags ]
           
        metadata = \
            { 'doctype' : 'attach', 'id' : attach.id }
           
        attributes = \
            search == 'xapian' and \
                [ 'XID:attach_%s'   % attach.id,                # id
                  'XCLASS:site', 'XCLASS:attach',               # class
                  'XUSER:%s'        % attach.uploader.username, # user
                  'XFILE:%s'        % attach.filename,          # file
                ] + \
                [ 'XTAG:%s'         % t                         # tag
                  for t in tagnames ] \
            or \
                []

        attrs    = ' '.join(
                        [ attach.uploader.username, attach.filename ] + tagnames
                   )
        try :
            content = unicode( self.content(attach) )
        except :
            content = ''
        document = [ content, attach.summary, attrs ]

        return [ metadata, attributes, document ]
