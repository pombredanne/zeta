# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Module contains the library functions, classes required to build and
data crunch view objects, that can be used in the templates.
----------------- DEPRECATED -----------------------
"""

# -*- coding: utf-8 -*-

# Gotchas :
#   1. There is an interesting side-effect observed here. If all the context
#      data are assigned at the module level, and if we depend on,
#           from zeta.lib.view import *
#      for the context to be updated, then it will work for the first time only.
#      Because subsequent imports do not reload the file, and the context is
#      destroyed for every request.
#   2. In-module caching implemented
#
# Notes   :
#   1. Consumes c.sysentries, c.authuser, c.authusername objects.
#
# Todo    : None

from   os.path                            import isfile

from   pylons                             import request, response
from   pylons                             import config
from   pylons                             import tmpl_context as c
from   pylons.controllers.util            import abort

from   zeta.config.routing                import *

from   zeta.lib.base                      import render
from   zeta.lib.constants                 import LEN_NAME
import zeta.lib.helpers                   as h

# View Object System.

class View( object ) :
    """Base class for all view object"""

anchor_types = [ 'link', 'pointer' ]
class Anchor( View ) :
    """Defines an anchor elements data"""
    def __init__( self, href=None, type='link', text=None, title=None,
                  **kwargs ) :
        """Instantiate an anchor object with the following fields,
        href     url
        type     type of anchor, either `link` or `pointer`
        text     text to be displayed to user
        title    mouse-over help text.
        **kwargs additional parameters that will be added to the object
        """
        self.href   = href
        self.text   = text
        self.title  = title
        self.type   = type
        [ self.__dict__.setdefault( k, kwargs[k] ) for k in kwargs ]

def metanav(environ) :
    metanavs = [
        Anchor( href=h.url_projindex, text='projects',
                title='All hosted projects' )
    ]
    if h.authorized( h.ValidUser( strict='True' )) :
        metanavs.extend([
            Anchor( href=None, type='pointer', text='quick-links',
                    title='Quick shortcut to useful links' ),
            Anchor( href=None, type='pointer', text='myprojects',
                    title='Goto projects' ),
            Anchor( href=h.url_userpref, text='preference',
                    title='Your account preference' ),
            Anchor( href=h.url_signout, text='signout',
                    title='Sign out' ),
        ])
    else :
        metanavs.extend([
            Anchor( href=h.url_signin, text='signin',
                    title='Sign in if already registered' ),
            Anchor( href=h.url_register, text='register',
                    title='New User ? Sign up' ),
        ])

    metanavs.extend([
        Anchor( href=h.url_aboutus, text='aboutus', title='About Us' ),
        Anchor( href=h.url_helppages, text='help',
                title='Learn how to use ' + config['zeta.sitename'] ),
    ])
    return metanavs

tabmap = {
    'projects' : 0,
    'projmount' : 0,
    'projwiki' : 1,
    'projticket' : 2,
    'projvcs' : 3,
    'projreview' : 4,
    'projadmin' : 5,
}
def mainnav( self, projname=None, controller='projects' ) :
    """Generate the mainnavigation panel for project, `projname`,
    with the active tab for the panel specifying by the offset activetab.

    Freshly constructed 'mainnavs' array of anchor objects, for a specific
    project can be cached harmlessly.
    """
    mainnavs = [
       Anchor( href=h.url_projecthome, text=projname,
               title='%s project home' % projname,
               tab='inactive',
             ),
       Anchor( href=h.url_projectwiki, text='Wiki',
               title='Wiki Pages for ' + projname,
               tab='inactive',
             ),
       Anchor( href=h.url_projectticket, text='Tickets',
               title='Open Tickets and issues for ' + projname,
               tab='inactive',
             ),
       Anchor( href=h.url_projectvcs, text='Source',
               title='Browse Source code for ' + projname,
               tab='inactive',
             ),
       Anchor( href=h.url_projectreview, text='Review',
               title='Manage project reviews ' + projname,
               tab='inactive',
             ),
    ]

    # `Admin` tab is visible only for current project's administrator and
    # site administrator
    if h.authorized( h.SiteAdmin() ) or h.authorized( h.ProjectAdmin() ) :
        mainnavs.append(
           Anchor( href=h.url_projectadmin, text='Admin',
                   title='Adminstration for ' + projname,
                   tab='inactive',
                 )
        )

    [ setattr( mainnavs[i], 'tab', 'inactive' ) for i in range(len( mainnavs )) ]
    mainnavs[tabmap[controller]].tab = 'active'
    return mainnavs
