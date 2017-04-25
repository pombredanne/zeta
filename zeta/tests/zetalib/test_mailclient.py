# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import time
import unittest
import os
from   os.path                   import join, isdir, basename, dirname
import random
from   random                    import choice, randint, shuffle, seed
from   datetime                  import datetime
import re
import pprint
import datetime                  as dt

import pylons.test
import pytz
from   nose.tools                import assert_equal, assert_raises, \
                                        assert_true, assert_false
from   nose.plugins.attrib       import attr
import simplejson                as json
from   sqlalchemy                import engine_from_config
 
from   zeta.auth.perm            import permissions
from   zeta.model                import init_model, create_models, delete_models
from   zeta.model                import meta
import zeta.lib.cache            as cachemod 
import zeta.lib.helpers          as h
from   zeta.lib.mailclient       import MailDB, OutMessage, SMTPconn, POPconn, \
                                        pmailaccount, inviteuser, resetpasswd, \
                                        mime_attachfname
from   zeta.lib.error            import ZetaFormError
from   zeta.tests.tlib           import *
from   zeta.tests.model.generate import genattachs

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None

compmgr     = None
userscomp   = None

def setUpModule() :
    global compmgr, userscomp, seed

    testdir  = os.path.basename( dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )

    compmgr     = config['compmgr']
    userscomp   = config['userscomp']

def tearDownModule() :
    testdir  = os.path.basename( dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )


