""" Gzip middleware """

import gzip
from   paste.response    import header_value, remove_header
from   paste.httpheaders import CONTENT_LENGTH

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def make_gzip_middleware(app, global_conf, compress_level=6):
    """
    Return a middleware application that applies gzipping to a response
    when it is supported by the browser and the content is of
    type ``text/*`` or ``application/*``.
    """
    compress_level = int(compress_level)
    return GzipMiddleware(app, global_conf, compress_level=compress_level)

class GzipMiddleware( object ) :
    """GZip middleware callable as wsgi application"""

    def __init__( self, app, global_conf, compress_level=6 ) :
        self.app = app
        self.global_conf = global_conf
        self.compress_level = compress_level

    def __call__( self, environ, start_response ) :
        if 'gzip' not in environ.get('HTTP_ACCEPT_ENCODING', ''): # supported ?
            return self.app( environ, start_response )

        # Try to do GZipping.
        self.environ = environ
        resp = GzipResponse()
        app_iter = self.app(environ, resp.gzip_start_response )
        resp.app_iter = app_iter
        resp.process( self.compress_level, start_response )
        return resp


class GzipResponse( list ) :
    """Response object that is compliant with WSGI iterable result"""

    def __init__( self, *args, **kwargs ) :
        self.buffer = StringIO()
        self.compressible = False
        list.__init__( self, *args, **kwargs )

    def close( self ) :
        if self.app_iter  and hasattr(self.app_iter, 'close' ) :
            self.app_iter.close()
        return None

    def gzip_start_response( self, status, headers, exc_info=None ) :
        cnttype = header_value( headers, 'content-type' )
        cntenc = header_value( headers, 'content-encoding' )
        # Compress only if content-type is 'text/*' or 'application/*'
        typeok = cnttype and \
                 (cnttype.startswith('text/') or cnttype.startswith('application/'))
        self.compressible = \
            True if typeok and ('zip' not in cnttype) and (not cntenc) else False
        self.compressible and headers.append(('content-encoding', 'gzip'))
        remove_header(headers, 'content-length')
        self.headers = headers
        self.status = status
        return self.buffer.write

    def process( self, compress_level, start_response ) :
        if self.app_iter is not None :
            output = gzip.GzipFile(
                        mode='wb', compresslevel=compress_level,
                        fileobj=self.buffer
                     ) if self.compressible else self.buffer
            [ output.write(s) for s in self.app_iter ]
            self.compressible and output.close()

            content_length = self.buffer.tell()
            CONTENT_LENGTH.update(self.headers, content_length)
            start_response( self.status, self.headers )
            content = self.content()
            self.append(content)
        else :
            start_response( self.status, self.headers )
        return

    def content( self ) :
        out = self.buffer
        out.seek(0)
        s = out.getvalue()
        out.close()
        return s
