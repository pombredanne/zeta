#! /usr/bin/env python

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Package dojo css files into a single file. and fix stuff like  url
references"""

import os
import re
import pprint

f_dest = 'zdojo/ztundra.css'
f_org  = 'zdojo/release/dijit/themes/tundra/tundra.css'
fd     = open( os.path.join( 'defenv/public', f_dest ), 'w' )

def url_reencode( fname, l ) :
    dname  = os.path.dirname( fname )
    url    = re.findall( r'.*url[ \t]*\((.*)\).*', l )[0].strip(' \t"\'') 
    encurl = os.path.join( dname, url )
    l      = l.replace( url, encurl )
    return l

for l in open( os.path.join( 'defenv/public', f_org ) ).readlines() :
    if not re.match( r'@import.*url.*\(.*\).*;.*', l ) :
        continue
    fname = os.path.join( 'defenv/public', os.path.dirname( f_org ),
                          re.findall( r'@import.*url.*\((.*)\).*;.*', l )[0].strip(' \t"') 
                        )
    for l1 in open( fname ).readlines() :
        if not re.match( r'.*url[ \t]*\(.*\).*', l1 ) :
            fd.write( l1 )
            continue
        print "Re-encoding ... %s" % l1
        fd.write( url_reencode( fname.replace( 'defenv/public/zdojo/', ''), l1 ))


# Code for testing the correctness of the above list comprehension
# pprint.pprint([ os.system( 'wc -l ' +  os.path.abspath(
#         os.path.join( '../defenv/public/zdojo/release/dijit/themes/tundra/', 
#                       re.findall( r'@import.*url.*\((.*)\).*;.*', l )[0].strip(' \t"') 
#                     )
#   )) for l in open( orgfile ).readlines()
#      if re.match( r'@import.*url.*\(.*\).*;.*', l ) ])
