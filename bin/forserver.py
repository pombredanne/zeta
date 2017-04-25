#! /usr/bin/env python

"""Simple and small script to change the server references in selenium UAT
test cases"""

import sys
import re

fromstr = sys.argv[1]
repl    = sys.argv[2]
files   = sys.argv[3:]
print repl
for f in files :
    print "%s ..." % f
    text = open(f).read()
    text = text.replace( fromstr, repl )
    open( f, 'w' ).write( text )
