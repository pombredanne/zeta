# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import time
import unittest
import os
from   os.path                   import join, isdir, basename
import random
from   random                    import choice, randint, shuffle, seed
from   datetime                  import datetime
import re

import pylons.test
import pylons
import pytz
from   nose.tools                import assert_equal, assert_raises, \
                                        assert_true, assert_false
import simplejson                as json
from   sqlalchemy                import engine_from_config
 
from   zeta.auth.perm            import permissions
from   zeta.model                import init_model, create_models, delete_models
from   zeta.model                import meta
import zeta.lib.cache            as cachemod 
import zeta.lib.helpers          as h
from   zeta.lib.error            import ZetaFormError
from   zeta.tests.tlib           import *
from   zeta.tests.model.generate import genattachs

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None

cachemgr= None
cachedir= '/tmp/testcache'

def setUpModule() :
    global cachemgr

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


@cachemod.cache( 'alphabets' )
def countelements( elements, **kwargs ) :
    d = {}
    for a in open( join(os.path.split(__file__)[0], 'testfile.data') ).read() :
        if a not in elements :
            continue
        d.setdefault( a, [] ).append( a )

    for a in d :
        d[a] = len(d[a])
    d.update( kwargs )
    return d


@cachemod.cache( 'alphabets', useargs=False )
def countelements_negargs( elements, **kwargs ) :
    d = {}
    for a in open( join(os.path.split(__file__)[0], 'testfile.data') ).read() :
        if a not in elements :
            continue
        d.setdefault( a, [] ).append( a )

    for a in d :
        d[a] = len(d[a])
    d.update( kwargs )
    return d


class TestCache( object ) :

    def test_1_func2namespace( self ) :
        """Testing func2namespace()"""
        log.info( "Testng func2namespace() ..." )

        config['cachemgr'] = cachemgr

        # Namespace for module function
        def func() :
            pass
        assert_equal( cachemod.func2namespace( func ), 'zetalib.test_cache',
                      'Mismatch in func2namespace for function' 
                    )

        # Namespace for class function
        class O( object ) :
            def func( self ) :
                pass
        o = O()
        #assert_equal( '.'join(cachemod.func2namespace(o.func).split('.')[1:]),
        assert_equal( cachemod.func2namespace(o.func), 'zetalib.test_cache.O',
                      'Mismatch in func2namespace for method'
                    )

    def test_2_decorators( self ) :
        """Testing decorators"""
        log.info( "Testing cache decorator ..." )

        config['cachemgr'] = cachemgr

        # Test simple caching
        st = time.time()
        d1 = countelements( '1234567890', key1='val1', key2='val2', key3='val3' )
        cachetime = time.time() - st

        st = time.time()
        d2 = countelements( '1234567890', key1='val1', key2='val2', key3='val3' )
        fetchtime = time.time() - st

        assert_equal( d1, d2, 'Mismatch in simple cache, value' )
        assert_true( fetchtime < (cachetime / 10),
                     'Mismatch in simple cache, timing' )

        st = time.time()
        d1 = countelements( 'abcdefghijklmnopqrstuv', key1='value1', key2='value2',
                            key3='value3' )
        cachetime = time.time() - st

        st = time.time()
        d2 = countelements( 'abcdefghijklmnopqrstuv', key1='value1', key2='value2',
                            key3='value3' )
        fetchtime = time.time() - st

        assert_equal( d1, d2, 'Mismatch in simple cache, value' )
        assert_true( fetchtime < (cachetime / 10),
                     'Mismatch in simple cache, timing' )

        # Test invalidating cache
        cachemod.invalidate( countelements, 'abcdefghijklmnopqrstuv' )

        st = time.time()
        d3 = countelements( 'abcdefghijklmnopqrstuv', key1='value1', key2='value2',
                            key3='value3' )
        fetchtime = time.time() - st

        assert_equal( d1, d3, 'Mismatch in invalidate cache, value' )
        assert_false( fetchtime < (cachetime / 10),
                     'Mismatch in invalidate cache, timing' )

        # Test invalidate all.
        cachemod.invalidate( countelements, clearall=True )

        # Test caching without using arguments.
        st = time.time()
        d1 = countelements_negargs(
                'abcdefghijklmnopqrstuv', key1='value1', key2='value2', key3='value3' )
        cachetime = time.time() - st

        st = time.time()
        d2 = countelements_negargs(
                    '1234567890', key1='val1', key2='val2', key3='val3' )
        fetchtime = time.time() - st

        assert_equal( d1, d2, 'Mismatch in simple cache, value' )
        assert_false( d2.pop( 'key1' ) == 'val1', 'Mismatch in clearall, key1' )
        assert_false( d2.pop( 'key2' ) == 'val2', 'Mismatch in clearall, key2' )
        assert_false( d2.pop( 'key3' ) == 'val3', 'Mismatch in clearall, key3' )
        assert_true( fetchtime < (cachetime / 10),
                     'Mismatch in caching without using args, timing' )
