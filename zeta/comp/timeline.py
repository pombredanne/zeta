# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component to access data base and do data-crunching on timeline tables.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Unit-test log(), fetchlogs(), get_log() method.

from   __future__              import with_statement

from   sqlalchemy              import insert, select

import zeta.lib.helpers        as h
from   zeta.lib.constants      import *
from   zeta.lib.error          import ZetaError
from   zeta.lib.base           import BaseController
from   zeta.ccore              import Component
from   zeta.model              import meta
from   zeta.model.schema       import t_wikipage, t_timeline, \
                                      at_user_logs, at_permgroup_logs, \
                                      at_tag_logs, at_attachment_logs, \
                                      at_license_logs, at_project_logs, \
                                      at_ticket_logs, at_review_logs, \
                                      at_vcs_logs, at_wiki_logs
from   zeta.model.tables       import Timeline, User, PermissionGroup, Tag, \
                                      Attachment, License, Project, Ticket, \
                                      Review, Vcs, Wiki

tbl_mappers = meta.tbl_mappers
metadata    = meta.metadata

class TimelineComponent( Component ) :

    def log( self, user, log, **kwargs ) :
        """Make an entry and all the timeline as logs to models, specified by
        kwargs, which can be,
            permgroup, tag, attach, license,
            project,
            ticket,
            review,
            wiki"""
        config = self.compmgr.config
        cntlr = BaseController()
        tl = None
        userscomp = h.fromconfig('userscomp')
        c = config.get( 'c', None )
        if not config['zeta.enabletline'] :
            return None

        user = user or ( c and c.authuser )
        user = isinstance(user, User) and user.id or user
        user = userscomp.get_user( user )
        log = user and ( u'%s' % log.decode( 'utf8' )) or log.decode('utf8')
        userhtml = '<a href="%s">%s</a>' % \
                        ( cntlr.url_user(user.username), user.username )
        itemhtml = url_formodels( **kwargs )

        msession  = meta.Session()
        with msession.begin( subtransactions=True ) :
            # Insert the timeline log
            stmt = t_timeline.insert().values(
                            log=unicode(log[:LEN_1K]),
                            userhtml=unicode(userhtml),                            
                            itemhtml=unicode(itemhtml),                            
                   )
            res = msession.connection().execute(stmt)
            tl_id = res.inserted_primary_key[0]

            # User log
            stmt = at_user_logs.insert().values(
                            timelineid=tl_id,
                            userid=user.id
                   )
            msession.connection().execute(stmt)

            # Object logs
            kwargs.pop( 'staticwiki', None )
            for k in kwargs :
                kw = { 'timelineid' : tl_id,
                        k+'id'       : kwargs[k].id
                     }
                stmt = obj2assctable[k].insert().values( **kw )
                msession.connection().execute(stmt)

        return None

    def fetchlogs( self, assc_tbls, modelobj=None, limit=None,
                   id=None, direction=None ) :
        """Fetch log entries for associated tables 'assc_tbls',
        if modelobj != None,
            logs associated to modelobj.id
        if limit :
            
        Always return list of Tline instances """
        msession  = meta.Session()

        if direction == 'newer' :
            q = msession.query( Timeline ).order_by( Timeline.id.asc() )
            q = id and q.filter( Timeline.id > id )
        elif direction == 'older' :
            q = msession.query( Timeline ).order_by( Timeline.id.desc() )
            q = id and q.filter( Timeline.id < id )
        else :
            q = msession.query( Timeline ).order_by( Timeline.id.desc() )

        if assc_tbls and isinstance( assc_tbls, list ) :
            q = q.join( *assc_tbls )
        elif assc_tbls :
            q = q.join( assc_tbls )

        if modelobj :
            q = q.filter_by( id=modelobj.id )

        if limit != None :
            q = q.limit( limit )
        
        # Adjust order
        logs = q.all()
        if direction == 'newer' and id :
            logs.reverse()
        return logs

    def fetchprojlogs( self, project, limit=None, id=None, direction=None ) :
        """Fetch log entries for 'project'"""
        msession  = meta.Session()
        
        if direction == 'newer' :
            common_q = msession.query( Timeline ).order_by( Timeline.id.asc() )
            common_q = id and common_q.filter( Timeline.id > id ) or common_q
        elif direction == 'older' :
            common_q = msession.query( Timeline ).order_by( Timeline.id.desc() )
            common_q = id and common_q.filter( Timeline.id < id ) or common_q
        else :
            common_q = msession.query( Timeline ).order_by( Timeline.id.desc() )

        # Fetch project logs.
        q    = common_q.join( 'project' ).filter_by( id=project.id )
        q    = limit and q.limit( limit ) or q
        logs = q.all()

        # Fetch project-ticket logs.
        q = common_q.join( 'ticket', 'project' ).filter_by( id=project.id )
        q = limit and q.limit( limit ) or q
        logs += q.all()

        # Fetch project-vcs logs.
        q = common_q.join( 'vcs', 'project' ).filter_by( id=project.id )
        q = limit and q.limit( limit ) or q
        logs += q.all()

        # Fetch project-review logs.
        q = common_q.join( 'review', 'project' ).filter_by( id=project.id )
        q = limit and q.limit( limit ) or q
        logs += q.all()

        # Fetch project-ticket logs.
        q = common_q.join( 'wiki', 'project' ).filter_by( id=project.id )
        q = limit and q.limit( limit ) or q
        logs += q.all()

        # Merge them and sort them
        logs = sorted( logs, key=lambda log : log.id, reverse=True )

        return logs

    def get_log( self, fromid, limit ) :
        """Fetch logs from `fromid` to `toid"""
        msession = meta.Session()
        q        = msession.query( Timeline 
                              ).filter( Timeline.id >= fromid )
        q        = limit and q.limit( limit ) or q
        logs     = q.all()
        return logs



