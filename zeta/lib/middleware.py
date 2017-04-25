# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

def make_gzip_middleware(app, global_conf, **app_conf):
    compresslevel = int( app_conf.get( 'compresslevel', 9 ))
    return GzipMiddleware( app, compresslevel )
