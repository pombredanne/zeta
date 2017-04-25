# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Controller module to manage site accounts."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

import logging
from   hashlib                  import sha1

from   pylons                   import request, response, config, session
from   pylons                   import tmpl_context as c
from   pylons.controllers.util  import abort

from   zeta.lib.base            import BaseController, render
from   zeta.lib.constants       import *
import zeta.lib.helpers         as h
from   zeta.lib.mailclient      import resetpasswd
from   zeta.lib.view            import metanav

log = logging.getLogger(__name__)

class AccountsController( BaseController ) :
    """Controller for User Account managment.
        Registration
        SignIn
        SignOut
    """

    okmsg1 = MESSAGE_FLASH + 'User successfully created. Try signing in.'
    okmsg2 = MESSAGE_FLASH + 'Password successfully reseted. Try signing in.'

    def __before__( self, environ ) :
        """Called before calling any actions under this controller"""

        # Collect the query values into 'context'
        c.digest = request.params.get( 'digest', '' )
        c.emailid = request.params.get( 'emailid', '' )
        c.usernames = []

        # Generic, app-level before-controller handler
        self.beforecontrollers( environ=environ )
        self.dourls( environ, None )
        c.metanavs = metanav( environ )

    @h.authorize( h.UserIn([ u'anonymous' ], "You are already signed-in"))
    def newaccount( self, environ ) :
        """Create new user account
        URLS :
            /accounts/newaccount?form=request&formname=createuser
            /accounts/newaccount?form=request&formname=createuser&digest=<digest>
            /accounts/newaccount?form=submit&formname=createuser
            /accounts/newaccount?form=submit&formname=createuser&digest=<digest>
        """
        from zeta.config.environment    import userscomp, vfcomp

        c.rclose = h.ZResp()

        # Calculate whether registration is allowed.
        regrbyinvite = h.str2bool( c.sysentries['regrbyinvite'] )
        c.uinv = None
        if not regrbyinvite :
            c.allowregistration = True
        elif c.digest :
            c.uinv = userscomp.invbydigest( c.digest )
            c.allowregistration = bool(c.uinv)
        else :
            c.uinv = None
            c.allowregistration = False

        # Setup context for page generation
        c.usernames = userscomp.usernames

        # Form handling
        def errhandler(ERROR_FLASH, errmsg) :
            h.flash( ERROR_FLASH + errmsg )
            h.redirect_url( h.url_register )
        vfcomp.process(
            request, c,
            defer=True, errhandler=h.hitchfn(errhandler, ERROR_FLASH),
            formnames=['createuser']
        )

        # If registeration was successful in `form handling` go-to-signin
        if c.form == 'submit' :
            username = request.POST.get( 'username', None )
            c.uinv and userscomp.acceptedby( unicode(username), c.uinv )
            h.flash( self.okmsg1 )
            h.redirect_url( h.url_signin )

        # Generate page
        c.rclose.append(render( '/derived/accounts/register.html' ))
        return c.rclose

    def signin( self, environ ) :
        """User Signin.
        - Actual signing is handled by MultiGate middleware (using 401 status)
        - Authorization decorator should not be used here since this action will
          interact back-and-forth with authentication middleware.
        URLS : 
            /accounts/signin
        """
        if c.authusername == 'anonymous' :
            # This triggers the MultiGate middleware to display the sign in form
            abort(401)

        else :
            # Gotcha : somehow the messages are not getting cleared when it is
            # read from the template. So force clear all the flash messsages
            # for a fresh log-in.
            h.flash.pop_messages()
            h.redirect_url( h.url_sitehome )

    def signout( self, environ ) :
        """User logout
        - Actual action is perfromed by MultiGate, including the removal of user
          session.
        URLS :
            /accounts/signout
        """
        h.redirect_url( h.url_sitehome )

    @h.authorize( h.UserIn([ u'anonymous' ], "You are already signed-in"))
    def forgotpass( self, environ ) :
        """Prompt user for his/her email-id to construct a reset-link
        URLS :
            /accounts/forgotpass?form=request&formname=forgotpass
            /accounts/forgotpass?form=submit&formname=forgotpass
        """
        from zeta.config.environment    import userscomp
        
        c.rclose = h.ZResp()

        c.errormsg = ''
        if c.form == 'submit' and c.formname == 'forgotpass' :
            # Send email to user with resetpassword link.
            emailid = request.POST.get( 'emailid', None )
            user = userscomp.userbyemailid( unicode(emailid) )
            if user :
                digest  = sha1( user.username + user.emailid + user.password 
                              ).hexdigest()
                fullurl = "%s/%s" % ( h.urlroot(environ),
                                      self.url_forresetp(digest, emailid) )
                resetpasswd( config, emailid, fullurl, c.sysentries['sitename'] )
            else :
                c.errormsg = 'Invalid emailid'

        # Generate page
        c.rclose.append( render( '/derived/accounts/forgotpass.html' ))
        return c.rclose

    def resetpass( self, environ ) :
        """Reset user password by validating emailid against `digest`, this
        controller / action will be invoked when user clicks the reset-link
        sent to his/her mail-id.
        URLS :
            /accounts/resetpass?form=request&formname=resetpass
                                &digest=<digest>&emailid=<emailid>
            /accounts/resetpass?form=submit&formname=resetpass
                                &emailid=<emailid>
        """
        from zeta.config.environment    import userscomp, vfcomp

        c.rclose = h.ZResp()

        # Form handling
        def errhandler(ERROR_FLASH, errmsg) :
            h.flash( ERROR_FLASH + errmsg )
            h.redirect_url( h.url_sitehome )
        vfcomp.process(
            request, c,
            defer=True, errhandler=h.hitchfn(errhandler, ERROR_FLASH),
            emailid=c.emailid, formnames=['resetpass']
        )

        if c.form == 'submit' :     # Reset password completed
            h.flash( self.okmsg2 )
            h.redirect_url( h.url_signin )

        if c.emailid and c.digest : # Prompt user for new password
            user = userscomp.userbyemailid( unicode(c.emailid) )
            refdigest = sha1( user.username + user.emailid + user.password
                            ).hexdigest()
            c.allowreset = True # (refdigest == c.digest)

            # Generate page
            c.rclose.append( render( '/derived/accounts/resetpass.html' ))
            return c.rclose

        h.redirect_url( h.url_sitehome )

    def __after__( self ) :
        """Called calling any actions under this controller"""
        self.aftercontrollers() # Genering, app-level after-controller handler
