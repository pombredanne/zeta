#! /usr/bin/env python

import sys 
import os
from   os.path       import join, basename, isdir, isfile, splitext

def main( tarfile ) :
    py_version = '%s.%s' % sys.version_info[:2]
    print 'Python Version %s' % py_version

    # Remove old zeta version
    cmd = 'rm -rf demo/lib/python%s/site-packages/zeta*' % py_version
    print ' > ', cmd
    os.system( cmd )

    # Remove old zwiki version
    cmd = 'rm -rf demo/lib/python%s/site-packages/zwiki*' % py_version
    print ' > ', cmd
    os.system( cmd )

    cmd = 'sudo rm -rf defenv'
    print ' > ', cmd
    os.system( cmd )

    # Cleanup files in current dir
    [ os.remove( f ) for f in os.listdir( '.' ) if isfile( f ) ]

    # Untar
    cmd = 'cp %s .' % tarfile
    print ' > ', cmd
    os.system( cmd )
    cmd = 'tar xvf %s' % basename( tarfile )
    print ' > ', cmd
    os.system( cmd )

    # Deploy
    zetafile  = [ f for f in os.listdir( '.' ) 
                    if f[:4] == 'zeta' and splitext( f )[1] == '.egg' ]
    zetafile  = zetafile and zetafile[0] or ''
    zwikifile = [ f for f in os.listdir( '.' ) 
                    if f[:5] == 'zwiki' and splitext( f )[1] == '.egg' ]
    zwikifile = zwikifile and zwikifile[0] or ''
    cmd = './deployzeta.sh demo %s %s ' % ( zetafile, zwikifile )
    print ' > ', cmd
    os.system( cmd )

    # Appsetup
    cmd = 'bash -c "source virtz-demo.sh; paster setup-app production.ini#zetapylons"'
    print ' > ', cmd
    os.system( cmd )

    cmd = 'sudo chgrp www-data .'
    print ' > ', cmd
    os.system( cmd )

    cmd = 'sudo chgrp -R www-data egg-cache'
    print ' > ', cmd
    os.system( cmd )

    cmd = 'sudo chgrp -R www-data defenv'
    print ' > ', cmd
    os.system( cmd )

    cmd = 'chmod -R g+w egg-cache'
    print ' > ', cmd
    os.system( cmd )

    cmd = 'chmod -R g+w defenv'
    print ' > ', cmd
    os.system( cmd )

    cmd = 'chmod g+w .'
    print ' > ', cmd
    os.system( cmd )


if __name__ == "__main__":
    (tarfile,) = sys.argv[1:]
    main( tarfile )
