#! /usr/bin/env python

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Package vim plugin for zeta"""

import os
from   os.path                 import abspath, isdir, dirname, join
from   shutil                  import copy

tmpdir  = "/tmp/pkgzvim"
rootdir = dirname( dirname( __file__ ))
tardst  = abspath( join( rootdir, 'tools/zetavim-0.1.tar.gz' ))

# Copy files to temporary directory
ftdetect = join( tmpdir, 'ftdetect' )
syntax   = join( tmpdir, 'syntax' )
plugin   = join( tmpdir, 'plugin' )
isdir( tmpdir ) or os.makedirs( tmpdir )
isdir( ftdetect ) or os.makedirs( ftdetect )
isdir( syntax ) or os.makedirs( syntax )
isdir( plugin ) or os.makedirs( plugin )
copy( join( rootdir, 'zeta/extras/vim/ftdetect/zwiki.vim' ),
      join( ftdetect, 'zwiki.vim' )
    )
copy( join( rootdir, 'zeta/extras/vim/syntax/zwiki.vim' ),
      join( syntax, 'zwiki.vim' )
    )
copy( join( rootdir, 'zeta/extras/vim/plugin/zeta.vim' ),
      join( plugin, 'zeta.vim' )
    )
copy( join( rootdir, 'zeta/extras/vim/plugin/zetavim.py' ),
      join( plugin, 'zetavim.vim' )
    )
copy( join( rootdir, 'zeta/extras/xrclients/zetaclient.py' ),
      join( plugin, 'zetaclient.vim' )
    )
copy( join( rootdir, 'zeta/lib/ztext.py' ),
      join( plugin, 'ztext.vim' )
    )

curdir = os.curdir
os.chdir( tmpdir )
cmd    = "tar cvfz %s ./" % tardst
print cmd
os.system( cmd )
