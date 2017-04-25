# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Authentication backend for Zeta."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   :
#   1. `pylons.config` is initialized as late as possible from 0.10rc1 and 1.0
#      versions, so methods that will be invoked via create_models() pass the
#      config parameter explicitly.

import os.path
from   hashlib                            import sha1
import time, random, urllib2, sys
import logging
from   hashlib                            import md5
from   os.path                            import isfile, dirname, join, abspath

from   multigate.authenticate.backend.sql import Sql
from   multigate                          import MultiGateConfigError

from   sqlalchemy.orm                     import sessionmaker, scoped_session
from   sqlalchemy                         import engine_from_config
from   sqlalchemy.sql                     import text

log = logging.getLogger( __name__ )

class AuthBackend( Sql ) :
    """
    Authentication details are available in sql database (specified by `url`)

    Following list of parameters can be used to configure this backend.
        'multigate.backend.sql.call'
        'multigate.backend.sql.url'
        'multigate.backend.sql.schema'
        'multigate.backend.sql.encrypt.function'
        'multigate.backend.sql.encrypt.secret'

    `schema` value is expected as,
        <tablename>:<userfield>,<passwordfield>
    """
    # Handle disabled users

    def __init__( self, mgconf, backconf ) :
        Sql.__init__( self, mgconf, backconf )


    # Existence Methods
    def user_exists( self, username, authchoice=None ) :
        """
        ``username`` is case insensitive.
        Returns,
            ``True`` if a user exists with the given username,
            ``False`` otherwise.
        """
        return Sql.user_exists( self, username, authchoice )
        
    # List Methods
    def list_users( self, authchoice=None ) :
        """
        Returns a lowecase list of all usernames ordered alphabetically
        """
        return Sql.list_users( self, authchoice )
        
    # User Methods
    def user( self, username, authchoice=None ) :
        """
        Returns a dictionary in the following format:
            { 'username': username,
              'password': password,
            }
        """
        return Sql.user( self, username, authchoice )
        
    def user_password( self, username, authchoice=None ) :
        """
        Returns,
            the password associated with the user or
            ``None`` if no password exists or user disabled.
        """
        from zeta.config.environment import userscomp

        user =  userscomp.get_user( username )
        if user.disabled :
            return None
        else :
            return user.password
        
    def user_has_password( self, username, password, authchoice=None ) :
        """
        Returns,
            ``True`` if the user has the password specified,
            ``False`` otherwise. Passwords are case sensitive.
        If user is disabled returns ``False``
        """
        from zeta.config.environment import userscomp

        user =  userscomp.get_user( username )
        if user.disabled :
            return False
        else :
            return user.password == self.encrypt( password )

    def authdigest( self, realm, username, authchoice=None ) :
        """
        Returns a hash digest based on,
            (realm, username, password)
        """
        log.debug(
            "digest_password called. username: %s, realm: %s", username, realm
        )
        password = self.user_password( username )
        if password :
            sitehash = md5( "%s:%s:%s" % (username,realm,password) ).hexdigest()
            return sitehash
        return None
