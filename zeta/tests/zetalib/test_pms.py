# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import logging
import os
from   os.path                  import join, isdir, basename
import random
from   random                   import choice, randint, shuffle, seed

from   nose.tools               import assert_equal, assert_raises, assert_true, \
                                       assert_false
import pylons.test
from   sqlalchemy               import engine_from_config

from   zeta.auth.perm           import permissions
from   zeta.model               import init_model, create_models, delete_models
from   zeta.model               import meta
from   zeta.lib.pms             import PMSystem
import zeta.lib.cache           as cachemod 
from   zeta.tests.tlib          import *

config  = pylons.test.pylonsapp.config
log     = logging.getLogger(__name__)
seed    = None
g_byuser= u'admin'
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


map_level1_1 = { ('t1', 't2') : [ 'PERM1', 'PERM2' ],
                 ('t3', 't4') : []
               }

map_level2_1 = { 's1'         : [ 'PERM3', 'PERM4' ],
                 ('t5', 't6') : [ 'PERM5', 'PERM6' ]
               }
map_level2_2 = lambda : {}

map_level3_1 = { 's2'         : [],
                 ('t7', 't8') : [ 'PERM7', 'PERM8' ]
               }
map_level3_2 = { 's3'         : [],
                 's4'         : []
               }
map_level3_3 = lambda : {}
map_level3_4 = { ('t9', 't10'): [ 'PERM9', 'PERM10', 'PERM11' ] }

contexts = [ ('t1', 't2'), ('t3', 't4'), 's1', ('t5', 't6'), 's2',
             ('t7', 't8'), 's3', 's4', ('t9', 't10')
           ]
literals = [ 'PERM1', 'PERM2', 'PERM3', 'PERM4', 'PERM5', 'PERM6', 'PERM7',
             'PERM8', 'PERM9', 'PERM10', 'PERM11'
           ]
ctx = lambda : [ choice( contexts ) ]

l31 = PMSystem( 'l31', ctx, map_level3_1, [] )
l32 = PMSystem( 'l32', ctx, map_level3_2, [] )
l33 = PMSystem( 'l33', ctx, map_level3_3, [] )
l34 = PMSystem( 'l34', ctx, map_level3_4, [] )
l21 = PMSystem( 'l21', ctx, map_level2_1, [ l31, l32 ] )
l22 = PMSystem( 'l22', ctx, map_level2_2, [ l33, l34 ] )
l11 = PMSystem( 'l11', ctx, map_level1_1, [ l21, l22 ] )


class TestPMS( object ) :

    def test_1_pmsystem( self ) :
        """Testing pms mapping and hierarchy"""

        assert_true(  l11.check( ['PERM1'], context=[('t1', 't2')]),
                      'Mismatch in check 1' )                           # 1
        assert_false( l11.check( ['PERM1'], context=[('t3', 't4')]),
                      'Mismatch in check 2' )                           # 2
        assert_false( l11.check( [],      context=[('t3', 't4')]),
                      'Mismatch in check 3' )                           # 3
        assert_true(  l11.check( ['PERM3','PERM4'], context=['s1']),
                      'Mismatch in check 4' )                           # 4
        assert_true(  l11.check( ['PERM4'], context=['s1']),
                      'Mismatch in check 5' )                           # 5
        assert_true(  l11.check( ['PERM6'], context=[('t5', 't6')]),
                      'Mismatch in check 6' )                           # 6
        assert_false( l11.check( ['PERM1'], context=[('t5', 't6')]),
                      'Mismatch in check 7' )                           # 7
        assert_true(  l11.check( ['PERM7','PERM8'], allliterals=True, 
                                 context=[('t7', 't8')]),
                      'Mismatch in check 8' )                           # 8
        assert_false( l11.check( ['PERM8'], context=[('t9', 't10')]),
                      'Mismatch in check 9' )                           # 9
        assert_false( l11.check( ['PERM8'], context=['s3']),
                      'Mismatch in check 10' )                          # 10

        assert_true(  l11.check( ['PERM1', 'PERM2'],
                                 allliterals=False,
                                 context=['s1', ('t1','t2')],
                               ),
                      'Mismatch in check 11' )                          # 11

        assert_true(  l11.check( ['PERM3', 'PERM4'],
                                 allliterals=True,
                                 context=['s1', ('t1','t2')],
                               ),
                      'Mismatch in check 12' )                          # 12

        assert_true(  l11.check( ['PERM1', 'PERM4'],
                                 allliterals=False,
                                 context=['s1', ('t1','t2')],
                               ),
                      'Mismatch in check 13' )                          # 12

        assert_false( l11.check( ['PERM1', 'PERM4'],
                                 allliterals=True,
                                 context=['s1', ('t1','t2')],
                               ),
                      'Mismatch in check 14' )                          # 12


        for i in range(100) :
            rc = l11.check( choice( literals ),
                            [choice([ None, None, choice(contexts) ])]
                          )
            assert_true( rc in [True, False] )
