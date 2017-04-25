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

import pylons.test
from   pylons                       import config
from   sqlalchemy                   import engine_from_config
from   nose.tools                   import assert_equal, assert_raises, \
                                           assert_false, assert_true
from   zwiki.zwparser               import ZWParser

from   zeta.auth.perm               import permissions
from   zeta.tests                   import *
from   zeta.model                   import meta
from   zeta.model                   import init_model, create_models, delete_models
from   zeta.tests.model.generate    import gen_projects, future_duedate
from   zeta.tests.model.populate    import pop_permissions, pop_user, pop_licenses
import zeta.lib.helpers             as h
import zeta.lib.cache               as cachemod 
from   zeta.lib.constants           import ACCOUNTS_ACTIONS, ATTACH_DIR, \
                                           LEN_TAGNAME, LEN_SUMMARY
from   zeta.lib.error               import ZetaTagError, ZetaAttachError, \
                                           ZetaProjectError
from   zeta.comp.attach             import AttachComponent
from   zeta.comp.tag                import TagComponent
from   zeta.comp.license            import LicenseComponent
from   zeta.comp.project            import ProjectComponent
from   zeta.tests.tlib              import *

config          = pylons.test.pylonsapp.config
log             = logging.getLogger(__name__)
seed            = None
g_byuser        = u'admin'
no_of_users     = 20
no_of_relations = 3
no_of_tags      = 3
no_of_attachs   = 1
no_of_projects  = 10

compmgr     = None
liccomp     = None
userscomp   = None
attachcomp  = None
projcomp    = None
projdata    = None
zwparser    = None
cachemgr    = None
cachedir    = '/tmp/testcache'


def setUpModule() :
    """Create database and tables."""
    global compmgr, liccomp, userscomp, attachcomp, projcomp, projdata, \
           zwparser, seed, cachemgr

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
    projcomp   = ProjectComponent( compmgr )
    # Populate DataBase with sample entries
    print "   Populating permissions ..."
    pop_permissions( seed=seed )
    print "   Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
                ( no_of_users, no_of_relations )
    pop_user( no_of_users, no_of_relations, seed=seed )
    print "   Populating licenses ( no_of_tags=%s, no_of_attachs=%s ) ..." % \
                ( no_of_tags, no_of_attachs )
    pop_licenses( no_of_tags, no_of_attachs, seed=seed )
    # Collect the expected database objects.
    perm_groups = userscomp.get_permgroup()
    users       = userscomp.get_user()
    teamtypes   = projcomp.get_teamtype()
    licenses    = liccomp.get_license()
    projdata    = gen_projects( userscomp.usernames, userscomp.perm_groups,
                                projcomp.teams, licenses, no_of_projects,
                                no_of_tags, no_of_attachs, seed=seed )
    print ( "   no_of_users=%s, no_of_relations=%s, no_of_tags=%s, " + \
            "no_of_attach=%s, no_of_projects=%s"  ) % \
          ( no_of_users, no_of_relations, no_of_tags, no_of_attachs,
            no_of_projects )

    zwparser = ZWParser( lex_optimize=True, yacc_debug=True,
                         yacc_optimize=False )

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


