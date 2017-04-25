#! /usr/bin/env python

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# Gotcha : None
# Notes  : None
# Todo   :
#
#   (Deployment / Installation)
#
#   * Management of configuration file.
#   * Upgradation and degradation database to next and previous DB version.
#   * Upgradataion and degradation of Zeta APP to next and previsou APP
#      version.
#   * Backup and restore of data-base and app-dir.
#   * Cloning of web-site.
#
#   (Back-end)
#
#   (DataBase)
#
#   * List of workflows and default workflow to be configurable by
#     `siteadmin`.
#   * workflow for a project should be configurable by project-admin.
#
#   (Security)
#
#   * SSL support.
#   * Hide Email feature, where ever `description`, `text` are rendered.
#
#   (Features)
#
#   * Favorites for project, wiki, ticket.
#   * Voting / Rating for wiki, ticket.
#   * Timeline display page for web-site, admin, project, tickets,
#     reviews, wikis.
#   * Version control system.
#   * Printable pages and pdf download.
#   * Notifications. Via e-mail, twit. For entries in timeline.
#   * Filtering, as a generic class, implemented for,
#       wikilist, ticketlist
#   * create a workflow directory to populate it with different workflow
#     modules(EG `Basic`). Workflow module should be configurable at project
#     level, so add a database column `workflow` in project table and a form
#     fields for the same in the project-admin forms.
#   ---
#   * The application's timezone is configurable. But not used !!
#   * Karma algorithm.
#   * Address-book.
#   * Forums.
#   * Messaging facility (1-1) (1-Many, twitter like).
#
#   (Miscellaneous)
#
#   * Web statistics.
#   * Update the `validate_fields()` helper function once the recent additions
#     to the database is over.
#   * The application code must use c.sysentries to get the system configured
#     parameters. Not config['zeta.*']
#
#   (GUI)
#
#   * Wiki difference should have borders to indicate changesets. Also the
#     actual text that is changed should be highlighted with darker color.
#   * HTML Template with JS handlers to shrink a given text by specified
#     number of characters and display as '...'. On clicking the '...' the
#     remaining text must be displayed.
#
#   (Testing )
#
import sys
from   zeta.model import create_model
from   sqlalchemy import engine_from_config
