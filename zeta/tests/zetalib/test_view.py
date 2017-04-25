# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import unittest
import os
from   os.path                  import join, isdir, basename
import difflib                  as diff
import random
from   random                   import choice, randint, shuffle, seed
from   datetime                 import datetime
import re

from   sqlalchemy               import engine_from_config
import pylons.test
import pytz
from   nose.tools               import assert_equal, assert_raises, assert_true

from   zeta.auth.perm           import permissions
from   zeta.model               import init_model, create_models, delete_models
from   zeta.model               import meta
import zeta.lib.helpers         as h
import zeta.lib.cache           as cachemod 
from   zeta.lib.error           import ZetaFormError
from   zeta.lib.view            import *
from   zeta.comp.forms          import *
from   zeta.tests.tlib          import *

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None

compmgr = None
cachemgr= None
cachedir= '/tmp/testcache'


def setUpModule() :
    global compmgr, seed, cachemgr

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

    compmgr = config['compmgr']

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



class TestView( object ) :
    
    def test_anchor( self ) :
        """Testing view.Anchor() class"""
        log.info( "Testing view.Anchor() class" )
        kwargs = { 'href'   : 'anchor href',
                   'text'   : 'anchor text',
                   'title'  : 'anchor title',
                   'type'   : 'anchor type',
                   'kwarg1' : 'anchor kwarg1',
                   'kwarg2' : 'anchor kwarg2'
                 }
        a = Anchor( **kwargs )
        [ assert_equal( a.__dict__[k], kwargs[k] ) for k in kwargs ]
