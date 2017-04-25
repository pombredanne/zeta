# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

from   zeta.ccore       import Component, ComponentManager, Interface, \
                               ExtensionPoint

class ZetaCompmgr( ComponentManager ) :
    """Component manager for zeta. The manager is refered to as the 
    environment."""
    config = None
    # Instance attributes
    # TODO : Manage Component Loading.
    def __init__( self, environ=None, start_response=None ) :
        ComponentManager.__init__( self )


def open_environment( config ) :
    """Create an instance of the component manager and return the same."""
    env         = ZetaCompmgr()
    env.config  = config
    return env
