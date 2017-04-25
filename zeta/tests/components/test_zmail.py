# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os                           import listdir
from   os.path                      import commonprefix, join, split, abspath, \
                                           basename, isdir, isfile
import random
from   random                       import choice, randint
import datetime                     as dt
import time

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true
from   nose.plugins.attrib          import attr

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_tickets, pop_wikipages, \
                                           pop_reviews, pop_vcs
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.ztext               import *
from   zeta.lib.mailclient          import OutMessage, SMTPconn, POPconn, \
                                           projectemail, mime_attachfname
from   zeta.comp.system             import SystemComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.zmail              import ZMailComponent
from   zeta.tests.tlib              import *
from   zeta.tests.model.generate    import gen_tickets, future_duedate
import zeta.tests.zetalib.ztextlib  as ztl

from   zeta.controllers.xmlrpc      import _result

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
g_byuser        = u'admin'
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 2
no_of_attachs   = 1
no_of_projects  = 10
no_of_tickets   = 20
no_of_wikis     = 20
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 20

compmgr     = None
userscomp   = None
syscomp     = None
attcomp     = None
projcomp    = None
wikicomp    = None
zmailcomp   = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attcomp, syscomp, projcomp, wikicomp, \
           zmailcomp, cachemgr

    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )

    info = "   Creating models (module-level) ... "
    log.info( info )
    print info
    # Setup SQLAlchemy database engine
    engine  = engine_from_config( config, 'sqlalchemy.' )
    # init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )
    compmgr    = config['compmgr']
    userscomp  = config['userscomp']
    syscomp    = SystemComponent( compmgr )
    attcomp    = AttachComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    zmailcomp  = ZMailComponent( compmgr, config=config )

    # Populate DataBase with sample entries
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    print "   Populating licenses ( no_of_tags=%s, no_of_attachs=%s ) ..." % \
                ( no_of_tags, no_of_attachs )
    pop_licenses( no_of_tags, no_of_attachs, seed=seed )
    print "   Populating projects ( no_of_projects=%s ) ..." % no_of_projects
    pop_projects( no_of_projects, no_of_tags, no_of_attachs, seed=seed )
    print "   Populating tickets ( no_of_tickets=%s ) ..." % no_of_tickets
    pop_tickets( no_of_tickets, no_of_tags, no_of_attachs, seed=seed )
    print "   Populating vcs ( no_of_vcs=%s ) ..." % no_of_vcs
    pop_vcs( no_of_vcs=no_of_vcs, seed=seed )
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
    print "   Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
    pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_reviews=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_reviews )

    # Setup cache manager
    #isdir( cachedir ) or os.makedirs( cachedir )
    #cachemgr = cachemod.cachemanager( cachedir )
    #config['cachemgr'] = cachemgr


def tearDownModule() :
    """Clean up database."""
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )
    info = "   Deleting models (module-level) ... "
    log.info( info )
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )


