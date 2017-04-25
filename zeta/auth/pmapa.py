# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Sample permission map.

        siteadmin
            |
        projadmin
          /   \ 
         /     \ 
        /       \ 
    projteams usersite
                 |
             anonymous

"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

from   pylons                   import tmpl_context as c

from   zeta.lib.pms             import PMSystem


pms_usersite = None
pms_projteams = None
pms_projadmin = None
pms_siteadmin = None
pms_anonymous = None

default_siteperms = [ 'LICENSE_VIEW', 'SEARCH_VIEW' ]
default_projperms = [ 'PROJECT_VIEW', 'TICKET_VIEW', 'REVIEW_VIEW', 'WIKI_VIEW',
                      'VCS_VIEW',
                    ]

#------------------------ Permission Mapping System --------------------------

def mapfor_usersite() :
    """Generate the permission map for site users"""
    from zeta.lib.helpers  import fromconfig
    from zeta.config.environment import userscomp, projcomp

    return userscomp.mapfor_usersite()

def mapfor_teamperms() :
    """Generate the permission map for project teams"""
    from zeta.lib.helpers  import fromconfig
    from zeta.config.environment import projcomp

    return projcomp.mapfor_teamperms()

def mapfor_projadmins() :
    """Generate the permission map for project teams"""
    from zeta.lib.helpers  import fromconfig
    from zeta.config.environment import projcomp

    return projcomp.mapfor_projadmins()

def mapfor_siteadmin() :
    """Generate the permission map for site administrator"""
    from zeta.lib.helpers  import fromconfig
    from zeta.config.environment import userscomp

    return { u'admin': [ 'SITE_ADMIN', 'PMS_PROJECT_ADMIN' ] +\
                       userscomp.perm_names }

def mapfor_anonymous() :
    """Generate the permission map for anonymous user"""
    from zeta.lib.helpers  import fromconfig

    return { u'anonymous': [ 'LICENSE_VIEW', 'SEARCH_VIEW', 'PROJECT_VIEW',
                             'TICKET_VIEW', 'REVIEW_VIEW', 'WIKI_VIEW', 
                             'VCS_VIEW'
                           ]
           }


def ctxtfor_projadmin() :
    """Generate the context for project admin"""
    return c.project \
           and [( c.project.projectname, c.authusername )] \
           or  []


def ctxtfor_projteams() :
    """Generate the context for the project team"""
    from zeta.lib.helpers  import fromconfig
    from zeta.config.environment import projcomp

    if c.project :
        # anonymous user is not part of non-members
        teams    = projcomp.userinteams( c.project, c.authusername ) + \
                   ( c.authusername != 'anonymous' and \
                     [ projcomp.team_nomember ] or [] )
        return [ ( c.project.projectname, t ) for t in teams ]
    else :
        return []


def init_pms( ctxt=None ) :
    """`ctxt` is used only for testing"""
    global pms_usersite, pms_projteams, pms_projadmin, pms_siteadmin, \
           pms_anonymous

    if not pms_siteadmin :

        strictauth = ctxt.get('strictauth', 'False') if ctxt != None else 'False'
        usersite_children = []
        if strictauth in [ 'False', 'false' ] :
            # VIEW permissions are available for anonymous users if
            # `strictauth` is disabled.
            pms_anonymous = \
                PMSystem(
                    'anonymous',
                    lambda : [ c.authusername ],    # Context
                    mapfor_anonymous,               # Permission Maps
                    []                              # children
                )
            usersite_children = [ pms_anonymous ]

        pms_usersite = \
            PMSystem(
                'usersite',
                lambda : [ c.authusername ],    # Context
                mapfor_usersite,                # Permission Maps
                usersite_children               # children
            )

        pms_projteams = \
            PMSystem(
                'projteams',
                ctxtfor_projteams,              # Context
                mapfor_teamperms,               # Permission Maps
                []                              # children
            )

        pms_projadmin = \
            PMSystem(
                'projadmin',
                ctxtfor_projadmin,              # Context
                mapfor_projadmins,              # Permission Maps
                [ pms_projteams, pms_usersite ] # children
           )

        pms_siteadmin =\
            PMSystem(
                'siteadmin',
                lambda : [ c.authusername ],    # Context
                mapfor_siteadmin(),             # Permission Maps
                [ pms_projadmin ]               # children
            )

    return pms_siteadmin
