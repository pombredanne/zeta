# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Component providing eXternal Inteface access to the server,
* Emails are pulled from POP3, for the site account and for each project
  account.
* The following parts in an e-mail will be interpreted,
  * To address, which should either point to site account name or project
    account name, if, project account name, `projectname` will be interpreted
    from To address,
  * one or more plain-text parts, which will be concatenated together
  * attachments parts, will be interpreted seperately and if the email
    addresses an attachable entity, attachments will be added to it.
  * Email end marker line
        #end
    to avoid signatures and other text to be inserted into database

General method,

* Email should be in plain-text,
* Every plain-text part will be stripped of empty lines.
* Plain-text part will be scanned for "Email-end-marker' from top.
* If "Email-end-marker" is not detected, the traling lines
  starting with '>' will be stipped (this considered as reply text)
* Plain-text parts will be concatenated together.
* The entire text bundle will be parsed for `structure` in it.

Users can do the following, by sending emails,

* Static wiki,

  * Create / Update static wiki pages

* Attachments,

  If sent to project account, `projectname` will be inferred from it.

  * Add attachments to site or any identified entity like project,
    wiki, tickets .. summary and tags will pertain to all the attachments in
    the mail, the following (key,value) pair must be present.
        attachment : new

  * Update summary, tags for an identified attachment.

* Wiki,

  If sent to project account, `projectname` will be inferred from it and takes
  priority.

  * Add new wiki page

  * Update existing page, including voting and favorites.

* Ticket,

  If sent to project account, `projectname` will be inferred from it and takes
  priority.

  * Add new ticket.

  * Update existing ticket, including voting and favorites.

"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
#   1. post-processing in functions that Create-Update-Delete database tables,
#           logging
#           cache-inavlidating
#           search-indexing
# Todo    : 
#   1. Complete the Ticket Reference interfaces.
#   2. Unit-test methods, computefilters().
#   3. Make sure that all methods have their test cases.

import sys
import pprint

from   zeta.ccore              import Component
import zeta.lib.helpers        as h
from   zeta.lib.constants      import *
from   zeta.lib.mailclient     import MailDB, fetchconfig, projectemail, \
                                      POPconn, mime_attachfname
from   zeta.lib.ztext          import email2text, parse, Context

