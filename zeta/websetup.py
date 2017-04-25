# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.


"""Setup the zeta application"""

import logging
import os
import sys
from   os.path                 import basename, join

import pylons.test

import zeta.config.environment as     environment
from   zeta.config.environment import setup_environment, setup_models
from   zeta.model              import meta

log = logging.getLogger(__name__)

virtualenv_pkgs = """
ALLDIRS = ['%s']

import sys
import site

# Remember original sys.path.
prev_sys_path = list( sys.path )

# Add each new site-packages directory.
for directory in ALLDIRS:
    site.addsitedir( directory )

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list( sys.path ) :
    if item not in prev_sys_path:
        new_sys_path.append( item )
        sys.path.remove( item )

sys.path[:0] = new_sys_path

"""

def setup_app( command, conf, vars ) :
    """Place any commands to setup zeta here"""

    # Load environment, and create the database schema
    print "Loading environment and Creating database ... "
    config  = setup_environment( conf.global_conf, conf.local_conf )
    print "ok"

    environment.websetupconfig = config

    # Initialize userscomp.
    userscomp = h.fromconfig('userscomp')

    # Don't reload the app if it was loaded under the testing environment
    #if not pylons.test.pylonsapp:
    #    print "Loading environment and Creating database ... "
    #    config  = setup_environment( conf.global_conf, conf.local_conf )
    #    print "ok"

    # Copy the defenv/ tree to the deployment directory
    print "Copying the environment directory ..."
    cmd = 'cp -r %s %s' % ( join( config['zeta.pkg_path'], 'defenv' ), config['zeta.envpath'] )
    print cmd
    os.system( cmd )

    datadir = join( '.', basename( config['zeta.envpath'] ), 'data' )
    if not os.path.isdir( datadir ) :
        os.mkdir( datadir )
    print "ok"

    # Create and initialize database tables.
    setup_models( config, userscomp=userscomp )

    # Instrument dispatch.wsgi for mod_wsgi
    try :
        wsgi_file = os.path.abspath( 'defenv/mod_wsgi/dispatch.wsgi' )
        sitepkgs  = os.path.dirname( config['zeta.pkg_path'] )
        eggcache  = os.path.abspath( 'egg-cache' )
        prodini   = os.path.abspath( 'production.ini' )
        text      = []
        print "Updating %s ... " % wsgi_file,
        for l in open( wsgi_file ).readlines() :
            l = l.strip('\n\r')
            if l == '#add-virtualenv-packages' :
                text.append( virtualenv_pkgs % sitepkgs )
            elif l == '#add-sitedir-here' :
                # Deprecated
                text.append( "site.addsitedir('%s')" % sitepkgs )
            #elif l == '#add-projsyspath-here' :
            #    # Deprecated
            #    text.append( 
            #        "sys.path.insert(0, '%s')" % join( sitepkgs,
            #                                           'zeta-0.71b1-py2.5.egg',
            #                                           'zeta'
            #                                         )
            #    )
            elif l == '#add-eggcache-here' :
                text.append( "os.environ['PYTHON_EGG_CACHE'] = '" + eggcache + "'" )
            elif l == '#add-config-here' :
                text.append( "application = loadapp('config:" + prodini + "')" )
            else :
                text.append( l )
        open( wsgi_file, 'w' ).write( '\n'.join(text) )
        print "ok"
    except :
        print sys.exc_info()
        raise

