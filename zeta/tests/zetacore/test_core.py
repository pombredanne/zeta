# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import os
from   os.path                  import join, isdir, basename
import logging
import random
from   random                   import choice, randint, shuffle, seed

import pylons.test

from   zeta.ccore               import *
from   zeta.ccore               import ComponentMeta, ComponentManager
from   nose.tools               import assert_false
from   zeta.tests.tlib          import *
import zeta.lib.cache           as cachemod 

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

    compmgr = config['compmgr']

    # Setup cache manager
    isdir( cachedir ) or os.makedirs( cachedir )
    cachemgr = cachemod.cachemanager( cachedir )
    config['cachemgr'] = cachemgr


def tearDownModule() :
    testdir  = os.path.basename( os.path.dirname( __file__ ))
    testfile = os.path.basename( __file__ )
    log_mfooter( log, testdir, testfile )

    # Clean up cache
    cachemod.cleancache( cachedir )


class TestInterface1( Interface ) :
    def method1() :
        pass
    def method2() :
        pass

class TestInterface2( Interface ) :
    def method1() :
        pass
    def method2() :
        pass

class TestInterface3( Interface ) :
    def method1() :
        pass
    def method2() :
        pass

class TestInterface4( Interface ) :
    def method1() :
        pass
    def method2() :
        pass

class TestInterface4( Interface ) :
    ext = ExtensionPoint( TestInterface1 )
    def method3() :
        pass
    def method4() :
        pass
    def interfaces( self ) :
        return [ comp for comp in self.ext ]


class TestCompBase1( Component ) :
    ext = ExtensionPoint( TestInterface2 )
    implements( TestInterface1 )

class TestCompBase2( Component ) :
    ext = ExtensionPoint( TestInterface1 )
    implements( TestInterface2 )

class TestCompBase3( TestCompBase1 ) :
    pass

class TestCompBase4( Component ) :
    pass

class TestComponent1( TestCompBase3 ) :
    ext = ExtensionPoint( TestInterface1 )
    implements( TestInterface2 )
    def __init__( self ) :
        pass
    def interfaces( self ) :
        return [ comp for comp in self.ext ]

class TestComponent2( Component ) :
    ext = ExtensionPoint( TestInterface2 )
    implements( TestInterface1 )
    def __init__( self ) :
        pass
    def interfaces( self ) :
        return [ comp for comp in self.ext ]

class TestComponent3( TestCompBase4 ) :
    implements( TestInterface1 )
    def __init__( self ) :
        pass

class TestComponent4( Component ) :
    implements( TestInterface1, TestInterface2 )
    def __init__( self ) :
        pass

class TestComponent5( Component ) :
    implements( TestInterface1 )
    implements( TestInterface2 )
    def __init__( self ) :
        pass
 
class TestComponent6( Component ) :
    implements( TestInterface1 )
    def __init__( self ) :
        pass

class TestComponent7( Component ) :
    ext = ExtensionPoint( TestInterface2 )
    implements( TestInterface2 )
    def __init__( self ) :
        pass
    def interfaces( self ) :
        return [ comp for comp in self.ext ]

class TestComponent8( Component ) :
    implements( TestInterface1, TestInterface2 )
    def __init__( self ) :
        pass


class TestManager1( ComponentManager ) :
    ext = ExtensionPoint( TestInterface1 )
    implements( TestInterface1 )
    implements( TestInterface2 )
    def __init__( self, *args ) :
        ComponentManager.__init__( self )
    def interfaces( self ) :
        return [ comp for comp in self.ext ]

class TestManager2( Component, ComponentManager ) :
    ext = ExtensionPoint( TestInterface2 )
    implements( TestInterface1 )
    def __init__( self, *args ) :
        ComponentManager.__init__( self )
    def interfaces( self ) :
        return [ comp for comp in self.ext ]


class testCore( object ) :

    def setUp( self ) :
        """Create the component manager instance"""
        self.mgr1 = TestManager1()
        self.mgr2 = TestManager2()
        g = globals()
        self.testclasses = [ g[k] for k in g if k[:4] == 'Test' ]

    def tearDown( self ) :
        """Destroy the component manager instance"""
        self.mgr1 = None
        self.mgr2 = None

    def test_baseclasses( self ) :
        """Testing registration skipping for core classes"""
        log.info( "Testng registration skipping for core classes ..." )
        assert_false( Interface in ComponentMeta._components )
        assert_false( ExtensionPoint in ComponentMeta._components )
        assert_false( ComponentMeta in ComponentMeta._components )
        assert_false( Component in ComponentMeta._components )

    #def test_extensionpoints( self ) :
    #    """Check the interface extension points that are created in each
    #    components"""
    #    extpoints = [ (TestModel1, TestInterfaceforModel1),
    #                  (TestInterface2, TestInterface1), 
    #                  (TestManager1, TestInterface1),
    #                  (TestComponent1, TestInterface2), 
    #                  (TestComponent2, TestInterface2),
    #                  (TestController2, TestInterface2),
    #                  (Testfactorycontroller2, TestInterface2), ]

    #    implementers = {
    #        TestInterfaceforModel2  : [ TestModel1 ],
    #        TestInterfaceforModel1  : [ TestModel2 ],
    #        TestInterface1          : [ TestManager1, TestComponent3, 
    #                                    TestComponent4, TestComponent5, 
    #                                    TestController1, TestController3, 
    #                                    TestController3, Testfactorycontroller1,
    #                                    Testfactorycontroller3,
    #                                    ],
    #        TestInterface2          : [ TestManager1, TestComponent1, 
    #                                    TestComponent4, TestComponent5, 
    #                                    TestController2, TestController3, 
    #                                    Testfactorycontroller2, ]
    #    }

    #    # Check for preserved ExtensionPoints properties
    #    extpointclasses = []
    #    msg = "Interface extended does not match the extension point !!"
    #    for c, i in extpoints :
    #        self.failUnless( c.ext.interface == i, msg=msg )
    #        extpointclasses.append( c )

    #    # A double check mechanism to make sure that the previous check does
    #    # not miss out a class having an extension point
    #    missedextpoints = [ c for c in self.testclasses 
    #                          if 'ext' in c.__dict__
    #                             and c not in extpointclasses ]
    #    msg = "Test class with extension point is not tested for validity !!"
    #    self.failUnless( missedextpoints == [], msg=msg )

    #    # Check for the components implementing interfaces.
    #    for c in self.testclasses :
    #        if not issubclass( c, Component ) :
    #            continue
    #        if 'ext' in c.__dict__ :
    #            comp  = self.mgr1[c]
    #            comps = comp.interfaces()
    #            comps.sort()
    #            refcomps = [ cls(self.mgr1) for cls in implementers[ c.ext.interface ]
    #                            if isinstance( cls( self.mgr1 ), Component ) ]
    #            refcomps.sort()
    #            self.failUnless( comps == refcomps )

    #    # TODO: The interfaces implemented by components that are disabled
    #    # should not be returned by the ExtensionPoint property