class TestZMail( object ) :

    def inmail_subj( self, inm ) :
        return inm.multipart and inm.rootpart.get( 'Subject' ) or \
               inm.m.get( 'Subject' )

    def cmp_inmail( self, a, b ) :
        return all([ self.inmail_subj(x) == self.inmail_subj(y)
                     for x, y in zip(a,b) ])

    def test_A_accounts( self ) :
        """Testing setupaccounts() cleanaccounts() methods"""
        log.info( "Testing setupaccounts() cleanaccounts() methods" )
        
        zmailcomp.cleanaccounts()

        addeddomains, addedusers = zmailcomp.setupaccounts()
        refdomains = [ config['zeta.smtp_user'].split('@')[1] ]
        refusers   = [ config['zeta.smtp_user'] 
                     ] + [ projectemail( config, p.projectname )
                           for p in projcomp.get_project() 
                         ]
        assert_equal( sorted(addeddomains), sorted(refdomains),
                      'Mismatch in addeddomains' )
        assert_equal( sorted(addedusers), sorted(refusers),
                      'Mismatch in addedusers' )

        deldomains, delusers = zmailcomp.cleanaccounts()
        assert_equal( sorted(deldomains), sorted(refdomains),
                      'Mismatch in deldomains' )
        assert_equal( sorted(delusers), sorted(refusers),
                      'Mismatch in delusers' )

    def test_B_virtualdomains( self ) :
        """Testing virtualdomain methods"""
        log.info( "Testing virtualdomain methods" )

        domains = [ 'zt.devwhiz.net', 'sandbox.devwhiz.net', 'top.devwhiz.net' ]
        zmailcomp.adddomains( domains )
        assert_equal( sorted(domains), sorted(zmailcomp.virtualdomains),
                      'Mismatch in virtualdomains property' )
        assert_equal( sorted(domains), sorted(zmailcomp.dbdomains),
                      'Mismatch in dbdomains property' )

        deldomains = [ d for d in domains if choice([True,False]) ]
        [ domains.remove(d) for d in deldomains ]
        zmailcomp.deldomains( deldomains )
        assert_equal( sorted(domains), sorted(zmailcomp.virtualdomains),
                      'Mismatch in virtualdomains property' )
        assert_equal( sorted(domains), sorted(zmailcomp.dbdomains),
                      'Mismatch in dbdomains property' )

    def test_C_virtualusers( self ) :
        """Testing virtualuser methods"""
        log.info( "Testing virtualuser methods" )

        zmailcomp.delusers( '*' )
        zmailcomp.deldomains( zmailcomp.dbdomains )

        zmailcomp.adddomains([ 'zt.devwhiz.net',
                               'sandbox.devwhiz.net', 'top.devwhiz.net' ])

        users   = [ 'enstein@zt.devwhiz.net', 'newton@sandbox.devwhiz.net',
                    'harshad@top.devwhiz.net' ]
        passwd  = config['zeta.smtp_password']
        [ zmailcomp.adduser( config, u, passwd ) for u in users ]
        assert_equal( sorted(users), 
                      sorted([ u for u, p in zmailcomp.virtualusers ]),
                      'Mismatch in virtualusers property' )
        assert_equal( sorted(users),
                      sorted([ u for u, p in zmailcomp.dbusers ]),
                      'Mismatch in dbusers property' )

        delusers = [ u for u in users if choice([True,False]) ]
        [ users.remove(u) for u in delusers ]
        zmailcomp.delusers( delusers )
        assert_equal( sorted(users),
                      sorted([ u for u, p in zmailcomp.virtualusers ]),
                      'Mismatch in virtualusers property' )
        assert_equal( sorted(users),
                      sorted([ u for u, p in zmailcomp.dbusers ]),
                      'Mismatch in dbusers property' )

        [ zmailcomp.adduser( config, u, passwd ) for u in users ]
        zmailcomp.delusers( '*' )
        assert_false( zmailcomp.virtualusers, 'Mismatch in virtualusers property' )

    def test_D_mailsysentry( self ) :
        """Testing methods to get / set mail sys-entry"""
        log.info( "Testing methods to get / set mail sys-entry" )
        
        domains = [ 'zt.devwhiz.net', 'sandbox.devwhiz.net', 'top.devwhiz.net' ]
        user    = 'enstein@zt.devwhiz.net'
        zmailcomp.adduser( config, user, config['zeta.smtp_password'] )
        zmailcomp.setupaccounts()
        zmailcomp.adddomains( domains )
        login = config['zeta.smtp_user']

        d = zmailcomp.mailoffset( login, byuser=g_byuser )
        assert_equal( d, MAIL_STARTCOUNT, 'Mismatch in mailoffset' )

        d = zmailcomp.updateoffset( login, 100, byuser=g_byuser )
        d = zmailcomp.mailoffset( login, byuser=g_byuser )
        assert_equal( d, 100, 'Mismatch in updateoffset' )

        d = zmailcomp.updateoffset( user, 100, byuser=g_byuser )
        d = zmailcomp.mailoffset( login, byuser=g_byuser )
        assert_equal( d, 100, 'Mismatch in updateoffset' )

    def test_E_mails( self ) :
        """Testing mail interface methods"""
        log.info( "Testing mail interface methods" )

        files = [ f for f in listdir( '.' ) if isfile(f) ]
        p     = choice(projcomp.get_project())

        serverip = config['zeta.smtp_serverip']
        domains  = [ 'zt.devwhiz.net', 'sandbox.devwhiz.net', 'top.devwhiz.net' ]
        snduser  = 'enstein@zt.devwhiz.net' 
        rcvuser  = '%s@virtual.test'  % p.projectname
        passwd   = config['zeta.smtp_password'] 
        [ zmailcomp.adduser( config, u, passwd ) for u in [ snduser, rcvuser ] ]
        zmailcomp.setupaccounts()
        zmailcomp.adddomains( domains )

        types = wikicomp.get_wikitype()
        user  = userscomp.get_user( g_byuser )
        sconn = SMTPconn( config, serverip, rcvuser, passwd )
        sconn.connect()

        pconn = POPconn( config, serverip, rcvuser, passwd )

        pconn.connect()
        mcount, size = pconn.stat()
        [ pconn.dele( i ) for i in range( 1, mcount+1 ) ]
        pconn.quit()

        # Send test case 1

        subj1 = "Create a new wiki page for `project`, using wikiurl, with type"
        type1 = choice(types)
        text1 = ztl.wiki_testcase_1( p, type1 )
        ctxt1 = parse(text1)
        assert_true( isinstance( ctxt1, Context ), 'parse return not a context' )
        sconn.sendmail( snduser, [rcvuser], subject=subj1, body=text1 )

        time.sleep(1)
        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=1, count=1 )
        assert_true( len(ins) == 1,
                     'Mismatch in pulling mails, fromwhich=1, count=1' )
        assert_equal( self.inmail_subj( ins[0] ), subj1,
                     'Mismatch in pulling mails, fromwhich=1, count=1' )
        zmailcomp.processmails(ins[0], rcvuser)
        assert_true( ztl.wiki_verify_1( wikicomp, p, type1 ), 'Fail wiki_verify_1()' )


        # Send test case 2
        subj2 = "Create a new wiki page for `project`, using projectname, pagename, with summary"
        type2 = choice(types)
        summ2 = 'some wiki summary ...'
        text2 = ztl.wiki_testcase_2( p, type2, summ2 )
        ctxt2 = parse(text2)
        assert_true( isinstance( ctxt2, Context ), 'parse return not a context' )
        sconn.sendmail( snduser, [rcvuser], subject=subj2, body=text2 )

        time.sleep(1)
        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=1, count=2 )
        assert_true( len(ins) == 2,
                     'Mismatch in pulling mails, fromwhich=1, count=2' )
        assert_equal( self.inmail_subj( ins[1] ).replace('\n\t', ' '), subj2,
                      'Mismatch in pulling mails, fromwhich=1, count=2' )
        zmailcomp.processmails(ins[1], rcvuser)
        assert_true( ztl.wiki_verify_2( wikicomp, p, type2, summ2 ), 'Fail wiki_verify_2()' )

        # Send test case 3
        subj3 ="Update a new wiki page for `project`, using wikiid, with tags"
        text3 = ztl.wiki_testcase_3( wikicomp, p )
        ctxt3 = parse(text3)
        assert_true( isinstance( ctxt3, Context ), 'parse return not a context' )
        sconn.sendmail( snduser, [rcvuser], subject=subj3, body=text3 )

        time.sleep(1)
        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=1, count=3 )
        assert_true( len(ins) == 3,
                     'Mismatch in pulling mails, fromwhich=1, count=3' )
        assert_equal( self.inmail_subj( ins[2] ), subj3,
                      'Mismatch in pulling mails, fromwhich=1, count=3' )
        zmailcomp.processmails(ins[2], rcvuser)
        assert_true( ztl.wiki_verify_3( wikicomp, p ), 'Fail wiki_verify_3()' )

        # Send test case 4
        subj4 ="Update a new wiki page for `project`, using projectid, pagename, with favorite and upvote"
        text4 = ztl.wiki_testcase_4( p.id, user )
        ctxt4 = parse(text4)
        assert_true( isinstance( ctxt4, Context ), 'parse return not a context' )
        sconn.sendmail( snduser, [rcvuser], subject=subj4, body=text4 )

        time.sleep(1)
        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=1, count=4 )
        assert_true( len(ins) == 4,
                     'Mismatch in pulling mails, fromwhich=1, count=4' )
        assert_equal( self.inmail_subj( ins[3] ).replace('\n\t', ' '), subj4,
                      'Mismatch in pulling mails, fromwhich=1, count=4' )
        zmailcomp.processmails(ins[3], rcvuser)
        assert_true( ztl.wiki_verify_4( wikicomp, p, user ), 'Fail wiki_verify_4()' )

        # Send test case 5
        subj5 ='Testing OutMessage with attach, %s'
        text5 = ztl.wiki_testcase_5( wikicomp, p )
        ctxt5 = parse(text5)
        assert_true( isinstance( ctxt5, Context ), 'parse return not a context' )
        dir   = os.path.dirname( __file__ )
        files5= [ join( dir, file ) for file in listdir(dir) ]
        msg   = OutMessage( fromaddr=snduser, toaddrs=rcvuser,
                            subject=subj5, body=text5, attachments=files5[:2] )
        msg.attach( files5[2] )
        msg   = msg.as_string()
        sconn.sendmsg( snduser, rcvuser, msg )

        time.sleep(1)
        ins   = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=1, count=5 )
        assert_true( len(ins) == 5,
                     'Mismatch in pulling mails, fromwhich=1, count=5' )
        assert_equal( self.inmail_subj( ins[4] ), subj5,
                      'Mismatch in pulling mails, fromwhich=1, count=5' )
        zmailcomp.processmails(ins[4], rcvuser)
        assert_true( ztl.wiki_verify_5( wikicomp, p, user ), 'Fail wiki_verify_5()' )
        atts = sorted(
                    [ (a.filename, attcomp.content(a))
                      for a in attcomp.get_attach()[-3:] ],
                    key=lambda x : x[0]
               )
        fils = sorted(
                    [ (basename(f), open(f).read()) for f in files5[:3] ],
                    key=lambda x : x[0]
               )
        for t1, t2 in zip( atts, fils ) :
            assert_true( t1[0] == t2[0], 'Mismatch in attachment' )


        # Send test case 6
        text6 = ztl.wiki_testcase_6()
        msg   = parse(text6)
        assert_equal( msg.message, 'Unable to identify the purpose of text !!',
                      'Fail wiki_testcase_6' )

        # Send test case 7
        text7 = ztl.wiki_testcase_7()
        ctxt7 = parse(text7)
        assert_true( isinstance( ctxt7, Context ), 'parse return not a context' )
        ctxt7.commit( config, g_byuser )

        sconn.quit()
        time.sleep(1)

        # A total of 5 mails should have been send !

        # Check pullmail() method
        inmails = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, count=10 )
        assert_true( len(inmails) == 5, 'Mismatch in pulling mails' )
        assert_equal( self.inmail_subj(inmails[0]), subj1, 'Mismatch in inmails 1' )
        assert_equal( self.inmail_subj(inmails[1]).replace('\n\t', ' '), subj2,
                      'Mismatch in inmails 2' )
        assert_equal( self.inmail_subj(inmails[2]), subj3, 'Mismatch in inmails 3' )
        assert_equal( self.inmail_subj(inmails[3]).replace('\n\t', ' '), subj4,
                      'Mismatch in inmails 4' )
        assert_equal( self.inmail_subj(inmails[4]), subj5, 'Mismatch in inmails 5' )

        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=1 )
        assert_true( len(ins) == 5, 'Mismatch in pulling mails, fromwhich=1' )
        assert_true( self.cmp_inmail(inmails, ins), 'Mismatch in pulling mails, fromwhich=1' )

        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd, fromwhich=6 )
        assert_true( len(ins) == 0, 'Mismatch in pulling mails, fromwhich=6' )

        # pull and delete mails
        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd,
                                       fromwhich=1, delete=True )
        assert_true( len(ins) == 5, 'Mismatch in pulling mails, fromwhich=6' )
        ins     = zmailcomp.pullmails( login=rcvuser, loginpass=passwd,
                                       fromwhich=1, delete=True )
        assert_true( len(ins) == 0, 'Mismatch in pulling mails, fromwhich=6' )
