#! /usr/bin/env python

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# Gotcha : 
# Notes  :
#   * The back-up direcotry structure,
#       <bkpdir>
#           |---<name>
#                  |---<name>-bkp-<timestamp>              (backup directory)
#                  |           |----<name>                 (hard-link to deployed dir)
#                  |           |----<name>-sql-<timestamp> (sqldumpfile)
#                  |
#                  |---<name>-bkp-<timestamp>.tar.gz
#                  |---backupz-log-<timestamp>

import sys
import getopt
from   optparse     import OptionParser
import os
from   os.path      import basename, abspath, dirname, isdir, isfile, join
import shutil       as sh
import time

progname = basename( __file__ )
usage    = "usage: %prog [options] name deploydir bkpdir"
pyver    = "%s.%s" % sys.version_info[:2]
python   = 'python%s' % pyver
timest   = time.localtime()
timestr  = '%s.%s.%s.%s' % timest[:4]
options  = None

def _cmdexecute( cmd, log=True ) :
    if log :
        print >> options.logfd, "  %s" % cmd
    rc = os.system( cmd )
    if rc != 0 :
        print >> options.logfd, "Command failed `%s`" % cmd
        sys.exit(1)

def cmdoptions() :
    op = OptionParser( usage=usage )
    #op.add_option( "--eggs", dest="fetcheggs", default="",
    #               help="Fetch all the egg files to the <fetcheggs> directory" )

    #op.add_option( "-H", dest="noindex", action="store_true", default=False,
    #               help="Do not look up into python package index" )

    options, args = op.parse_args()
    return op, options, args

def backupsql( name, destfile ) :
    cmd = 'mysqldump %s -u %s --password=%s#321 > %s' % (
                name, name, name, destfile )
    _cmdexecute( cmd )

if __name__ == '__main__' :
    op, options, args = cmdoptions()
    if len(args) == 3 :
        options.name     = args[0]
        options.deploydir= abspath(args[1])
        options.bkpdir   = join( abspath(args[2]), options.name,
                                 '%s-bkp-%s' % (options.name, timestr) )
        options.sqldump  = join( options.bkpdir,
                                 '%s-sql-%s' % (options.name, timestr) )
        options.logfile  = join( dirname(options.bkpdir),
                                 'backupz-log-%s' % timestr )
        options.targz    = join( dirname(options.bkpdir),
                                 '%s-bkp-%s.tar.gz' % (options.name, timestr) )

        os.makedirs( options.bkpdir )
        options.logfd = open( options.logfile, 'w' )


        # Symbolically link deployed directory for backup
        os.symlink( options.deploydir, join( options.bkpdir, options.name ) )

        # SQL dump
        backupsql( options.name,
                   join( options.bkpdir, '%s-%s.sql' % (options.name, timestr) )
                 )

        # Tar and gzip
        cmd = 'tar cfhlz %s %s' % ( options.targz, options.bkpdir )
        _cmdexecute( cmd )

        # Remove the original tar tree
        sh.rmtree( options.bkpdir )

    else :
        op.print_help()
