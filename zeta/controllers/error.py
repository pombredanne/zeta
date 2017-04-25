import cgi
from   os.path                 import join

from   paste.urlparser         import StaticURLParser
from   pylons                  import request
from   pylons.controllers.util import forward
from   pylons.middleware       import error_document_template, media_path
from   webhelpers.html.builder import literal

from   zeta.lib.base           import BaseController
import zeta.lib.helpers        as h

class ErrorController(BaseController):
    """Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.
    
    """
    def __before__( self, environ=None ) :
        self.beforecontrollers( environ=environ )

    def document(self):
        """Render the error document"""
        resp = request.environ.get('pylons.original_response')
        # Gotcha : 
        #   When tested for test_account, sign-in after sign-in the
        #   request `message` seems to be absent. Something to do with
        #   multigate ???
        content = literal(resp.body)
        if not content :
            content = request.GET.get('message') or ''
            content = cgi.escape(content)
        #page = error_document_template % \
        #    dict(prefix=request.environ.get('SCRIPT_NAME', ''),
        #         code=cgi.escape(request.GET.get('code', str(resp.status_int))),
        #         message=content)
        #return page
        return content

    def img(self, id):
        """Serve Pylons' stock images"""
        return self._serve_file(join(media_path, 'img'), id)

    def style(self, id):
        """Serve Pylons' stock stylesheets"""
        return self._serve_file(join(media_path, 'style'), id)

    def _serve_file(self, root, path):
        """Call Paste's FileApp (a WSGI application) to serve the file
        at the specified path
        """
        static = StaticURLParser(root)
        request.environ['PATH_INFO'] = '/%s' % path
        return static(request.environ, self.start_response)
