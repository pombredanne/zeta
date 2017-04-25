#! /usr/bin/env python

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# Note :
#   Only recently '==' based dependency is being used. But this script may
#   need to handle '>=' kind of dependency from older versions. So, lots of
#   work-arounds with eventually needs to be fixed.

import sys
import getopt
from   optparse     import OptionParser
import os
from   os.path      import basename, abspath, dirname, join, isdir, isfile
import shutil       as sh
import re

pyver      = "%s.%s" % sys.version_info[:2]

""" Configuration

It is better to allow the egg files fetched for each previous version instead
of using cached packages. That way, we will know whether the dependancies are
met.
"""

zwikidir      = '/home/pratap/mybzr/pratap/dev/zwiki'
zetadir       = '/home/pratap/mybzr/pratap/dev/zeta'
eggdest_06b1  = '/home/pratap/mybzr/pratap/dev/zeggs-0.6b1'
eggdest_061b1 = '/home/pratap/mybzr/pratap/dev/zeggs-0.61b1'
eggdest_07b1  = '/home/pratap/mybzr/pratap/dev/zeggs-0.7b1'
zetaver       = '0.7b1'            # <---------    To be updated
zwikiver      = '0.91b'          # <---------    To be updated
regrdir       = '/home/pratap/mybzr/pratap/dev/regr-%s-%s' % (zetaver, zwikiver)
eggpkgs_061b1 = join( eggdest_061b1, 'lib', 'python%s'%pyver, 'site-packages' )
eggpkgs       = join( eggdest_07b1,  'lib', 'python%s'%pyver, 'site-packages' )
reltags       = [ ( '0.61b1', '0.9beta', eggpkgs_061b1 ),
                  ( '0.7b1',  '0.9beta', eggpkgs_07b1 ),
                  ( '0.71b1', '0.91b', eggpkgs ),  # Always the latest branch
                ]

# Egg for latest package version
zetaegg    = join( zetadir,  'dist', 'zeta-%s-py%s.egg' % (zetaver, pyver) )
zwikiegg   = join( zwikidir, 'dist', 'zwiki_zeta-%s-py%s.egg' % (zwikiver, pyver) )

# Compute egg file for each previous versions (tags)
# TODO: zwikieggf handles the renaming of zwiki package to zwiki_zeta. Remove
#       once this workaround is no longer needed
zetaeggf   = lambda tag : 'zeta-%s-py%s.egg' % (tag, pyver)
zwikieggf  = lambda tag : tag in [ '0.9beta' ] and 'zwiki_zeta-%s-py%s.egg' % (tag, pyver) \
                            or 'zwiki-%s-py%s.egg' % (tag, pyver)
reltagd    = lambda zetag, zwtag : 'reltag-%s-%s' % (zetag, zwtag)
idxreltags = lambda zetag : map( lambda x: x[0], reltags ).index( zetag )


def _cmdexecute( cmd, log=False, strict=True ) :
    """Execute shell command"""

    if log : print "  %s" % cmd
    rc = os.system( cmd )
    if rc != 0 and strict :
        raise Exception( "Command failed `%s`" % cmd )


brcmd  = "bzr branch %s %s"
tbrcmd = "bzr branch -r tag:%s %s %s"
def branch( src, dest, tag=None ) :
    """Branch a repository from source to destination based on `tag`"""

    if tag :
        _cmdexecute( tbrcmd % (tag, src, dest), log=True )
    else :
        _cmdexecute( brcmd % (src, dest), log=True )


def buildzwiki( dir ) :
    """Change to zwiki dir and package the egg."""

    print "...... Building zwiki @ %s ..." % dir
    pwd = abspath( os.curdir )
    os.chdir( dir )
    # TODO : pkgzwiki.sh is changed to `pkg.py egg`, work-around to be
    #        removed later
    if isfile( './bin/pkg.py' ) :
        pkgcmd = "./bin/pkg.py egg > ../pkgzwiki.log"
    elif isfile( './bin/pkgzwiki.sh' ) :
        pkgcmd = "./bin/pkgzwiki.sh > ../pkgzwiki.log"
    _cmdexecute( "./bin/cleanzwiki.sh > ../cleanzwiki.log", log=True, strict=False )
    _cmdexecute( pkgcmd, log=True  )
    os.chdir( pwd )
    print '\n'