obj2assctable = {
    'user'      : at_user_logs,
    'permgroup' : at_permgroup_logs,
    'tag'       : at_tag_logs,
    'attach'    : at_attachment_logs,
    'license'   : at_license_logs,
    'project'   : at_project_logs,
    'ticket'    : at_ticket_logs,
    'review'    : at_review_logs,
    'vcs'       : at_vcs_logs,
    'wiki'      : at_wiki_logs,
}

def url_formodel( name, obj ) :
    """Compute the href for model object"""
    from zeta.config.environment import \
            userscomp, attcomp, tagcomp, liccomp, projcomp, wikicomp, \
            tckcomp, revcomp, vcscomp

    a_tmpl = name + ' <a href="%s" title="%s">%s</a>'
    cntlr = BaseController()

    if name == 'user' :
        u = userscomp.get_user( obj )
        a = a_tmpl % ( cntlr.url_user( u.username ), u.username, u.username )

    elif name == 'tag' :
        t = tagcomp.get_tag( obj )
        a = a_tmpl % ( cntlr.url_tag( t.tagname ), t.tagname, t.tagname )

    elif name == 'attach' :
        att = attcomp.get_attach( obj )
        a = a_tmpl % ( cntlr.url_attach( att.id ), att.filename, att.filename )

    elif name == 'license' :
        l = liccomp.get_license( obj )
        a = a_tmpl % ( cntlr.url_forlicense( l.id ), l.summary, l.licensename )

    elif name == 'project' :
        p = projcomp.get_project( obj )
        a = a_tmpl % ( cntlr.url_forproject( p.projectname ), p.summary, p.projectname )

    elif name == 'ticket' :
        a = a_tmpl % ( cntlr.url_ticket( obj.project.projectname, obj.id ),
                       obj.summary, obj.id )

    elif name == 'review' :
        a = a_tmpl % ( cntlr.url_revwid( obj.project.projectname, obj.id ),
                       obj.resource_url, obj.resource_url )

    elif name == 'vcs' :
        a = a_tmpl % ( cntlr.url_vcsbrowse( obj.project.projectname, obj.id ),
                       obj.name, obj.name )

    elif name == 'wiki' :
        a = a_tmpl % ( obj.wikiurl, obj.summary, obj.wikiurl )

    elif name == 'staticwiki' :
        a = a_tmpl % ( obj.path, obj.path, obj.path )

    else :
        raise ZetaError( 'Unkown model name in timeline reference' )

    return a

def url_formodels( **kwargs ) :
    return ', '.join([ url_formodel( k, kwargs[k] ) 
                       for k in kwargs if kwargs[k] ])

