# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import os
from   random   import randint

class FileObject( object) :
    pass

class MultiDict( object ) :

    def __init__( self ) :
        self.fields = []

    def get( self, item, default=None ) :
        for itm, v in self.fields :
            if itm == item :
                rvalue = v
                break
        else :
            rvalue = default
        return rvalue

    def getall( self, item, default=[] ) :
        rvalue = []
        for itm, v in self.fields :
            if itm == item :
                rvalue.append( v )
        rvalue = rvalue or default
        return rvalue

    def add( self, item, value ) :
        self.fields.append( (item, value) )

    def clearfields( self ) :
        self.fields = []

class RequestObject( object ) :

    def __init__( self, method='POST' ) :
        self.POST   = MultiDict()
        self.params = MultiDict()
        self.method = 'POST'

    def requestform( self ) :
        self.params.add( 'form', 'request' )

    def submitform( self ) :
        self.params.add( 'form', 'submit' )

class ContextObject( object ) :
    pass


def log_mheader( log, testdir, testfile, seed ) :
    logthead = ">> Setting up tests for `%s` with seed %s" % \
               ( os.path.join( testdir, testfile ), seed )
    print '\n', logthead
    log.info( logthead )

def log_mfooter( log, testfile, testdir ) :
    logttail = ">> Tearing down tests for `%s` " % \
               os.path.join( testdir, testfile )
    print logttail
    log.info( logttail )

def genseed() :
    return randint(1, 100000)
