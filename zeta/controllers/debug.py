import logging

from   pylons                  import request, response
from   pylons                  import config
from   pylons                  import session
from   pylons                  import tmpl_context as c
from   pylons.controllers.util import abort

from   zeta.lib.base           import BaseController, render

log = logging.getLogger( __name__ )

def _dumpdict( d ) :
    """
    """
    skeys = d.keys()
    skeys.sort()
    return '\n'.join([ "%s = %s " % (k, d[k]) for k in skeys ])

def _dumpnesteddict( d, prefix="" ) :
    """
    """
    out = ''
    skeys = d.keys()
    skeys.sort()
    for k in skeys :
        if isinstance( d[k], dict ) :
            out += prefix + "%s = \n" % k
            out += _dumpnesteddict( d[k], "    " )
        else :
            out += prefix + "%s = %s \n" % (k, d[k])
    return out


class DebugController( BaseController ) :

    def __before__( self, environ ) :
        self.beforecontrollers( environ=environ )

    def index( self ) :
        if not config['debug'] :
            return ''
        queries = request.params.getall( 'var' )
        output = ''
        if not queries or 'all' in queries :
            queries = [ 'config', 'app_globals', 'request', 'session' ]
        for v in queries :
            if v == 'config' :
                output += "\n------------ Pylons Config ----\n"
                output += _dumpnesteddict( config )
            if v == 'app_globals' :
                output += "\n------------ Pylons App-Globals----\n"
                output += _dumpnesteddict( config['pylons.app_globals'].__dict__ )
            if v == 'request' :
                output += "\n------------ Pylons Request ----\n"
                output += "\n------------ request.environ ----\n"
                output += _dumpnesteddict( request.environ )
                output += "\n------------ request.urlvars ----\n"
                output += _dumpdict( request.urlvars )
                output += "\n------------ request.params ----\n"
                p = request.params
                output += '\n'.join([ "%s" % p.getall( k ) for k in p ])
                output += "\n------------ request.headers ---\n"
                output += _dumpdict( request.headers )
                output += "\n------------ request.cookies ----\n"
                output += _dumpdict( request.cookies )
            if v == 'session' :
                output += "\n------------ Pylons Session ----\n"
                output += _dumpnesteddict( session )
                    
        response.content_type = 'text/plain'
        return output
