# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on license tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   1. post-processing function can be subscribed to onclose event and can
#      thus be delayed until the request is completed.
# Todo    :
#   1. While license is removed, remove them from search index as well.


from   __future__               import with_statement

from   sqlalchemy               import *
from   sqlalchemy.orm           import *

from   zeta.ccore               import Component
from   zeta.model               import meta
from   zeta.model.schema        import t_license, t_attachment, t_tag, t_user, \
                                       t_project, \
                                       at_license_attachments, at_attachment_tags, \
                                       at_attachment_uploaders, at_project_licenses
from   zeta.model.tables        import License
from   zeta.lib.error           import ZetaLicenseError
import zeta.lib.helpers         as h

class LicenseComponent( Component ) :
    """Component License."""

    @h.postproc()
    def create_license( self, licensedetail, update=False, doclose=None,
                        byuser=None ) :
        """Create an entry in the license table.
        licensedetail is,
            (licid, licensename, summary, text, source)
        if update=True,
            An exisiting license identified by `licensedetail[0]` will be
            updated with licensedetail.
            `licid` can be `id` ir `License` instance."""
        from zeta.config.environment import tlcomp, srchcomp

        if filter( h.filter_badargs, licensedetail[1:] ) :
            raise ZetaLicenseError(
                "License Field empty while creating license entry ( %s ) !!" \
                        % licensedetail )

        msession = meta.Session()
        license = (update and self.get_license( licensedetail[0] )) or None
        with msession.begin( subtransactions=True ) :
            if ( update and license ) or license :
                licensedetail[1] and \
                        setattr( license, 'licensename', licensedetail[1] )
                licensedetail[2] and \
                        setattr( license, 'summary', licensedetail[2] )
                licensedetail[3] and \
                        setattr( license, 'text', licensedetail[3] )
                licensedetail[4] and \
                        setattr( license, 'source', licensedetail[4] )
                log        = 'updated license'
                idxreplace = True
            else :
                license = License( *licensedetail[1:] )
                msession.add( license )
                msession.flush()
                log        = 'created new license'
                idxreplace = False

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, license, byuser, log, idxreplace) :
            log and tlcomp.log( byuser, log, license=license )
            srchcomp.indexlicense( [license], replace=idxreplace )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, license, byuser, log, idxreplace ))
        return license

    def get_license( self, license=None, attrload=[], attrload_all=[] ) :
        """Get the License instance identified by,
        `licence` which can be,
            `id` or `licensename` or License instance.

        Returns,
            License instance or,
            List of License instance."""
        if isinstance( license, License ) and attrload==[] and attrload_all==[]:
            return license

        msession = meta.Session()

        # Compose query based on `license` type
        if isinstance( license, (int,long) ) :
            q = msession.query( License ).filter_by( id=license )
        elif isinstance( license, (str, unicode) ) :
            q = msession.query( License ).filter_by( licensename=license )
        elif isinstance( license, License ) :
            q = msession.query( License ).filter_by( id=license.id )
        else :
            q = None

        # Compose eager-loading options
        if q != None :
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            license = q.first()

        elif license == None :
            q = msession.query( License )
            q = q.options( *[ eagerload_all( e ) for e in attrload_all ] )
            q = q.options( *[ eagerload( e ) for e in attrload ] )
            license = q.all()

        else :
            license = None

        return license


    def license_exists( self, license ) :
        """Check whether there is a license entry identified by,
        `licence` which can be,
            `id` or `licensename` or License instance.

        Return,
            True    if license entry is already present.
            False   if license entry is not present. 
        """
        license = self.get_license( license )
        return license and True or False

    @h.postproc()
    def remove_license( self, license, doclose=False, byuser=None ) :
        """Remove the license instance identified by,
        `licence` which can be,
            `id` or `licensename` or License instance.
        """
        from zeta.config.environment import tlcomp, srchcomp

        msession = meta.Session()
        license  = self.get_license( license )
        licname  = license and license.licensename or ''
        with msession.begin( subtransactions=True ) :
            license and msession.delete( license )

        # Post processing, optional deferred handling
        def onclose(tlcomp, licname, byuser) :
            tlcomp.log( byuser, 'deleted license %s' % licname )
        doclose( h.hitchfn( onclose, tlcomp, licname, byuser ))
        return None

    @h.postproc()
    def add_tags( self, license, tags=[], doclose=None, byuser=None ) :
        """For the license entry added tags.
        `license` which can be,
            `id` or `licensename` or License instance.
        `tags` which can be,
            `tagname`."""
        from zeta.config.environment import tagcomp, tlcomp, srchcomp

        license = self.get_license( license )
        if license and tags :
            addtags = tagcomp.model_add_tags( tags, license, byuser )
        else :
            addtags = []

        log = addtags and 'added tags, %s' % ', '.join( addtags ) or ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, license, log, byuser) :
            log and tlcomp.log( byuser, log, license=license )
            srchcomp.indexlicense( [license], replace=True )
        doclose( h.hitchfn( onclose, tlcomp, srchcomp, license, log, byuser ))
        return addtags

    @h.postproc()
    def remove_tags( self, license, tags=[], doclose=None, byuser=None ) :
        """For the license entry identified by,
        `licence` which can be,
            `id` or `licensename` or License instance.
        remove tags specified by `tags`."""
        from zeta.config.environment import tagcomp, tlcomp, srchcomp

        license = self.get_license( license )
        if license and tags :
            rmtags = tagcomp.model_remove_tags( tags, license, byuser )
        else :
            rmtags = []

        log = rmtags and 'deleted tags, %s' % ', '.join( rmtags )

        # Post processing, optional deferred handling
        def onclose(tlcomp, srchcomp, license, log, byuser) :
            log and tlcomp.log( byuser, log, license=license )
            srchcomp.indexlicense( [license], replace=True )
        doclose( h.hitchfn(onclose, tlcomp, srchcomp, license, log, byuser ))
        return rmtags

    @h.postproc()
    def add_attach( self, license, attach, doclose=None, byuser=None ) :
        """Add attachment to the license identified by,
        `license` which can be,
            `id` or `licensename` or License instance.
        `attach` can be
            `id` or `resource_url` or `Attachment` instance."""
        from zeta.config.environment import attachcomp, tlcomp, srchcomp

        license = self.get_license( license )
        attach = attachcomp.get_attach( attach )
        if license and attach:
            attachcomp.model_add_attach( attach, license, byuser )
            log = 'uploaded attachment %s' % attach.filename
        else :
            log = ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, license, log, byuser) :
            log and tlcomp.log( byuser, log, license=license )
        doclose( h.hitchfn( onclose, tlcomp, license, log, byuser ))
        return None

    @h.postproc()
    def remove_attach( self, license, attach, doclose=None, byuser=None ) :
        """Remove attachment to the license identified by,
        `license` which can be,
            `id` or `licensename` or License instance.
        `attach` can be
            `id` or `resource_url` or `Attachment` instance."""
        from zeta.config.environment import attachcomp, tlcomp, srchcomp

        license    = self.get_license( license )
        attach     = attachcomp.get_attach( attach )
        if license and attach:
            attachcomp.model_remove_attach( attach, license, byuser )
            log = 'deleted attachment %s' % attach.filename
        else :
            log = ''

        # Post processing, optional deferred handling
        def onclose(tlcomp, license, log, byuser) :
            log and tlcomp.log( byuser, log, license=license )
        doclose( h.hitchfn( onclose, tlcomp, license, log, byuser ))
        return None


    # Data Crunching methods on user tables.

    def licensefields( self ) :
        """Fetch unique license fields from all licenses from database and
        return them as a list of tuples"""
        return [ [ l.id, l.licensename,
                   [ [ p.id, p.projectname ] for p in l.projects ]
                 ] for l in self.get_license( attrload=[ 'projects' ] ) ]

    def licprojects( self, licid=None ) :
        """Fetch list of projects under license(s)"""
        licprojects = {}

        # Prepare statement and Query database
        oj = t_license.outerjoin( at_project_licenses ).outerjoin( t_project )
        q  = select( [ t_license.c.id, t_project.c.projectname ],
                     bind=meta.engine
                   ).select_from( oj )
        if licid :
            q = q.where( t_license.c.id == licid )

        # Prepare data
        [ licprojects.setdefault( tup[0], [] ).append( tup[1] )
          for tup in q.execute().fetchall() if tup[0] ]

        return licprojects

    # Doc - metadata for 'license' table entries
    def documentof( self, license, search='xapian' ) :
        """Make a document for 'license' entry to create a searchable index
            [ metadata, attributes, document ], where

            metadata   : { key, value } pairs to be associated with document
            attributes : searchable { key, value } pairs to be associated with
                         document
            document   : [ list , of, ... ] document string, with increasing
                         weightage
        """
        license  = self.get_license( license, attrload=[ 'tags' ] )
        tagnames = [ t.tagname for t in license.tags ]
        metadata = \
            { 'doctype' : 'license', 'id' : license.id }
           
        attributes = \
            search == 'xapian' and \
                [ 'XID:license_%s' % license.id,                # id
                  'XCLASS:site', 'XCLASS:license',              # class
                  'XLICENSE:%s'    % license.licensename,       # license
                ] + \
                [ 'XTAG:%s'        % t                          # tag
                  for t in tagnames ] \
            or \
                []

        attrs    = ' '.join( [ license.licensename ] + tagnames )
        document = [ license.text,
                     '%s %s' % (license.summary, license.source),
                     attrs
                   ]

        return [ metadata, attributes, document ]


    def attachments( self ) :
        """Collect attachment list for license,
        Return attachments"""

        oj = t_license.outerjoin( at_license_attachments
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

        q  = select( [ t_license.c.id, t_license.c.licensename,
                       t_attachment.c.id, t_attachment.c.filename,
                       t_attachment.c.size, t_attachment.c.summary,
                       t_attachment.c.download_count, t_attachment.c.created_on,
                       t_user.c.username, t_tag.c.tagname,
                     ],
                     bind=meta.engine
                   ).select_from( oj )

        entries = q.execute().fetchall()
        result  = {}
        for tup in entries :
            if tup[2] == None : continue
            forlic = result.get( tup[0:2], {} )
            foratt = forlic.get( tup[2], [] )
            if foratt :
                tup[9] and foratt[-1].append( tup[9] )
            else :
                foratt = list( tup[3:9] )
                foratt.append( tup[9] and [ tup[9] ] or [] )
            forlic[ tup[2] ]   = foratt
            result[ tup[0:2] ] = forlic

        return result

    # License component properties
    licensenames = property(
                        lambda self : [ lic.licensename
                                            for lic in self.get_license() ]
                   )
