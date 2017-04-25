# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Permission definitions for the entire web application.
This moddule and `zmultigate` module form the applications authentication
sub-system.

Permission objects are used to define which users should have access to a
particular resource. They are checked using some of the authorization objects
either in the ``multigate.authorize`` module or ``multigate.pylons_adaptors``
module if you are using Pylons.

Permissions objects are very similar to WSGI applications and can perform a
check based on the request or the response. Not all of the authorization
objects have access to the response because the permission might be checked as
part of a code block before the response is generated. This leads to two
classes of permissions, request-based (which can be checked anywhere) and
response-based which can only be checked when the authorization object has
access to the response. 

All the built-in MultiGate permissions are request-based but you can use the
permissions objects defined in this module or create your own derived from
``multigate.permission.Permission``.

Permissions are described in detail in the MultiGate manual.
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Finish the implementation of Exists(), FromIP(), BetweenTimes(),
#      HasPermgroup(), And()

import datetime
import logging
import types

from   pylons                   import config
from   pylons                   import tmpl_context as c
from   multigate                import PermissionError, PermissionSetupError, \
                                       NotAuthenticatedError, \
                                       NotAuthorizedError, MultiGateConfigError
from   multigate.authorize      import middleware
from   multigate.permissions    import Permission, RequestPermission

from   zeta.lib.error           import ZetaPermError
from   zeta.lib.pms             import PMSystem

log = logging.getLogger( __name__ )

permissions = {}
pms_root = None
init_pms = None
mapmodule = None
default_siteperms = []
default_projperms = []

# The dictionary that holds the complete list of permissions
class AppPermission( object ) :
    """Create a new permission name for application."""
    def __init__( self, comp, perm_name, project=True ) :
        """Instantiate a permission object 'perm_name' belonging to 'comp'
        (component) which is optionally under a 'project' project's context"""
        self.perm_name = perm_name
        self.comp      = comp
        self.project   = project
        if perm_name in [ ap.perm_name for aplist in permissions.values()
                                       for ap in aplist ] :
            raise ZetaPermError("App Permission %r already exists" % perm_name)            
        permissions.setdefault( comp, [] ).append( self )

    def __repr__( self ) :
        return "<AppPermission('%s',%s)>" % ( self.comp, self.perm_name )

# All the permissions related to Zeta Application.
# There a two permission catagories.
#   1. site permission only (project=False)
#   2. project permissions (project=True)

AppPermission( 'system',    'EMAIL_VIEW',         project=False )
AppPermission( 'system',    'SITE_ADMIN',         project=False )
AppPermission( 'system',    'STATICWIKI_CREATE',  project=False )
# Site level License Permissions
AppPermission( 'license',   'LICENSE_VIEW',       project=False )
AppPermission( 'license',   'LICENSE_CREATE',     project=False )
AppPermission( 'search',    'SEARCH_VIEW',        project=False )

# Project permissions
AppPermission( 'project',   'PROJECT_VIEW' )

# When project configuration needs to be enabled to other users, then provide
# this permission.
# AppPermission( 'project',   'PROJECT_CONFIG' ),

# Ticket permissions
AppPermission( 'ticket',    'TICKET_VIEW' )
AppPermission( 'ticket',    'TICKET_CREATE' )
AppPermission( 'ticket',    'TICKET_STATUS_CREATE' )
AppPermission( 'ticket',    'TICKET_COMMENT_CREATE' )
# Review permissions
AppPermission( 'review',    'REVIEW_VIEW' )
AppPermission( 'review',    'REVIEW_CREATE' )
# VCS permissions
AppPermission( 'vcs',       'VCS_VIEW' )
AppPermission( 'vcs',       'VCS_CREATE' )
# Wiki permissions
AppPermission( 'wiki',      'WIKI_VIEW' )
AppPermission( 'wiki',      'WIKI_CREATE' )
AppPermission( 'wiki',      'WIKICOMMENT_CREATE' )
# Xmlrpc permissions
AppPermission( 'xmlrpc',    'XMLRPC_VIEW' )

def _currentuser() :
    try :
        authuser = getattr( c, 'authuser', None )
    except :
        authuser = None
    return authuser

#-------------------- Permission derived classes -----------------------------

class UserIn( RequestPermission ) :
    """Simple permission object. Does not use Permission Mapping
    System(PMS).
    Checks whether REMOTE_USER is one of the users specified.
    """

    def __init__( self, users, msg=None ) :
        """Takes the following arguments:
        `users`
            A list of usernames, to whom permission is granted.

        If there is no `REMOTE_USER` `NotAuthenticatedError` is raised. If
        the `REMOTE_USER` is not in `users` a `NotAuthorizedError` is raised.

        `username` in `users` are expected to be in lower case."""
        self.users = users
        self.msg = msg if msg \
                       else "You are not allowed to access this resource."

    def check( self, app, environ, start_response ) :
        authusername = environ.get( 'REMOTE_USER', u'anonymous' )
        if authusername not in self.users:
            raise NotAuthorizedError( self.msg )
        return app( environ, start_response )


