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
                                           assert_false, assert_true
from   zwiki.zwparser               import ZWParser

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, \
                                           delete_models
from   zeta.tests.model.populate    import gen_licenses, pop_permissions, \
                                           pop_user
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 3
no_of_tags      = 5
no_of_attachs   = 2

g_byuser        = u'admin'

sampledata_dir  = os.path.join( os.path.split(__file__)[0], '..', 'model',
                                'sampledata' )

compmgr    = None
liccomp    = None
userscomp  = None
attachcomp = None
licdata    = None
zwparser   = None
cachemgr   = None
cachedir   = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, liccomp, userscomp, attachcomp, licdata, zwparser, seed, \
           cachemgr

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
    liccomp    = LicenseComponent( compmgr )
    attachcomp = AttachComponent( compmgr )
    # Populate DataBase with sample entries
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    licdata    = gen_licenses( no_of_tags=no_of_tags, no_of_attachs=no_of_attachs )
    print "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, no_of_attach=%s" % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs )

    zwparser = ZWParser( lex_optimize=True, yacc_debug=True, yacc_optimize=False )

    # Setup cache manager
    isdir( cachedir ) or os.makedirs( cachedir )
    cachemgr = cachemod.cachemanager( cachedir )
    config['cachemgr'] = cachemgr


def tearDownModule() :
    """Clean up database."""
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )
    info = "   Deleting models (module-level) ... "
    log.info( info )
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )


