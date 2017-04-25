# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os.path                      import join, isdir, basename
import random
from   random                       import choice, randint

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_true, assert_false
from   nose.plugins.attrib          import attr

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.populate    import pop_permissions, pop_user
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 4 
no_of_attach    = 50
g_byuser        = u'admin'

tmp_dir     = '/tmp/testattachs'
fsize_unit  = 1000
alphanum    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
extnames    = [ '.py', '.c', '.asm', '.exe', '.tar.gz', '.tar', '.rpm',
                '.deb', '.jpg', '.jpeg', '.gif', '.png' ]

taglist     = None
fnamelist   = None
lines       = None
compmgr     = None
userscomp   = None
attachcomp  = None
liccomp     = None
projcomp    = None
tckcomp     = None
revcomp     = None
wikicomp    = None
tagcomp     = None
filenames   = None
files       = []
prevattachs = []

cachemgr    = None
cachedir    = '/tmp/testcache'


gen_filecontent = lambda len : '\n'.join([ choice(lines) for i in range(0,len,80) ])
def gen_localfiles( path, filenames ) :
    currfilenames = os.path.isdir( path ) and os.listdir( path )
    if currfilenames and len(currfilenames) == len(filenames) :
        absfilenames = [ os.path.join( path, f ) for f in currfilenames ]
    else :
        os.system( 'rm ' + path + '/*' )
        os.removedirs( path )
        os.makedirs( path )
        count = 1
        absfilenames = []
        for f in filenames :
            filename = os.path.join( path, f )
            data     = gen_filecontent( count * fsize_unit )
            fd       = open( filename, 'w' )
            fd.write( data )
            fd.close()
            absfilenames.append( filename )
    return absfilenames


def setUpModule() :
    """Create database and tables."""
    global taglist, fnamelist, lines, compmgr, userscomp, filenames, \
           attachcomp, liccomp, projcomp, tckcomp, revcomp, wikicomp, \
           tagcomp, seed, cachemgr
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )
    info = "   Creating models (module-level) ... "
    log.info( info )
    print info

    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    # init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )
    # prepare data for testing
    taglist   = [ unicode(h.randomname( randint(0,LEN_TAGNAME), alphanum))
                                for i in range(randint(0,500)) ]
    fnamelist = [ h.randomname( randint(1,128) ) + choice( extnames ) 
                                for i in range(1000) ]
    lines     = [ ''.join([ choice( alphanum )
                                for i in range(80) ]) for i in range(50) ]
    compmgr   = config['compmgr']
    userscomp = config['userscomp']
    attachcomp= AttachComponent( compmgr )
    tagcomp   = TagComponent( config['compmgr'] )
    liccomp   = LicenseComponent( compmgr )
    projcomp  = ProjectComponent( compmgr )
    tckcomp   = TicketComponent( compmgr )
    revcomp   = ReviewComponent( compmgr )
    wikicomp  = WikiComponent( compmgr )

    print "   Creating `%s` directory for generating attachments ..." % tmp_dir
    not os.path.isdir( tmp_dir ) and os.makedirs( tmp_dir )
    filenames = gen_localfiles(
                    tmp_dir,
                    [ fnamelist.pop( fnamelist.index(choice(fnamelist)) )
                                    for i in range( no_of_attach ) ]
                )
    # Populate DataBase with sample entries
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    print "   no_of_users=%s, no_of_relations=%s, no_of_attach=%s" % \
          (no_of_users, no_of_relations, no_of_attach)

    # Setup cache manager
    isdir( cachedir ) or os.makedirs( cachedir )
    cachemgr = cachemod.cachemanager( cachedir )
    config['cachemgr'] = cachemgr


def tearDownModule() :
    """Clean up database."""
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )
    info = "   Removing attachment files ..."
    log.info( info )
    print info

    info = "   Deleting models (module-level) ... "
    log.info( info )
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )


class TestAttach( TestController ) :

    def _get_attach( self ) :
        dbattachs = attachcomp.get_attach()
        [ dbattachs.remove( a ) for a in prevattachs ]
        return dbattachs

    def _validate_defer( self, user, defer, c, assertlogic ) :
        user = isinstance( user, (int, long)) and user \
               or isinstance( user, (str, unicode)) and user \
               or user.id

        if defer :
            user = userscomp.get_user( user, attrload=['logs'] )
            assert_false( assertlogic(user), 'Mismatch in defer' )
        defer and c.rclose.close()
        user = userscomp.get_user( user, attrload=[ 'logs' ] )
        assert_true( assertlogic(user), 'Mismatch in defer' )

    def test_1_createattach( self ) :
        """Testing attachment creating method"""
        log.info( "Testing attachment creating method ..." )
        global files, prevattachs
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users       = userscomp.get_user()
        prevattachs = attachcomp.get_attach()
        for i in range(no_of_attach) :
            c.rclose    = h.ZResp()
            filename = choice(filenames)
            fdfile   = choice([True,True,True,False]) and \
                       open( filename, 'r' )
            uploader = choice([ choice(users), choice(users).id,
                                choice(users).username ])
            summary  = unicode(' '.join([ h.randomname(randint(0,20))
                                        for i in range(randint(0,10)) ]))
            tags     = sorted(list(set(
                            [ choice(taglist) for i in range(randint(0,10)) ]
                       )))
            defer = choice([True, False])
            if len(summary) > LEN_SUMMARY :
                summary  = u''
                attach   = attachcomp.create_attach(
                                os.path.basename(filename),
                                fdfile,
                                uploader,
                                summary,
                                c=c,
                                defer=defer
                           )
            else :
                attach   = attachcomp.create_attach(
                                os.path.basename(filename),
                                fdfile,
                                uploader,
                                summary,
                                c=c,
                                defer=defer
                           )

            if defer :
                c.rclose.close()
                assert_true( len(c.rclose.func_onclose) == 1,
                             'Mismatch in defer' )
            else :
                assert_true( len(c.rclose.func_onclose) == 0,
                             'Mismatch in defer' )

            files.append([ filename, fdfile, uploader, summary, tags, attach ])

        assert_equal( sorted( self._get_attach() ),
                      sorted([ f[5] for f in files ]),
                      'Mismatch in created attachmentments'
                    )

    def test_2_updatesummray( self ) :
        """Testing summary updating method"""
        log.info( "Testing summary updating method ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser
        users = userscomp.get_user()
        for i in range(len(files)) :
            attach = files[i][5]
            user   = choice( users )
            if choice([ True, False ]) :        # Update summary
                summary = unicode(
                            ' '.join([ h.randomname(10)
                                       for j in range(randint(0,10)) ])
                          )
                defer = choice([True, False ])
                attachcomp.edit_summary( attach, summary, c=c, defer=defer )
                files[i][3] = summary

                self._validate_defer(
                        c.authuser, False, c, 
                        lambda u : 'Updated summary' in u.logs[-1].log
                )

        assert_equal( sorted([ a.summary for a in self._get_attach() ]),
                      sorted([ f[3] for f in files ]),
                      'Mismatch in edited summary'
                    )

    def test_3_getattach( self ) :
        """Testing attachment getting method"""
        log.info( "Testing attachment getting method ..." )
        assert_equal( sorted([ attachcomp.get_attach(
                                    choice([ f[5], f[5].id ])
                               ) for f in files ]),
                      sorted( self._get_attach() ),
                      'Mismatch in getting attachments'
                    )

    def test_4_tags( self ) :
        """Testing attachment tags"""
        log.info( "Testing attachment tags ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for i in range(len(files)) :
            attach = files[i][5]

            # Add tags, Prune Invalid tags
            defer = choice([True, False ])
            invtags = [t for t in files[i][4] if not tagcomp.is_tagnamevalid(t)]
            attachcomp.add_tags(
                    choice([attach, attach.id]), files[i][4], c=c, defer=defer )
            attach = attachcomp.get_attach( attach.id )
            [ files[i][4].remove( t ) for t in invtags ]

            if files[i][4] :
                self._validate_defer(
                        c.authuser, False, c, 
                        lambda u : 'added tags' in u.logs[-1].log
                )

            # Remove tags
            defer = choice([True, False ])
            rmtags = [ t for t in files[i][4] if choice([True,False,False]) ]
            [ files[i][4].remove( t ) for t in rmtags ]
            attachcomp.remove_tags( attach, rmtags, c=c, defer=defer )

            if rmtags :
                self._validate_defer(
                        c.authuser, False, c, 
                        lambda u : 'deleted tags' in u.logs[-1].log
                )

        cr_attachs = [ f[5] for f in files ]
        for a in self._get_attach() :
            assert_equal( sorted( files[cr_attachs.index( a )][4] ),
                          sorted([ t.tagname for t in a.tags ]),
                          'Mismatch in attachment tags'
                        )

    def test_5_removeattach( self ) :
        """Testing attachment removal method"""
        log.info( "Testing attachment removal method ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        rmfiles = [ files[i] for i in range(len(files))
                             if choice([ False, False, False, False, True ]) ]
        for file in rmfiles :
            attach = file[5]
            filename = attachcomp._contentfile(attach)
            attachcomp.remove_attach( choice([ file[5], file[5].id]) )
            files.remove( file )
            assert_false( os.path.isfile(filename),
                          "Mismatch, while removing attachment, file remains" )

        assert_equal( sorted( self._get_attach() ),
                      sorted([ f[5] for f in files ]),
                      'Mismatch in removed attachmentments'
                    )

    def test_6_download( self ) :
        """Testing attachment download and validation"""
        log.info( "Testing attachment download and validation ..." )
        for i in range(len(files)) :
            filename = files[i][0]
            fname    = os.path.basename( filename )
            attach, content = attachcomp.downloadattach( files[i][5].id )
            if files[i][1] : 
                assert_equal( str(content), open( files[i][0] ).read(),
                        'Data mismatches between files `%s` and `%s`' % \
                                (files[i][0], attach.id) )
            else :
                assert_false( content )
            uploader = files[i][2] and userscomp.get_user( files[i][2] )
            assert_equal( uploader, attach.uploader,
                          'Mismatch in uploader' )
            assert_equal( files[i][3], attach.summary,
                          'Mismatch in summary' )
            assert_equal( files[i][4], sorted([ t.tagname for t in attach.tags ]),
                          'Mismatch in tags' )

            # Check whether the download count is incrementing.
            i_downcount = attach.download_count
            attach, content = attachcomp.downloadattach( attach.id )
            assert_equal( i_downcount+1, attach.download_count,
                          'Mismatch in download_count' )

    def test_7_attachments( self ) :
        """Testing method, attachments()"""
        log.info( "Testing method, attachments()" )

        attachments = attachcomp.attachments()
        attachs     = attachcomp.get_attach( attrload=[ 'uploader', 'tags'] )
        assert_equal( len(attachs), len(attachments.keys()),
                      'Mismatch in number of attachments' )

        for ref_a in attachs :
            a = attachments[ref_a.id]
            a[-1] = sorted( a[-1] ) # sort tagnames.
            assert_equal(
                a, 
                [ ref_a.filename, ref_a.size, ref_a.summary,
                  ref_a.download_count, ref_a.created_on,
                  ref_a.uploader.username, sorted([ tag.tagname for tag in ref_a.tags ])
                ],
                'Mismatch in attachments, %s' % ref_a.id
            )
                           
    def test_8_latestattachs( self ) :
        """Testing method, latestattachs()"""
        log.info( "Testing method, latestattachs()" )

        attachs = sorted( attachcomp.get_attach(), key=lambda a : a.id )
        att     = attachcomp.latestattachs()
        assert_true( att.id == attachs[-1].id, 'Mismatch in latestattachs()' )
                           
    @attr(type='attachassc')
    def test_9_attachassc( self ) :
        """Testing method, attachassc()"""
        log.info( "Testing method, attachassc()" )
        
        data = attachcomp.attachassc()

        ref  = {}

        [ ( u.iconfile and ref.setdefault( u.iconfile.id, [] ).append( ('user', u.id) ),
            u.photofile and ref.setdefault( u.photofile.id, [] ).append( ('user', u.id) )
          ) for u in userscomp.get_user( attrload=[ 'iconfile', 'photofile' ]) ]

        [ ref.setdefault( a.id, [] ).append( ('license', l.id) )
          for l in liccomp.get_license( attrload=['attachments'] )
          for a in l.attachments ]

        [ ( ref.setdefault( p.iconfile.id, [] ).append( ('project', p.id) ),
            ref.setdefault( p.logofile.id, [] ).append( ('project', p.id) )
          ) for p in projcomp.get_project( attrload=['attachments'] ) ]

        [ ref.setdefault( a.id, [] ).append( ('project', p.id) )
          for p in projcomp.get_project( attrload=['attachments'] )
          for a in p.attachments ]

        [ ref.setdefault( a.id, [] ).append( ('ticket', t.id) )
          for t in tckcomp.get_ticket( attrload=['attachments'] )
          for a in t.attachments ]

        [ ref.setdefault( a.id, [] ).append( ('review', r.id) )
          for r in revcomp.get_review( attrload=['attachments'] )
          for a in r.attachments ]

        [ ref.setdefault( a.id, [] ).append( ('wiki', w.id) )
          for w in wikicomp.get_wiki( attrload=['attachments'] )
          for a in w.attachments ]

        assert_equal( ref, data, 'Mismatch in attachassc' )