class TestProject( object ) :

    def _validate_proj( self, projdata, projects ) :
        """`projdata` and `projects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database'
                    )
        for i in range(len(projects)) :
            p            = projects[i]
            proj         = projdata[p.projectname]
            projfields   = [ proj['projectname'], proj['summary'],
                             proj['admin_email'], proj['license'],
                             userscomp.get_user( proj['admin'] ),
                             proj['description'] ]
            dbprojfields = [ p.projectname, p.summary, p.admin_email, p.license,
                             p.admin, p.project_info.description ]
            assert_equal( projfields, dbprojfields,
                          'Mismatch in the project detail' )

    def _validate_projconfig( self, projdata, projects ) :
        """validate the project configurations.
        `projdata` and `projects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database' )
        for i in range(len(projects)) :
            p            = projects[i]
            proj         = projdata[p.projectname]
            projfields   = [ os.path.basename( proj['logofile'][0] ),
                             userscomp.get_user( proj['logofile'][1] ),
                             os.path.basename( proj['iconfile'][0] ),
                             userscomp.get_user( proj['iconfile'][1] ),
                             proj['disabled'], proj['exposed'],
                             proj['license'], proj['admin'] ]
            dbprojfields = [ p.logofile.filename, p.logofile.uploader,
                             p.iconfile.filename, p.iconfile.uploader,
                             p.disabled, p.exposed, p.license, p.admin ]
            assert_equal( projfields, dbprojfields,
                          'Mismatch in project config detail' )

    def _validate_mlists( self, projdata, projects ) :
        """validate the project mailing lists.
        `projdata` and `projects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database' )
        for i in range(len(projects)) :
            p            = projects[i]
            proj         = projdata[p.projectname]
            assert_equal( sorted( proj['mailing_list'] ),
                          sorted([ m.mailing_list for m in p.mailinglists ]),
                          'Mismatch in project mailing list'
                        )

    def _validate_irc( self, projdata, projects ) :
        """validate the project ircchannel lists.
        `projdata` and `projects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database' )
        for i in range(len(projects)) :
            p            = projects[i]
            proj         = projdata[p.projectname]
            assert_equal( sorted( proj['ircchannel'] ),
                          sorted([ i.ircchannel for i in p.ircchannels ]),
                          'Mismatch in project ircchannel list'
                        )

    def _validate_component( self, compdata, components ) :
        """validate the project components.
        `compdata` and `components` are sorted based on the component object"""
        assert_equal( len(compdata), len(components),
                      'Mismatch with the number of components in the database' )
        for i in range(len(components)) :
            c         = components[i]
            comp      = compdata[c.componentname] 
            compdet   = [ comp['id'], comp['componentname'],
                          comp['description'],
                          userscomp.get_user( comp['owner'] ) ]
            dbcompdet = [ c, c.componentname, c.description, c.owner ]
            assert_equal( compdet, dbcompdet, 'Mismatch in project component' )

    def _validate_components( self, projdata, projects ) :
        """validate the project components.
        `projdata` and `projects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database' )
        for i in range(len(projects)) :
            p            = projects[i]
            proj         = projdata[p.projectname]
            compdata     = proj['components']
            self._validate_component(
                    compdata,
                    sorted( projcomp.get_component( project=p ) )
            )

    def _validate_milestone( self, mstndata, milestones ) :
        """validate the project milestone.
        `mstndata` and `components` are sorted based on the milestone object"""
        assert_equal( len(mstndata), len(milestones),
                      'Mismatch with the number of milestones in the database' )
        for i in range(len(milestones)) :
            m         = milestones[i]
            mstn      = mstndata[m.milestone_name]
            mstndet   = [ mstn['id'], mstn['milestone_name'],
                          mstn['description'], mstn['due_date'] ]
            dbmstndet = [ m, m.milestone_name, m.description, m.due_date ]
            assert_equal( mstndet, dbmstndet,
                          'Mismatch in project milestone details' )
            mstncrm   = [ mstn['closing_remark'] ]
            mstncrm.append([ False, True ][ mstn['status'] == 'completed' ])
            mstncrm.append([ False, True ][ mstn['status'] == 'cancelled' ])
            dbmstncrm = [ m.closing_remark or '', m.completed, m.cancelled ]
            assert_equal( mstncrm, dbmstncrm,
                          'Mismatch in project milestone closing remarks' )

    def _validate_milestones( self, projdata, projects ) :
        """validate the project milestones.
        `projdata` and `projtects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database' )
        for i in range(len(projects)) :
            p           = projects[i]
            proj        = projdata[p.projectname]
            mstndata    = proj['milestones']
            self._validate_milestone(
                mstndata,
                sorted( projcomp.get_milestone( project=p ) )
            )
            
    def _validate_version( self, verdata, versions) :
        """validate the project versions.
        `verdata` and `versions` are sorted based on the Version object"""
        assert_equal( len(verdata), len(versions),
                      'Mismatch with the number of versions in the database' )
        for i in range(len(versions)) :
            v        = versions[i]
            ver      = verdata[v.version_name]
            verdet   = [ ver['id'], ver['version_name'], ver['description'] ]
            dbverdet = [ v, v.version_name, v.description ]
            assert_equal( verdet, dbverdet,
                          'Mismatch in project version' )

    def _validate_versions( self, projdata, projects ) :
        """validate the project versions.
        `projdata` and `projects` are sorted based on the project object"""
        assert_equal( len(projdata), len(projects),
                      'Mismatch with the number of projects in the database' )
        for i in range(len(projects)) :
            p           = projects[i]
            proj        = projdata[p.projectname]
            verdata     = proj['versions']
            self._validate_version(
                verdata,
                sorted( projcomp.get_version( project=p ) )
            )

    def _testwiki_execute( self, type, model, attr, ref='' ) :
        wikitext    = getattr( model, attr, '' )

        # Characterize the generated wikitext set the wikiproperties
        wikiprops = {}
        wikitext  = ( "@ %s " % wikiprops ) + '\n' + wikitext

        # Prepare the reference.
        ref         = ref or wikitext
        ref         = zwparser.wiki_preprocess( ref )
        props, ref  = zwparser._wiki_properties( ref )

        # Test by comparing the dumps
        try :
            tu      = zwparser.parse( wikitext, debuglevel=0 )
            result  = tu.dump()[:-1]
        except :
            tu     = zwparser.parse( wikitext, debuglevel=2 )
            result = tu.dump()[:-1]
        if result != ref :
            print ''.join(diff.ndiff( result.splitlines(1), ref.splitlines(1) ))
        assert result == ref, type + '... testcount : dump mismatch'

        # Test by comparing the html
        tu  = zwparser.parse( getattr( model, attr, '' ), debuglevel=0 )
        ref = tu.tohtml()
        if attr == 'closing_remark' :
            result = model.crtranslate()
            assert result == ref, type + '... testcount html mismatch'
        else :
            result = model.translate()
            assert result == ref, type + '... testcount html mismatch'

        # Test by translating to html
        #tu   = zwparser.parse( wikitext, debuglevel=0 )
        #html = tu.tohtml()
        #et.fromstring( html ) 

    def test_1_createprojects( self ) :
        """Testing project creation"""
        log.info( "Testing project creation ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        # Test Project Creation
        for projectname in projdata :
            proj       = projdata[projectname]
            projdet    = [ proj['id'], proj['projectname'], proj['summary'],
                           proj['admin_email'], proj['license'], proj['admin']
                         ]
            projidet   = [ proj['description'] ]
            proj['id'] = projcomp.create_project( projdet, projidet )
        self._validate_proj( projdata, sorted( projcomp.get_project() ))

    def test_2_updateprojects( self ) :
        """Testing project updation"""
        log.info( "Testing project updation ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser
        
        users       = userscomp.get_user()
        licenses    = liccomp.get_license()
        updtfields  = {
                         'projectname'   : u'updateprojectname',
                         'summary'       : u'updateprojectsummary',
                         'admin_email'   : u'updateadmin@email.com',
                         'license'       : choice(licenses), 
                         'admin'         : choice(users),
                         'description'   : u'updateprojectdescription' 
                      }
        users       = userscomp.get_user()
        count       = 1
        # Gotcha : When admin is updated, the generate data is not updated.
        for projectname in projdata :
            proj  = projdata[projectname]
            updtfields['projectname'] = u'updateprojectname'+str(count)
            count += 1
            if choice([ True, False ]) :
                continue
            key               = choice( updtfields.keys() )
            if key == 'projectname' :
                proj          = projdata.pop( projectname )
                value         = updtfields[key] 
                proj[key]     = value
                projdata[value] = proj
            else :
                proj[key] = updtfields[key]
            projdet    = [ proj['id'], proj['projectname'], proj['summary'],
                           proj['admin_email'], proj['license'], proj['admin']
                         ]
            projidet   = [ proj['description'] ]
            proj['id'] = projcomp.create_project( projdet, projidet, update=True )
        self._validate_proj( projdata, sorted( projcomp.get_project() ))

    def test_3_configproject( self ) :
        """Testing project configuration method"""
        log.info( "Testing project configuration method ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        licenses = liccomp.get_license()
        for projectname in projdata :
            proj      = projdata[projectname]
            projusers = [ userscomp.get_user(u) for u in proj['projusers'] ]
            p         = proj['id']
            p         = choice([ p.id, p.projectname, p ])
            logofile, luploader = proj['logofile']
            logo = attachcomp.create_attach( os.path.basename( logofile ),
                                             fdfile=open( logofile, 'r' ),
                                             uploader=luploader
                   )
            iconfile, iuploader = proj['iconfile']
            icon = attachcomp.create_attach( os.path.basename( iconfile ),
                                             fdfile=open( iconfile, 'r' ),
                                             uploader=iuploader
                   )
            r    = randint(0,3)
            proj['license'] = choice( licenses )
            proj['admin']   = choice( projusers )
            if r == 0 :
                projcomp.config_project( p, logo=logo, uploader=luploader )
                projcomp.config_project( p, icon=icon, uploader=iuploader )
                projcomp.config_project( p, disable=proj['disabled'] )
                projcomp.config_project( p, expose=proj['exposed'] )
                projcomp.config_project( p, license=proj['license'] )
                projcomp.config_project( p, admin=proj['admin'] )
            elif r == 1 :
                proj['logofile'][1] = iuploader
                projcomp.config_project( p, icon=icon, logo=logo,
                                         uploader=iuploader )
                projcomp.config_project( p, disable=proj['disabled'] )
                projcomp.config_project( p, expose=proj['exposed'] )
                projcomp.config_project( p, license=proj['license'] )
                projcomp.config_project( p, admin=proj['admin'] )
            elif r == 2 :
                proj['logofile'][1] = iuploader
                projcomp.config_project( p, disable=proj['disabled'],
                                        icon=icon, logo=logo,
                                        uploader=iuploader
                )
                projcomp.config_project( p, expose=proj['exposed'] )
                projcomp.config_project( p, license=proj['license'] )
                projcomp.config_project( p, admin=proj['admin'] )
            elif r == 3 :
                proj['logofile'][1] = iuploader
                projcomp.config_project( p, disable=proj['disabled'],
                                         expose=proj['exposed'],
                                         license=proj['license'],
                                         icon=icon, logo=logo,
                                         uploader=iuploader )
                projcomp.config_project( p, admin=proj['admin'] )
            elif r == 4 :
                proj['logofile'][1] = iuploader
                projcomp.config_project( p, disable=proj['disabled'],
                                         expose=proj['exposed'],
                                         license=proj['license'],
                                         admin=proj['admin'],
                                         icon=icon, logo=logo,
                                         uploader=iuploader )
        self._validate_proj( projdata, sorted( projcomp.get_project() ))
        self._validate_projconfig( projdata, sorted( projcomp.get_project() ))

    def test_4_getproject( self ) :
        """Testing get_project() method"""
        log.info( "Testing get_project() method ..." )
        dbprojects = projcomp.get_project()
        projs      = []
        for projectname in projdata :
            proj = projdata[projectname]
            p    = proj['id']  
            projs.append( projcomp.get_project( choice([ p, p.id, p.projectname ])))
        assert_equal( sorted(dbprojects), sorted(projs),
                      'Mismatch in get_project() method' )

        # Test get_projectlist() method
        dbprojects = projcomp.get_project( attrload=['admin', 'project_info'] )
        projs      = []
        for projectname in projdata :
            proj = projdata[projectname]
            p    = proj['id']  
            projs.append( projcomp.get_project( choice([ p, p.id, p.projectname ])))
        assert_equal( sorted(dbprojects), sorted(projs),
                      'Mismatch in get_projectlist() method' )

    def test_5_getteamtype( self ) :
        """Testing get_teamtype() method"""
        log.info( "Testing get_teamtype() method ..." )
        teamtypes   = config['zeta.projteamtypes']
        dbteamtypes = [ t.team_type for t in projcomp.get_teamtype() ]
        assert_equal( sorted(teamtypes),
                      sorted(dbteamtypes),
                      'Mismatch in project team types stored in database'
                    )

    def test_6_setmailinglist( self ) :
        """Testing mailinglist configuration for projects"""
        log.info( "Testing mailinglist configuration for projects ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        newlist = [ u'bashdev@googlegroups.com', u'bash@googlegroups.com',
                    u'bash.bugs@googlegroups.com' ]
        for projectname in projdata :
            proj = projdata[projectname]
            p    = proj['id']
            projcomp.set_mailinglists( choice([ p.id, p.projectname, p ]),
                                       proj['mailing_list'],
                                       append=choice([True, False ]) )
        for projectname in projdata :
            if choice([ True, False ]) :
                continue
            proj   = projdata[projectname]
            p      = proj['id']
            mlist  = choice([ newlist, newlist, [], None ])
            append = choice([ True, False ])
            if append == False :
                proj['mailing_list'] = []
            if mlist :
                proj['mailing_list'] += mlist
            projcomp.set_mailinglists( choice([ p.id, p.projectname, p ]),
                                       mlist, append=append )
        self._validate_mlists( projdata, sorted( projcomp.get_project() ))

    def test_7_setircchannels( self ) :
        """Testing ircchannels configuration for projects"""
        log.info( "Testing ircchannels configuration for projects ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        newirc = [ u'pydev#netirc.com', u'pyuser#netirc.com', ]
        for projectname in projdata :
            proj = projdata[projectname]
            p    = proj['id']
            projcomp.set_ircchannels( choice([ p.id, p.projectname, p ]),
                                      proj['ircchannel'],
                                      append=choice([True, False ]) )
        for projectname in projdata :
            if choice([ True, False ]) :
                continue
            p      = proj['id']
            irc    = choice([ newirc, newirc, [], None ])
            append = choice([ True, False ])
            if append == False :
                proj['ircchannel'] = []
            if irc :
                proj['ircchannel'] += irc
            projcomp.set_ircchannels( choice([ p.id, p.projectname, p ]),
                                      irc, append=append )
        self._validate_irc( projdata, sorted( projcomp.get_project() ))

    def test_8_component( self ) :
        """Testing project component creation and removal methods"""
        log.info( "Testing project component creation and removal methods..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for projectname in projdata :
            proj        = projdata[projectname]
            projusers   = [ userscomp.get_user(u) for u in proj['projusers'] ]
            compdata    = proj['components']
            p           = proj['id']
            updtdetails = {
                            'componentname'    : u'updtcompname',
                            'description'       : u'updatedescription',
                            'owner'             : choice(projusers)
                          }
            # Create components
            for cn in compdata :
                comp       = compdata[cn]
                compdetail = [ comp['id'], comp['componentname'],
                               comp['description'], comp['owner'] ]
                comp['id'] = projcomp.create_component( p, compdetail )
            # Update components
            ucompdata = {}
            for cn in compdata :
                comp       = compdata[cn]
                key        = choice( updtdetails.keys() )
                comp[key]  = updtdetails[key]
                compdetail = [ comp['id'], comp['componentname'],
                               comp['description'], comp['owner'] ]
                comp['id'] = projcomp.create_component( p, compdetail, update=True )
                ucompdata[comp['componentname']] = comp
                if key == 'componentname' :
                    updtdetails.pop( 'componentname' )
            proj['components'] = ucompdata
            compdata           = proj['components']
            # Remove components
            rmcomp = [ cn for cn in compdata if choice([ True, False, False ]) ]
            [ ( projcomp.remove_component( p, compdata[cn]['id'] ),
                compdata.pop( cn ), 
              ) for cn in rmcomp ]
        self._validate_components( projdata, sorted( projcomp.get_project() ))

    def test_9_getcomponent( self ) :
        """Testing get_component() method"""
        log.info( "Testing get_component() method ..." )
        allcomps  = []
        for pn in projdata :
            proj     = projdata[pn]
            p        = proj['id']
            p        = choice([ p.id, p.projectname, p ])
            compdata = proj['components']
            comps    = [ compdata[cn]['id'] for cn in compdata ]
            dbcomps  = [ projcomp.get_component(
                                choice([ compdata[cn]['id'].comp_number,
                                         compdata[cn]['id'] ]),
                                p
                         ) for cn in compdata ]
            assert_equal( sorted( comps ), sorted( dbcomps ),
                          'Mismatch in getting individual project-component' )
            dbcomps  = [ projcomp.get_component(
                                choice([ compdata[cn]['id'].id,
                                         compdata[cn]['id'] ])
                         ) for cn in compdata ]
            assert_equal( sorted( comps ), sorted( dbcomps ),
                          'Mismatch in getting individual component' )
            dbcomps  = projcomp.get_component( project=p ) 
            assert_equal( sorted( comps ), sorted( dbcomps ),
                          'Mismatch in getting components by project'
                        )
            allcomps.extend( comps )
        dballcomps = projcomp.get_component()
        assert_equal( sorted( dballcomps ), sorted( allcomps ),
                      'Mismatch in getting all the components' )

    def test_A_milestone( self ) :
        """Testing project milestone creation, updation and removal methods"""
        log.info( "Testing project milestone creation, updation and removal methods ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for pn in projdata :
            proj        = projdata[pn]
            projusers   = [ userscomp.get_user(u) for u in proj['projusers'] ]
            mstndata    = proj['milestones']
            p           = proj['id']
            updtdetails = {
                            'milestone_name'    : u'updtmstnname',
                            'description'       : u'updatedescription',
                            'due_date'          : future_duedate(
                                                    *dt.datetime.utcnow().timetuple()
                                                  ),
                          }
            # Create milestones
            for mn in mstndata :
                mstn       = mstndata[mn]
                mstndetail = ( mstn['id'], mstn['milestone_name'],
                               mstn['description'], mstn['due_date'] )
                mstn['id']    = projcomp.create_milestone( p, mstndetail )
            # Update milestones
            umstndata = {}
            for mn in mstndata :
                mstn       = mstndata[mn]
                key        = choice( updtdetails.keys() )
                mstn[key]  = updtdetails[key]
                mstndetail = ( mstn['id'], mstn['milestone_name'],
                               mstn['description'], mstn['due_date'] )
                mstn['id'] = projcomp.create_milestone( p, mstndetail, update=True )
                umstndata[mstn['milestone_name']] = mstn
                if key == 'milestone_name' :
                    updtdetails.pop( 'milestone_name' )
            proj['milestones'] = umstndata
            mstndata           = proj['milestones']

            # Close milestones
            [ projcomp.close_milestone(
                choice([ mstndata[mn]['id'], mstndata[mn]['id'].id ]),
                mstndata[mn]['closing_remark'], mstndata[mn]['status']
              ) for mn in mstndata if mstndata[mn]['status'] ]

            # Re-open milestones
            closed = [ mn for mn in mstndata if mstndata[mn]['status'] ]
            if closed :
                mn = closed.pop(0)
                status = mstndata[mn]['status']
                cr = mstndata[mn]['closing_remark']
                m = mstndata[mn]['id']

                projcomp.open_milestone( choice([ m, m.id ]), u"" )
                m = projcomp.get_milestone(m.id)
                assert_equal( [ m.cancelled, m.completed, m.closing_remark ],
                              [ False, False, ""],
                              "Mismatch while re-opening a milestone"
                            )
                projcomp.close_milestone( m, cr, status )

            # Remove milestones
            rmmstn = [ mn for mn in mstndata if choice([ True, False, False ]) ]
            [ ( projcomp.remove_milestone( p, mstndata[mn]['id'] ),
                mstndata.pop( mn ),
              ) for mn in rmmstn ]

        self._validate_milestones( projdata, sorted( projcomp.get_project() ))

    def test_B_getmilestone( self ) :
        """Testing get_milestone() method"""
        log.info( "Testing get_milestone() method ..." )
        allmstns  = []
        for pn in projdata :
            proj     = projdata[pn]
            p        = proj['id']
            p        = choice([ p.id, p.projectname, p ])
            mstndata = proj['milestones']
            mstns    = [ mstndata[mn]['id'] for mn in mstndata ]
            dbmstns  = [ projcomp.get_milestone(
                                choice([ mstndata[mn]['id'].mstn_number,
                                         mstndata[mn]['id'] ]),
                                p
                         ) for mn in mstndata ]
            assert_equal( sorted( mstns ), sorted( dbmstns ),
                          'Mismatch in getting individual project-milestone' )
            dbmstns  = [ projcomp.get_milestone(
                                choice([ mstndata[mn]['id'].id, mstndata[mn]['id'] ])
                         ) for mn in mstndata ]
            assert_equal( sorted( mstns ), sorted( dbmstns ),
                          'Mismatch in getting individual milestone' )
            dbmstns  = projcomp.get_milestone( project=p ) 
            assert_equal( sorted( mstns ), sorted( dbmstns ),
                          'Mismatch in getting milestones by project'
                        )
            allmstns.extend( mstns )
        dballmstns = projcomp.get_milestone()
        assert_equal( sorted( dballmstns ), sorted( allmstns ),
                      'Mismatch in getting all the milestones' )

    def test_C_version( self ) :
        """Testing project version creation and removal methods"""
        log.info( "Testing project version creation and removal methods ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for pn in projdata :
            proj        = projdata[pn]
            verdata     = proj['versions']
            p           = proj['id']
            updtdetails = { 'version_name'  : u'updtvername',
                            'description'   : u'updatedescription',
                          }
            # Create versions
            for vn in verdata :
                ver       = verdata[vn]
                verdetail = ( ver['id'], ver['version_name'], ver['description'] )
                ver['id'] = projcomp.create_version( p, verdetail )
            # Update versions
            uverdata = {}
            for vn in verdata :
                ver       = verdata[vn]
                key       = choice( updtdetails.keys() )
                ver[key]  = updtdetails[key]
                verdetail = ( ver['id'], ver['version_name'], ver['description'] )
                ver['id'] = projcomp.create_version( p, verdetail, update=True )
                uverdata[ver['version_name']] = ver
                if key == 'version_name' :
                    updtdetails.pop( 'version_name' )
            proj['versions'] = uverdata
            verdata          = proj['versions']
            # Remove versions
            rmver = [ vn for vn in verdata if choice([ True, False, False ]) ]
            [ ( projcomp.remove_version( p, verdata[vn]['id'] ),
                verdata.pop( vn ), 
              ) for vn in rmver ]
        self._validate_versions( projdata, sorted( projcomp.get_project() ))

    def test_D_getversion( self ) :
        """Testing get_version() method"""
        log.info( "Testing get_version() method ..." )
        allvers  = []
        for pn in projdata :
            proj     = projdata[pn]
            p        = proj['id']
            p        = choice([ p.id, p.projectname, p ])
            verdata  = proj['versions']
            vers     = [ verdata[vn]['id'] for vn in verdata ]
            dbvers   = [ projcomp.get_version(
                                choice([ verdata[vn]['id'].ver_number,
                                         verdata[vn]['id'] ]),
                                p
                         ) for vn in verdata ]
            assert_equal( sorted( vers ), sorted( dbvers ),
                          'Mismatch in getting individual project-version' )
            dbvers   = [ projcomp.get_version(
                                choice([ verdata[vn]['id'].id,
                                         verdata[vn]['id'] ])
                         ) for vn in verdata ]
            assert_equal( sorted( vers ), sorted( dbvers ),
                          'Mismatch in getting individual version' )
            dbvers   = projcomp.get_version( project=p ) 
            assert_equal( sorted( vers ), sorted( dbvers ),
                          'Mismatch in getting versions by project'
                        )
            allvers.extend( vers )
        dballvers  = projcomp.get_version()
        assert_equal( sorted( dballvers ), sorted( allvers ),
                      'Mismatch in getting all the version' )

    def test_E_projectteam( self ) :
        """Testing project team methods"""
        log.info( "Testing project team methods ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        teams = []
        # Create users in project team
        for pn in projdata :
            proj = projdata[pn]
            p    = proj['id']
            p    = choice([ p, p.id, p.projectname ])
            for team_type in proj['projectteams'] :
                addusers = proj['projectteams'][team_type]
                for pt in projcomp.add_project_user(p, team_type, addusers) :
                    teams.append([ p, pt.user, team_type, pt ])

        pteams   = projcomp.get_projectteam()
        [ projcomp.approve_project_user( projectteam=pt ) for pt in pteams ]

        # Remove users from project team
        rmteams  = [ pt for pt in pteams if choice([ True, False, False ]) ]
        [ teams.remove( team )
                for pt in rmteams for team in teams if pt == team[3] ]

        # update the generated data.
        for pt in rmteams :
            for pn in projdata :
                proj = projdata[pn]
                if pn != pt.project.projectname :
                    continue
                proj['projectteams'][pt.teamtype.team_type].remove( pt.user.username )
                pt.user.username in proj['projusers'] and \
                        proj['projusers'].remove( pt.user.username )
                pt.user.username in proj['projectperms'] and \
                        proj['projectperms'].pop( pt.user.username )

        if choice([ True, False ]) :
            [ projcomp.remove_project_users( pt ) for pt in rmteams ]
        else :
            projcomp.remove_project_users( rmteams )
        assert_equal( sorted([ team[3] for team in teams ]),
                      sorted( projcomp.get_projectteam() ),
                      'Mismatch in created teams'
                    )

    def test_F_getprojectteam( self ) :
        """Testing get_projectteam() method"""
        log.info( "Testing get_projectteam() method ..." )
        dballteams = projcomp.get_projectteam()
        # Get using project
        allteams   = []
        [ allteams.extend( projcomp.get_projectteam( project=projdata[pn]['id'] ))
                for pn in projdata ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting project teams via project reference'
                    )
        # Get using user
        allteams   = []
        [ allteams.extend( projcomp.get_projectteam( user=u ))
                for u in userscomp.get_user() ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting project teams via user reference'
                    )
        # Get using teamtype
        allteams   = []
        [ allteams.extend( projcomp.get_projectteam( teamtype=t ))
                for t in projcomp.get_teamtype() ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting project teams via teamtype reference'
                    )
        # Get using project, user
        allteams   = []
        [ allteams.extend( projcomp.get_projectteam(
                                project=projdata[pn]['id'], user=u ))
                for pn in projdata for u in userscomp.get_user() ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting project teams via project,user reference'
                    )
        # Get using project, teamtype
        allteams   = []
        [ allteams.extend( projcomp.get_projectteam(
                                project=projdata[pn]['id'], teamtype=t ))
                for pn in projdata for t in projcomp.get_teamtype() ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting project teams via project,teamtype reference'
                    )
        # Get using user, teamtype
        allteams   = []
        [ allteams.extend( projcomp.get_projectteam( user=u, teamtype=t ))
                for u in userscomp.get_user() for t in projcomp.get_teamtype() ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting project teams via user,teamtype reference'
                    )
        # Get using actual object instance.
        allteams   = [ projcomp.get_projectteam( choice([ pt, pt.id ]) )
                                    for pt in allteams ]
        assert_equal( sorted(allteams), sorted(dballteams),
                      'Mismatch in getting full project teams'
                    )

    def test_G_projectteamperms( self ) :
        """Testing project team permissions methods"""
        log.info( "Testing project team permissions methods ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        tperms = []

        # Create permissions for project team
        for pn in projdata :
            proj = projdata[pn]
            p    = proj['id']
            p    = choice([ p, p.id, p.projectname ])
            for team_type in proj['teamperms'] :
                permgroups = proj['teamperms'][team_type]
                for ptp in projcomp.add_projectteam_perm(p, team_type, permgroups) :
                    tperms.append([ p, team_type, ptp.permgroup, ptp ])

        # Remove users from project team
        perms    = projcomp.get_projectteamperm()
        rmtperms = [ p for p in perms if choice([ True, False, False ]) ]
        [ tperms.remove( tperm )
                for p in rmtperms for tperm in tperms if p == tperm[3] ]

        if choice([ True, False ]) :
            [ projcomp.remove_projectteam_perm( tp ) for tp in rmtperms ]
        else :
            projcomp.remove_projectteam_perm( rmtperms )

        assert_equal( sorted([ tperm[3] for tperm in tperms ]),
                      sorted( projcomp.get_projectteamperm() ),
                      'Mismatch in created project team permissions'
                    )

        # Try to assign site-level permission to team.
        pg = userscomp.get_permgroup(
                        'defgrp_' + choice(userscomp.site_permnames) )
        assert_raises( ZetaProjectError, projcomp.add_projectteam_perm,
                       p, team_type, pg )



    def test_H_getprojectteamperm( self ) :
        """Testing get_projectteamperm() method"""
        log.info( "Testing get_projectteamperm() method ..." )
        dballtperms = projcomp.get_projectteamperm()
        # Get using project
        alltperms   = []
        [ alltperms.extend( projcomp.get_projectteamperm(
                                        project=projdata[pn]['id'] ))
          for pn in projdata ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting project team perms via project reference'
                    )
        # Get using teamtype
        alltperms   = []
        [ alltperms.extend( projcomp.get_projectteamperm( teamtype=t ))
                for t in projcomp.get_teamtype() ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting project team perms via teamtype reference'
                    )
        # Get using perm_group
        alltperms   = []
        [ alltperms.extend( projcomp.get_projectteamperm( permgroup=pg ))
                for pg in userscomp.get_permgroup() ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting project team perms via perm_group reference'
                    )
        # Get using project, perm_group
        alltperms   = []
        [ alltperms.extend( projcomp.get_projectteamperm( 
                                        project=projdata[pn]['id'], permgroup=pg ))
          for pn in projdata for pg in userscomp.get_permgroup() ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting project team perms via project,perm_group reference'
                    )
        # Get using project, teamtype
        alltperms   = []
        [ alltperms.extend( projcomp.get_projectteamperm(
                                        project=projdata[pn]['id'], teamtype=t ))
          for pn in projdata for t in projcomp.get_teamtype() ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting project team perms via project,teamtype reference'
                    )
        # Get using perm_group, teamtype
        alltperms   = []
        [ alltperms.extend( projcomp.get_projectteamperm( permgroup=pg, teamtype=t ))
                for pg in userscomp.get_permgroup() for t in projcomp.get_teamtype() ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting project team perms via perm_group,teamtype reference'
                    )
        # Get using actual object instance.
        alltperms   = [ projcomp.get_projectteamperm( choice([ pt, pt.id ]) )
                                    for pt in alltperms ]
        assert_equal( sorted(alltperms), sorted(dballtperms),
                      'Mismatch in getting full project team perms'
                    )

    #def test_I_projectperms( self ) :
    #    """Testing project permissions methods"""
    #    log.info( "Testing project permissions methods ..." )
    #    c           = ContextObject()
    #    config['c'] = c
    #    c.authuser  = g_byuser

    #    pperms = []
    #    # Create permissions for project perms
    #    for pn in projdata :
    #        proj = projdata[pn]
    #        p    = proj['id']
    #        p    = choice([ p, p.id, p.projectname ])
    #        [ pperms.append(
    #            [ p, uname, pg,
    #              projcomp.add_project_permission( p, uname, pg ) ]
    #          ) for uname in proj['projectperms']
    #            for pg in proj['projectperms'][uname] ]
    #    # Remove users from project perms
    #    perms    = projcomp.get_projectperm()
    #    rmpperms = [ p for p in perms if choice([ True, False, False ]) ]
    #    [ pperms.remove( pperm )
    #      for p in rmpperms for pperm in pperms if p == pperm[3] ]
    #    # update generated data
    #    for p in rmpperms :
    #        for pn in projdata :
    #            proj = projdata[pn]
    #            if proj['id'].projectname != p.project.projectname :
    #                continue
    #            proj['projectperms'][p.user.username].remove( p.permgroup ) 

    #    if choice([ True, False ]) :
    #        [ projcomp.remove_project_permission( pp ) for pp in rmpperms ]
    #    else :
    #        projcomp.remove_project_permission( rmpperms )
    #    assert_equal( sorted([ pperm[3] for pperm in pperms ]),
    #                  sorted( projcomp.get_projectperm() ),
    #                  'Mismatch in created project user permissions'
    #                )

    #def test_J_getprojectperm( self ) :
    #    """Testing get_projectperm() method"""
    #    log.info( "Testing get_projectperm() method ..." )
    #    dballpperms = projcomp.get_projectperm()
    #    # Get using project
    #    allpperms   = []
    #    [ allpperms.extend( projcomp.get_projectperm(
    #                                    project=projdata[pn]['id'] ))
    #      for pn in projdata ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting project user perms via project reference'
    #                )
    #    # Get using user
    #    allpperms   = []
    #    [ allpperms.extend( projcomp.get_projectperm( user=u ))
    #            for u in userscomp.get_user() ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting project user perms via user reference'
    #                )
    #    # Get using perm_group
    #    allpperms   = []
    #    [ allpperms.extend( projcomp.get_projectperm( permgroup=pg ))
    #            for pg in userscomp.get_permgroup() ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting project user perms via perm_group reference'
    #                )
    #    # Get using project, perm_group
    #    allpperms   = []
    #    [ allpperms.extend( projcomp.get_projectperm(
    #                                    project=projdata[pn]['id'], permgroup=pg ))
    #            for pn in projdata for pg in userscomp.get_permgroup() ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting project user perms via project,perm_group reference'
    #                )
    #    # Get using project, user
    #    allpperms   = []
    #    [ allpperms.extend( projcomp.get_projectperm( 
    #                                    project=projdata[pn]['id'], user=u ))
    #            for pn in projdata for u in userscomp.get_user() ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting project user perms via project,user reference'
    #                )
    #    # Get using perm_group, user
    #    allpperms   = []
    #    [ allpperms.extend( projcomp.get_projectperm( permgroup=pg, user=u ))
    #            for pg in userscomp.get_permgroup() for u in userscomp.get_user() ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting project team perms via perm_group,user reference'
    #                )
    #    # Get using actual object instance.
    #    allpperms   = [ projcomp.get_projectperm( choice([ pp, pp.id ]) )
    #                                for pp in allpperms ]
    #    assert_equal( sorted(allpperms), sorted(dballpperms),
    #                  'Mismatch in getting full project user perms'
    #                )

    def test_K_tags( self ) :
        """Testing project tags"""
        log.info( "Testing project tags ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for pn in projdata :
            proj     = projdata[pn]
            # Add / Remove tags for components
            p        = proj['id']
            compdata = proj['components']
            mstndata = proj['milestones']
            verdata  = proj['versions']
            for cn in compdata :
                comp      = compdata[cn]
                c         = comp['id']
                byuser    = choice( comp['tags'].keys() ) 
                tags      = comp['tags'][byuser]
                tagaslist = tags and choice(tags) or u''
                tagasitem = tags and choice(tags) or u''
                rmtag     = tags and choice(tags) or u''
                projcomp.add_tags( choice([ p.id, p.projectname, p ]),
                                   entity='component', id=choice([ c.id, c ]),
                                   tags=tags, byuser=byuser
                                 )
                projcomp.remove_tags( choice([ p.id, p.projectname, p ]),
                                      entity='component', id=choice([ c.id, c ]),
                                      tags=rmtag, byuser=byuser
                                    )
                rmtag and tags.remove( rmtag )
                comptags =  [ t.tagname for t in projcomp.get_component( c.id ).tags ]
                assert_equal( sorted( tags ), sorted( comptags ),
                              'Mismatch in project-component tag methods' )
            # Add / Remove tags for milestones
            for mn in mstndata :
                mstn      = mstndata[mn]
                m         = mstn['id']
                byuser    = choice( mstn['tags'].keys() )
                tags      = mstn['tags'][byuser]
                tagaslist = tags and choice(tags) or u''
                tagasitem = tags and choice(tags) or u''
                rmtag     = tags and choice(tags) or u''
                projcomp.add_tags( choice([ p.id, p.projectname, p ]),
                                   entity='milestone', id=choice([ m.id, m ]),
                                   tags=tags, byuser=byuser
                                 )
                projcomp.remove_tags( choice([ p.id, p.projectname, p ]),
                                      entity='milestone', id=choice([ m.id, m ]),
                                      tags=[ rmtag ], byuser=byuser
                                    )
                rmtag and tags.remove( rmtag )
                mstntags =  [ t.tagname for t in projcomp.get_milestone( m.id ).tags ]
                assert_equal( sorted( tags ), sorted( mstntags ),
                              'Mismatch in project-milestone tag methods' )
            # Add / Remove tags for version
            for vn in verdata :
                ver       = verdata[vn]
                v         = ver['id']
                byuser    = choice( ver['tags'].keys() )
                tags      = ver['tags'][byuser]
                tagaslist = tags and choice(tags) or u''
                tagasitem = tags and choice(tags) or u''
                rmtag     = tags and choice(tags) or u''
                projcomp.add_tags( choice([ p.id, p.projectname, p ]),
                                   entity='version', id=choice([ v.id, v ]),
                                   tags=tags, byuser=byuser
                                 )
                projcomp.remove_tags( choice([ p.id, p.projectname, p ]),
                                      entity='version', id=choice([ v.id, v ]),
                                      tags=rmtag, byuser=byuser
                                    )
                rmtag and tags.remove( rmtag )
                vertags = [ t.tagname for t in projcomp.get_version( v.id ).tags ]
                assert_equal( sorted( tags ), sorted( vertags ),
                              'Mismatch in project-version tag methods' )
            byuser    = choice( proj['tags'].keys() )
            tags      = proj['tags'][byuser]
            rmtag     = tags and choice(tags) or u''
            projcomp.add_tags( choice([ p.id, p.projectname, p ]),
                               tags=tags, byuser=byuser
                             )
            projcomp.remove_tags( choice([ p.id, p.projectname, p ]),
                                  tags=rmtag, byuser=byuser
                                )
            rmtag and tags.remove( rmtag )
            p = projcomp.get_project( p.projectname )
            assert_equal( sorted( tags ), sorted([ t.tagname for t in p.tags ]),
                          'Mismatch in project tag methods' )

    def test_L_attachs( self ) :
        """Testing project attachments"""
        log.info( "Testing project attachments ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        users = userscomp.get_user()
        attachs = {}
        for pn in projdata :
            proj = projdata[pn]
            attachs[pn] = []
            for u in proj['attachs'] :
                for f in proj['attachs'][u] :
                    attach = attachcomp.create_attach(
                                            os.path.basename( f ),
                                            choice([ open( f, 'r' ), None  ]),
                                            uploader=u,
                                            summary='',
                             )
                    projcomp.add_attach( proj['id'], attach )
                    attachs[pn].append( (u, f, attach) )
            rmattach = [ tup for tup in attachs[pn]  if choice([ True, False ]) ]
            for tup in rmattach :
                attachs[pn].remove( tup )
                projcomp.remove_attach( proj['id'], tup[2] )
                proj['attachs'][tup[0]].remove( tup[1] )
        for p in projcomp.get_project() :
            atts = [ tup[2] for tup in attachs[p.projectname] ]
            assert_equal( sorted(atts), sorted(p.attachments),
                          'Mismatch in project attachments' )

    def test_M_projectteams( self ) :
        """Testing data crunching method projectteams()"""
        log.info( "Testing data crunching method projectteams() ..." )
        allteams  = []
        teamtypes = sorted(projcomp.teams)
        usernames = sorted(userscomp.usernames)
        for pn in projdata :
            proj   = projdata[pn]
            pteams = projcomp.projectteams( proj['id'] )
            assert_true( sorted(pteams.keys()) == teamtypes,
                         'Mismatch in teams under project users' )
            for t in pteams :
                y_usernames = [ pt[1] for pt in pteams[t][0] ]
                x_usernames = pteams[t][1]
                allteams.extend([ pt[0] for pt in pteams[t][0] ])
                assert_equal( sorted(list(set(y_usernames + x_usernames ))),
                              usernames,
                             'Some user is left out in project team configuration'
                           )
                assert_false( set(y_usernames).intersection( set(x_usernames) ),
                              'projteams y/x are not mutually exclusive'
                            )

        assert_equal( sorted(allteams),
                      sorted([ pt.id
                               for pt in projcomp.get_projectteam() ]),
                      'Mismatch in project teams'
                    )

    def test_N_teamperms( self ) :
        """Testing data crunching method teamperms()"""
        log.info( "Testing data crunching method teamperms() ..." )
        allteamperms  = []
        teamtypes     = sorted(projcomp.teams)
        perms         = sorted(userscomp.mixedpnames)
        [ perms.remove(pn) for pn in userscomp.site_permnames ]
        for pn in projdata :
            proj      = projdata[pn]
            teamperms = projcomp.teamperms( proj['id'] )
            assert_true( sorted(teamperms.keys()) == teamtypes,
                         'Mismatch in teams under prj team perms' )
            for t in teamperms :
                y_permnames = [ ptp[1] for ptp in teamperms[t][0] ]
                x_permnames = teamperms[t][1]
                y_pnpg      = []
                [ y_pnpg.extend(
                    [ p.perm_name
                      for p in userscomp.get_permgroup(mixp).perm_names ]
                  ) for mixp in y_permnames if mixp.islower() ]
                allteamperms.extend([ ptp[0] for ptp in teamperms[t][0] ])
                assert_equal( sorted(list(set( y_permnames + y_pnpg + x_permnames ))),
                              perms,
                              'Some permission is left out in project team permission configuration'
                            )
                assert_false( set(y_permnames).intersection( set(x_permnames) ),
                              'teamperms y/x are not mutually exclusive'
                            )

        assert_equal( sorted(allteamperms),
                      sorted([ ptp.id
                               for ptp in projcomp.get_projectteamperm() ]),
                      'Mismatch in project team permissions'
                    )

    def test_O_projectuserperms( self ) :
        """Testing data crunching method projectuserperms()"""
        log.info( "Testing data crunching method projectuserperms() ..." )
        allpuserperms = []
        perms         = sorted( userscomp.mixedpnames )
        for pn in projdata :
            proj       = projdata[pn]
            projusers  = sorted( projcomp.projusernames( proj['id'] ))
            puserperms = projcomp.projectuserperms( proj['id'] )
            for u in puserperms :
                y_permnames = [ pup[1] for pup in puserperms[u][0] ]
                x_permnames = puserperms[u][1] 
                y_pnpg      = []
                [ y_pnpg.extend(
                    [ p.perm_name
                      for p in userscomp.get_permgroup(mixp).perm_names ]
                  ) for mixp in y_permnames if mixp.islower() ]
                allpuserperms.extend([ pup[0] for pup in puserperms[u][0] ])
                assert_equal( sorted(list(set( y_permnames + y_pnpg + x_permnames ))),
                              perms,
                             'Some permission is left out in project user permission configuration'
                           )
                assert_false( set(y_permnames).intersection( set(x_permnames) ),
                              'prjperms y/x are not mutually exclusive'
                            )
        assert_equal( sorted(allpuserperms),
                      sorted([ ptp.id for ptp in projcomp.get_projectperm() ]),
                      'Mismatch in project user permissions'
                    )

    def test_P_userpermissions( self ) :
        """Testing userpermissions()"""
        log.info( "Testing userpermissions() ..." )
        projects = projcomp.get_project()
        for p in projects :
            projusers = projcomp.projusernames( p ) + [ p.admin.username ]
            for u in projusers :
                user  = userscomp.get_user( u )
                spnames = set(userscomp.user_permnames( user ))
                teams = [ pt.teamtype.team_type for pt in user.projectteams
                             if pt.project.projectname == p.projectname ]
                tpnames = []
                for t in teams :
                    tpnames.extend([ pn.perm_name for ptp in p.projteamperms
                                     if ptp.teamtype.team_type == t
                                     for pn in ptp.permgroup.perm_names ])
                tpnames = set(tpnames)
                upnames = [ pn.perm_name for pup in p.projectperms 
                                         if pup.user.username == user.username
                                         for pn in pup.permgroup.perm_names ]
                upnames = set(upnames)
                permnames = list(
                        spnames.intersection( tpnames ).intersection( upnames )
                        )
                assert_equal( permnames,
                              projcomp.userpermissions( user, p ),
                              'Mismatch in user permission for %s, %s' % \
                                      ( user.username, p.projectname )
                            )

    def test_Q_minifunctions( self ) :
        """Testing projcomp minifunctions"""
        log.info( "Testing projcomp minifunctions ..." )

        # Test code for projusernames
        for pn in projdata :
            proj = projdata[pn]
            p    = proj['id']
            projusers = list(set([ pt.user.username 
                                   for pt in projcomp.get_projectteam( project=p )
                                 ] ))
            assert_equal( sorted( projusers ),
                          sorted(
                              projcomp.projusernames(
                                  choice([ p, p.id, p.projectname ]))
                          ),
                          'Mismatch in projusernames() function'
                        )

        # Test code for userinteams
        ref = {}
        for pt in projcomp.get_projectteam() :
            ref.setdefault( pt.project.projectname, {} 
                          ).setdefault( pt.user.username, [] 
                                      ).append( pt.teamtype.team_type )
        for pn in projdata :
            proj  = projdata[pn]
            p     = proj['id']
            pusers= {}
            for pt in p.team :
                pusers.setdefault( pt.user.username, [] 
                                 ).append( pt.teamtype.team_type )
            for u in pusers :
                assert_equal( sorted(pusers[u]), sorted(ref[p.projectname][u]),
                              'Mismatch in userinteams() function' )


    def test_R_properties( self ) :
        """Testing project properties"""
        log.info( "Testing project properties ..." )
        [ assert_true(
            projcomp.project_exists( p )
          ) for p in projcomp.projectnames ]
        allcompnames = []
        [ allcompnames.extend( projcomp.prjcompnames( p ))
                for p in projcomp.get_project() ]
        assert_equal( sorted( allcompnames ),
                      sorted( projcomp.compnames ),
                      "Mismatch between `prjcompnames'` and `compnames`"
                    )

        allmstnnames = []
        [ allmstnnames.extend( projcomp.prjmstnnames( p ))
                for p in projcomp.get_project() ]
        assert_equal( sorted( allmstnnames ),
                      sorted( projcomp.mstnnames ),
                      "Mismatch between `prjmstnnames'` and `mstnnames`"
                    )

        allvernames = []
        [ allvernames.extend( projcomp.prjvernames( p ))
                for p in projcomp.get_project() ]
        assert_equal( sorted( allvernames ),
                      sorted( projcomp.vernames ),
                      "Mismatch between `prjvernames'` and `vernames`"
                    )

        assert_equal( sorted([ p.projectname for p in projcomp.get_project() ]),
                      sorted( projcomp.projectnames ),
                      'Mismatch in `projectnames` property'
                    )

        assert_equal( sorted([ p.projectname
                               for p in projcomp.get_project() if p.disabled ]),
                      sorted( projcomp.disabledprojs ),
                      'Mismatch in `disabledprojs` property'
                    )
        assert_equal( sorted([ p.projectname
                               for p in projcomp.get_project() if not p.disabled ]),
                      sorted( projcomp.enabledprojs ),
                      'Mismatch in `enabledprojs` property'
                    )
        assert_equal( sorted([ p.projectname
                               for p in projcomp.get_project() if p.exposed ]),
                      sorted( projcomp.exposedprojs ),
                      'Mismatch in `exposedprojs` property'
                    )
        assert_equal( sorted([ p.projectname
                               for p in projcomp.get_project() if not p.exposed ]),
                      sorted( projcomp.privateprojs ),
                      'Mismatch in `privateprojs` property'
                    )
        assert_equal( sorted([ t.team_type for t in projcomp.get_teamtype() ]),
                      sorted( projcomp.teams ),
                      'Mismatch in `teams` property'
                    )

    def test_S_projectteamtypes( self ) :
        """Testing project teamtype creation"""
        log.info( "Testing project teamtype creation ..." )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        ref_teamtypes = projcomp.teams
        add_teamtypes = [ u'teamtype1', u'teamtype2' ]
        ref_teamtypes += add_teamtypes
        projcomp.create_projteamtype( add_teamtypes )
        assert_equal( sorted(ref_teamtypes), projcomp.teams,
                      'Mismatch in creating project team types as list' )


        add_teamtypes = u'teamtype3'
        ref_teamtypes += [ add_teamtypes ]
        projcomp.create_projteamtype( add_teamtypes )
        assert_equal( sorted(ref_teamtypes), projcomp.teams,
                      'Mismatch in creating project team types as string' )

    def test_T_wikitranslate( self ) :
        """Testing wiki translation for entry description(s) and closing_remark"""
        log.info( "Testing wiki translation for entry description(s) and closing remark" )
        for pn in projdata :
            proj = projdata[pn]
            p    = proj['id']
            self._testwiki_execute( 'projdesc', p.project_info, 'description' )
            compdata = proj['components']
            mstndata = proj['milestones']
            verdata  = proj['versions']
            for cn in compdata :
                comp = compdata[cn]
                self._testwiki_execute( 'compdesc', comp['id'], 'description' )
            for mn in mstndata :
                mstn = mstndata[mn]
                self._testwiki_execute( 'mstndesc', mstn['id'], 'description' )
                self._testwiki_execute( 'mstndesc', mstn['id'], 'closing_remark' )
            for vn in verdata :
                ver  = verdata[vn]
                self._testwiki_execute( 'verdesc', ver['id'], 'description' )
        for p in projcomp.get_project() :
            self._testwiki_execute( 'projdesc', p.project_info, 'description' )
        for c in projcomp.get_component() :
            self._testwiki_execute( 'compdesc', c, 'description' )
        for m in projcomp.get_milestone() :
            self._testwiki_execute( 'mstndesc', m, 'description' )
            self._testwiki_execute( 'mstndesc', m, 'closing_remark' )
        for v in projcomp.get_version() :
            self._testwiki_execute( 'verdesc', v, 'description' )

    def test_U_favorites( self ) :
        """Testing favorite addition and deletion for projects"""
        log.info( "Testing favorite addition and deletion for projects" )
        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for pn in projdata :
            proj = projdata[pn]
            p    = proj['id']
            if choice([ True, False ]) : # as list
                projcomp.addfavorites( p, proj['favusers'] )
            else :                       # as byuser
                for u in proj['favusers'] :
                    projcomp.addfavorites( p, u, byuser=u )
            rmfavusers = [ u for u in proj['favusers'] if choice([ 1, 0, 0 ]) ]
            [ proj['favusers'].remove( u ) for u in rmfavusers ]
            if choice([ True, False ]) : # as list
                projcomp.delfavorites( p, rmfavusers )
            else :                       # as byuser
                for u in rmfavusers :
                    projcomp.delfavorites( p, u, byuser=u )
        for pn in projdata :
            proj = projdata[pn]
            p    = projcomp.get_project( proj['id'].projectname )
            assert_equal( sorted(p.favoriteof),
                          sorted([ userscomp.get_user( u ) 
                                   for u in proj['favusers'] ]),
                          'Mismatch in creating project favorites'
                        )

    def test_V_projectdetails( self ) :
        """Testing projectdetails() method"""
        log.info( "Testing projectdetails() method" )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        for p in projcomp.get_project() :
            comps = dict([ (comp.id, comp.componentname) for comp in p.components ])
            mstns = dict([ (m.id, m.milestone_name) for m in p.milestones ])
            vers  = dict([ (v.id, v.version_name) for v in p.versions ])
            projusers = sorted( projcomp.projusernames( p ))
            res       = projcomp.projectdetails( p )
            res[3]    = sorted( res[3] )
            assert_equal( res, [ comps, mstns, vers, projusers ],
                          'Mismatch in projectdetails'
                        )

    def test_X1_upgradewiki( self ) :
        """Testing upgradewiki() method"""
        log.info( "Testing upgradewiki() method" )

        c           = ContextObject()
        config['c'] = c
        c.authuser  = g_byuser

        pcnt, ccnt, mcnt, vcnt = projcomp.upgradewiki( byuser=g_byuser )
        assert_equal( [ pcnt, ccnt, mcnt, vcnt ],
                      [ len(projcomp.get_project()),
                        len(projcomp.get_component()),
                        len(projcomp.get_milestone()),
                        len(projcomp.get_version()),
                      ],
                      'Mismatch in upgradewiki()'
                    )

    def test_X2_attachments( self ) :
        """Testing method, attachments()"""
        log.info( "Testing method, attachments()" )

        projects = projcomp.get_project(
                                attrload_all=[ 'attachments.uploader',
                                               'attachments.tags' ]
                   )
        for p in projects :
            pattachs = {}
            attachs = {}
            for a in p.attachments :
                attachs[a.id] = [ a.filename, a.size, a.summary, a.download_count,
                                  a.created_on, a.uploader.username,
                                  [ tag.tagname for tag in a.tags ]
                                ]
            if attachs :
                pattachs = { (p.id, p.projectname) : attachs }
            attachments = projcomp.attachments( p )
            assert_equal( attachments, pattachs, 
                          'Mismatch in attachments, for project %s' % p.projectname )

    def test_X3_adminprojects( self ) :
        """Testing method, adminprojects()"""
        log.info( "Testing method, adminprojects()" )

        admins = {}
        for p in projcomp.get_project() :
            admins.setdefault( p.admin.username, [] ).append( p.projectname )

        for u in admins :
            assert_equal( sorted(projcomp.adminprojects( userscomp.get_user( u) )),
                          sorted(admins[u]),
                          'Mismatch in adminprojects, for user %s' % u
                        )

    def test_X4_userprojects( self ) :
        """Testing method, userprojects()"""
        log.info( "Testing method, userprojects()" )

        for u in userscomp.get_user() :
            refteams = {}
            [ refteams.setdefault( pt.project.projectname, [] 
                              ).append( pt.teamtype.team_type )
              for pt in u.projectteams ]
            refteams = dict([ (k, sorted(refteams[k])) for k in refteams ])
            teams = projcomp.userprojects( u )
            teams = dict([ (k, sorted(teams[k])) for k in teams ])
            assert_equal( refteams, teams,
                          'Mismatch in userprojects, for user %s' % u.username )
