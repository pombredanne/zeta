# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Cache tool kit. Beaker is used as the backend to store / synchronize data
while this module provides convenient apis and decorators to avail caching

Caching is done per namespace, using (key,value) pairs. The namespace is
calculated based on the function name.

Key is computer as,
    * positional arguments passed to `cache` decorator. Note that the first
      argument must always be unique within the class or module containing the
      function.
    * optionally use the positional argument passed to decorated function.
"""

# -*- coding: utf-8 -*-

# Gotchas : 
#   1. 'cachenm' is expected to be a single element list.
# Notes   : None
# Todo    :

import types
import os
from   os.path          import join
from   hashlib          import sha1

from   beaker.cache     import CacheManager
from   beaker.util      import parse_cache_config_options

import zeta.lib.helpers as h

cachedir = 'data/cache' 
datadir  = 'data/cache/data' 
lockdir  = 'data/cache/lock' 

def cachemanager( envpath ) :
    """Configuration parameters for cache module. Beaker is used as the back
    end """
    cacheconf = {
        'cache.type'     : 'file',
        'cache.data_dir' : join( envpath, datadir ),
        'cache.lock_dir' : join( envpath, lockdir ),
    }
    return CacheManager(**parse_cache_config_options( cacheconf ))

def cleancache( envpath ) :
    """Cleanup cached data. The convinient way as, prescribed by pylons is to
    remove the cache directory (including its sub-directory)"""
    cmd = 'rm -rf %s/*' % join( envpath, datadir )
    os.system( cmd )
    cmd = 'rm -rf %s/*' % join( envpath, lockdir )
    os.system( cmd )

def func2namespace( func ) :
    """Generates a unique namespace for a function"""
    if hasattr( func, 'im_func' ) :     # Is function part of class ?
        cls  = func.im_class
        func = func.im_func
        return '%s.%s' % ( cls.__module__, cls.__name__ )
    else:
        return '%s' % ( func.__module__ )

def filterargs( func, args ) :
    """Generates a unique namespace for a function"""
    args = filter( lambda a : not ( isinstance( a, types.ObjectType ) or\
                                    isinstance( a, types.ClassType )
                                  ),
                   args )
    return args

def cache( *cacheargs, **cachekwargs ) :
    """Decorator to cache a function, under the key specified by 'cacheargs'
    and optionally, the positional arguments passed to the decorated function.
    Again, these positional arguments passed to the decorated function can be
    skipped by specifying useargs=False in 'cachekwargs'.
    Other keyword arguments are only meant for configuring the cache object
    (Refer beaker).
    """
    key     = ''
    useargs = cachekwargs.pop( 'useargs', True )
    key     = ' '.join([ str(x) for x in cacheargs ])
    cachenm = [None]
    
    def decorate( func ) :
        """The decorator for function 'func'"""
        namespace = func2namespace( func )

        def cacheit( *args, **kwargs ) :
            """This function replaces the target function 'func'. Accepts
            'args' and 'kwargs' arguments when ever the target function is
            called. Caches the value returned by the target function `func`
            under previously computed `key`"""

            # Dirty heuristics,
            cachemgr  = h.fromconfig( 'cachemgr' )

            cachenm[0]= cachenm[0] or cachemgr.get_cache( namespace, **cachekwargs )
            cache_key = key
            if useargs and args :
                cache_key += ( " " + " ".join([ str(x) for x in args ]) )

            def dofun():
                if args and kwargs :
                    return func( *args, **kwargs )
                elif args :
                    return func( *args )
                elif kwargs :
                    return func( **kwargs )

            # Do calling and caching.
            return cachenm[0].get( key=sha1(cache_key).hexdigest(),
                                   createfunc=dofun )

        cacheit._namespace = namespace
        cacheit._kwargs    = cachekwargs
        cacheit._cache_key = key    # Without including positional arguments
        cacheit._useargs   = useargs

        return cacheit

    return decorate

def invalidate( func, *args, **kwargs ) :
    """Invalidate the cache for the namespace for function 'func'. If 'useargs'
    was True while 'cache'ing the function, then provide the same 'args'
    (positional parameter) that was used while calling the decorated function.
    """
    # Dirty heuristics,
    cachemgr = h.fromconfig( 'cachemgr' )

    cachenm  = cachemgr.get_cache( func._namespace, **func._kwargs )
    clearall = kwargs.pop( 'clearall', False )
    if clearall :
        cachenm.clear()
    else :
        cache_key = func._cache_key 
        useargs   = func._useargs
        if useargs and args :
            cache_key += ( " " + " ".join([ str(x) for x in args ]) )
        try :
            cachenm.remove_value( key=sha1(cache_key).hexdigest() )
        except OSError :
            pass
