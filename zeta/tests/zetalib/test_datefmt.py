# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import unittest
import os
from   os.path                  import join, isdir, basename
import difflib                  as diff
import random
from   random                   import choice, randint, shuffle
from   datetime                 import datetime
import datetime                 as dt
import re

from   sqlalchemy               import engine_from_config
import pylons.test
import pytz
from   pytz                     import timezone
from   nose.tools               import assert_equal

from   zeta.auth.perm           import permissions
from   zeta.model               import meta
from   zeta.model               import init_model, create_models, delete_models
import zeta.lib.datefmt         as datefmt
import zeta.lib.cache           as cachemod 
from   zeta.tests.tlib          import *

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None

cachemgr= None
cachedir= '/tmp/testcache'

def setUpModule() :
    global seed, cachemgr

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


class TestDatefmt( object ) :

    def _test_execute( self, utcdt, usertz ) :
        userdt = datefmt.utc_2_usertz( utcdt, usertz )
        utcdt  = utcdt.tzinfo and utcdt or timezone('UTC').localize( utcdt )
        userdt = choice([ userdt, datetime( *userdt.timetuple()[:7] ) ])
        _utcdt = datefmt.usertz_2_utc( userdt, usertz )
        assert_equal( utcdt.timetuple(), _utcdt.timetuple() )

    def test_conversions( self ) :
        """Testing date format conversions"""
        log.info( "Testing date format conversions" )
        utctz    = timezone( 'UTC' )
        timelist = list( datetime.timetuple( datetime.utcnow() ) )[:7] 
        utcdt    = choice([ datetime( *timelist ),
                            utctz.localize( datetime( *timelist )) ])
        for usertz in pytz.all_timezones :
            yield self._test_execute, utcdt, choice([ usertz, timezone( usertz ) ])
