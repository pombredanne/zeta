# /usr/bin/env python

import httplib
import time


while 1 :
    start = time.time()
    conn  = httplib.HTTPConnection( "sandbox.devwhiz.net" )
    conn.request( "GET", "/help/zwiki" )
    print time.time() - start
