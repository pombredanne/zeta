#! /usr/bin/env python

# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Simple and small script to check for LICENSE header"""

import os
import re
import pprint
import difflib
from   os.path              import join, basename, split, abspath, splitext

root = split( split( abspath(__file__) )[0] )[0]

skipdirs = [
    './bin',
    './build',
    './dist',
    './docs',
    './zeta.egg-info',
    './.bzr',
    './docs',
    './tools',
    './zeta/lib/.Attic',
    './zeta/templates-dojo/component/.Attic',
    './zeta/tests/testDB',
    './zeta/tests',
    './zeta/tests/functional',
    './zeta/tests/model/.Attic',
    './zeta/tests/model/sampledata',
    './zeta/tests/model/sqlscripts',
    './zeta/tests/zetalib',
    './zeta/tests/zetalib/dotdir',
    './zeta/tests/UAT_selenium/ZetaSignin'
    './zeta/tests/UAT_selenium/StaticWikiTest'
    './zeta/tests/UAT_selenium/betasuite'
    './zeta/templates/component/.Attic',
    './zeta/extras/tests',
    './zeta/xrclients',
    './zeta/vim',
    './zeta/vim/syntax',
    './zeta/vim/ftdetect',
    './zeta/vim/plugin',
    './defenv/staticfiles',
    './defenv/data',
    './defenv/log',
    './defenv/public/upgradescripts',
    './defenv/public/screenshots',
    './defenv/public/highcharts',
    './defenv/public/zetaicons',
    './defenv/public/jquery',
    './defenv/public/captcha',
    './defenv/public/zdojo/templates',
    './defenv/public/zdojo/release',
    './defenv/public/zdojo/build',
]

skippatterns = [ r'.*.pyc', r'.*.swp', r'__init__.py', r'deployment.ini_tmpl',
                 r'\.vim.*', r'lextab.py', r'yacctab.py', r'parser.out',
                 r'dispatch.wsgi', r'.*.jpg', r'.*.png', r'.*.log', r'.*.css',
                 r'.*.json', r'.*.zip',  r'.*.gz',  r'.*.egg', r'.*.tar',
                 r'.*.css.org', r'tckfilters.pyd', r'jquery-1.4.2.min.js',
                 r'favicon.ico', r'googleanalytics.html', r'UserTitlePane.js',
                 r'README',
               ]
def filterfile( f ) :
    res = all( map( lambda pattr : not re.match( pattr, f ),
                       skippatterns ))
    return res
    
pyhdrline1   = "# This file is subject to the terms and conditions defined in"
pyhdrline2   = "# file 'LICENSE', which is part of this source code package."
pyhdrline3   = "#       Copyright (c) 2009 SKR Farms (P) LTD."
htmlhdrline1 = "## This file is subject to the terms and conditions defined in"
htmlhdrline2 = "## file 'LICENSE', which is part of this source code package."
htmlhdrline3 = "##       Copyright (c) 2009 SKR Farms (P) LTD."
jshdrline1   = "// This file is subject to the terms and conditions defined in"
jshdrline2   = "// file 'LICENSE', which is part of this source code package."
jshdrline3   = "//       Copyright (c) 2009 SKR Farms (P) LTD."
def checkheader( checkfiles ) :
    for file in checkfiles :
        lines = [ l.strip('\n') for l in open( file ).readlines()[:3] ]

        ext   = splitext( file )[1]
        if ext == '.py' or ext == '.sh' :
            line1 = pyhdrline1
            line2 = pyhdrline2
            line3 = pyhdrline3
        elif ext == '.js' :
            line1 = jshdrline1
            line2 = jshdrline2
            line3 = jshdrline3
        else    : # ext == '.html'
            line1 = htmlhdrline1
            line2 = htmlhdrline2
            line3 = htmlhdrline3

        if len(lines) == 3 and lines[0] == line1 and \
                lines[1] == line2 and lines[2] == line3 :
            continue

        print "Header not found in %s " % file
        #if len(lines) == 3 :
        #    print '\n'.join(lines[:3])
        #    print '\n'.join([ line1, line2, line3 ])

def main() :
    print "Checking header for files under %s" % root

    for path, dirs, files in os.walk( '.' ) :
        [ dirs.remove( d ) for d in dirs[:] if join( path, d ) in skipdirs ]
        if path == '.' :
            continue
        checkfiles   = filter( filterfile, files )
        skippedfiles = set( files ).difference( set(checkfiles) )
        if skippedfiles :
            skippedfiles = [ f for f in skippedfiles
                             if '.pyc' not in f and \
                                '.swp' not in f ] 
            print "Path %s" % path
            print "   ", skippedfiles
        checkfiles   = [ join( path, f ) for f in checkfiles ]
        checkheader( checkfiles )


if __name__ == '__main__' :
    main()

