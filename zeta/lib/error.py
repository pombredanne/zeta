# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Exceptions and Errors"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. The error message should be displayed to the user as html page.


class ZetaError( Exception ) :
    """Exception base class for errors in Zeta."""

    title = 'Zeta Error'
    
    def _get_message(self): 
        return self._message

    def _set_message(self, message): 
        self._message = message

    def __init__( self, message, title=None, show_traceback=False ) :
        Exception.__init__( self, message )
        self.message   = message
        if title:
            self.title = title
        self.show_traceback = show_traceback

    def __unicode__( self ):
        return unicode( self.message )

    message = property(_get_message, _set_message)


class ZetaComponentError( ZetaError ) :
    """Handles all errors detected on Component core"""

class ZetaPermError( ZetaError ) :
    """Handles all errors detected on user / project permissions"""

class ZetaUserError( ZetaError ) :
    """Use this exception to raise errors related to user auth component and
    models."""

class ZetaAuthorizationError( ZetaError ) :
    """Handles all errors detected on user information"""

class ZetaAuthenticationError( ZetaError ) :
    """Handles all errors detected on user information"""

class ZetaTagError( ZetaError ) :
    """Use this exception to raise errors related to Tag component and
    models."""

class ZetaAttachError( ZetaError) :
    """Use this exception to raise errors related to Attachment component and
    models."""

class ZetaLicenseError( ZetaError ) :
    """Use this exception to raise errors related to License component and
    models."""

class ZetaProjectError( ZetaError ) :
    """Use this exception to raise errors related to Project component and
    models."""

class ZetaTicketError( ZetaError ) :
    """Use this exception to raise errors related to Ticket component and
    models."""

class ZetaWikiError( ZetaError ) :
    """Use this exception to raise errors related to Wiki component and
    models."""

class ZetaFormError( ZetaError ) :
    """Handles all errors detected during form request/submit"""

class ZetaSMTPError( ZetaError ) :
    """Handles all smtp client error"""

class ZetaPOP3Error( ZetaError ) :
    """Handles all pop3 client error"""

class ZetaMailtextParse( ZetaError ) :
    """Handles all mail text parse error"""


