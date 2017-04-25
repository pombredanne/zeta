# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os.path                      import join, isdir, basename, dirname
import random
from   random                       import choice, randint
import datetime                     as dt
from   pytz                         import all_timezones, timezone

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true

import zeta
from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.vcs                import VcsComponent
from   zeta.comp.system             import SystemComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 10
no_of_relations = 3
g_byuser        = u'admin'

compmgr   = None
userscomp = None
syscomp   = None
projcomp  = None
tckcomp   = None
revcomp   = None
vcscomp   = None
wikicomp  = None
tagcomp   = None
attachcomp= None
cachemgr  = None
cachedir  = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, syscomp, projcomp, tckcomp, revcomp, vcscomp, wikicomp,\
           tagcomp, attachcomp, seed, cachemgr

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
    userscomp  = config['userscomp']
    compmgr    = config['compmgr']
    syscomp    = SystemComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
    revcomp    = ReviewComponent( compmgr )
    vcscomp    = VcsComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    tagcomp    = TagComponent( compmgr )
    attachcomp = AttachComponent( compmgr )
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )

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


class TestSystemForms( object ) :

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

    def test_1_formsystem( self ) :
        """Testing FormSystem for userreltypes entry with valid and invalid
        input"""
        log.info( "Testing FormSystem for userreltypes entry with valid and invalid input" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users        = userscomp.get_user()
        u            = choice( users )
        c.sysentries = syscomp.get_sysentry()
        c.rclose = h.ZResp()

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'system' )

        ref_reltypes  = [ choice(userscomp.reltypes) for i in range(2) ] + \
                        [ choice([ '', ' ', ' reltype1', 'reltype1 ', ' reltype3 ', 'reltype2  ' ])
                          for i in range(20) ]
        ref_reltypes  += userscomp.reltypes
        reltypes      = ','.join( ref_reltypes )

        ref_ptt       = [ choice(projcomp.teams) for i in range(2) ] + \
                        [ choice([ '', ' ', ' pteamtype1', 'pteamtype2 ', ' pteamtype3 ', 'pteamtype4  ' ])
                          for i in range(20) ]
        ref_ptt       += projcomp.teams
        projteamtypes = ','.join( ref_ptt )

        ref_tt        = [ choice(tckcomp.tcktypenames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' tickettype1', 'tickettype2 ', ' tickettype3 ', 'tickettype4  ' ])
                          for i in range(20) ]
        ref_tt        += tckcomp.tcktypenames
        tickettypes   = ','.join( ref_tt )

        ref_tst       = [ choice(tckcomp.tckstatusnames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' tstatus1', 'tstatus2 ', ' tstatus3 ', 'tstatus4  ' ])
                          for i in range(20) ]
        ref_tst       += tckcomp.tckstatusnames
        ticketstatus  = ','.join( ref_tst )

        ref_tsv       = [ choice(tckcomp.tckseveritynames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' tseverity1', 'tseverity2 ', ' tseverity3 ', 'tseverity4  ' ])
                          for i in range(20) ]
        ref_tsv       += tckcomp.tckseveritynames
        ticketseverity= ','.join( ref_tsv )

        ref_rnatr     = [ choice(revcomp.naturenames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' rnature1', 'rnature2 ', ' rnature3 ', 'rnature4  ' ])
                          for i in range(20) ]
        ref_rnatr     += revcomp.naturenames
        reviewnatures = ','.join( ref_rnatr )

        ref_ractn     = [ choice(revcomp.actionnames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' raction1', 'raction2 ', ' raction3 ', 'raction4  ' ])
                          for i in range(20) ]
        ref_ractn     += revcomp.actionnames
        reviewactions = ','.join( ref_ractn )

        ref_vtypes    = [ choice(vcscomp.vcstypenames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' vcstype1', 'vcstype2 ', ' vcstype3 ', 'vcstype4  ' ])
                          for i in range(20) ]
        ref_vtypes    += vcscomp.vcstypenames
        vcstypes       = ','.join( ref_vtypes )

        ref_wtypes    = [ choice(wikicomp.typenames) for i in range(2) ] + \
                        [ choice([ '', ' ', ' wikitype1', 'wikitype2 ', ' wikitype3 ', 'wikitype4  ' ])
                          for i in range(20) ]
        ref_wtypes    += wikicomp.typenames
        wikitypes     = ','.join( ref_wtypes )

        ticketresolv = set([ choice(tckcomp.tckstatusnames) for i in range(2) ])
        ticketresolv = ', '.join( ticketresolv )
        specialtags  = set([ choice(tagcomp.tagnames) for i in range(4) ])
        specialtags  = ', '.join( specialtags )
        def_wikitype = choice(wikicomp.typenames)
        strictauth   = choice([ u'True', u'False' ])
        welcomestring= u'site level welcome string'

        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'userrel_types', reltypes )
        request.POST.add( 'projteamtypes', projteamtypes )
        request.POST.add( 'tickettypes', tickettypes )
        request.POST.add( 'ticketstatus', ticketstatus )
        request.POST.add( 'ticketseverity', ticketseverity )
        request.POST.add( 'reviewnatures', reviewnatures )
        request.POST.add( 'reviewactions', reviewactions )
        request.POST.add( 'vcstypes', vcstypes )
        request.POST.add( 'wikitypes', wikitypes )
        request.POST.add( 'ticketresolv', ticketresolv )
        request.POST.add( 'specialtags', specialtags )
        request.POST.add( 'def_wikitype', def_wikitype )
        request.POST.add( 'strictauth', strictauth )
        request.POST.add( 'welcomestring', welcomestring )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['system'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'system configuration' in u.logs[-1].log 
        )

        se = syscomp.get_sysentry()

        ref_reltypes = list(set( h.parse_csv( ','.join( ref_reltypes )) ))
        assert_equal( sorted( ref_reltypes ), sorted( userscomp.reltypes ),
                      'Mismatch while updating user relation types' )
        assert_equal( ', '.join( userscomp.reltypes ), se['userrel_types'],
                      'Mismatch in system entry for userrel_types' )

        ref_ptt = list(set( h.parse_csv( ','.join(  ref_ptt )) ))
        assert_equal( sorted( ref_ptt ), sorted( projcomp.teams ),
                     'Mismatch while updating project team types' )
        assert_equal( ', '.join( projcomp.teams ), se['projteamtypes'],
                      'Mismatch in system entry for projteamtypes' )

        ref_tt = list(set( h.parse_csv( ','.join(  ref_tt )) ))
        assert_equal( sorted( ref_tt ), sorted( tckcomp.tcktypenames ),
                     'Mismatch while updating ticket types' )
        assert_equal( ', '.join( tckcomp.tcktypenames ), se['tickettypes'],
                      'Mismatch in system entry for tickettypes' )

        ref_tst = list(set( h.parse_csv( ','.join(  ref_tst )) ))
        assert_equal( sorted( ref_tst ), sorted( tckcomp.tckstatusnames ),
                     'Mismatch while updating ticket status' )
        assert_equal( ', '.join( tckcomp.tckstatusnames ), se['ticketstatus'],
                      'Mismatch in system entry for ticketstatus' )

        ref_tsv = list(set( h.parse_csv( ','.join(  ref_tsv )) ))
        assert_equal( sorted( ref_tsv ), sorted( tckcomp.tckseveritynames ),
                     'Mismatch while updating ticket severity' )
        assert_equal( ', '.join( tckcomp.tckseveritynames ), se['ticketseverity'],
                      'Mismatch in system entry for ticketseverity' )

        ref_rnatr = list(set( h.parse_csv( ','.join(  ref_rnatr )) ))
        assert_equal( sorted( ref_rnatr ), sorted( revcomp.naturenames ),
                     'Mismatch while updating review nature' )
        assert_equal( ', '.join( revcomp.naturenames ), se['reviewnatures'],
                      'Mismatch in system entry for reviewnatures' )

        ref_ractn = list(set( h.parse_csv( ','.join(  ref_ractn )) ))
        assert_equal( sorted( ref_ractn ), sorted( revcomp.actionnames ),
                     'Mismatch while updating review action' )
        assert_equal( ', '.join( revcomp.actionnames ), se['reviewactions'],
                      'Mismatch in system entry for reviewactions' )

        ref_vtypes = list(set( h.parse_csv( ','.join(  ref_vtypes )) ))
        assert_equal( sorted( ref_vtypes ), sorted( vcscomp.vcstypenames ),
                     'Mismatch while updating vcs types' )
        assert_equal( ', '.join( vcscomp.vcstypenames ), se['vcstypes'],
                      'Mismatch in system entry for vcstypes' )

        ref_wtypes = list(set( h.parse_csv( ','.join(  ref_wtypes )) ))
        assert_equal( sorted( ref_wtypes ), sorted( wikicomp.typenames ),
                     'Mismatch while updating wiki types' )
        assert_equal( ', '.join( wikicomp.typenames ), se['wikitypes'],
                      'Mismatch in system entry for wikitypes' )

        assert_equal( ticketresolv, se['ticketresolv'],
                     'Mismatch system entry for ticketresolv' )
        assert_equal( specialtags, se['specialtags'],
                     'Mismatch system entry for specialtags' )
        assert_equal( def_wikitype, se['def_wikitype'],
                     'Mismatch system entry for def_wikitype' )
        assert_equal( strictauth, se['strictauth'],
                     'Mismatch system entry for strictauth' )
        assert_equal( welcomestring, se['welcomestring'],
                     'Mismatch system entry for welcomestring' )

    def test_2_sitelogo( self ) :
        """Testing FormSiteLogo with valid and invalid input"""
        log.info( "Testing FormSiteLogo with valid and invalid input ..." )
        request = RequestObject()
        c       = ContextObject()
        vf      = VForm( compmgr )

        users           = userscomp.get_user()
        u               = choice( users )
        config['c']     = c
        c.authuser      = g_byuser

        envlogofile     = join( dirname( dirname( zeta.__file__ )),
                                'defenv/public/sitelogo' )
        c.sitelogo      = '/sitelogo'

        # Add sitelogo
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'sitelogo' )

        request.POST.add( 'user_id', str(u.id) )
        attach          = FileObject()
        attachfile      = choice( attachfiles )
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )
        request.POST.add( 'sitelogofile', attach )
        user            = choice( userscomp.get_user() )
        vf.process( request, c, user=user.username )
        assert_equal( open( attachfile ).read(), open( envlogofile ).read(),
                      'Mismatch in adding site logo'
                    )


    def test_3_staticwiki( self ) :
        """Testing FormStaticWiki with valid and invalid input"""
        log.info( "Testing FormStaticWiki with valid and invalid input ..." )
        request = RequestObject()
        c = ContextObject()
        vf = VForm( compmgr )

        users = userscomp.get_user()
        swikis = syscomp.get_staticwiki()
        u = choice( users )
        config['c'] = c
        c.authuser = g_byuser
        sw = choice(swikis)
        swtype = choice(wikicomp.get_wikitype())
        sourceurl = "http://discoverzeta.com"

        # Edit static wiki
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'editsw' )

        text = u'Updating static wiki'
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'pathurl', sw.path )
        request.POST.add( 'text', text )
        request.POST.add( 'wiki_typename', swtype.wiki_typename )
        request.POST.add( 'sourceurl', sourceurl )
        user = choice( userscomp.get_user() )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['editsw'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated guest wiki page' in u.logs[-1].log 
        )
        
        sw = syscomp.get_staticwiki(sw.path)
        assert_equal( [sw.type.wiki_typename, sw.sourceurl, sw.text],
                      [swtype.wiki_typename, sourceurl, text],
                      'Mismatch in editing static wiki'
                    )

        # Edit static wiki, with empty text
        text = u''
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'pathurl', sw.path )
        request.POST.add( 'text', text )
        user = choice( userscomp.get_user() )
        vf.process( request, c, user=user.username )
        sw = syscomp.get_staticwiki(sw.path)
        assert_equal( sw.text, text,
                      'Mismatch in editing static wiki'
                    )

        # Delete static wiki page
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delsw' )

        path = sw.path
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'pathurl', path )
        user = choice( userscomp.get_user() )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['delsw'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted guest wiki pages' in u.logs[-1].log 
        )

        sw = syscomp.get_staticwiki(path)
        assert_false( sw, 'Mismatch in deleting static wiki' )
