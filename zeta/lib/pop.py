# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""POP Client to receive mails.
Mails are sent for,
    * Inviting users
    * Sending urls for resetting forgotten password
    * Notifications on timeline logs

config parameters used,
    zeta.smtp_serverip,
    zeta.smtp_user,
    zeta.smtp_password,
from .ini file to login into SMTP server.

*********************** DEPRECATED *************************
"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

serverip = None
login    = None
password = None
def _fetchconfig() :
    """Same smtp configurations are used for pop3 as well"""
    global serverip, login, password
    if serverip == None :
        serverip = h.fromconfig( 'zeta.smtp_serverip' )
        login    = h.fromconfig( 'zeta.smtp_user' )
        password = h.fromconfig( 'zeta.smtp_password' )
    return (serverip, login, password )
