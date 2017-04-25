# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import sys
import os
from   os.path                      import join, isdir, basename
import random
from   random                       import choice, randint
import datetime                     as dt
from   pytz                         import all_timezones, timezone

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_not_equal, \
                                           assert_raises, \
                                           assert_false, assert_true
from   nose.plugins.attrib          import attr

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_vcs, pop_tickets, pop_reviews, \
                                           pop_wikipages
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
import zeta.lib.analytics           as ca
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.ticket             import TicketComponent
from   zeta.comp.vcs                import VcsComponent
from   zeta.comp.review             import ReviewComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.comp.timeline           import TimelineComponent
from   zeta.comp.system             import SystemComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 5
no_of_attachs   = 1
no_of_projects  = 5
no_of_tickets   = 50
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 50
no_of_wikis     = 5
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
attachcomp  = None
tagcomp     = None
syscomp     = None
liccomp     = None
projcomp    = None
tckcomp     = None
vcscomp     = None
revcomp     = None
wikicomp    = None
tlcomp      = None
cachemgr    = None
cachedir    = '/tmp/testcache'
dotdir      = os.path.join( os.path.dirname( __file__ ), 'dotdir' )

attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, tagcomp, syscomp, liccomp, \
           projcomp, tckcomp, vcscomp, revcomp, wikicomp, tlcomp, seed, cachemgr

    isdir(dotdir) or os.makedirs(dotdir)

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
    attachcomp = AttachComponent( compmgr )
    tagcomp    = TagComponent( compmgr )
    syscomp    = SystemComponent( compmgr )
    liccomp    = LicenseComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    tckcomp    = TicketComponent( compmgr )
    vcscomp    = VcsComponent( compmgr )
    revcomp    = ReviewComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
    tlcomp     = TimelineComponent( compmgr )


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
    print "   Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
    pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
    print "   Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
    pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_tickets=%s" + \
            "no_of_vcs=%s, no_of_reviews=%s, no_of_wikis=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_tickets, no_of_vcs, no_of_reviews, no_of_wikis
          )

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
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )

class TestAnalytics( object ) :

    @attr(type='tag')
    def test_1_tag( self ) :
        """Testing Tag analytics"""
        log.info( "Testing Tag analytics" )

        ta = ca.get_analyticobj( 'tags' )
        ta.analyse()
        ta.cacheme()
        ta = ca.get_analyticobj( 'tags' )

        attrs = [ 'attachments', 'licenses', 'projects', 'tickets', 'reviews',
                  'wikipages' ]

        # chart1_data
        for t, v in ta.chart1_data.iteritems() :
            t    = tagcomp.get_tag(t)
            data = [ [ a, len(getattr( t, a, [] )) ] for a in attrs ]
            assert_equal( sorted(v, key=lambda x : x[0] ),
                          sorted(data, key=lambda x : x[0] ),
                          'Mismatch in chart1_data' )

        # chart1_rtags
        # TODO : not testing the percentile of related tags.
        for t, v in ta.chart1_rtags.iteritems() :
            t    = tagcomp.get_tag(t)
            ref  = []
            for a in attrs :
                objs = getattr( t, a )
                ref.extend([ rtag.tagname
                             for obj in objs 
                             for rtag in getattr(obj, 'tags', [])
                             if rtag.tagname != t.tagname ])
            ref  = list(set(ref))
            data = map( lambda x : x[0], v )
            assert_equal( sorted(data), sorted(ref), 'Mismatch in chart1_rtag' )

        # chart4_data
        for t, atts in ta.chart4_data :
            t    = tagcomp.get_tag(t)
            ref  = sorted( [ [a.id, a.filename] for a in t.attachments ],
                           key=lambda x: x[0] )
            data = sorted( atts, key=lambda x: x[0] )
            assert_equal( data, ref, 'Mismatch in chart4_data' )

        # chart4_tags
        data = []
        for a in attachcomp.get_attach( attrload=[ 'tags' ] ) :
            data.extend([ t.tagname for t in a.tags ])
        data = list(set(data))
        assert_equal( sorted(data), sorted(ta.chart4_tags),
                      'Mismatch in chart4_tag' )

        # chart7_data
        for t, lics in ta.chart7_data :
            t    = tagcomp.get_tag(t)
            ref  = sorted( [ [l.id, l.licensename] for l in t.licenses ],
                           key=lambda x: x[0] )
            data = sorted( lics, key=lambda x: x[0] )
            assert_equal( data, ref, 'Mismatch in chart7_data' )

        # chart7_tags
        data = []
        for l in liccomp.get_license( attrload=[ 'tags' ] ) :
            data.extend([ t.tagname for t in l.tags ])
        data = list(set(data))
        assert_equal( sorted(data), sorted(ta.chart7_tags),
                      'Mismatch in chart7_tag' )

        # chart20_data
        for p, v in ta.chart20_data.iteritems() :
            p = projcomp.get_project(p)
            for t, wikis in v :
                t = tagcomp.get_tag(t)
                ref  = sorted([ [w.id, h.wiki_parseurl(w.wikiurl), w.wikiurl]
                                for w in t.wikipages if w.project == p ],
                              key=lambda x : x[0] )
                data = sorted( wikis, key=lambda x : x[0] )
                assert_equal( data, ref, 'mismatch in chart20_data' )

        # chart20_tag
        data = []
        projects = projcomp.get_project( attrload=[ 'wikis'],
                                         attrload_all=[ 'wikis.tags' ] )
        for p in projects :
            ref = sorted(list(set([ t.tagname for w in p.wikis for t in w.tags ])))
            assert_equal( ref, ta.chart20_tags[p.id],
                          'mismatch in chart20_tag' )

    @attr(type='attach')
    def test_2_attach( self ) :
        """Testing Attachment analytics"""
        log.info( "Testing Attachment analytics" )

        aa = ca.get_analyticobj( 'attachs' )
        aa.analyse()
        aa.cacheme()
        aa = ca.get_analyticobj( 'attachs' )

        # chart2_data
        ref = []
        for u in userscomp.get_user( attrload=[ 'uploadedattachments' ]) :
            if not u.uploadedattachments : continue
            atts = len(u.uploadedattachments)
            pyld = sum([ a and len(attachcomp.content(a)) or 0
                         for a in u.uploadedattachments ])
            ref.append([ u.username, atts, pyld ])

        assert_equal( sorted( ref, key=lambda x: x[0] ),
                      sorted( aa.chart2_data, key=lambda x : x[0] ),
                      'mismatch in chart2_data' )

        # chart2_fcnt
        attachs = attachcomp.get_attach()
        assert_equal( len(attachs), aa.chart2_fcnt, 'Mismatch in chart2_fcnt' )

        # chart2_payld
        ref = sum([ len(attachcomp.content(a)) for a in attachs if a ])
        assert_equal( ref, aa.chart2_payld, 'Mismatch in chart2_payld' )

        # chart3_data
        ref  = sorted( [ [ a.id, a.filename, a.download_count ] for a in attachs ],
                       key=lambda x : x[0] )
        data = sorted( aa.chart3_data, key=lambda x : x[0] )
        assert_equal( ref, data, 'mismatch in chart3_data' )

        # chart5_data
        data = []
        [ data.extend( v ) for v in aa.chart5_data ]
        ref = [ [ a.id, a.filename, a.created_on.ctime(), a.created_on ]
                for a in sorted( attachs, key=lambda a : a.created_on ) ]
        assert_equal( ref, data, 'Mismatch in chart5_data' )

    @attr(type='staticwiki')
    def test_3_staticwiki( self ) :
        """Testing SWiki analytics"""
        import lxml.html as lh

        log.info( "Testing SWiki analytics" )

        swa = ca.get_analyticobj( 'staticwiki' )
        swa.analyse()
        swa.cacheme()
        swa = ca.get_analyticobj( 'staticwiki' )

        # pagesnippets
        ref = []
        for (swid, (hd, pr)) in swa.pagesnippets.items() :
            sw = syscomp.get_staticwiki( swid )
            root = sw.texthtml and lh.fromstring(sw.texthtml)
            heads = root.xpath("//h1") or root.xpath("//h2") or \
                    root.xpath("//h3") or root.xpath("//h4") or root.xpath("//h5")
            ref_head = heads and ''.join( heads.pop(0).xpath(".//text()") ) or u''
            ref_para = ''.join(root.xpath("//p/text()"))
            assert_true( hd == ref_head,
                         'Mismatch in head snippet from static wiki' )
            assert_true( pr == ref_para,
                         'Mismatch in para snippet from static wiki' )


    @attr(type='users')
    def test_4_users( self ) :
        """Testing User analytics"""
        log.info( "Testing User analytics" )

        ua = ca.get_analyticobj( 'users' )
        ua.analyse()
        ua.cacheme()
        ua = ca.get_analyticobj( 'users' )

        users = userscomp.get_user(
                    attrload=[ 'logs', 'permgroups',
                               'adminprojects', 'owncomponents' ] )
        # chart8_data
        ref  = sorted( [ [ u.id, u.username, len(u.logs) ] for u in users ],
                       key= lambda u : u[0] )
        data = sorted( ua.chart8_data, key= lambda u : u[0] )

        # chart9_data
        pnames = userscomp.site_permnames
        ref = []
        for u in users :
            if u.username == 'admin' :
                upnames = pnames
            else :
                upnames = [ pn.perm_name
                            for pg in u.permgroups for pn in pg.perm_names ]
            ref.append([ u.id, u.username,
                         list(set(pnames).intersection(upnames)),
                         list(set(pnames).difference(upnames))
                      ])
        assert_equal( sorted( ref, key=lambda u : u[0] ),
                      sorted( ua.chart9_data, key=lambda u : u[0] ),
                      'Mismatch in chart9_data' )

        # chart10_data
        ref = [ [ u.id, u.username,
                  sorted([ p.projectname for p in u.adminprojects ])
                ] for u in users ]
        ref = filter( lambda x : x[2], ref )
        assert_equal( sorted( ref, key=lambda x : x[0] ),
                      sorted( ua.chart10_data, key=lambda x : x[0] ),
                      'mismatch in chart10_data' )

        # chart11_data
        ref = [ [ u.id, u.username,
                  sorted([ comp.componentname for comp in u.owncomponents ])
                ] for u in users ]
        ref = filter( lambda x : x[2], ref )
        assert_equal( sorted( ref, key=lambda x : x[0] ),
                      sorted( ua.chart11_data, key=lambda x : x[0] ),
                      'mismatch in chart11_data' )

    @attr(type='license')
    def test_5_license( self ) :
        """Testing License analytics"""
        log.info( "Testing License analytics" )

        la = ca.get_analyticobj( 'license' )
        la.analyse()
        la.cacheme()
        la = ca.get_analyticobj( 'license' )
    
        # chart6_data
        ref = [ [ l.id, l.licensename,
                  [ p.projectname for p in l.projects ]
                ] for l in liccomp.get_license( attrload=[ 'projects' ] ) ]
        assert_equal( sorted(ref, key=lambda l : l[0] ),
                      sorted(la.chart6_data, key=lambda l : l[0] ),
                      'mismatch in chart6_data' )

    @attr(type='projects')
    def test_6_projects( self ) :
        """Testing Project analytics"""
        log.info( "Testing Project analytics" )

        pa = ca.get_analyticobj( 'projects' )
        pa.analyse()
        pa.cacheme()
        pa = ca.get_analyticobj( 'projects' )

    @attr(type='tickets')
    def test_7_tickets( self ) :
        """Testing Ticket analytics"""
        log.info( "Testing Ticket analytics" )

        ta = ca.get_analyticobj( 'tickets' )
        ta.analyse()
        ta.cacheme()
        ta = ca.get_analyticobj( 'tickets' )

        projects = dict([ (p.id, p) 
                          for p in projcomp.get_project( attrload=[ 'tickets' ] )
                       ])

        # chart21_data
        for p, v in ta.chart21_data.iteritems() :
            p   = projects[p]
            ref = len(p.tickets)
            assert_equal( ref, sum([ x[1] for x in v[0] ]),
                          'mismatch in chart21_data' )
            assert_equal( ref, sum([ x[1] for x in v[1] ]),
                          'mismatch in chart21_data' )
            assert_equal( ref, sum([ x[1] for x in v[2] ]),
                          'mismatch in chart21_data' )

        # chart22_data
        for p, v in ta.chart22_data.iteritems() :
            p = projects[p]
            assert_equal( set( [ x[0] for x in v ]
                             ).difference( projcomp.projusernames(p) +
                                           [ p.admin.username ]
                             ),
                          set([]),
                          'mismatch in chart22_data' )

        # chart23_data
        for p, v in ta.chart23_data.iteritems() :
            p = projects[p]
            assert_equal( set( [ x[0] for x in v ]
                             ).difference(
                                 [ comp.componentname for comp in p.components ]
                             ),
                          set([]),
                          'mismatch in chart23_data' )

        # chart24_data
        for p, v in ta.chart24_data.iteritems() :
            p = projects[p]
            assert_equal( set( [ x[0] for x in v ]
                             ).difference(
                                 [ m.milestone_name for m in p.milestones ]
                             ),
                          set([]),
                          'mismatch in chart24_data' )

        # chart25_data
        for p, v in ta.chart25_data.iteritems() :
            p = projects[p]
            assert_equal( set( [ x[0] for x in v ]
                             ).difference(
                                 [ v.version_name for v in p.versions ]
                             ),
                          set([]),
                          'mismatch in chart25_data' )

    @attr(type='reviews')
    def test_8_reviews( self ) :
        """Testing Review analytics"""
        log.info( "Testing Review analytics" )

        ra = ca.get_analyticobj( 'reviews' )
        ra.analyse()
        ra.cacheme()
        ra = ca.get_analyticobj( 'reviews' )

    @attr(type='wiki')
    def test_9_wiki( self ) :
        """Testing Wiki analytics"""
        log.info( "Testing Wiki analytics" )

        wa = ca.get_analyticobj( 'wiki' )
        wa.analyse()
        wa.cacheme()
        wa = ca.get_analyticobj( 'wiki' )
