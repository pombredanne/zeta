# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

# Add the virtual Python environment site-packages directory to the path

ALLDIRS = ['/home/pratap/dev/virtualenvs/pylons/lib/python2.6/site-packages',
           '/home/pratap/dev/multigate/',
           '/home/pratap/dev/zwiki/',
          ]

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
new_sys_path.append( '/home/pratap/dev/zeta' )

sys.path[:0] = new_sys_path

# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
os.environ['PYTHON_EGG_CACHE'] = '/home/pratap/dev/zeta/egg-cache'

# Load the Pylons application
from paste.deploy import loadapp
application = loadapp('config:/home/pratap/dev/zeta/development.ini')