def buildzeta( dir ) :
    """Change to zeta dir and package the egg. And generate the deployment
    tar"""
        
    print "...... Building zeta @ %s ..." % dir
    pwd = abspath( os.curdir )
    os.chdir( dir )
    _cmdexecute( "./bin/cleanzeta.sh > ../cleanzeta.log", log=True, strict=False )
    _cmdexecute( "./bin/pkgzeta.sh > ../pkgzeta.log", log=True )
    os.chdir( pwd )
    print '\n'


def createdatabase( zetatag, _zetadir ) :
    """Create a database for this release upgrade"""

    idx  = idxreltags( zetatag )
    name   = 'zetadev%s' % (idx+1)
    print "...... Creating database for %s ..." % name
    # Create database
    _cmdexecute(
        'echo "CREATE DATABASE %s; \
               GRANT ALL ON %s.* TO zetadev@localhost IDENTIFIED BY \'zetadev#321\'" | \
         mysql -u root --password=root123' % ( name, name )
    )
    print "\n"

def populatedatabase( zetatag, _zetadir ) :
    """Populate database with the corresponding release's sampledata"""

    idx  = idxreltags( zetatag )
    name   = 'zetadev%s' % (idx+1)
    sqlbkp = join( _zetadir, 'zeta/tests/testDB/small-zetadevsql.bkp' )
    print "...... Populate database %s ..." % name
    # Populate database
    _cmdexecute(
        'echo "use %s; source %s;" | mysql -u zetadev --password=zetadev#321' % \
                ( name, sqlbkp )
    )
    print "\n"


def adjustini( file, zetatag, zwikitag ) :
    """Adjust the production.ini file for this release upgrade"""

    print "...... Adjusting production.ini for %s ..." % zetatag
    idx  = idxreltags( zetatag )
    name = 'zetadev%s' % (idx+1)
    cont = open( file ).read()
    # Adjust port
    cont = re.sub( r'port[ ]*=[ ]*5000', 'port = %s' % (5001+idx), cont )
    # Adjust sqlurl
    cont = re.sub( r'mysql://zetadev:zetadev#321@localhost:3306/zetadev',
                    'mysql://zetadev:zetadev#321@localhost:3306/%s' % name,
                   cont
                 )
    open( file, 'w' ).write( cont )
    print '\n'