class TestSMTP( object ) :


    @attr( type='maildb' )
    def test_A_maildb( self ) :
        """Testing MailDB class and its methods"""
        log.info( "Testing MailDB class and its methods" )

        mdb     = MailDB( config )
        assert_true( mdb.Session, "Mismatch, Session is false" )
        mdb.deldomains( mdb.listdomains() )
        [ mdb.deluser( e ) for e, p in mdb.listusers() ]

        mdb.adddomains( 'virtual.test' )
        mdb.adddomains( 'example.com' )
        mdb.adduser( config, 'pratap@virtual.test', 'pratap123' )
        mdb.adduser( config, 'sales@example.com', 'password' )

        domains = mdb.listdomains()
        users   = sorted( mdb.listusers(), key=lambda x : x[0] )

        # Test adding domains
        mdb.adddomains( 'zt.devwhiz.net' )
        mdb.adddomains([ 'sandbox.devwhiz.net', 'top.devwhiz.net' ])
        refdomains = domains + [ 'zt.devwhiz.net', 'sandbox.devwhiz.net',
                                 'top.devwhiz.net' ]
        assert_equal( sorted(refdomains),
                      sorted(mdb.listdomains()),
                      'Mismatch in adding domains'
                    )
        
        # Test adding user
        mdb.adduser( config, 'user1@zt.devwhiz.net', 'user1_123' )
        mdb.adduser( config, 'user2@zt.devwhiz.net', 'user2_123' )
        refusers = users + [ ('user1@zt.devwhiz.net', 'user1_123'),
                             ('user2@zt.devwhiz.net', 'user2_123'),
                           ]
        assert_equal( sorted( refusers, key=lambda x: x[0] ),
                      sorted( mdb.listusers(), key=lambda x : x[0] ),
                      'Mismatch in adding users'
                    )

        # Test deleting users
        mdb.deluser( 'user1@zt.devwhiz.net' )
        mdb.deluser( 'user2@zt.devwhiz.net' )
        refusers = sorted( users, key=lambda x: x[0] )
        dbusers  = sorted( mdb.listusers(), key=lambda x: x[0] )
        assert_equal( refusers, dbusers, 'Mismatch in deleting users' )

        # Test deleting domains
        mdb.deldomains( 'zt.devwhiz.net' )
        mdb.deldomains([ 'sandbox.devwhiz.net', 'top.devwhiz.net' ])
        refdomains = domains
        assert_equal( refdomains, mdb.listdomains(), 'Mismatch is deleting domains' )

        # Test pmailaccount
        projname = 'testproject'
        pmailaccount( projname, config )
        refusers = sorted( users, key=lambda x : x[0] ) + \
                   [( '%s@virtual.test' % projname, config['zeta.smtp_password'] )]
        dbusers  = sorted( mdb.listusers(), key=lambda x: x[0] )
        assert_equal( refusers, dbusers, 'Mismatch in pmailaccount()' )
        mdb.deluser( '%s@virtual.test'%projname )

        mdb.deldomains( 'virtual.test' )
        mdb.deldomains( 'example.com' )
        mdb.deluser( 'pratap@virtual.test' )
        mdb.deluser( 'sales@example.com' )


    @attr( type='omsg' )
    def test_B_omsg( self ) :
        """Testing OutMessage class and its methods"""
        log.info( "Testing OutMessage class and its methods" )
        
        dir   = dirname( __file__ )
        files = [ join( dir, file ) for file in os.listdir(dir) ]
        mdb   = MailDB( config )

        # Fixture
        mdb.adddomains( 'virtual.test' )
        mdb.adddomains( 'example.com' )
        mdb.adduser( config, 'pratap@virtual.test', 'pratap123' )
        mdb.adduser( config, 'sales@example.com', 'password' )

        # Test without attachments
        omsg = OutMessage( fromaddr='pratap@virtual.test',
                           toaddrs='sales@example.com',
                           subject='Testing OutMessage without attach',
                           body='With out attachments. Let God help us !!',
                         )
        msg = omsg.as_string()
        assert_true( 'Content-Type: text/plain; charset="utf8"' in msg )
        assert_true( 'MIME-Version: 1.0' in msg )
        assert_true( 'Content-Transfer-Encoding: base64' in msg )
        assert_true( 'Subject: Testing OutMessage without attach' in msg )
        assert_true( 'From: pratap@virtual.test' in msg )
        assert_true( 'To: sales@example.com' in msg )
        assert_true(
            'V2l0aCBvdXQgYXR0YWNobWVudHMuIExldCBHb2QgaGVscCB1cyAhIQ==' in
            msg
        )


        # Test without attachments
        omsg = OutMessage( fromaddr='pratap@virtual.test',
                           toaddrs='sales@example.com',
                           subject='Testing OutMessage with attach',
                           body='With attachments Let God help us !!',
                           attachments=files[:2]
                         )
        omsg.attach( files[2] )
        msg = omsg.as_string()

        # Teardown Fixture
        mdb.deldomains( 'virtual.test' )
        mdb.deldomains( 'example.com' )
        mdb.deluser( 'pratap@virtual.test' )
        mdb.deluser( 'sales@example.com' )

    @attr( type='loopback' )
    def test_C_loopback( self ) :
        """Testing loopback"""
        log.info( "Testng loopback ..." )

        # Fixture
        serverip = config['zeta.smtp_serverip']
        mdb      = MailDB( config )
        mdb.adddomains( u'virtual.test' )
        mdb.adddomains( u'example.com' )
        mdb.adduser( config, u'pratap@virtual.test', u'pratap123' )
        mdb.adduser( config, u'sales@example.com', u'password' )
        sconn = SMTPconn( config, serverip, u'pratap@virtual.test', u'pratap123' )
        pconn = POPconn( config, serverip, u'sales@example.com', u'password' )

        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele( i ) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        sconn.connect()

        # Send mails without attachments
        fromaddr = 'pratap@virtual.test'
        toaddrs  = [ 'sales@example.com' ]
        ccaddrs  = 'pratap@virtual.test'
        for i in range(1, 5+1) :
            sconn.sendmail(
                    fromaddr, toaddrs, ccaddrs=ccaddrs,
                    subject=('Testing OutMessage without attach, %s' % i),
                    body=('With out attachments. Let God help us !!, %s' % i),
                  )

        # Send mails with attachments
        dir      = dirname( __file__ )
        files    = [ join( dir, file ) for file in os.listdir(dir) ]
        fromaddr = 'pratap@virtual.test'
        toaddrs  = [ 'sales@example.com' ]
        ccaddrs  = 'pratap@virtual.test'
        for i in range(1, 5+1) :
            msg = OutMessage(
                    fromaddr=fromaddr, toaddrs=toaddrs, ccaddrs=ccaddrs,
                    subject='Testing OutMessage with attach, %s' % i,
                    body='With attachments. Let God help us !!, %s' % i,
                    attachments=files[:2]
                  )
            msg.attach( files[2] )
            msg = msg.as_string()
            sconn.sendmsg( fromaddr, toaddrs, msg )

        sconn.quit()
        time.sleep(1)

        # Test pconn.stat(), pconn.list()
        pconn.connect()
        mcount, size = pconn.stat()
        assert_equal( mcount, 10, 'Mismatch in mcount' )
        assert_equal( mcount, len(pconn.list()[1]),
                      'Mismatch in len(pconn.list())' )

        # Test pconn.dele()
        pconn.dele(5); pconn.dele(10)
        mcount, size = pconn.stat()
        assert_equal( mcount, 8, 'Mismatch in mcount' )
        assert_equal( mcount, len(pconn.list()[1]),
                      'Mismatch in len(pconn.list())' )
        pconn.quit()

        # Test pconn.retr() for mail without attachment
        pconn.connect()
        inm = pconn.retr(1)
        assert_equal( inm.m.get( 'Return-Path', ), '<pratap@virtual.test>',
                      'Mismatch in `Return-Path`' ),
        assert_equal( inm.m.get( 'X-Original-To' ), 'sales@example.com',
                      'Mismatch in `X-Original-To`' ),
        assert_equal( inm.m.get( 'Delivered-To' ), 'sales@example.com',
                      'Mismatch in `Delivered-To`' ),
        assert_equal( inm.m.get( 'Content-Type' ),
                      'text/plain; charset="utf8"',
                      'Mismatch in `Content-Type`' ),
        assert_equal( inm.m.get( 'MIME-Version' ), '1.0',
                      'Mismatch in `MIME-Version`' ),
        assert_equal( inm.m.get( 'Content-Transfer-Encoding', ), 'base64',
                      'Mismatch in `Content-Transfer-Encoding`' ),
        assert_equal( inm.m.get( 'From' ), 'pratap@virtual.test',
                      'Mismatch in `From`' ),
        assert_equal( inm.m.get( 'To' ), 'sales@example.com',
                      'Mismatch in `To`' ),
        assert_equal( inm.m.get( 'Cc' ), 'pratap@virtual.test',
                      'Mismatch in `Cc`' ),

        for i in range( 1, 5 ) :
            inm = pconn.retr(i)
            assert_equal( inm.m.get( 'Subject' ),
                          'Testing OutMessage without attach, %s' % i ,
                          'Mismatch in `Subject`' ),
            assert_equal( inm.m.get_payload( decode=True ),
                          'With out attachments. Let God help us !!, %s' % i,
                          'Mismatch in payload' )
                
        # Test pconn.retr() for mail with attachment
        for i in range( 1, 5 ) :
            num = i+4
            inm = pconn.retr( num )
            reffiles = files[:]

            assert_true( inm.multipart, 'Mismatch, not a mutipart' )
            assert_equal( inm.rootpart.get( 'Subject' ),
                          'Testing OutMessage with attach, %s' % i,
                          'Mismatch in multipart, subject'
                        )

            for part in inm.messages :
                assert_equal( part.get_payload( decode=True ),
                              'With attachments. Let God help us !!, %s' % i,
                              'Mismatch in multipart text'
                            )

            for part in inm.attachments :
                file  = reffiles.pop( 0 )
                cdisp = part.get( 'Content-Disposition' )
                fname = cdisp.split( ';', 1 )[1].strip( ' \t' )
                assert_equal( mime_attachfname(fname), basename( file ),
                              'Mismatch in filename'
                            )
                assert_equal( part.get_payload( decode=True ),
                              open( file ).read(),
                              'Mismatch in attachment content'
                            )
        pconn.quit()

        # Teardown Fixture
        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele( i ) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        mdb.deldomains( u'virtual.test' )
        mdb.deldomains( u'example.com' )
        mdb.deluser( u'pratap@virtual.test' )
        mdb.deluser( u'sales@example.com' )


    @attr( type='invu' )
    def test_D_inviteuser( self ) :
        """Testing inviteuser()"""
        log.info( "Testng inviteuser() ..." )

        # Fixture
        serverip = config['zeta.smtp_serverip']
        mdb      = MailDB( config )
        mdb.adddomains( u'virtual.test' )
        mdb.adddomains( u'example.com' )
        mdb.adduser( config, u'pratap@virtual.test', u'pratap123' )
        mdb.adduser( config, u'sales@example.com', u'password' )
        pconn = POPconn( config, serverip, 'sales@example.com', 'password' )

        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele(i) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        inviteuser( config, 'prataprc@gmail.com', 'http://zt.devwhiz.net',
                    'pratap', 'Zeta On Zeta' )

        inviteuser( config, 'sales@example.com', 'http://zt.devwhiz.net',
                    'pratap', 'Zeta On Zeta' )

        time.sleep(1)

        pconn.connect()
        mcount, size = pconn.stat()
        assert_equal( mcount, 1, 'Mismatch in mcount' )
        inmails = pconn.fetchmail( fromwhich=1 )
        pconn.quit()

        assert_equal( len(inmails), 1, 'Mismatch in inmails size' )
        inm = inmails[0]
        assert_false( inm.multipart, 'Mismatch inmail multipart' )
        assert_equal( inm.m.get('Subject'),
                      'Invitation to join `Zeta On Zeta`',
                      'Mismatch in inmail subject' 
                    )
        assert_equal( inm.m.get('From'), 'pratap@virtual.test',
                      'Mismatch in inmail from address' 
                    )
        body = inm.m.get_payload( decode=True )
        assert_true( 'zt.devwhiz.net' in body, 'Mismatch in inmail body' )
        assert_true( 'Zeta On Zeta' in body, 'Mismatch in inmail body' )

        # Teardown Fixture
        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele( i ) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        mdb.deldomains( u'virtual.test' )
        mdb.deldomains( u'example.com' )
        mdb.deluser( u'pratap@virtual.test' )
        mdb.deluser( u'sales@example.com' )


    @attr( type='rpass' )
    def test_E_resetpasswd( self ) :
        """Testing resetpasswd()"""
        log.info( "Testng resetpasswd() ..." )

        # Fixture
        serverip = config['zeta.smtp_serverip']
        mdb      = MailDB( config )
        mdb.adddomains( u'virtual.test' )
        mdb.adddomains( u'example.com' )
        mdb.adduser( config, u'pratap@virtual.test', u'pratap123' )
        mdb.adduser( config, u'sales@example.com', u'password' )
        pconn = POPconn( config, serverip, 'sales@example.com', 'password' )

        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele( i ) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        time.sleep(1)

        resetpasswd( config, 'prataprc@gmail.com', 'http://zt.devwhiz.net',
                     'Zeta On Zeta' )

        resetpasswd( config, 'sales@example.com', 'http://zt.devwhiz.net',
                     'Zeta On Zeta' )

        time.sleep(1)

        pconn.connect()
        mcount, size = pconn.stat()
        assert_equal( mcount, 1, 'Mismatch in mcount' )
        inmails = pconn.fetchmail( fromwhich=1 )
        pconn.quit()

        assert_equal( len(inmails), 1, 'Mismatch in inmails size' )
        inm = inmails[0]
        assert_false( inm.multipart, 'Mismatch inmail multipart' )
        assert_equal( inm.m.get('Subject'),
                      'Reset your password @ Zeta On Zeta',
                      'Mismatch in inmail subject' 
                    )
        assert_equal( inm.m.get('From'), 'pratap@virtual.test',
                      'Mismatch in inmail from address' 
                    )
        body = inm.m.get_payload( decode=True )
        assert_true( 'zt.devwhiz.net' in body, 'Mismatch in inmail body' )
        assert_true( '- Site Administrator' in body, 'Mismatch in inmail body' )

        # Teardown Fixture
        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele( i ) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        mdb.deldomains( u'virtual.test' )
        mdb.deldomains( u'example.com' )
        mdb.deluser( u'pratap@virtual.test' )
        mdb.deluser( u'sales@example.com' )