class TestTag( object ) :

    def _validate_lictable( self, licdata, license ) :
        assert_equal( sorted([ l.licensename for l in license ]),
                      sorted([ licensename for licensename in licdata ]),
                      'Mismatch in licensename after creating license'
                    )
        assert_equal( sorted([ l.summary for l in license ]),
                      sorted([ licdata[ln]['summary'] for ln in licdata ]),
                      'Mismatch in license summary after creating license'
                    )
        assert_equal( sorted([ l.text for l in license ]),
                      sorted([ licdata[ln]['text'] for ln in licdata ]),
                      'Mismatch in license text after creating license'
                    )
        assert_equal( sorted([ l.source for l in license ]),
                      sorted([ licdata[ln]['source'] for ln in licdata ]),
                      'Mismatch in license source after creating license'
                    )

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

    def _testlicdesc_execute( self, type, lic, ref='' ) :
        wikitext    = lic.text
        # Prepare the reference.
        ref         = ref or wikitext
        ref         = zwparser.wiki_preprocess( ref )
        props, ref  = zwparser._wiki_properties( ref )

        # Characterize the generated wikitext set the wikiproperties
        wikiprops = {}
        wikitext  = ( "@ %s " % wikiprops ) + '\n' + wikitext

        # Test by comparing the dumps
        try :
            tu      = zwparser.parse( wikitext, debuglevel=0 )
            result  = tu.dump()[:-1]
        except :
            tu     = zwparser.parse( wikitext, debuglevel=2 )
            result = tu.dump()[:-1]
        if result != ref :
            print ''.join(diff.ndiff( result.splitlines(1), ref.splitlines(1) ))
        assert result == ref, type + '... testcount : %s - dump mismatch' % count

        # Test by comparing the html
        ref    = tu.tohtml()
        result = lic.translate()
        assert result == ref, type + '... testcount %s - html mismatch' % count

        # Test by translating to html
        #tu   = zwparser.parse( wikitext, debuglevel=0 )
        #html = tu.tohtml()
        #et.fromstring( html ) 

        
    def test_1_createlicense( self ) :
        """Testing license create methods"""
        log.info( "Testing license create methods..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        # Collect expected objects from database.
        users = userscomp.get_user()
        for ln in licdata :
            lic = licdata[ln]
            tup = ( lic['id'],   lic['licensename'], lic['summary'], 
                    lic['text'], lic['source'] )
            l = liccomp.create_license( tup, c=c, defer=choice([True, False]) )
            lic['id']= l

            self._validate_defer(
                    c.authuser, False, c,
                    lambda u : 'created new license' in u.logs[-1].log 
            )

        self._validate_lictable( licdata, liccomp.get_license() )

    def test_2_updatelicense( self ) :
        """Testing license updation"""
        log.info( "Testing license updation ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        licupdt = { 'licensename' : u'updatedlicname',
                    'summary'     : u'updatedlicsummary',
                    'text'        : u'updatedlictext',
                    'source'      : u'updatedlicsource'
                  }
        count = 1
        for ln in licdata :
            lic = licdata[ln]
            if choice([True, False]) :
                continue
            key = choice( licupdt.keys() )
            if key == 'licensename' :
                lic      = licdata.pop( ln )
                value    = licupdt[key] + str(count)
                lic[key] = value
                licdata[value] = lic
            else :
                lic[key] = licupdt[key] + str(count)
            count += 1
            tup = ( lic['id'], lic['licensename'], lic['summary'],
                    lic['text'], lic['source'] )
            defer = choice([True, False])
            l = liccomp.create_license( tup, update=True, c=c, defer=defer )
            lic['id']= l

            self._validate_defer(
                    c.authuser, False, c,
                    lambda u : 'updated license' in u.logs[-1].log 
            )

        self._validate_lictable( licdata, liccomp.get_license() )

    def test_3_get( self ) :
        """Testing get methods"""
        log.info( "Testing get methods ..." )
        dblicense = []
        for ln in licdata :
            l = licdata[ln]['id']
            dblicense.append( liccomp.get_license( 
                                choice([ l, l.licensename, l.id ])))
        assert_equal( sorted(dblicense),
                      sorted(liccomp.get_license()),
                      'Mismatch in getting licenses from database'
                    )

    def test_4_existense( self ) :
        """Testing existence method"""
        log.info( "Testing existence method ..." )
        [ assert_true( liccomp.license_exists( licdata[ln]['id'] ),
                       'Expected license does not exist %s' % ln
                     ) for ln in licdata ]

    def test_5_remove( self ) :
        """Testing license removal method"""
        log.info( "Testing license removal method ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        rmlic = [ ln for ln in licdata if not randint(0,4) ]
        for ln in rmlic :
            c.rclose = h.ZResp()
            l = licdata[ln]['id']
            defer = choice([True, False])
            liccomp.remove_license(
                    choice([ l.id, l.licensename, l ]), c=c, defer=defer )

            self._validate_defer(
                    c.authuser, defer, c, lambda u : ln in u.logs[-1].log )

            licdata.pop( ln )

        self._validate_lictable( licdata, liccomp.get_license() )


    def test_6_tags( self ) :
        """Testing tag additions and removals"""
        log.info( "Testing tag additions and removals ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for ln in licdata :
            c.rclose = h.ZResp()
            lic       = licdata[ln]
            l         = lic['id']
            byuser    = choice( lic['tags'].keys() )
            tags      = lic['tags'][byuser]
            tagaslist = tags and choice(tags) or ''
            tagasitem = tags and choice(tags) or ''
            rmtag     = tags and choice(tags) or ''
            defer = False

            tags and \
                liccomp.add_tags( choice([ l.id, l.licensename, l ]), 
                                  tags, c=c, defer=defer, byuser=byuser )
            tagaslist and \
                liccomp.add_tags( choice([ l.id, l.licensename, l ]),
                                  [tagaslist], c=c, defer=defer, byuser=byuser )
            tagasitem and \
                liccomp.add_tags( choice([ l.id, l.licensename, l ]),
                                  tagasitem, c=c, defer=defer, byuser=byuser )

            # Validate deferred post processing
            if tags or tagaslist or tagasitem :
                self._validate_defer(
                        byuser, defer, c,
                        lambda u : 'added tags' in u.logs[-1].log 
                )

            if rmtag :
                defer = choice([True, False])
                c.rclose = h.ZResp()
                liccomp.remove_tags( l, rmtag, c=c, defer=defer )
                lic['tags'][byuser].remove( rmtag )

                self._validate_defer(
                        c.authuser, defer, c,
                        lambda u : 'deleted tags' in u.logs[-1].log 
                )


        for l in liccomp.get_license() :
            tags = []
            [ tags.extend( v ) for v in  licdata[l.licensename]['tags'].values() ]
            assert_equal( sorted(tags),
                          sorted([ t.tagname for t in l.tags ]),
                          'Mismatch in tag creation'
                        )

    def test_7_attach( self ) :
        """Testing attachment additions and removals"""
        log.info( "Testing attachment additions and removals ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        attachs = {}
        for ln in licdata :
            lic         = licdata[ln]
            attachs[ln] = []
            for u in lic['attachs'] :
                for f in lic['attachs'][u] :
                    attach = attachcomp.create_attach(
                                            os.path.basename(f), 
                                            choice([ open(f,'r'), None  ]),
                                            uploader=u,
                                            summary='',
                             )
                    defer = choice([True, False])
                    liccomp.add_attach( lic['id'], attach, c=c, defer=defer )
                    attachs[ln].append( (u, f, attach) )

                    self._validate_defer(
                            c.authuser, False, c,
                            lambda u : 'uploaded attachment' in u.logs[-1].log
                    )

            rmattach = [ tup for tup in attachs[ln]  if choice([ True, False ]) ]
            for tup in rmattach :
                attachs[ln].remove( tup )
                defer = choice([True, False])
                liccomp.remove_attach( lic['id'], tup[2], c=c, defer=defer )
                lic['attachs'][tup[0]].remove( tup[1] )

                self._validate_defer(
                        c.authuser, False, c,
                        lambda u : 'deleted attachment' in u.logs[-1].log
                )

        for l in liccomp.get_license() :
            atts = [ tup[2] for tup in attachs[l.licensename] ]
            assert_equal( sorted(atts), sorted(l.attachments),
                          'Mismatch in license attachments' )

    def test_8_translate( self ) :
        """Testing license description translation to wiki"""
        log.info( "Testing license description translation to wiki" )
        #for ln in licdata :
        #    lic = licdata[ln]
        #    self._testlicdesc_execute( 'licdesc', lic['id'] )
        #licenses = liccomp.get_license()
        #for l in licenses :
        #    self._testlicdesc_execute( 'licdesc', l )

    def test_9_licensefields( self ) :
        """Testing license licensefields() method"""
        log.info( "Testing license licensefields() method" )
        licfields = liccomp.licensefields()
        dbfields  = [ [ l.id, l.licensename,
                        sorted( [ (p.id, p.projectname) for p in l.projects ],
                                key=lambda x : x[1] )
                      ] for l in liccomp.get_license() ]
        assert_equal( sorted( licfields, key=lambda x: x[0] ),
                      sorted( dbfields, key=lambda x: x[0] ),
                      'Mismatch in licensefields() method'
                    )
         
    def test_9_licprojects( self ) :
        """Testing license licprojects() method"""
        log.info( "Testing license licprojects() method" )

        licenses  = liccomp.get_license()

        licprojs = {}
        [ licprojs.update( liccomp.licprojects( l.id ) )
          for l in licenses ]

        assert_equal( liccomp.licprojects(), licprojs,
                      'Mismatch in licprojects() method'
                    )

    def test_A_attachments( self ) :
        """Testing method, attachments()"""
        log.info( "Testing method, attachments()" )

        license  = liccomp.get_license(
                            attrload_all=[ 'attachments.uploader',
                                           'attachments.tags' ]
                   )
        lattachs = {}
        for l in license :
            attachs = {}
            for a in l.attachments :
                attachs[a.id] = [ a.filename, a.size, a.summary, a.download_count,
                                  a.created_on, a.uploader.username,
                                  [ tag.tagname for tag in a.tags ]
                                ]
            if attachs :
                lattachs[(l.id, l.licensename)] = attachs
        attachments = liccomp.attachments()
        assert_equal( attachments, lattachs, 'Mismatch in attachments' )
