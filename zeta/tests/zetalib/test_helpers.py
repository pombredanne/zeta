# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import unittest
import os
from   os.path                   import join, isdir, basename
import difflib                   as diff
import random
from   random                    import choice, randint, shuffle, seed
from   datetime                  import datetime
import re

import pylons.test
import pytz
from   nose.tools                import assert_equal, assert_raises, assert_true
import simplejson                as json
from   sqlalchemy                import engine_from_config
 
from   zeta.auth.perm            import permissions
from   zeta.model                import init_model, create_models, delete_models
from   zeta.model                import meta
from   zeta.lib.base             import BaseController
import zeta.lib.helpers          as h
import zeta.lib.cache            as cachemod 
from   zeta.lib.error            import ZetaFormError
from   zeta.comp.forms           import *
from   zeta.comp.tag             import TagComponent
from   zeta.comp.project         import ProjectComponent
from   zeta.comp.wiki            import WikiComponent
from   zeta.tests.tlib           import *
from   zeta.tests.model.generate import genattachs

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None

compmgr   = None
userscomp = None
projcomp  = None
tagcomp   = None
cachemgr  = None
cachedir  = '/tmp/testcache'

def _check_file( path,f ) :
    try :
        open( os.path.join(path,f), 'r' )
    except :
        return None
    else :
        return f

def setUpModule() :
    global compmgr, userscomp, projcomp, tagcomp, seed, cachemgr

    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    seed     = config['seed'] and int(config['seed']) or genseed()
    log_mheader( log, testdir, testfile, seed )
    random.seed( seed )

    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    # init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )

    compmgr   = config['compmgr']
    userscomp = config['userscomp']
    projcomp  = ProjectComponent( compmgr )
    tagcomp   = TagComponent( compmgr )

    # Setup cache manager
    isdir( cachedir ) or os.makedirs( cachedir )
    cachemgr = cachemod.cachemanager( cachedir )
    config['cachemgr'] = cachemgr


def tearDownModule() :
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )

    info = "   Deleting models ... "
    log.info( info )
    print info
    delete_models( meta.engine )

    # Clean up cache
    cachemod.cleancache( cachedir )


class Scoop( object ) :
    def __init__( self, name ) :
        self.name = name

