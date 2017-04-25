# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""The application's model interface"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
#   1. Logs backreference attribute should be same as the 'assc_tables'
# Todo    : None

from   sqlalchemy.ext.declarative import declarative_base
from   sqlalchemy.orm             import sessionmaker, mapper, scoped_session, \
                                         relation, backref, deferred
from   sqlalchemy                 import create_engine
from   sqlalchemy                 import Table, Column, MetaData, ForeignKey
from   sqlalchemy                 import Integer, String

import meta
from   zeta.model.create          import create_models, delete_models
from   zeta.model.schema          import *
from   zeta.model.tables          import *


tbl_mappers = meta.tbl_mappers      # { Table_Class : mapper instance }

# Note :
#   The following needs to be addressed while designing the database.
#
#   * Try to vertically partition one or more tables. Where tables can have
#     constraints on other tables in the same partitions.
#   * Tables across the partitions are related only through association
#     tables. This becomes important especially for entry deletion.
#   * Cascading. Only cascade the tables that are closely related.
#   * Vertical partition can help in scaling the database across several
#     sql servers.
#   * A draw back in relating tables through association table is that, we can
#     not enforce relationship as mandatory. So, document these relationship
#     requirements.
#
#   Mandatory relationship between `user` Table and other Table.
#
#       uploader    - Attachment
#       admin       - Project
#       owner       - Component
#       promptuser  - Ticket
#       owner       - TicketStatusHistory
#       commentby   - TicketComment
#       author      - Review
#       moderator   - Review
#       commentby   - ReviewComment
#       creator     - Wiki
#       author      - WikiPage
#       commentby   - WikiComment
#
#   Mandatory relationship between `license` Table and other table.
#       
#       license     - Project
#
#   Mandatory relationship between `project` Table and other table.
#
#       project     - Ticket
#       projects    - Wiki

#-----------------------------------------------------------------------------