class ZMailComponent( Component ) :
    """Component to interface with XMLRPC"""

    def _listdomains( self ) :
        if not self.ok : return []
        return self.mdb.listdomains()

    def _listusers( self ) :
        if not self.ok : return []
        return self.mdb.listusers()

    def _listemails( self ) :
        return [ entry[0] for entry in self._listusers() ]

    def _virtualdomains( self ) :
        """List of virtual domains"""
        if not self.ok : return []
        return self.dbdomains

    def _virtualusers( self ) :
        """List of virtual users"""
        if not self.ok : return []
        return self.dbusers

    def __init__( self, *args, **kwargs ) :
        """Fetch mail server configurations configuration"""
        config = kwargs.pop('config')

        self.server, self.login, self.loginpass  = fetchconfig(config)
        if self.login :
            self.foruser, self.atdomain = self.login.split( '@' )
        self.mdb = MailDB( config )
        self.ok = self.server and self.login and self.loginpass and self.mdb
        Component.__init__( self, *args, **kwargs )

    def setupaccounts( self ) :
        """Based on the configuration details, domains and user accounts will
        be created for site and hosted projects"""
        from zeta.config.environment import projcomp

        config = self.compmgr.config
        if not self.ok : return ( [], [] )

        addeddomains = []
        addedusers   = []
        emails       = self.dbemails

        if self.atdomain not in self.dbdomains :
            self.adddomains( self.atdomain )
            addeddomains.append( self.atdomain )

        if self.login not in emails :
            self.adduser( config, self.login, self.loginpass )
            addedusers.append( self.login )

        for p in projcomp.projectnames :
            plogin = projectemail( config, p )
            if plogin not in emails :
                self.adduser( config, plogin, self.loginpass )
                addedusers.append( plogin )

        return addeddomains, addedusers

    def cleanaccounts( self ) :
        """Clean up domains and users accounts for site and hosted projects"""
        from zeta.config.environment import projcomp

        config = self.compmgr.config
        if not self.ok : return ( [], [] )

        deleteddomains = []
        deletedusers   = []

        if self.atdomain in self.dbdomains :
            self.mdb.deldomains( self.atdomain )
            deleteddomains.append( self.atdomain )

        if self.login in self.dbemails :
            self.mdb.deluser( self.login )
            deletedusers.append( self.login )

        for p in projcomp.projectnames :
            plogin = projectemail( config, p )
            if plogin not in self.dbemails : continue
            self.mdb.deluser( plogin )
            deletedusers.append( plogin )
        return deleteddomains, deletedusers

    def adddomains( self, domains ) :
        """Add virtual `domains`"""
        if isinstance( domains, (str, unicode)) :
            domains = [ domains ]
        addeddomains = []
        self.ok and [ ( self.mdb.adddomains( dn ), addeddomains.append( dn )
                      ) for dn in domains if dn not in self.dbdomains ]
        return addeddomains

    def deldomains( self, domains ) :
        """Delete virtual `domains`"""
        if isinstance( domains, (str, unicode)) :
            domains = [ domains ]

        deleteddomains = []

        self.ok and domains == '*' and \
            [ ( self.mdb.deldomains( dn ), deleteddomains.append( dn )
              ) for dn in self.dbdomains ]

        self.ok and isinstance( domains, list ) and \
            [ ( self.mdb.deldomains( dn ), deleteddomains.append( dn )
              ) for dn in domains if dn in self.dbdomains ]

        self.ok and domains in self.dbdomains and \
            [ self.mdb.deldomains( domains ), deleteddomains.append( domains ) ]

        return deleteddomains

    def adduser( self, config, email, password ) :
        """Add user"""
        addeduser = []
        config = config or self.compmgr.config
        self.ok and email not in self.dbemails and \
            [ self.mdb.adduser( config, email, password ), addeduser.append(email) ]
        return addeduser

    def delusers( self, emails ) :
        """Delete user"""
        deletedusers = []

        self.ok and emails == '*' and \
            [ ( self.mdb.deluser(em), deletedusers.append(em)
              ) for em in self.dbemails ]

        self.ok and isinstance( emails, list ) and \
            [ ( self.mdb.deluser( em ), deletedusers.append( em )
              ) for em in emails if em in self.dbemails ]

        self.ok and emails in self.dbemails and \
            [ self.mdb.deluser( emails ), deletedusers.append( emails ) ]

        return deletedusers

    def mailoffset( self, account, byuser=None ) :
        """Use `system-entries` field `mailacc_offsets` and remember the
        `offset` from which to fetch mails for `account`"""
        from zeta.config.environment import syscomp

        accoffsets = eval( syscomp.get_sysentry( u'mailacc_offsets', '{}' ))
        if account in accoffsets :
            offset = accoffsets[account]
        else :
            offset = MAIL_STARTCOUNT
            self.updateoffset( account, offset, byuser=byuser )
        return offset

    def updateoffset( self, account, offset, byuser=None ) :
        """Remember `offset` till which mails where fetched for `account`"""
        from zeta.config.environment import syscomp

        accoffsets = eval( syscomp.get_sysentry( u'mailacc_offsets', '{}' ))
        accoffsets[account] = offset
        accoffsets = pprint.pformat( accoffsets )
        syscomp.set_sysentry( { u'mailacc_offsets' : unicode(accoffsets) },
                              byuser=byuser )

    def pullmails( self, login=None, loginpass=None, fromwhich=None, count=None,
                   delete=False ) :
        """Pull mails from POP3 server, from `fromwhich` for `count` number of
        mails, optionally delete the retrieved mails"""
        from zeta.config.environment import syscomp

        config = self.compmgr.config
        inmails = []
        if not self.ok : return inmails

        server    = self.server
        login     = login or self.login
        loginpass = loginpass or self.loginpass

        pconn = POPconn( config, serverip=server, login=login, password=loginpass )
        pconn.connect()

        mcount, size = pconn.stat()
        inmails = pconn.fetchmail( fromwhich=fromwhich, count=count,
                                   delete=delete )
        pconn.quit()
        return inmails

    def processmails( self, inmails, account ) :
        """Process `inmails` extracting fields, text and attachment and
        process them for structured text, return a context object for each
        inmail"""
        from zeta.config.environment import userscomp, projcomp

        config = self.compmgr.config
        user = userscomp.get_user( u'admin' )

        if not isinstance( inmails, list ) :
            inmails = [inmails]

        ctxts   = []
        attachs = []
        for inmail in inmails :
            if inmail.multipart :
                From = inmail.rootpart.get( 'From' )
                To   = [ to.strip(' \t')
                         for to in inmail.rootpart.get( 'To' ).split( ',' ) ]
                Sub  = inmail.rootpart.get( 'Subject' )
                textparts = [ part.get_payload( decode=True )
                              for part in inmail.messages ]
                for part in inmail.attachments :
                    cdisp = part.get( 'Content-Disposition' )
                    fname = cdisp.split( ';', 1 )[1].strip( ' \t' )
                    cont  = part.get_payload( decode=True )
                    fname = mime_attachfname(fname)
                    attachs.append( (fname, cont) )
            else :
                From = inmail.m.get( 'From' )
                To   = [ to.strip(' \t')
                         for to in inmail.m.get( 'To' ).split( ',' ) ]
                Sub  = inmail.m.get( 'Subject' )
                textparts = [ inmail.m.get_payload( decode=True ) ]

            if account != self.login :
                projstr = 'project : %s\n' % account.split('@',1)[0]
            else :
                projstr = ''

            text = email2text( textparts )
            text = projstr + text
            ctxt = parse( text )
            ctxt.commit( config, user, attachments=attachs )
            ctxts.append(ctxt) 

        return ctxts

    virtualdomains = property( _virtualdomains )
    virtualusers   = property( _virtualusers )

    dbdomains      = property( _listdomains )
    dbusers        = property( _listusers )
    dbemails       = property( _listemails )