def deployapp( rtdir, zetatag, zwikitag, _eggpkgs, upgrade=True ) :
    """
    * Extract zetaegg, zwikiegg and deployzeta.py from deployment tar file
    * Replace deployzeta.sh (if present) with the latest deployzeta.py
      and deploy application
    * Adjust production.ini
    * setup-app, chmod, chgrp
    """
    pwd       = abspath( os.curdir )
    _zetaegg  = zetaeggf( zetatag )
    _zwikiegg = zwikieggf( zwikitag )
    deploydir = join( rtdir, 'deploy' )
    _zetadir   = join( rtdir, 'zeta' )
    tarfile   = join( _zetadir, 'dist', '%s.tar' % _zetaegg )
    # FIXME : Wondering whether to always use the latest version of
    # deployzeta.py, some times it seems to be so much outdated.
    deployzeta= '../../../zeta/bin/deployzeta.py'

    os.chdir( deploydir )

    # Untar
    print "...... Extracting from %s ..." % basename(tarfile)
    sh.copy( tarfile, deploydir )
    _cmdexecute( 'tar -xvf %s' % tarfile )
    print '\n'

    # Create Database
    createdatabase( zetatag, join( rtdir, 'zeta' ) )

    # Deploy
    print "...... Deploying application @ `deploy` using %s ..." % basename(_zetaegg)
    _cmdexecute(
        'python %s -f %s deploy %s %s' % (deployzeta, _eggpkgs, _zetaegg, _zwikiegg)
    )

    # Adjust production.ini
    adjustini( join( deploydir, 'production.ini' ), zetatag, zwikitag )

    # Application setup
    print "...... Application ..."
    _cmdexecute( 
        'bash -c "source virtz-deploy.sh; paster setup-app production.ini#zetapylons"',
        log=True
    )
    _cmdexecute( "chgrp -R www-data .", log=True )
    _cmdexecute( "chmod -R g+w .", log=True )
    print '\n'

    # Populate database
    populatedatabase( zetatag, join( rtdir, 'zeta' ))

    # TODO : Due to the name change for package zwiki_zeta, older package had
    #        to be removed manually. Remove this workaround later.
    oldzwiki = 'deploy/lib/python%s/site-packages/zwiki-0.83dev-py2.6.egg' % pyver
    if isfile( oldzwiki ) :
        _cmdexecute( 'rm %s' % oldzwiki )

    # Upgrade packages, wiki, database, environment directory
    if upgrade :
        print "...... Upgrading deployment %s ..." % zetatag 
        _cmdexecute( 
            'python %s --upgrade deploy %s %s' % (deployzeta, zetaegg, zwikiegg)
        )

    os.chdir( pwd )


# Span out Upgrade tree
#   regr-..-../
#       <reltag-..-..>
#           <zeta>
#           <zwiki>
#           <deploy>

def setupreltag( regrdir, zetatag=None, zwikitag=None, eggpkgs=eggpkgs ) :
    zetag  = zetatag or zetaver
    zwtag  = zwikitag or zwikiver

    print "...... Setup release upgraded for, zeta:%s & zwiki:%s ..." % ( zetag, zwtag )
    # Create release tag directory
    rtdir  = join( regrdir, reltagd( zetag, zwtag ))
    _cmdexecute( "mkdir -p %s" % rtdir, log=True )
    _cmdexecute( "mkdir -p %s" % join( rtdir, 'deploy' ), log=True )
    # Branch zeta and zwiki
    branch( zwikidir, join( rtdir, 'zwiki' ), tag=zwikitag )
    branch( zetadir, join( rtdir, 'zeta' ), tag=zetatag )
    print "\n"

    # FIXME : Remove this block of code
    txt = open( join(rtdir, 'zeta/setup.py') ).read()
    txt = txt.replace( 'MySQL_python==1.2.3c1', 'MySQL_python==1.2.2' )
    open( join(rtdir, 'zeta/setup.py'), 'w' ).write( txt )

    # Build zeta and zwiki
    buildzwiki( join( rtdir, 'zwiki' ) )
    buildzeta( join( rtdir, 'zeta' ) )

    # Deploy application
    deployapp( rtdir, zetag, zwtag, eggpkgs )


def setupregr( regrdir ) :
    print "...... Starting release upgrade regression ..."
    _cmdexecute( "mkdir -p %s" % regrdir, log=True )
    print "\n"
    for zetag, zwtag, eggpkgs in reltags :
        if zetag == zetaver :
            setupreltag( regrdir )  # Latest
        else :
            setupreltag( regrdir, zetatag=zetag, zwikitag=zwtag,
                         eggpkgs=eggpkgs )


def fetcheggs( eggdest, zetaegg, zwikiegg ) :
    """Just fetch the egg files in zipped format and save in under
    `eggdest`"""

    print "...... Fetching Egg files ..."
    deployzeta = join( zetadir, 'bin', 'deployzeta.py' )
    _cmdexecute(
        "python %s --eggs=%s deploydummy %s %s" % ( deployzeta, eggdest, zetaegg, zwikiegg )
    )


if __name__ == '__main__' :
    buildzwiki( zwikidir )
    buildzeta( zetadir )
    # fetcheggs( eggdest, zetaegg, zwikiegg )
    setupregr( regrdir )