class Exists( RequestPermission ) :
    """Simple permission object. Does not use Permission Mapping
    System(PMS).
    Checks whether specified key is present in the ``environ``."""

    def __init__( self, key, error=NotAuthorizedError('Not Authorized') ) :
        """Takes the following arguments:
            `key`
                The required key
            `error`
                The error to be raised if the key is missing.
                XXX This argument may be deprecated soon.
        """
        self.key   = key
        self.error = error
    
    def check( self, app, environ, start_response ) :
        if self.key not in environ:
            raise self.error
        return app( environ, start_response )

        
class PermAnd( RequestPermission ) :
    """Checks all the permission objects listed as keyword arguments in turn.
    Permissions are checked from left to right. The error raised by the ``And``
    permission is the error raised by the first permission check to fail.
    """

    def __init__( self, *permissions ) :
        if len(permissions) < 2 :
            raise PermissionSetupError('Expected at least 2 permissions objects')
        permissions = list( permissions )
        permissions.reverse()
        self.permissions = permissions
        
    def check( self, app, environ, start_response ) :
        for permission in self.permissions:
            app = middleware( app, permission )
        return app( environ, start_response )

class RemoteUser( RequestPermission ) :
    """Checks someone is signed in by checking for the presence of the
    REMOTE_USER.
    
    """

    def __init__( self, anonymous=False, accept_empty=False ) :
        """If 'accept_empty' is 'False' (the default) then an empty
        'REMOTE_USER' will not be accepted and the value of 'REMOTE_USER' must
        evaluate to 'True' in Python."""
        self.accept_empty = accept_empty
        self.anonymous    = anonymous

    def check( self, app, environ, start_response ) :
        if self.anonymous :
            if 'REMOTE_USER' in environ :
                raise NotAuthorizedError( 'Not an anonymous user' )
        else :
            if 'REMOTE_USER' not in environ :
                raise NotAuthenticatedError( 'Not Authenticated' )
            elif self.accept_empty==False and not environ['REMOTE_USER'] :
                raise NotAuthorizedError( 'Not Authorized' )
        return app( environ, start_response )


#
# Permissions to work with the MultiGate user management API
#

class HasPermgroup( RequestPermission ) :
    """Designed to work with the user management API described in the MultiGate 
    manual.

    This permission checks that the signed in user belongs to one of the
    permission groups specified in ``permgroups``."""

    def __init__( self, permgroups, all=True, strict=None, error=None ) :
        if isinstance( permgroups, str ) :
            permgroups = [permgroups]
        self.permgroups = permgroups
        self.all        = all
        self.error      = error
        self.strict     = strict

    def check( self, app, environ, start_response ) :
        """
        Should return True if the user belong to all or any of the permission
        group or False if the user doesn't exist or permission check fails.

        In this implementation group names are lower case.
        """
        from zeta.lib.helpers  import fromconfig
        from zeta.config.environment import userscomp, syscomp

        authusername = environ.get( 'REMOTE_USER', u'anonymous' )
        if not _currentuser() and not userscomp.user_exists( authusername ) :
            raise NotAuthorizedError('No such user')
        # If Strict authentication is enabled, and REMOTE_USER is 'anonymous'
        strict = self.strict or syscomp.get_sysentry( 'strictauth' )
        if (authusername == 'anonymous') and (strict in ['True', 'true']) :
            raise NotAuthenticatedError( 'Please login or Register yourself' )

        # Check for permission groups
        if not userscomp.user_has_permgroups( authusername, self.permgroups,
                                              self.all ) :
            if self.error:
                raise self.error
            else:
                raise NotAuthorizedError(
                    "User doesn't belong to permgroups %s" % self.permgroups )
        return app( environ, start_response )


class ValidUser( UserIn ) :
    """Checks that the signed in user is one of the registered users.
    If `strict` is False,
        then `anonymous` user will be considered a valid user.
    If `strict` is True,
        then `anonymous` user will not be considered a valid user.
    """
    def __init__( self, strict=None ) :
        self.strict = strict
    
    def check( self, app, environ, start_response ) :
        from zeta.lib.helpers  import fromconfig
        from zeta.config.environment import userscomp, syscomp

        authusername = environ.get( 'REMOTE_USER', u'anonymous' )

        # If and when strict authentication
        strict = self.strict or syscomp.get_sysentry( 'strictauth' )
        if (authusername == 'anonymous') and (strict in ['True', 'true']) :
            raise NotAuthenticatedError( 'Please login or Register yourself' )

        # Valid user
        if not _currentuser() and not userscomp.user_exists( authusername ) :
            raise NotAuthorizedError(
                        'You are allowed to access this resource.' )
        return app( environ, start_response )


