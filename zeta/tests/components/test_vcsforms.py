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

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.model.tables            import UserRelation
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects, \
                                           pop_wikipages
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.comp.forms              import *
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.comp.vcs                import VcsComponent
from   zeta.comp.wiki               import WikiComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 2
no_of_tags      = 5
no_of_attachs   = 1
no_of_projects  = 10
no_of_vcs       = no_of_projects * 2
g_byuser        = u'admin'

compmgr     = None
userscomp   = None
attachcomp  = None
liccomp     = None
projcomp    = None
wikicomp    = None
vcscomp     = None
cachemgr    = None
cachedir    = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, attachcomp, liccomp, projcomp, vcscomp, \
           wikicomp, seed, cachemgr

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
    liccomp    = LicenseComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    vcscomp    = VcsComponent( compmgr )
    wikicomp   = WikiComponent( compmgr )
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
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s, no_of_vcs=%s" ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects, no_of_vcs )

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


class TestVcsForms( object ) :

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

    def test_1_integratevcs_valid( self ) :
        """Testing FormIntegrateVcs with valid input"""
        log.info( "Testing FormIntegrateVcs with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'integratevcs' )

        users        = userscomp.get_user()
        projects     = projcomp.get_project()
        u            = choice( users )
        p            = choice( projects )
        types        = vcscomp.get_vcstype()

        # Integrate a vcs entry
        c.rclose = h.ZResp()
        rooturl = u'file:///some/url/path/to/repository/root'
        type = choice( types )
        name = u'some-svn-name'
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'vcs_typename', type.vcs_typename )
        request.POST.add( 'name', name )
        request.POST.add( 'rooturl', rooturl )
        request.POST.add( 'loginname', u.username )
        request.POST.add( 'password', u.username )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['integratevcs'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'added project repository' in _u.logs[-1].log 
        )

        v = vcscomp.get_vcs(sorted([ v.id for v in vcscomp.get_vcs() ])[-1])
        assert_equal( [ type.vcs_typename, name, rooturl, u.username, u.username,
                        p.projectname ],
                      [ v.type.vcs_typename, v.name, v.rooturl, v.loginname,
                        v.password, v.project.projectname ],
                      'Mismatch in creating vcs entry'
                    )

        # Integrate a second vcs entry
        request.POST.clearfields()
        rooturl      = u'file:///some/url/path/to/repository/root'
        type         = choice( types )
        name         = u'some-svn-name'
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'vcs_typename', type.vcs_typename )
        request.POST.add( 'name', name )
        request.POST.add( 'rooturl', rooturl )
        vf.process( request, c )
        v = vcscomp.get_vcs(sorted([ v.id for v in vcscomp.get_vcs() ])[-1])
        assert_equal( [ type.vcs_typename, name, rooturl, p.projectname ],
                      [ v.type.vcs_typename, v.name, v.rooturl, 
                        v.project.projectname ],
                      'Mismatch in creating partial vcs entry'
                    )

    def test_2_integratevcs_invalid( self ) :
        """Testing FormIntegrateVcs with invalid input"""
        log.info( "Testing FormIntegrateVcs with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'integratevcs' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        types    = vcscomp.get_vcstype()
        u        = choice( users )
        p        = choice( projects )
        type     = choice( types )
        # Try creating vcs page with in sufficient data
        request.POST.add( 'user_id', str(u.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try creating vcs page with in-sufficient data
        request.POST.add( 'project_id', str(p.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try creating vcs page with in-sufficient data
        request.POST.add( 'vcs_typename', type.vcs_typename )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try creating vcs page with in-sufficient data
        request.POST.add( 'name', u'some name' )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_3_configvcs( self ) :
        """Testing FormConfigVcs with valid and invalid input"""
        log.info( "Testing FormConfigVcs with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'configvcs' )

        users    = userscomp.get_user()
        projects = projcomp.get_project()
        u        = choice( users )
        p        = choice( projects )
        types    = vcscomp.get_vcstype()

        # Randomly config wiki.
        c.rclose = h.ZResp()
        v         = vcscomp.get_vcs( 1 )
        type      = choice( types + [ None ]*5 )
        name      = choice( [u'configured-name'] + [None]*5 )
        rooturl   = choice( [u'file:///some/url/'] + [None]*5 )
        loginname = choice( [u.username] + [None]*5 )
        password  = choice( [u.username] + [None]*5 )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'vcs_id', str(v.id) )
        if type :
            request.POST.add( 'vcs_typename', type.vcs_typename )
        if name :
            request.POST.add( 'name', name )
        if rooturl :
            request.POST.add( 'rooturl', rooturl )
        if loginname :
            request.POST.add( 'loginname', loginname )
        if password :
            request.POST.add( 'password', password )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['configvcs'] )

        if type or name or rooturl :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda _u : 'changed attributes' in _u.logs[-1].log 
            )
        else :
            c.rclose.close()

        v = vcscomp.get_vcs( 1 )
        if type :
            assert_equal( v.type.vcs_typename, type.vcs_typename,
                          'Mismatch in configuring type for vcs' )
        if name :
            assert_equal( v.name, name, 
                          'Mismatch in configuring name for vcs' )
        if rooturl :
            assert_equal( v.rooturl, rooturl, 
                          'Mismatch in configuring rooturl for vcs' )
        if loginname :
            assert_equal( v.loginname, loginname, 
                          'Mismatch in configuring loginname for vcs' )
        if password :
            assert_equal( v.password, password, 
                          'Mismatch in configuring password for vcs' )

    def test_3_deletevcs( self ) :
        """Testing FormDeleteVcs with valid and invalid input"""
        log.info( "Testing FormDeleteVcs with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deletevcs' )

        users      = userscomp.get_user()
        projects   = projcomp.get_project()
        vcsentries = vcscomp.get_vcs()
        u          = choice( users )
        p          = choice( projects )
        v          = choice( vcsentries )
        vcsentries.remove( v )

        c.rclose = h.ZResp()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'vcs_id', str(v.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['deletevcs'] )
        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'deleted project repository' in _u.logs[-1].log 
        )
        assert_equal( sorted(vcsentries), sorted(vcscomp.get_vcs()),
                      'Mismatch in deleting vcs entry' )

    def test_4_createmount_valid( self ) :
        """Testing FormCreateVcsmount with valid input"""
        log.info( "Testing FormCreateVcsmount with valid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createmount' )

        users        = userscomp.get_user()
        repos        = vcscomp.get_vcs()
        u            = choice( users )
        v            = choice( repos )

        # Create a mount entry without content
        name      = u'mountname1'
        repospath = u'some/path/to/mount'

        c.rclose = h.ZResp()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'vcs_id', str(v.id) )
        request.POST.add( 'name', name )
        request.POST.add( 'repospath', repospath )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createmount'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'Mounted directory ' in _u.logs[-1].log 
        )

        m = vcscomp.get_mount()[-1]
        assert_equal( [ v.id, name, repospath, h.MNT_TEXTCONTENT ],
                      [ m.vcs.id, m.name, m.repospath, m.content ],
                      'Mismatch in creating mount entry'
                    )

        # Create a mount entry with content
        request.POST.clearfields()
        name      = u'mountname2'
        repospath = u'some/path/to/mount2'
        content   = choice(vcscomp.mountcontents)
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'vcs_id', str(v.id) )
        request.POST.add( 'name', name )
        request.POST.add( 'repospath', repospath )
        request.POST.add( 'content', content )
        vf.process( request, c )
        m = vcscomp.get_mount()[-1]
        assert_equal( [ v.id, name, repospath, content ],
                      [ m.vcs.id, m.name, m.repospath, m.content ],
                      'Mismatch in creating mount entry'
                    )

    def test_5_createmount_invalid( self ) :
        """Testing FormCreateVcsmount with invalid input"""
        log.info( "Testing FormCreateVcsmount with invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'integratevcs' )

        users    = userscomp.get_user()
        repos    = vcscomp.get_vcs()
        u        = choice( users )
        v        = choice( repos )
        # Try creating vcs page with in sufficient data
        request.POST.add( 'user_id', str(u.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try creating vcs page with in-sufficient data
        request.POST.add( 'vcs_id', str(v.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try creating vcs page with in-sufficient data
        request.POST.add( 'name', 'mountname3' )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_6_updatemount( self ) :
        """Testing FormUpdateVcsmount with valid and invalid input"""
        log.info( "Testing FormUpdateVcsmount with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updatemount' )

        users    = userscomp.get_user()
        repos    = vcscomp.get_vcs()
        mounts   = vcscomp.get_mount()
        u        = choice( users )
        v        = choice( repos )
        m        = choice( mounts )

        # Update mount
        name      = u'updatemount1'
        repospath = u'some/update/path/to/mount'
        content   = choice(vcscomp.mountcontents)

        c.rclose = h.ZResp()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'mount_id', str(m.id) )
        if name :
            request.POST.add( 'name', name )
        if repospath :
            request.POST.add( 'repospath', repospath )
        if content :
            request.POST.add( 'content', content )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, fromnames=['updatemount'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'Updated repository mount' in _u.logs[-1].log 
        )

        m = vcscomp.get_mount( m.id )

        if name :
            assert_equal( m.name, name, 
                          'Mismatch in configuring name for mount' )
        if repospath :
            assert_equal( m.repospath, repospath, 
                          'Mismatch in configuring repospath for mount' )
        if content :
            assert_equal( m.content, content, 
                          'Mismatch in configuring content for mount' )

    def test_7_deletemount( self ) :
        """Testing FormDeleteVcsmount with valid and invalid input"""
        log.info( "Testing FormDeleteVcsmount with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'deletemount' )

        users    = userscomp.get_user()
        mounts   = vcscomp.get_mount()
        u        = choice( users )
        m        = choice( mounts )
        mid      = m.id
        count    = len(vcscomp.get_mount())

        c.rclose = h.ZResp()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'mount_id', str(m.id) )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['deletemount'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'Deleted mount point' in _u.logs[-1].log 
        )

        assert_false( vcscomp.get_mount(mid),
                      'Mismatch in deleting mount entry' )
        assert_equal( len(vcscomp.get_mount()), count-1,
                     'Mismatch in deleting mount entry')

    def test_8_vcsfile2wiki( self ) :
        """Testing FormVcsfile2Wiki with valid and invalid input"""
        log.info( "Testing FormVcsfile2Wiki with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'vcsfile2wiki' )

        users = userscomp.get_user()
        projects = projcomp.get_project()
        u = choice( users )
        p = choice( projects )

        # Test with valid data, pagename as wikiurl
        sourceurl = u"/p/%s/s/1/mako/trunk/setup.py&wikifile=1,cnttype=text" % p.projectname
        pagename = u"/p/%s/wiki/Mapped2VCS" % p.projectname
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'sourceurl', sourceurl )
        request.POST.add( 'pagename', pagename )
        vf.process( request, c )
        w = wikicomp.get_wiki(pagename)
        wcnt = wikicomp.get_content(w)
        wcnt.translate(wiki=w, cache=True)
        wcnt = wikicomp.get_content(w)
        assert_equal( [w.wikiurl, w.sourceurl, w.type.wiki_typename],
                      [pagename, sourceurl, h.WIKITYPE_IFRAME],
                      'Mismatch in vcsfile2wiki with pagename as wikiurl' )
        assert_true( sourceurl in wcnt.texthtml,
                     'Mismatch in wiki tranlation for vcsfile2wiki')

        # Test with valid data
        request.POST.clearfields()
        sourceurl = u"/p/%s/s/1/mako/trunk/setup.py&wikifile=1,cnttype=text" % p.projectname
        pagename = u"Mapped2VCS1"
        wikiurl = u"/p/%s/wiki/Mapped2VCS1" % p.projectname
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'sourceurl', sourceurl )
        request.POST.add( 'pagename', pagename )
        vf.process( request, c )
        w = wikicomp.get_wiki(wikiurl)
        wcnt = wikicomp.get_content(w)
        wcnt.translate(wiki=w, cache=True)
        wcnt = wikicomp.get_content(w)
        assert_equal( [w.wikiurl, w.sourceurl, w.type.wiki_typename],
                      [wikiurl, sourceurl, h.WIKITYPE_IFRAME],
                      'Mismatch in vcsfile2wiki with pagename as wikiurl' )
        assert_true( sourceurl in wcnt.texthtml,
                     'Mismatch in wiki tranlation for vcsfile2wiki')

        # Test with invalid data
        request.POST.clearfields()
        sourceurl = "/p/%s/s/1/mako/trunk/setup.py&wikifile=1,cnttype=text" % p.projectname
        pagename = "Mapped2VCS1"
        wikiurl = "/p/%s/wiki/Mapped2VCS1" % p.projectname
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'pagename', pagename )
        assert_raises( ZetaFormError, vf.process, request, c )