def map_tables() :
    """Map Python objects and Table Schemas"""
    global tbl_mappers

    if tbl_mappers :
        return

    #------------------------ System Table Mapping -----------------------------

    tbl_mappers[System]         = \
            mapper( System, t_system )

    tbl_mappers[StaticWiki]     = \
            mapper( StaticWiki, t_staticwiki,
                    properties={ 'type' : relation( WikiType )
                               })

    #------------------------ Permission Table Mapping -----------------------

    tbl_mappers[PermissionName]  = \
            mapper( PermissionName, t_permission_name )
    tbl_mappers[PermissionGroup] = \
            mapper( PermissionGroup, t_permission_group,
                    properties={ 'perm_names'     : relation( PermissionName,
                                                              secondary=at_permission_maps, 
                                                            ),
                                 'users'          : relation( User, 
                                                              secondary=at_user_permissions, 
                                                              backref='permgroups'
                                                            ),
                                 'projectperms'   : relation( ProjectPerm,
                                                              backref='permgroup',
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'projteamperms'  : relation( ProjectTeam_Perm,
                                                              backref='permgroup',
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'logs'           : relation( Timeline,
                                                              secondary=at_permgroup_logs,
                                                              backref=backref( 'permgroup', uselist=False ),
                                                            ),
                               })

    #------------------------ User Table Mapping -----------------------------

    tbl_mappers[UserRelation_Type]   = \
            mapper( UserRelation_Type, t_userrelation_type )
    tbl_mappers[User]           = \
            mapper( User, t_user,
                    properties={ 'userinfo'        : relation( UserInfo,
                                                               uselist=False,
                                                               backref=backref( 'user', uselist=False ),
                                                               cascade='all, delete-orphan',
                                                             ),
                                 'photofile'       : relation( Attachment, 
                                                               secondary=at_user_photos,
                                                               uselist=False, 
                                                               backref=backref( 'photoofuser', uselist=False ),
                                                             ),
                                 'iconfile'        : relation( Attachment,
                                                               secondary=at_user_icons,
                                                               uselist=False,
                                                               backref=backref( 'iconofuser', uselist=False ),
                                                             ),
                                 'userconnections' : relation( UserRelation,
                                                               primaryjoin=(t_user_relation.c.userfrom_id==t_user.c.id),
                                                               backref=backref( 'userfrom', uselist=False ),
                                                               cascade='all, delete-orphan'
                                                             ),
                                 'connectedusers'  : relation( UserRelation,
                                                               primaryjoin=(t_user_relation.c.userto_id==t_user.c.id),
                                                               backref=backref( 'userto', uselist=False ),
                                                               cascade='all, delete-orphan'
                                                             ),
                                 'projectperms'    : relation( ProjectPerm,
                                                               backref=backref( 'user', uselist=False ),
                                                               cascade='all, delete-orphan'
                                                             ),
                                 'projectteams'    : relation( ProjectTeam,
                                                               backref=backref( 'user', uselist=False ),
                                                               cascade='all, delete-orphan'
                                                             ),
                                 'favoriteprojects': relation( Project,
                                                               secondary=at_project_favorites,
                                                               backref='favoriteof',
                                                             ),
                                 'favoritetickets' : relation( Ticket,
                                                               secondary=at_ticket_favorites,
                                                               backref='favoriteof',
                                                             ),
                                 'favoritereviews' : relation( Review,
                                                               secondary=at_review_favorites,
                                                               backref='favoriteof',
                                                             ),
                                 'favoritewikis'   : relation( Wiki,
                                                               secondary=at_wiki_favorites,
                                                               backref='favoriteof',
                                                             ),
                                 'votes'           : relation( Vote,
                                                               backref=backref( 'voter', uselist=False ),
                                                               cascade='all, delete-orphan'
                                                             ),
                                 'logs'            : relation( Timeline,
                                                               secondary=at_user_logs,
                                                               backref=backref( 'user', uselist=False ),
                                                             ),
                               })
    tbl_mappers[UserInfo]       = \
            mapper( UserInfo, t_user_info )
    tbl_mappers[UserRelation]   = \
            mapper( UserRelation, t_user_relation,
                    properties={ 'userreltype' : relation( UserRelation_Type, uselist=False ) })

    #------------------------ General Table Mapping -----------------------------

    tbl_mappers[Tag]            = \
            mapper( Tag, t_tag,
                    properties={ 'logs'        : relation( Timeline,
                                                           secondary=at_tag_logs,
                                                           backref=backref( 'tag', uselist=False ),
                                                         ),
                               })
    tbl_mappers[Attachment]     = \
            mapper( Attachment, t_attachment, 
                    properties={ 'tags'        : relation( Tag,
                                                           secondary=at_attachment_tags,
                                                           backref='attachments',
                                                         ),
                                 'uploader'    : relation( User,
                                                           secondary=at_attachment_uploaders,
                                                           uselist=False,
                                                           backref='uploadedattachments',
                                                         ),
                                 'logs'        : relation( Timeline,
                                                           secondary=at_attachment_logs,
                                                           backref=backref( 'attachment', uselist=False ),
                                                         ),
                                 'content'     : deferred( t_attachment.c.content ),
                               })
    tbl_mappers[License]        = \
            mapper( License, t_license,
                    properties={ 'attachments' : relation( Attachment,
                                                           secondary=at_license_attachments,
                                                           backref='licenses', cascade='all'
                                                         ),
                                 'tags'        : relation( Tag,
                                                           secondary=at_license_tags,
                                                           backref='licenses'
                                                         ),
                                 'logs'        : relation( Timeline,
                                                           secondary=at_license_logs,
                                                           backref=backref( 'license', uselist=False ),
                                                         ),
                               })
    tbl_mappers[Vote]           = mapper( Vote, t_vote )

    #------------------------ Project Table Mapping ---------------------------

    tbl_mappers[ProjectTeam_Type]   = \
            mapper( ProjectTeam_Type, t_projectteam_type )
    tbl_mappers[Project]        =  \
            mapper( Project, t_project, 
                    properties={ 'project_info'   : relation( ProjectInfo,
                                                              uselist=False,
                                                              backref=backref( 'project', uselist=False ),
                                                              cascade='all, delete-orphan',
                                                            ),
                                 'license'        : relation( License,
                                                              secondary=at_project_licenses,
                                                              uselist=False,
                                                              backref='projects'
                                                            ),
                                 'admin'          : relation( User,
                                                              secondary=at_project_admins,
                                                              uselist=False,
                                                              backref='adminprojects'
                                                            ),
                                 'logofile'       : relation( Attachment, 
                                                              secondary=at_project_logos,
                                                              uselist=False, 
                                                              backref=backref( 'logoofproject', uselist=False ),
                                                            ),
                                 'iconfile'       : relation( Attachment,
                                                              secondary=at_project_icons,
                                                              uselist=False,
                                                              backref=backref( 'iconofproject', uselist=False ),
                                                            ),
                                 'mailinglists'   : relation( MailingList,
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'ircchannels'    : relation( IRCChannel,
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'components'     : relation( PrjComponent,
                                                              backref='project',
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'milestones'     : relation( Milestone,
                                                              backref='project',
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'versions'       : relation( Version,
                                                              backref='project',
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'team'           : relation( ProjectTeam,
                                                              backref=backref( 'project', uselist=False ),
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'projectperms'   : relation( ProjectPerm,
                                                              backref=backref( 'project', uselist=False ),
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'projteamperms'  : relation( ProjectTeam_Perm,
                                                              backref=backref( 'project', uselist=False ),
                                                              cascade='all, delete-orphan'
                                                            ),
                                 'attachments'    : relation( Attachment,
                                                              secondary=at_project_attachments,
                                                              backref='projects',
                                                            ),
                                 'tags'           : relation( Tag,
                                                              secondary=at_project_tags,
                                                              backref='projects'
                                                            ),
                                 'logs'           : relation( Timeline,
                                                              secondary=at_project_logs,
                                                              backref=backref( 'project', uselist=False ),
                                                            ),
                               })
    tbl_mappers[ProjectInfo]    = \
            mapper( ProjectInfo, t_project_info )
    tbl_mappers[MailingList]    = \
            mapper( MailingList, t_mailinglist )
    tbl_mappers[IRCChannel]    = \
            mapper( IRCChannel, t_ircchannel )
    tbl_mappers[PrjComponent]      = \
            mapper( PrjComponent, t_component,
                    properties={ 'owner'   : relation( User,
                                                       secondary=at_component_owners,
                                                       uselist=False,
                                                       backref='owncomponents'
                                                     ),
                                 'tags'    : relation( Tag,
                                                       secondary=at_component_tags,
                                                       backref='components'
                                                     ),
                               })
    tbl_mappers[Milestone]      = \
            mapper( Milestone, t_milestone,
                    properties={ 'tags' : relation( Tag,
                                                    secondary=at_milestone_tags,
                                                    backref='milestones' )
                               })
    tbl_mappers[Version]        = \
            mapper( Version, t_version,
                    properties={ 'tags' : relation( Tag,
                                                    secondary=at_version_tags,
                                                    backref='versions' )
                               })
    tbl_mappers[ProjectPerm]   = \
            mapper( ProjectPerm, t_project_perm )
    tbl_mappers[ProjectTeam_Perm]   = \
            mapper( ProjectTeam_Perm, t_projectteam_perm,
                    properties={ 'teamtype'  : relation( ProjectTeam_Type, uselist=False ) })
    tbl_mappers[ProjectTeam]   = \
            mapper( ProjectTeam, t_project_team,
                    properties={ 'teamtype' : relation( ProjectTeam_Type, uselist=False ) })


    #------------------------ Ticket Table Mapping ---------------------------

    tbl_mappers[TicketStatus]   = \
            mapper( TicketStatus, t_ticket_status )
    tbl_mappers[TicketType]     = \
            mapper( TicketType, t_ticket_type )
    tbl_mappers[TicketSeverity] = \
            mapper( TicketSeverity, t_ticket_severity )
    tbl_mappers[Ticket]         =  \
            mapper( Ticket, t_ticket, 
                    properties={ 
                                 'project'      : relation( Project,
                                                            secondary=at_ticket_projects,
                                                            uselist=False,
                                                            backref='tickets',
                                                          ),
                                 'components'   : relation( PrjComponent,
                                                            secondary=at_ticket_components,
                                                            backref='tickets',
                                                          ),
                                 'milestones'   : relation( Milestone,
                                                            secondary=at_ticket_milestones, 
                                                            backref='tickets',
                                                          ),
                                 'versions'     : relation( Version,
                                                            secondary=at_ticket_versions,
                                                            backref='tickets',
                                                          ),
                                 'statushistory': relation( TicketStatusHistory,
                                                            backref=backref( 'ticket', uselist=False ),
                                                            cascade='all, delete-orphan'
                                                          ),
                                 'comments'     : relation( TicketComment,
                                                            backref=backref( 'ticket', uselist=False ),
                                                            cascade='all, delete-orphan' ),
                                 'references'   : relation( TicketReference,
                                                            backref=backref( 'ticket', uselist=False ),
                                                            cascade='all, delete-orphan' ),
                                 'blockedby'    : relation( Ticket,
                                                            secondary=at_ticket_blockers,
                                                            primaryjoin=(at_ticket_blockers.c.blockingid==t_ticket.c.id),
                                                            secondaryjoin=(at_ticket_blockers.c.blockedbyid==t_ticket.c.id),
                                                            backref='blocking',
                                                         ),
                                 'type'         : relation( TicketType,
                                                            uselist=False,
                                                            backref='tickets'
                                                          ),
                                 'severity'     : relation( TicketSeverity,
                                                            uselist=False,
                                                            backref='tickets'
                                                          ),
                                 'children'     : relation( Ticket,
                                                            secondary=at_ticket_hier,
                                                            primaryjoin=(at_ticket_hier.c.partckid==t_ticket.c.id),
                                                            secondaryjoin=(at_ticket_hier.c.childtckid==t_ticket.c.id),
                                                            backref=backref( 'parent', uselist=False ),
                                                          ),
                                 'promptuser'   : relation( User,
                                                            secondary=at_ticket_promptusers,
                                                            uselist=False,
                                                            backref='promptingtickets'
                                                          ),
                                 'tags'         : relation( Tag,
                                                            secondary=at_ticket_tags,
                                                            backref='tickets',
                                                          ),
                                 'attachments'  : relation( Attachment,
                                                            secondary=at_ticket_attachments,
                                                            backref='tickets',
                                                          ),
                                 'votes'        : relation( Vote,
                                                            secondary=at_ticket_votes,
                                                            backref=backref( 'ticket', uselist=False ),
                                                          ),
                                 'logs'         : relation( Timeline,
                                                            secondary=at_ticket_logs,
                                                            backref=backref( 'ticket', uselist=False ),
                                                          ),
                               })
    tbl_mappers[TicketStatusHistory] = \
            mapper( TicketStatusHistory, t_ticket_status_history, 
                    properties={ 'owner'        : relation( User,
                                                            secondary=at_ticketstatus_owners,
                                                            uselist=False,
                                                            backref='owntickets',
                                                          ),
                                 'status'       : relation( TicketStatus, uselist=False )
                               })
    tbl_mappers[TicketComment] = \
            mapper( TicketComment, t_ticket_comment, 
                    properties={ 'commentby' : relation( User,
                                                         secondary=at_ticketcomment_authors,
                                                         uselist=False,
                                                         backref='ticketcomments',
                                                       ),
                                 'replies'   : relation( TicketComment,
                                                         secondary=at_ticket_replies,
                                                         primaryjoin=(
                                                            at_ticket_replies.c.replytoid==t_ticket_comment.c.id),
                                                         secondaryjoin=(
                                                            at_ticket_replies.c.ticketcommentid==t_ticket_comment.c.id),
                                                       ),
                               })
    tbl_mappers[TicketFilter] = \
            mapper( TicketFilter, t_ticket_filter, 
                    properties={ 'foruser' : relation( User,
                                                       uselist=False,
                                                       backref=backref( 'ticketfilters' ),
                                                     ),
                               })
    tbl_mappers[TicketReference] = \
            mapper( TicketReference, t_ticket_reference )

    #------------------------ Review Table Mapping ---------------------------

    tbl_mappers[ReviewComment_Nature] = \
            mapper( ReviewComment_Nature, t_reviewcomment_nature )
    tbl_mappers[ReviewComment_Action] = \
            mapper( ReviewComment_Action, t_reviewcomment_action )
    tbl_mappers[ReviewSet]         = \
            mapper( ReviewSet, t_reviewset,
                    properties={ 'project'      : relation( Project,
                                                            uselist=False,
                                                            backref='reviewsets',
                                                          ),
                                 'reviews'      : relation( Review,
                                                            secondary=at_reviewset_reviews,
                                                            backref=backref( 'reviewset', uselist=False ),
                                                          ),
                               })
    tbl_mappers[Review]         = \
            mapper( Review, t_review,
                    properties={ 'project'      : relation( Project,
                                                            secondary=at_review_projects,
                                                            uselist=False,
                                                            backref='reviews',
                                                          ),
                                 'author'       : relation( User,
                                                            secondary=at_review_authors,
                                                            uselist=False,
                                                            backref='authorreviews',
                                                          ),
                                 'moderator'    : relation( User,
                                                            secondary=at_review_moderators,
                                                            uselist=False,
                                                            backref='moderatereviews',
                                                          ),
                                 'participants' : relation( User,
                                                            secondary=at_review_participants,
                                                            backref='participatereviews'
                                                          ),
                                 'comments'     : relation( ReviewComment,
                                                            backref=backref( 'review', uselist=False ),
                                                            cascade='all, delete-orphan'
                                                          ),
                                 'tags'         : relation( Tag,
                                                            secondary=at_review_tags,
                                                            backref='reviews',
                                                          ),
                                 'attachments'  : relation( Attachment,
                                                            secondary=at_review_attachments,
                                                            backref='reviews',
                                                          ),
                                 'logs'         : relation( Timeline,
                                                            secondary=at_review_logs,
                                                            backref=backref( 'review', uselist=False ),
                                                          ),
                               })
    tbl_mappers[ReviewComment]  = \
            mapper( ReviewComment, t_review_comment,
                    properties={ 'commentby'    : relation( User,
                                                            secondary=at_review_commentors,
                                                            uselist=False,
                                                            backref='reviewcomments'
                                                          ),
                                 'nature'       : relation( ReviewComment_Nature,
                                                            uselist=False,
                                                            backref='reviewcomments',
                                                          ),
                                 'action'       : relation( ReviewComment_Action,
                                                            uselist=False,
                                                            backref='reviewcomments',
                                                          ),
                                 'replies'      : relation( ReviewComment,
                                                            secondary=at_review_replies,
                                                            primaryjoin=(
                                                            at_review_replies.c.replytoid==t_review_comment.c.id),
                                                            secondaryjoin=(
                                                            at_review_replies.c.reviewcommentid==t_review_comment.c.id),
                                                          ),
                               })

    #------------------------ Vcs Table Mapping ---------------------------

    tbl_mappers[VcsType]  = \
            mapper( VcsType, t_vcs_type )
    tbl_mappers[Vcs]           = \
            mapper( Vcs, t_vcs,
                    properties={ 'type'         : relation( VcsType ),
                                 'project'      : relation( Project,
                                                            secondary=at_vcs_projects,
                                                            uselist=False,
                                                            backref='vcslist'
                                                          ),
                                 'logs'         : relation( Timeline,
                                                            secondary=at_vcs_logs,
                                                            backref=backref( 'vcs', uselist=False ),
                                                          ),
                               })
    tbl_mappers[VcsMount]           = \
            mapper( VcsMount, t_vcsmount,
                    properties={ 'vcs'          : relation( Vcs,
                                                            uselist=False,
                                                            backref='mounts'
                                                          ),
                               })

    #------------------------ Wiki Table Mapping ---------------------------

    tbl_mappers[WikiType]  = \
            mapper( WikiType, t_wiki_type )
    tbl_mappers[WikiTable_Map]  = \
            mapper( WikiTable_Map, t_wikitable_map )
    tbl_mappers[Wiki]           = \
            mapper( Wiki, t_wiki,
                    properties={ 'creator'      : relation( User,
                                                            secondary=at_wiki_creators,
                                                            uselist=False,
                                                            backref='wikis'
                                                          ),
                                 'type'         : relation( WikiType ),
                                 'tablemap'     : relation( WikiTable_Map,
                                                            uselist=False,
                                                            backref=backref( 'wiki', uselist=False ),
                                                            cascade='all, delete-orphan'
                                                          ),
                                 'comments'     : relation( WikiComment,
                                                            backref=backref( 'wiki', uselist=False ),
                                                            cascade='all, delete-orphan' ),
                                 'project'      : relation( Project,
                                                            uselist=False,
                                                            secondary=at_wiki_projects,
                                                            backref='wikis',
                                                          ),
                                 'tags'         : relation( Tag,
                                                            secondary=at_wiki_tags,
                                                            backref='wikipages',
                                                          ),
                                 'attachments'  : relation( Attachment,
                                                            secondary=at_wiki_attachments,
                                                            backref='wikipages',
                                                          ),
                                 'votes'        : relation( Vote,
                                                            secondary=at_wiki_votes,
                                                            backref=backref( 'wiki', uselist=False ),
                                                          ),
                                 'logs'         : relation( Timeline,
                                                            secondary=at_wiki_logs,
                                                            backref=backref( 'wiki', uselist=False ),
                                                          ),
                               })
    tbl_mappers[WikiComment] = \
            mapper( WikiComment, t_wiki_comment,
                    properties={ 'commentby' : relation( User,
                                                         secondary=at_wiki_commentors,
                                                         uselist=False,
                                                         backref='wikicomments',
                                                       ),
                                 'replies'   : relation( WikiComment,
                                                         secondary=at_wiki_replies,
                                                         primaryjoin=(
                                                            at_wiki_replies.c.replytoid==t_wiki_comment.c.id),
                                                         secondaryjoin=(
                                                            at_wiki_replies.c.wikicommentid==t_wiki_comment.c.id),
                                                       ),
                               })

    #------------------------ Timeline Table Mapping ---------------------------
    tbl_mappers[Timeline] = \
            mapper( Timeline, t_timeline )
    #------------------------ Timeline Table Mapping ---------------------------
    tbl_mappers[UserInvitation] = \
            mapper( UserInvitation, t_userinvitation,
                    properties={ 'byuser' : relation( User,
                                                      uselist=False,
                                                      backref='invitations',
                                                    ),
                               })
    #------------------------ Survey Table Mapping ---------------------------
    tbl_mappers[Survey] = \
            mapper( Survey, t_survey,
                    properties={ 'moderator' : relation( User,
                                                         secondary=at_survey_moderators,
                                                         backref='modsurveys',
                                                       ),
                                 'votes'     : relation( Vote,
                                                         secondary=at_survey_votes,
                                                         backref=backref( 'survey', uselist=False ),
                                                       ),
                               })

    return tbl_mappers


def init_model( engine ) :
    """Call me before using any of the tables or classes in the model"""
    sm               = sessionmaker( autoflush=True, autocommit=True, bind=engine )
    meta.engine      = engine
    meta.Session     = scoped_session( sm )
    meta.tbl_mappers = map_tables()