class TestHelpers( object ) :

    def test_scoopvalues( self ) :
        """Testing h.scoopvalues()"""
        log.info( "Testng h.scoopvalues ..." )
        objects = []
        names   = []
        for i in range(randint(0,100)) :
            name = h.randomname()
            objects.append( Scoop( name ))
            names.append( name )
        assert_equal( names, h.scoopvalues( objects, 'name' ))
        
    def test_validate_fields( self ) :
        """Testing h.validate_fields()"""
        log.info( "Testng h.validate_fields ..." )
        request = RequestObject()
        c       = ContextObject()
        vf      = VForm( compmgr )

        # Test timezone field both valid and invalid.
        request.POST.add( 'timezone', choice( pytz.all_timezones ))
        h.validate_fields( request ) 
        request.POST.clearfields()
        request.POST.add( 'timezone', 'invalid' )
        assert_raises( ZetaFormError, h.validate_fields, request )

        # Test form field both valid and invalid
        request.POST.clearfields()
        request.POST.add( 'perm_name', 'SAM' )
        h.validate_fields( request )

        request.POST.clearfields()
        request.POST.add( 'perm_name', 'S' )
        h.validate_fields( request )

        request.POST.clearfields()
        request.POST.add( 'perm_name', 'SA' * 100 )
        assert_raises( ZetaFormError, h.validate_fields, request )

        # Test username, projectname, tagname with special characters.
        request.POST.clearfields()
        request.POST.add( 'username', 'gandhi_mk' )
        request.POST.add( 'projectname', 'Congress_in.old' )
        request.POST.add( 'tagname', 'ok' )
        h.validate_fields( request )

        request.POST.clearfields()
        request.POST.add( 'tagname', 'hello.world_howareyou!' )
        h.validate_fields( request )

        request.POST.clearfields()
        request.POST.add( 'username', 'gandhi mk' )
        assert_raises( ZetaFormError, h.validate_fields, request )
        request.POST.clearfields()
        request.POST.add( 'projectname', 'congress-in' )
        assert_raises( ZetaFormError, h.validate_fields, request )
        request.POST.clearfields()
        request.POST.add( 'tagname', 'o' )
        h.validate_fields( request )

    def test_url_for_mform( self ) :
        """Testing h.url_for_mform()"""
        log.info( "Testng h.url_for_mform ..." )
        refurl = '/p/someproject/admin?form=submit&view=js&' + \
                 'formname=updateprj&formname=prjexp&formname=prjml'
        cntlr = BaseController()
        url = cntlr.url_for_mform(
                        h.r_projadmin, projectname='someproject',
                        form='submit', view='js',
                        formname=[ 'updateprj', 'prjexp', 'prjml' ]
                    )
        assert_true( url == refurl,
                     'Failed %s ' % url )
                    
    def test_todojoreadstore( self ) :
        """Testing todojoreadstore() function"""
        log.info( "Testng h.todojoreadstore ..." )
        # Testing the list
        samp = {
                   'identifier' : 'id1',
                   'label'      : 'lab1',
                   'items'      : [ [ '0', 'hello' ], [ '0.1', 'world' ] ]
               }
        jsonstr = h.todojoreadstore( samp['items'], lambda x : { x[0] : x[1] },
                                     id='id1', label='lab1' )
        samp['items'] = [ { x[0] : x[1] } for x in samp['items'] ]
        assert_equal( samp, json.loads( jsonstr ),
                      'Mismatch in converting list items to dojoreadstore'
                    )
        # Testing the dictionary
        samp = {
                   'identifier' : 'id1',
                   'label'      : 'lab1',
                   'items'      : { '0' : 'hello', '0.1' : 'world' }
               }
        jsonstr = h.todojoreadstore( samp['items'], lambda k, v : { k : v },
                                     id='id1', label='lab1' )
        samp['items'] = [ { k : samp['items'][k] } for k in samp['items'] ]
        assert_equal( samp, json.loads( jsonstr ),
                      'Mismatch in converting dict items to dojoreadstore'
                    )

    def test_hitch( self ) :
        """Testing the hitch functionality"""
        log.info( "Testng h.hitch ..." )
        refargs = ()
        refkw   = {}
        class O( object ) :
            pass

        def checkhitch( self, *args, **kwargs ) :
            assert_equal( args, refargs,
                          'Mismatch in Variable arguments, \n args : %s \n refargs : %s' % ( args, refargs )
                        )
            assert_equal( kwargs, refkw,
                          'Mismatch in Keyword arguments, \n kwargs : %s \n refkw : %s' % ( kwargs, refkw )
                        )
            return 'hello world'

        o       = O()
        refargs = (0, 1, 2)
        args    = (3, 4, 5)
        refkw   = { 'arg1':'hello', 'world' : 'how are you' }
        kwargs  = { 'world':10, 'kwarg2':20 }
        o.fhitch= h.hitch( o, O, checkhitch, *refargs, **refkw )
        refargs = refargs + args
        refkw.update( kwargs )
        assert_equal( o.fhitch( *args, **kwargs ),
                      'hello world',
                      'Mismatch in the return value of the hitched function' 
                    )

    def test_parse_csv( self ) :
        """Testing the h.parse_csv() function"""
        log.info( "Testng h.parser_csv ..." )
        line = 'item1, item2, ,, item3, item4 ,,,'
        assert_equal( h.parse_csv( line ),
                      [ 'item1', 'item2', 'item3', 'item4' ],
                      'Mismatch in parsed csv with sample data 1'
                    )
        line = ''
        assert_equal( h.parse_csv( line ), [],
                      'Mismatch in parsed csv with sample data 2'
                    )
        line = ', ,  ,,'
        assert_equal( h.parse_csv( line ), [],
                      'Mismatch in parsed csv with sample data 3'
                    )

    def test_autoreference( self ) :
        """Testing the h.autoreference() function"""
        log.info( "Testing the h.autoreference() function" )
        file = choice([ f for f in os.listdir( '/etc/' ) 
                          if _check_file( '/etc/', f ) ])
        text = open( os.path.join( '/etc/', file )).read()

        username = 'administrator'
        tagname  = 'compression'
        projname = 'python'
        kwargs   = { 'tagnames' : [tagname, 'programming'] }

        idx   = randint(0, len(text)-1)
        ntext = text[0:idx] + ' ' + tagname + ' ' + text[idx:]
        assert_true( ' [< <a href="/tag/compression">compression</a> >] ' \
                      in h.autoreference( ntext, **kwargs ),
                      'Mismatch in automatic referencing tagname'
                   )

    def test_authxmlrpc( self ) :
        """Testing h.authxmlrpc() method"""
        log.info( "Testing h.authxmlrpc() method" )

        for user in userscomp.get_user() :
            url = 'http://%s:%s@192.168.0.101/xmlrpc' % \
                                    ( user.username, user.password )
            u   = h.auth_xmlrpc( url )
            assert_equal( user, u,
                          'Mismatch xmlrpc auth, for user %s' % user.username
                        )
