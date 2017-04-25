# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Simple utility functions to access and process database models.
This module is not in use now !!"""

from __future__         import with_statement

from zeta.model         import meta
from zeta.model.tables  import PermissionName, PermissionGroup, \
                               User, UserInfo

def get_permnames() :
    """Return a list of all the entries in the permission_name table."""
    msession = meta.Session()
    with msession.begin( subtransactions=True ) :
        pnames = msession.query( PermissionName ).all()
    return pnames


def get_permgroups() :
    """Return a list of all the entries in the permission_group table."""
    msession = meta.Session()
    with msession.begin( subtransactions=True ) :
        pgroups = msession.query( PermissionGroup ).all()
    return pgroups


def get_users( field=None ) :
    """Return a list of all the entries in the user table. If the field
    keyword is passed, then return the list of field values """
    msession = meta.Session()
    with msession.begin( subtransactions=True ) :
        users = msession.query( User ).all()
    if field :
        users = [ getattr(u, field) for u in users ]
    return users


def get_userinfos() :
    """Return a list of all the entries in the user_info table."""
    msession = meta.Session()
    with msession.begin( subtransactions=True ) :
        userinfo = msession.query( UserInfo ).all()
    return userinfo
