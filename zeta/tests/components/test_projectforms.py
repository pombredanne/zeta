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
from   zeta.tests.model.generate    import future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, \
                                           pop_licenses, pop_projects
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import *
from   zeta.lib.error               import ZetaTagError, ZetaAttachError
from   zeta.comp.forms              import *
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.system             import SystemComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
no_of_users     = 20
no_of_relations = 2
no_of_tags      = 3
no_of_attachs   = 1
no_of_projects  = 10
g_byuser        = u'admin'

tagchars   = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
taglist     = None 

compmgr     = None
userscomp   = None
syscomp     = None
attachcomp  = None
tagcomp     = None
liccomp     = None
projcomp    = None
cachemgr    = None
cachedir    = '/tmp/testcache'


attachfiles = [ os.path.join( '/usr/include', f)  
                for f in os.listdir( '/usr/include' )
                if os.path.isfile( os.path.join( '/usr/include', f )) ]

def setUpModule() :
    """Create database and tables."""
    global compmgr, userscomp, syscomp, attachcomp, tagcomp, liccomp, taglist, \
           projcomp, seed, cachemgr

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
    attachcomp = AttachComponent( compmgr )
    tagcomp    = TagComponent( compmgr )
    liccomp    = LicenseComponent( compmgr )
    projcomp   = ProjectComponent( compmgr )
    taglist = [ unicode(h.randomname( randint(0,LEN_TAGNAME), tagchars))
                            for i in range(randint(1,no_of_tags)) ]
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
    print "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, no_of_attach=%s" % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs )

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