class SiteAdmin( RequestPermission ) :
    """Check whether the logged in user is the site administrator."""
    def __init__( self, strict=None ) :
        self.strict = strict

    def check( self, app, environ, start_response ) :
        from zeta.lib.helpers  import fromconfig
        from zeta.config.environment import userscomp, syscomp

        authusername = environ.get( 'REMOTE_USER', u'anonymous' )
        # If and when strict authentication
        strict = self.strict or syscomp.get_sysentry( 'strictauth' )
        if (authusername == 'anonymous') and (strict in ['True', 'true']) :
            raise NotAuthenticatedError( 'Please login or Register yourself' )

        status = pms_root.check( [ 'SITE_ADMIN' ],
                                 context=lambda : [ authusername ] )

        if status == False :
            raise NotAuthorizedError('You are not site administrator')

        return app( environ, start_response )


class ProjectAdmin( RequestPermission ) :
    """Check whether the logged in user is the administrator for the
    project"""

    def __init__( self, project=None, strict=None ) :
        self.strict  = strict
        self.project = project

    def check( self, app, environ, start_response ) :
        from zeta.lib.helpers  import fromconfig
        from zeta.config.environment import userscomp, syscomp

        authusername = environ.get( 'REMOTE_USER', u'anonymous' )
        # If and when strict authentication
        strict = self.strict or syscomp.get_sysentry( 'strictauth' )
        if (authusername == 'anonymous') and (strict in ['True', 'true']) :
            raise NotAuthenticatedError( 'Please login or Register yourself' )

        if self.project :   # This block is only used for testing.
            p       = self.project
            context = [ (p.projectname, authusername) ]
        else :
            context = None

        # Check permissions
        status = pms_root.check( [ 'PMS_PROJECT_ADMIN' ], context=context )

        if status == False :
            raise NotAuthorizedError( 'You are not the project administrator' )

        return app( environ, start_response )


class HasPermname( RequestPermission ) :
    """Designed to work with the user management API described in the MultiGate 
    manual.

    This permission checks that the signed in user has any of the permission
    names specified in 'permnames'. If 'all' is 'True', the user must 
    have all the permission names for the permission check to pass."""

    def __init__( self, permnames, all=False, project=None, strict=None, 
                  error=None ) :
        if isinstance( permnames, (str, unicode) ) :
            permnames    = [ permnames ]
        self.all       = all
        self.permnames = permnames
        self.project   = project
        self.error     = error
        self.strict    = strict

    def check( self, app, environ, start_response ) :
        """Should return True if the user has all or any permissions or
        False if the user doesn't exist or the permission check fails.

        In this implementation permission names are uppercase."""
        from zeta.lib.helpers  import fromconfig
        from zeta.config.environment import userscomp, syscomp, projcomp

        authusername = environ.get( 'REMOTE_USER', u'anonymous' )
        if not _currentuser() and not userscomp.user_exists( authusername ) :
            raise NotAuthorizedError( 'No such user %s' % authusername )
        # If and when strict authentication
        strict = self.strict or syscomp.get_sysentry( 'strictauth' )
        if (authusername == 'anonymous') and (strict in ['True', 'true']) :
            raise NotAuthenticatedError( 'Please login or Register yourself' )

        if self.project :   # This block is only used for testing.
            p       = self.project
            teams   = projcomp.userinteams( p, authusername ) + \
                      [ projcomp.team_nomember ]
            context = [ (p.projectname, t) for t in teams ] + [ authusername ]
        else :
            context = None

        # Check for permissions.
        status = pms_root.check( self.permnames, allliterals=self.all, 
                                 context=context )
        if status == False :
            raise NotAuthorizedError(
                        "User doesn't have the permissions %s" % self.permnames
                  )
            
        return app( environ, start_response )

    
class FromIP( RequestPermission ) :
    """Checks that the remote host specified in the environment ``key`` is one 
    of the hosts specified in ``hosts``.
    """
    def __init__( self, hosts, key='REMOTE_ADDR' ) :
        self.hosts = hosts
        if not isinstance( self.hosts, (list, tuple) ) :
            self.hosts = [hosts]
        self.key = key
        
    def check( self, app, environ, start_response) :
        if self.key not in environ:
            raise Exception(
                "No such key %r in environ so cannot check the host"%self.key
            )
        if not environ.get( self.key ) in self.hosts:
            raise NotAuthorizedError(
                'Host %r not allowed'%environ.get(self.key)
            )
        return app( environ, start_response )


class BetweenTimes( RequestPermission ) :
    """Only grants access if the request is made on or after ``start`` and 
    before ``end``. Times should be specified as datetime.time objects.
    """
    def __init__( self, start, end, 
            error=NotAuthorizedError("Not authorized at this time of day") ) :
        self.start = start
        self.end   = end
        self.error = error

    def check( self, app, environ, start_response ) :
        today = datetime.datetime.now()
        now   = datetime.time(  today.hour, today.minute, 
                                today.second, today.microsecond )
        if self.end > self.start:
            if now >= self.start and now < self.end:
                return app(environ, start_response)
            else:
                raise self.error
        else:
            if now < datetime.time(23, 59, 59, 999999) and now >= self.start:
                return app(environ, start_response)
            elif now >= datetime.time(0) and now < self.end:
                return app(environ, start_response)
            else:
                raise self.error