class TestProjectForms( object ) :

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

    def test_1_createproject_valid( self ) :
        """Testing FormCreateProject with valid input"""
        log.info( "Testing FormCreateProject with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
        c.sysentries= syscomp.get_sysentry()

        users   = userscomp.get_user()
        license = liccomp.get_license()
        u       = choice( users )
        l       = choice( license )

        # Create project
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createprj' )
        projectname = u'someprojectname'
        summary     = u'someprojectsummary'
        admin_email = u.emailid
        description = u'some project description'
        licensename = l.licensename
        admin       = u.username
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'projectname', projectname )
        request.POST.add( 'summary',     summary )
        request.POST.add( 'admin_email', admin_email )
        request.POST.add( 'description', description )
        request.POST.add( 'licensename', licensename )
        request.POST.add( 'admin',       admin )
        defer = choice([True, False])
        vf.process( request, c, defer=defer, formnames=['createprj'] )

        def defercheck(log) :
            reflogs = [ 'created a new project', 'created the wiki page',
                        'updated wiki content' ]
            return all(map( lambda l : l in log, reflogs ))

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : defercheck( ''.join(map(lambda l: l.log, u.logs[-3:])) )
        )

        p = projcomp.get_project( projectname )
        assert_equal( [ projectname, summary, admin_email, description, 
                        licensename, admin ],
                      [ p.projectname, p.summary, p.admin_email,
                        p.project_info.description, p.license.licensename,
                        p.admin.username ],
                      'Mismatch while creating project'
                    )
        assert_true( PROJHOMEPAGE in p.wikis[-1].wikiurl,
                     'Default front page not created for the project' )
        
        # update project
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updateprj' )
        projectname = u'updated_projectname'
        summary = u'updated project summary'
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'projectname', projectname )
        request.POST.add( 'summary',     summary )
        request.POST.add( 'admin_email', admin_email )
        request.POST.add( 'description', description )
        request.POST.add( 'licensename', licensename )
        request.POST.add( 'admin',       admin )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['updateprj'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated project information' in u.logs[-1].log
        )

        p       = projcomp.get_project( projectname )
        assert_equal( [ projectname, summary, admin_email, description, 
                        licensename, admin ],
                      [ p.projectname, p.summary, p.admin_email,
                        p.project_info.description, p.license.licensename,
                        p.admin.username ],
                      'Mismatch while updating project'
                    )

    def test_2_createproject_invalid( self ) :
        """Testing FormCreateProject with invalid input"""
        log.info( "Testing FormCreateProject with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
        c.sysentries= syscomp.get_sysentry()

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createprj' )

        users   = userscomp.get_user()
        license = liccomp.get_license()
        u       = choice( users )
        l       = choice( license )
        # Try creating project with missing fields.
        request.POST.add( 'user_id', str(u.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        projectname = u'someprojectname1'
        request.POST.add( 'projectname', projectname )
        assert_raises( ZetaFormError, vf.process, request, c )

        summary     = u'someprojectsummary'
        request.POST.add( 'summary',     summary )
        assert_raises( ZetaFormError, vf.process, request, c )

        admin_email = u.emailid
        request.POST.add( 'admin_email', admin_email )
        assert_raises( ZetaFormError, vf.process, request, c )

        description = u'some project description'
        request.POST.add( 'description', description )
        assert_raises( ZetaFormError, vf.process, request, c )

        licensename = l.licensename
        request.POST.add( 'licensename', licensename )
        assert_raises( ZetaFormError, vf.process, request, c )

        admin       = u.username
        request.POST.add( 'admin',       admin )
        vf.process( request, c )

        # Try creating an existing project.
        projectname = u'someprojectname1'
        summary     = u'someprojectsummary'
        admin_email = u.emailid
        description = u'some project description'
        licensename = l.licensename
        admin       = u.username
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'projectname', projectname )
        request.POST.add( 'summary',     summary )
        request.POST.add( 'admin_email', admin_email )
        request.POST.add( 'description', description )
        request.POST.add( 'licensename', licensename )
        request.POST.add( 'admin',       admin )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_3_projectlicense( self ) :
        """Testing FormProjectLicense with valid and invalid inputs"""
        log.info( "Testing FormProjectLicense with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        u        = choice( users )
        projects = projcomp.get_project()
        p        = choice( projects )

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjlic' )

        for l in liccomp.get_license() :
            request.POST.clearfields()
            licensename = l.licensename
            if p.license and p.license.licensename == licensename :
                continue

            c.rclose = h.ZResp()
            request.POST.add( 'user_id', str(u.id) )
            defer = choice([ True, False ])
            r = randint(0,2)
            if r == 0 :
                request.POST.add( 'project_id', str(p.id) )
                request.POST.add( 'licensename', licensename )
                vf.process( request, c, defer=defer, formnames=['prjlic'] )
                p = projcomp.get_project( p.projectname )
                assert_equal( p.license, l, 
                              'Mismatch will assigning license to project' )
            if r == 1 :
                request.POST.add( 'project_id', str(p.id) )
                p    = projcomp.get_project( p.projectname )
                assert_raises( ZetaFormError, vf.process, request, c,
                               defer=defer, formnames=['prjlic'] )
            if r == 2 :
                request.POST.add( 'licensename', licensename )
                vf.process( request, c, defer=defer, formnames=['prjlic'] )
                p = projcomp.get_project( p.projectname )
                assert_not_equal(
                    p.license, l, 
                    'Mismatch will assigning license to project'
                )

            if r == 0 :
                self._validate_defer(
                        c.authuser, defer, c,
                        lambda u : 'updated project attributes' in u.logs[-1].log \
                                   and l.licensename in u.logs[-1].log
                )

    def test_4_projectadmin( self ) :
        """Testing FormProjectAdmin with valid and invalid inputs"""
        log.info( "Testing FormProjectAdmin with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        u        = choice( users )
        projects = projcomp.get_project()
        p        = choice( projects )

        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjadmin' )

        for admin in userscomp.get_user() :
            request.POST.clearfields()
            adminname = admin.username
            if p.admin and p.admin.username == adminname :
                continue

            c.rclose = h.ZResp()
            request.POST.add( 'user_id', str(u.id) )
            defer = choice([ True, False ])
            r = randint(0,2)
            if r == 0 :
                request.POST.add( 'project_id', str(p.id) )
                request.POST.add( 'adminname', adminname )
                vf.process( request, c, defer=defer, formnames=['prjadmin'] )
                p = projcomp.get_project( p.projectname )
                assert_equal( p.admin, admin, 
                              'Mismatch will assigning admin to project' )
            if r == 1 :
                request.POST.add( 'project_id', str(p.id) )
                p = projcomp.get_project( p.projectname )
                assert_raises( ZetaFormError, vf.process, request, c,
                               defer=defer, formnames=['prjadmin'] )
            if r == 2 :
                request.POST.add( 'adminname', adminname )
                vf.process( request, c, defer=defer, formnames=['prjadmin'] )
                p = projcomp.get_project( p.projectname )
                assert_not_equal(
                    p.admin, admin, 
                    'Expected admin assignement to project to fail'
                )

            if r == 0 :
                self._validate_defer(
                        c.authuser, defer, c,
                        lambda u : 'updated project attributes' in u.logs[-1].log \
                                   and adminname in u.logs[-1].log
                )

    def test_5_projectdisable( self ) :
        """Testing FormProjectDisable with valid and invalid inputs"""
        log.info( "Testing FormProjectDisable with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        u        = choice( users )
        projects = projcomp.get_project()

        # Disable all projects
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjdis' )
        disprojs = projects[:]
        while disprojs :
            c.rclose = h.ZResp()
            projs   = [ disprojs.pop() for i in range(randint(0,len(disprojs))) ]
            request.POST.clearfields()
            request.POST.add( 'user_id', str(u.id) )
            [ request.POST.add( 'disable_project', p.projectname )
              for p in projs ]
            vf.process( request, c, defer=False, formnames=['prjdis'] )

            if projs :
                _fn = lambda l : getattr( getattr(l, 'project', ''), 'projectname', '' )
                self._validate_defer(
                    c.authuser, False, c,
                    lambda u : ('updated project attributes' in u.logs[-1].log) \
                               and (p.projectname == _fn(u.logs[-1]))
                )

        # Enable all projects
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjenb' )
        enprojs = projects[:]
        while enprojs :
            c.rclose = h.ZResp()
            projs   = [ enprojs.pop() for i in range(randint(0,len(enprojs))) ]
            request.POST.clearfields()
            request.POST.add( 'user_id', str(u.id) )
            [ request.POST.add( 'enable_project', p.projectname )
              for p in projs ]
            vf.process( request, c, defer=False, formnames=['prjenb'] )

            if projs :
                _fn = lambda l : getattr( getattr(l, 'project', ''), 'projectname', '' )
                self._validate_defer(
                    c.authuser, False, c,
                    lambda u : 'updated project attributes' in u.logs[-1].log \
                               and (p.projectname == _fn(u.logs[-1]))
                )

        projects = projcomp.get_project()
        assert_true( all([ p.disabled == False for p in projects ]),
                     'Mismatch while disabling projects' )

        # Disable few projects
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjenb' )
        request.POST.add( 'user_id', str(u.id) )
        disprojs = list(set([ choice(projects)
                              for p in range(randint(0,len(projects))) ]))
        [ request.POST.add( 'disable_project', p.projectname )
          for p in disprojs ]
        vf.process( request, c )

        projects = projcomp.get_project()
        assert_equal( sorted([ p.projectname for p in projects
                                             if p.disabled == True ]),
                      sorted([ p.projectname for p in disprojs ]),
                      'Mismatch while disabling projects' )

    def test_6_projectexpose( self ) :
        """Testing FormProjectExpose with valid and invalid inputs"""
        log.info( "Testing FormProjectExpose with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users    = userscomp.get_user()
        u        = choice( users )
        projects = projcomp.get_project()

        # Expose all projects
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjexp' )
        expprojs = projects[:]
        while expprojs :
            projs   = [ expprojs.pop() for i in range(randint(0,len(expprojs))) ]
            request.POST.clearfields()
            request.POST.add( 'user_id', str(u.id) )
            [ request.POST.add( 'expose_project', p.projectname )
              for p in projs ]

            c.rclose = h.ZResp()
            vf.process( request, c, defer=False, formnames=['prjexp'] )
            if projs :
                _fn = lambda l : getattr( getattr(l, 'project', ''), 'projectname', '' )
                self._validate_defer(
                    c.authuser, False, c,
                    lambda _u : 'updated project attributes' in _u.logs[-1].log \
                                and (p.projectname == _fn(_u.logs[-1]))
                )

        # Private all projects
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjprv' )
        prvprojs = projects[:]
        while prvprojs :
            projs   = [ prvprojs.pop() for i in range(randint(0,len(prvprojs))) ]
            request.POST.clearfields()
            request.POST.add( 'user_id', str(u.id) )
            [ request.POST.add( 'private_project', p.projectname )
              for p in projs ]

            c.rclose = h.ZResp()
            vf.process( request, c, defer=False, formnames=['prjexp'] )
            if projs :
                _fn = lambda l : getattr( getattr(l, 'project', ''), 'projectname', '' )
                self._validate_defer(
                    c.authuser, False, c,
                    lambda _u : 'updated project attributes' in _u.logs[-1].log \
                                and (p.projectname == _fn(_u.logs[-1]))
                )
        assert_true( all([ p.exposed == False for p in projects ]),
                     'Mismatch while exposing projects' )

        request.POST.clearfields()
        vf.process( request, c )

        # Expose few projects
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjexp' )
        request.POST.add( 'user_id', str(u.id) )
        expprojs = list(set([ choice(projects)
                              for p in range(randint(0,len(projects))) ]))
        [ request.POST.add( 'expose_project', p.projectname )
          for p in expprojs ]
        vf.process( request, c )
        projects = projcomp.get_project()
        assert_equal( sorted([ p.projectname for p in projects
                                             if p.exposed == True ]),
                      sorted([ p.projectname for p in expprojs ]),
                      'Mismatch while disabling projects' )

    def test_7_projectlogo_valid( self ) :
        """Testing FormProjectLogo with valid input"""
        log.info( "Testing FormProjectLogo with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        projects        = projcomp.get_project()
        user            = choice( users )
        p               = choice( projects )

        # Attach project logo
        c.rclose = h.ZResp()
        attachfile = choice( attachfiles )
        attach = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file = open( attachfile, 'r' )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjlogo' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'attachfile', attach  )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['addprjlogo'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'project-logo' in _u.logs[-1].log and \
                            attach.filename in _u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        assert_equal( p.logofile.filename, attach.filename,
                      'Mismatch in logo attachment'
                    )
        a, cont = attachcomp.downloadattach(p.logofile.id)
        assert_equal( str(cont), open( attachfile ).read(),
                      'logo files mismatches between files `%s` and `%s`' % \
                      (attachfile, p.logofile.id)
                    )

        # Delete project logo
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjlogo' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        vf.process( request, c )
        p  = projcomp.get_project( p.projectname )
        assert_false( p.logofile, 'Found logo attachment even after removing it' )

    def test_8_projectlogo_invalid( self ) :
        """Testing FormProjectLogo with invalid input"""
        log.info( "Testing FormProjectLogo with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        user            = choice( userscomp.get_user() )
        p               = choice( projcomp.get_project() )

        # Try adding attachment
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjlogo' )
        attachfile      = choice( attachfiles )
        attach          = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjlogo' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'attachfile', attach  )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_9_projecticon_valid( self ) :
        """Testing FormProjectIcon with valid input"""
        log.info( "Testing FormProjectIcon with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        projects        = projcomp.get_project()
        user            = choice( users )
        p               = choice( projects )

        # Add project icon
        c.rclose = h.ZResp()
        attachfile      = choice( attachfiles )
        attach          = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjicon' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'attachfile', attach  )
        defer = choice([True, False])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['addprjicon'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda _u : 'project-icon' in _u.logs[-1].log 
        )

        p = projcomp.get_project( p.projectname )
        assert_equal( p.iconfile.filename, attach.filename,
                      'Mismatch in icon attachment'
                    )
        a, cont = attachcomp.downloadattach(p.iconfile.id)
        assert_equal( str(cont), open( attachfile ).read(),
                      'icon files mismatches between files `%s` and `%s`' % \
                      (attachfile, p.iconfile.id)
                    )

        # Delete project icon
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjicon' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        vf.process( request, c )
        p = projcomp.get_project( p.projectname )
        assert_false( p.iconfile,
                      'Found icon attachment even after removing it' )

    def test_A_projecticon_invalid( self ) :
        """Testing FormProjectIcon with invalid input"""
        log.info( "Testing FormProjectIcon with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        user            = choice( userscomp.get_user() )
        p               = choice( projcomp.get_project() )

        # Try adding icon
        attachfile      = choice( attachfiles )
        attach          = FileObject()
        attach.filename = os.path.basename( attachfile )
        attach.file     = open( attachfile, 'r' )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjicon' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        assert_raises( ZetaFormError, vf.process, request, c )

        # Try deleting icon
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjicon' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'attachfile', attach  )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_B_projectmailinglist( self ) :
        """Testing FormProjectMailinglist with valid and invalid inputs"""
        log.info( "Testing FormProjectMailinglist with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        u = choice( users )
        projects = projcomp.get_project()
        p = choice( projects )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjml' )
        
        c.rclose = h.ZResp()
        mailinglists = u',, , some1@mailinglist.com,some2@mailinglist.com , some3@mailinglist.com'
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'mailinglists', mailinglists )
        refmaillists = [ m.mailing_list for m in p.mailinglists ] + \
                       [ m for m in [ m.strip(' ') for m in mailinglists.split( ',' ) ] if m ]
        defer = choice([ True, False ])
        vf.process( request, c, appendml=True, defer=defer, formnames=['prjml'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'mailing-lists' in u.logs[-1].log
        )

        p = projcomp.get_project( p )
        assert_equal( sorted( refmaillists ),
                      sorted([ m.mailing_list for m in p.mailinglists ]),
                     'Mismatch while appending mailinglist to projects' )

        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        mailinglists = choice([ ', ,,', '' ])
        request.POST.add( 'mailinglists', mailinglists )
        vf.process( request, c, appendml=False )
        p = projcomp.get_project( p )
        assert_false( p.mailinglists, 'Expected mailinglists to be deleted' )

    def test_C_projectirchannels( self ) :
        """Testing FormProjectIRCchannels with valid and invalid inputs"""
        log.info( "Testing FormProjectIRCchannels with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        u = choice( users )
        projects = projcomp.get_project()
        p = choice( projects )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'prjirc' )

        c.rclose = h.ZResp()
        ircchannels  = u',, , some1#ircchannel,some2#ircchannel , some3#ircchannel'
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ircchannels', ircchannels )
        refircchannels = [ irc.ircchannel for irc in p.ircchannels ] + \
                         [ irc for irc in [ irc.strip(' ') for irc in ircchannels.split( ',' ) ] if irc ]
        defer = choice([ True, False ])
        vf.process( request, c, appendirc=True, defer=defer, formnames=['prjirc'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'irc-channels' in u.logs[-1].log
        )

        p = projcomp.get_project( p )
        assert_equal( sorted( refircchannels ),
                      sorted([ irc.ircchannel for irc in p.ircchannels ]),
                     'Mismatch while appending ircchannels to project' )

        request.POST.clearfields()
        ircchannels = choice([ ', ,,', '' ])
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'ircchannels', ircchannels )
        vf.process( request, c, appendirc=False )
        p           = projcomp.get_project( p )
        assert_false( p.ircchannels, 'Expected ircchannels to be deleted' )

    def test_D_projectcreatecomponent_valid( self ) :
        """Testing FormProjectCreateComponent with valid inputs"""
        log.info( "Testing FormProjectCreateComponent with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = projcomp.get_project()
        p           = choice( projects )

        # Create a new component
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createpcomp' )
        componentname = u'somecomponentname' 
        description   = u'somecomponentdescription' 
        owner         = u.username
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'componentname', componentname )
        request.POST.add( 'description',   description)
        request.POST.add( 'owner',         owner )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['createpcomp'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'created new project component' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        comp = [ comp for comp in p.components if comp.componentname == componentname ][0]
        assert_equal( [ componentname, description, owner ],
                      [ comp.componentname, comp.description, comp.owner.username ],
                      'Mismatch while creating a component'
                    )

        # Update component
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updatepcomp' )
        componentname = u'updatedcomponentname'
        description = u'updated component description'
        owner = choice( users ).username
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'component_id', str(comp.id) )
        request.POST.add( 'componentname', componentname )
        request.POST.add( 'description',   description)
        request.POST.add( 'owner',         owner )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['updatepcomp'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated project component' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        comp = [ comp for comp in p.components if comp.componentname == componentname ][0]
        assert_equal( [ componentname, description, owner ],
                      [ comp.componentname, comp.description, comp.owner.username ],
                      'Mismatch while updating a component'
                    )

    def test_E_projectcreatecomponent_invalid( self ) :
        """Testing FormProjectCreateComponent with invalid inputs"""
        log.info( "Testing FormProjectCreateComponent with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = projcomp.get_project()
        p           = choice( projects )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createpcomp' )

        # Try filling the form with in-sufficient data
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        componentname = u'somecomponentname' 
        request.POST.add( 'componentname', componentname )
        assert_raises( ZetaFormError, vf.process, request, c )

        description   = u'somecomponentdescription' 
        request.POST.add( 'description',   description)
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_F_projectcomponentowner( self ) :
        """Testing FormProjectComponentOwner with valid and invalid inputs"""
        log.info( "Testing FormProjectComponentOwner with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users         = userscomp.get_user()
        u             = choice( users )
        projects      = projcomp.get_project()
        p             = choice([ p for p in projects if p.components ])
        comp          = choice( p.components )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'pcompowner' )

        c.rclose = h.ZResp()
        componentname = comp.componentname
        description   = comp.description
        owner         = choice( users ).username
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'component_id', str(comp.id) )
        request.POST.add( 'owner',         owner )
        vf.process( request, c, defer=False, formnames=['pcompowner'] )

        self._validate_defer(
                c.authuser, False, c,
                lambda u : 'owner' in u.logs[-1].log
        )

        comp = projcomp.get_component( component=comp.id )
        assert_equal( [ componentname, description, owner ],
                      [ comp.componentname, comp.description, comp.owner.username ],
                      'Mismatch while updating component owner'
                    )

    def test_G_projectremovecomponent( self ) :
        """Testing FormProjectRemoveComponent with valid and invalid inputs"""
        log.info( "Testing FormProjectRemoveComponent with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users         = userscomp.get_user()
        projects      = projcomp.get_project()
        components    = projcomp.get_component()
        p             = choice( projects )
        u             = choice( users )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmpcomp' )

        c.rclose = h.ZResp()
        rmcomps = list(set([ choice(p.components) 
                             for i in range(randint(0,len(p.components))) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'component_id', str(comp.id) ) for comp in rmcomps ]
        request.POST.add( 'component_id', str(len(components)*3) )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['rmpcomp'] )

        if rmcomps :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted project component' in u.logs[-1].log
            )

        p = projcomp.get_project( p.projectname )
        for comp in rmcomps :
            assert_false( comp in p.components, 'Mismatch in removing components' )

        # Try removing zero components
        components    = projcomp.get_component()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        vf.process( request, c )
        assert_equal( sorted(components), sorted(projcomp.get_component()),
                      'Mismatch while trying to create zero components'
                    )

    def test_H_projectcreatemilestone_valid( self ) :
        """Testing FormProjectCreateMilestone with valid inputs"""
        log.info( "Testing FormProjectCreateMilestone with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = projcomp.get_project()
        p           = choice( projects )

        # Create a new milestone
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createmstn' )
        milestone_name = u'somemilestonename' 
        description    = u'somemilestonedescription' 
        due_date       = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date       = due_date.isoformat().split('T')[0]
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'milestone_name', milestone_name )
        request.POST.add( 'description',   description)
        request.POST.add( 'due_date',      due_date )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['createmstn'] )

        self._validate_defer(
            c.authuser, defer, c,
            lambda u : 'created new project milestone' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        m = [ m for m in p.milestones if m.milestone_name == milestone_name ][0]
        # Convert the due_date to UTC before comparing.
        due_date = h.usertz_2_utc(
                        dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                        timezone( u.timezone )
                   )
        assert_equal( [ milestone_name, description, due_date ],
                      [ m.milestone_name, m.description, m.due_date ],
                      'Mismatch while creating a milestone'
                    )

        # Update milestone
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updatemstn' )
        milestone_name = u'updatedmilestonename'
        description    = u'updated milestone description'
        due_date       = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date       = due_date.isoformat().split('T')[0]
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        request.POST.add( 'milestone_name', milestone_name )
        request.POST.add( 'description',   description)
        request.POST.add( 'due_date',      due_date )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['updatemstn'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated project milestone' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        m = [ m for m in p.milestones if m.milestone_name == milestone_name ][0]
        # Convert the due_date to UTC before comparing.
        due_date = h.usertz_2_utc(
                        dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                        timezone( u.timezone )
                   )
        assert_equal( [ milestone_name, description, due_date ],
                      [ m.milestone_name, m.description, m.due_date ],
                      'Mismatch while updating a milestone'
                    )

    def test_I_projectcreatemilestone_invalid( self ) :
        """Testing FormProjectCreateMilestone with invalid inputs"""
        log.info( "Testing FormProjectCreateMilestone with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = projcomp.get_project()
        p           = choice( projects )

        # Try creating milestone with in-sufficient data.
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createmstn' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        milestone_name = u'somemilestonename' 
        request.POST.add( 'milestone_name', milestone_name )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_J_projectmilestoneduedate( self ) :
        """Testing FormProjectMilestoneDuedate with valid and invalid inputs"""
        log.info( "Testing FormProjectMilestoneDuedate with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = [ p for p in projcomp.get_project() if p.milestones ]
        p           = choice( projects )
        m           = choice( p.milestones )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'mstnduedate' )

        c.rclose = h.ZResp()
        due_date    = future_duedate( *dt.datetime.utcnow().timetuple() )
        due_date    = due_date.isoformat().split('T')[0]
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        request.POST.add( 'due_date',      due_date )
        vf.process( request, c, defer=False, formnames=['mstnduedate'] )

        self._validate_defer(
                c.authuser, False, c,
                lambda u : 'due_date' in u.logs[-1].log
        )

        m = projcomp.get_milestone( m.id )
        # Convert the due_date to UTC before comparing.
        due_date = h.usertz_2_utc(
                        dt.datetime.strptime( due_date, '%Y-%m-%d' ),
                        timezone( u.timezone )
                   )
        assert_equal( due_date, m.due_date,
                      'Mismatch while updating a milestone'
                    )

    def test_K_projectclosemilestone( self ) :
        """Testing FormProjectCloseMilestone with valid and invalid inputs"""
        log.info( "Testing FormProjectCloseMilestone with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = [ p for p in projcomp.get_project() if p.milestones ]
        p           = choice( projects )
        m           = choice( p.milestones )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'mstnclose' )

        c.rclose = h.ZResp()
        closing_remark = u'some closing remark for milestone'
        status  = choice([ 'completed', 'cancelled' ])
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        request.POST.add( 'closing_remark', closing_remark )
        request.POST.add( 'status', status )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['mstnclose'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Closing milestone' in u.logs[-1].log
        )

        m = projcomp.get_milestone( m.id )
        dbstatus    = ( m.completed and 'completed' ) or ( m.cancelled and 'cancelled' )
        assert_equal( [ closing_remark, status ],
                      [ m.closing_remark, dbstatus ],
                      'Mismatch in closing milestone'
                    )

        # Re-open the status
        c.rclose = h.ZResp()
        closing_remark = u'Re-opening the milestone'
        status         = 'open'
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        request.POST.add( 'closing_remark', closing_remark )
        request.POST.add( 'status', status )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['mstnclose'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'Re-opened milestone' in u.logs[-1].log
        )

        m = projcomp.get_milestone( m.id )
        assert_equal( [ closing_remark, False, False ],
                      [ m.closing_remark, m.completed, m.cancelled ],
                      'Mismatch in re-opening milestone'
                    )
        vf.process( request, c )

        # Try closing without closing remarks
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        vf.process( request, c )

        # Try closing with wrong status
        request.POST.add( 'status', 'invalidstatus' )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_K_projectremovemilestone( self ) :
        """Testing FormProjectRemoveMilestone with valid and invalid inputs"""
        log.info( "Testing FormProjectRemoveMilestone with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users       = userscomp.get_user()
        projects    = [ p for p in projcomp.get_project() if p.milestones ]
        milestones  = projcomp.get_milestone()
        u           = choice( users )
        p           = choice( projects )
        m           = choice( p.milestones )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmmstn' )

        c.rclose = h.ZResp()
        rmmstns     = list(set([ choice(p.milestones) 
                                   for i in range(randint(0,len(p.milestones))) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'milestone_id', str(m.id) ) for m in rmmstns ]
        request.POST.add( 'milestone_id', str(len(milestones)*3) )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['rmmstn'] )

        if rmmstns :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted project milestone' in u.logs[-1].log
            )

        p = projcomp.get_project( p.projectname )
        for m in rmmstns :
            assert_false( m in p.milestones,
                          'Mismatch in removing milestones'
                        )

        # Try removing zero milestones
        milestones    = projcomp.get_milestone()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        vf.process( request, c )
        assert_equal( sorted(milestones), sorted(projcomp.get_milestone()),
                      'Mismatch while trying to create zero milestone'
                    )

    def test_L_projectcreateversion_valid( self ) :
        """Testing FormProjectCreateVersion with valid inputs"""
        log.info( "Testing FormProjectCreateVersion with valid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = projcomp.get_project()
        p           = choice( projects )

        # Create a new component
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createver' )
        version_name  = u'someversioname' 
        description   = u'someversiondescription' 
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'version_name', version_name )
        request.POST.add( 'description',   description)
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['createver'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'created new project version' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        v = [ v for v in p.versions if v.version_name == version_name ][0]
        assert_equal( [ version_name, description ],
                      [ v.version_name, v.description ],
                      'Mismatch while creating a version'
                    )

        # Update version
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'updatever' )
        version_name  = u'updatedversionname'
        description   = u'updated version description'
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'version_id', str(v.id) )
        request.POST.add( 'version_name', version_name )
        request.POST.add( 'description',   description)
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['updatever'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'updated project version' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        v = [ v for v in p.versions if v.version_name == version_name ][0]
        assert_equal( [ version_name, description ],
                      [ v.version_name, v.description ],
                      'Mismatch while creating a version'
                    )

    def test_M_projectcreateversion_invalid( self ) :
        """Testing FormProjectCreateVersion with invalid inputs"""
        log.info( "Testing FormProjectCreateVersion with invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users       = userscomp.get_user()
        u           = choice( users )
        projects    = projcomp.get_project()
        p           = choice( projects )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'createver' )

        # Try filling the form with in-sufficient data
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        assert_raises( ZetaFormError, vf.process, request, c )
        version_name = u'someversioname' 
        request.POST.add( 'version_name', version_name )
        assert_raises( ZetaFormError, vf.process, request, c )

    def test_N_projectremoveversion( self ) :
        """Testing FormProjectRemoveVersion with valid and invalid inputs"""
        log.info( "Testing FormProjectRemoveVersion with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser
    
        users         = userscomp.get_user()
        projects      = projcomp.get_project()
        versions      = projcomp.get_version()
        p             = choice( projects )
        u             = choice( users )
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'rmver' )

        c.rclose = h.ZResp()
        rmvers = list(set([ choice(p.versions) 
                            for i in range(randint(0,len(p.versions))) ]))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'version_id', str(v.id) ) for v in rmvers ]
        request.POST.add( 'version_id', str(len(versions)*3) )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['rmver'] )

        if rmvers :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted project version' in u.logs[-1].log
            )

        p = projcomp.get_project( p.projectname )
        for v in rmvers :
            assert_false( v in p.versions, 'Mismatch in removing components' )

        # Try removing zero versions
        versions    = projcomp.get_version()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        vf.process( request, c )
        assert_equal( sorted(versions), sorted(projcomp.get_version()),
                      'Mismatch while trying to create zero version'
                    )

    def test_O_projecttags( self ) :
        """Testing FormProjectTags with valid and invalid input"""
        log.info( "Testing FormProjectTags with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users         = userscomp.get_user()
        projects      = projcomp.get_project()
        components    = projcomp.get_component()
        milestones    = projcomp.get_milestone()
        versions      = projcomp.get_version()
        u             = choice( users )
        comp          = choice( components )
        m             = choice( milestones )
        v             = choice( versions )

        # Add tags to component
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjtags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda t : tagcomp.is_tagnamevalid( t ),
                                tagnames ) + \
                        [ t.tagname for t in comp.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(comp.project.id) )
        request.POST.add( 'component_id', str(comp.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['addprjtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added tags' in u.logs[-1].log and \
                           'to component' in u.logs[-1].log
        )

        comp = projcomp.get_component( comp.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in comp.tags ]),
                      'Mismatch while creating project component tags'
                    )

        # Delete tags from component
        c.rclose = h.ZResp()
        rmtag     = choice( reftags )
        reftags.remove( rmtag )
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjtags' )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(comp.project.id) )
        request.POST.add( 'component_id', str(comp.id) )
        request.POST.add( 'tags', rmtag )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['delprjtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted tags' in u.logs[-1].log and \
                           'from component' in u.logs[-1].log
        )

        comp = projcomp.get_component( comp.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in comp.tags ]),
                      'Mismatch while deleting project component tags'
                    )

        # Add tags to milestone
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjtags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda t : tagcomp.is_tagnamevalid( t ),
                                tagnames ) + \
                        [ t.tagname for t in m.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(m.project.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['addprjtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added tags' in u.logs[-1].log and \
                           'to milestone' in u.logs[-1].log
        )

        m = projcomp.get_milestone( m.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in m.tags ]),
                      'Mismatch while creating project milestone tags'
                    )

        # Delete tags from milestone
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjtags' )
        rmtag     = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(m.project.id) )
        request.POST.add( 'milestone_id', str(m.id) )
        request.POST.add( 'tags', rmtag )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['delprjtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted tags' in u.logs[-1].log and \
                           'from milestone' in u.logs[-1].log
        )

        m = projcomp.get_milestone( m.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in m.tags ]),
                      'Mismatch while deleting project milestone tags'
                    )

        # Add tags to version
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjtags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda t : tagcomp.is_tagnamevalid( t ),
                                tagnames ) + \
                        [ t.tagname for t in v.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(v.project.id) )
        request.POST.add( 'version_id', str(v.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['addprjtags'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added tags' in u.logs[-1].log and \
                           'to version' in u.logs[-1].log
        )

        v = projcomp.get_version( v.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in v.tags ]),
                      'Mismatch while creating project version tags'
                    )

        # Delete tags from version
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjtags' )
        rmtag     = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(v.project.id) )
        request.POST.add( 'version_id', str(v.id) )
        request.POST.add( 'tags', rmtag )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['delprjtags'] )
        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted tags' in u.logs[-1].log and \
                           'from version' in u.logs[-1].log
        )
        v = projcomp.get_version( v.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in v.tags ]),
                      'Mismatch while deleting project version tags'
                    )

        # Add tags to project
        p         = choice(projects)
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjtags' )
        tagnames  = list(set([ choice( taglist) for i in range(10) ]))
        reftags   = list(set(
                        filter( lambda t : tagcomp.is_tagnamevalid( t ),
                                tagnames ) + \
                        [ t.tagname for t in p.tags ]
                    ))
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'tags', ', '.join([ tagname for tagname in tagnames ]) )
        vf.process( request, c )
        p = projcomp.get_project( p.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in p.tags ]),
                      'Mismatch while creating project tags'
                    )

        # Delete tags to project
        request.params.clearfields()
        request.POST.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjtags' )
        rmtag     = choice( reftags )
        reftags.remove( rmtag )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'tags', rmtag )
        vf.process( request, c )
        p = projcomp.get_project( p.id )
        assert_equal( sorted(reftags),
                      sorted([ t.tagname for t in p.tags ]),
                      'Mismatch while deleting project tags'
                    )

    def test_P_projectattachs( self ) :
        """Testing FormProjectAttachs with valid and invalid input"""
        log.info( "Testing FormProjectAttachs with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        projects        = projcomp.get_project()
        u               = choice( users )
        p               = choice( projects )

        # Clean attachments in project
        [ projcomp.remove_attach( p, attach ) for attach in p.attachments ]

        # Add attachments
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjattachs' )
        user    = choice( users )
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        attachmentfiles = []
        for i in range(randint(0,3)) :
            attach          = FileObject()
            attachfile      = choice( attachfiles )
            attach.filename = os.path.basename( attachfile )
            attach.file     = open( attachfile, 'r' )
            request.POST.add( 'attachfile', attach  )
            attachmentfiles.append( attach )
        defer = choice([ True, False ])
        vf.process( request, c, user=user.username, defer=defer,
                    formnames=['addprjattachs'] )

        if attachmentfiles :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'uploaded attachment' in u.logs[-1].log
            )

        p = projcomp.get_project( p.projectname )
        assert_equal( sorted([ a.filename for a in p.attachments ]),
                      sorted([ attach.filename for attach in attachmentfiles ]),
                      'Mismatch in adding project attachment'
                    )

        # Remove attachments
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjattachs' )
        request.POST.clearfields()
        request.POST.add( 'user_id', str(u.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'attach_id', str(a.id) ) for a in p.attachments ]
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['delprjattachs'] )

        if p.attachments :
            self._validate_defer(
                    c.authuser, defer, c,
                    lambda u : 'deleted attachment' in u.logs[-1].log
            )

        p = projcomp.get_project( p.id )
        assert_false( p.attachments, 'Mismatch in removing project attachment' )

    def test_Q_projectpermission( self ) :
        """Testing FormProjectPermission with valid and invalid inputs"""
        log.info( "Testing FormProjectPermission with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        permgroups      = userscomp.get_permgroup()
        projects        = projcomp.get_project()
        user            = choice( users )
        p               = choice( projects )

        # Remove all the project permission
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjperms' )
        projperms       = projcomp.get_projectperm()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'project_perm_id', str(pp.id) ) for pp in projperms ]
        vf.process( request, c )
        assert_false( projcomp.get_projectperm(),
                      'Finding project permission entries even after removing all'
                    )

        # Add project permissions
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjperms' )
        p           = choice( projects )
        projusers   = list(set([ choice(users) for i in range(randint(0, len(users))) ]))
        userppgs    = dict([ ( u.username,
                               list(set([ choice(permgroups).perm_group
                                          for i in range(randint(0,len(permgroups))) ])),
                             ) for u in projusers ])
        for username in userppgs :
            request.POST.clearfields()
            request.POST.add( 'user_id', str(user.id) )
            request.POST.add( 'project_id', str(p.id) )
            request.POST.add( 'projuser', username )
            [ request.POST.add( 'perm_group', perm_group )
              for perm_group in userppgs[username] ]
            vf.process( request, c )
        p = projcomp.get_project( p.projectname )
        dbuserppgs  = {}
        for pp in p.projectperms :
            dbuserppgs.setdefault( pp.user.username, [] ).append( pp.permgroup.perm_group )
        for username in dbuserppgs :
            assert_equal( sorted(dbuserppgs[username]),
                          sorted(userppgs[username]),
                          'Mismatch in creating project permissions'
                        )

    def test_R_projectteampermission( self ) :
        """Testing FormProjectTeamPermissions with valid and invalid inputs"""
        log.info( "Testing FormProjectTeamPermissions with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        permgroups      = userscomp.projpgroups
        projects        = projcomp.get_project()
        user            = choice( users )
        p               = choice( projects )

        # Remove all the project team permission
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delteamperms' )
        projteamperms   = projcomp.get_projectteamperm()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'projectteam_perm_id', str(ptp.id) ) for ptp in projteamperms ]
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['delteamperms'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted permission' in u.logs[-1].log
        )

        assert_false( projcomp.get_projectteamperm(),
                      'Finding project team permission entries even after removing all'
                    )

        # Add project permissions
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addteamperms' )
        p = choice( projects )
        teamtypes   = projcomp.get_teamtype()
        teampgs     = dict([ ( t.team_type,
                               list(set([ choice(permgroups).perm_group
                                          for i in range(randint(0,len(permgroups))) ])),
                             ) for t in teamtypes ])
        defer = choice([ True, False ])
        for team_type in teampgs :
            request.POST.clearfields()
            request.POST.add( 'user_id', str(user.id) )
            request.POST.add( 'project_id', str(p.id) )
            request.POST.add( 'team_type', team_type )
            [ request.POST.add( 'perm_group', perm_group )
              for perm_group in teampgs[team_type] ]
            vf.process( request, c, defer=defer, formnames=['addteamperms'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added permissions' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        dbteampgs   = {}
        for ptp in p.projteamperms :
            dbteampgs.setdefault( ptp.teamtype.team_type, [] ).append( ptp.permgroup.perm_group )
        for team_type in dbteampgs  :
            assert_equal( sorted(dbteampgs[team_type]),
                          sorted(teampgs[team_type]),
                          'Mismatch in creating project team permissions'
                        )

    def test_S_projectteam( self ) :
        """Testing FormProjectTeam with valid and invalid inputs"""
        log.info( "Testing FormProjectTeam with valid and invalid input ..." )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        projects        = projcomp.get_project()
        teams           = projcomp.get_teamtype()
        user            = choice( users )
        p               = choice( projects )

        # Remove all the project team
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'delprjteam' )
        projteams       = projcomp.get_projectteam()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        [ request.POST.add( 'project_team_id', str(pt.id) ) for pt in projteams ]
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['delprjteam'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'deleted users' in u.logs[-1].log
        )

        assert_false( projcomp.get_projectteam(),
                      'Finding project team entries even after removing all'
                    )

        # Add project team
        c.rclose = h.ZResp()
        request.params.clearfields()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'addprjteam' )
        p           = choice( projects )
        teamtypes   = projcomp.get_teamtype()
        pteamusers  = dict([ ( t.team_type,
                               list(set([ choice(users).username
                                          for i in range(randint(1,len(users))) ])),
                             ) for t in teamtypes ])
        defer = choice([ True, False ])
        for team_type in pteamusers :
            request.POST.clearfields()
            request.POST.add( 'user_id', str(user.id) )
            request.POST.add( 'project_id', str(p.id) )
            request.POST.add( 'team_type', team_type )
            [ request.POST.add( 'projuser', username )
              for username in pteamusers[team_type] ]
            vf.process( request, c, defer=defer, formnames=['addprjteam'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added users' in u.logs[-1].log
        )

        p = projcomp.get_project( p.projectname )
        dbpteamusers = {}
        for pt in p.team :
            dbpteamusers.setdefault( pt.teamtype.team_type, [] ).append( pt.user.username )
        for team_type in dbpteamusers :
            assert_equal( sorted(dbpteamusers[team_type]),
                          sorted(pteamusers[team_type]),
                          'Mismatch in creating project team'
                        )

    def test_T_projectfavorite( self ) :
        """Testing FormProjectFavorite with valid and invalid inputs"""
        log.info( "Testing FormProjectFavorite with valid and invalid inputs" )
        request     = RequestObject()
        c           = ContextObject()
        vf          = VForm( compmgr )
        config['c'] = c
        c.authuser  = g_byuser

        users           = userscomp.get_user()
        projects        = projcomp.get_project()
        user            = choice( users )
        p               = choice( projects )

        projcomp.delfavorites( p, p.favoriteof, byuser=g_byuser )

        # Add favorite user
        c.rclose = h.ZResp()
        request.params.add( 'form', 'submit' )
        request.params.add( 'formname', 'projfav' )
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'addfavuser', user.username )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['projfav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'added project as favorite' in u.logs[-1].log
        )

        assert_equal( projcomp.get_project( p.id ).favoriteof, [ user ],
                      'Mismatch in adding favorite user for project'
                    )

        # Del favorite user
        c.rclose = h.ZResp()
        request.POST.clearfields()
        request.POST.add( 'user_id', str(user.id) )
        request.POST.add( 'project_id', str(p.id) )
        request.POST.add( 'delfavuser', user.username )
        defer = choice([ True, False ])
        vf.process( request, c, defer=defer, formnames=['projfav'] )

        self._validate_defer(
                c.authuser, defer, c,
                lambda u : 'removed project from favorite' in u.logs[-1].log
        )

        assert_equal( projcomp.get_project( p.id ).favoriteof, [],
                      'Mismatch in deleting favorite user for project'
                    )
