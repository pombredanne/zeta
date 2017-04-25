# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Permission Via Mapping and Hierarchy"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :

import types

class PMSystem( object ) :
    """Mapping system for granting permissions for CRUDing access. The map
    object should in the following format."""

    def __init__( self, name, context, maps, children=[] ) :
        """context - must be a function that returns a literal
           map     - must be a permission map, supporting literal lookup.
           children- A children of PMSystem()"""

        self.name     = name
        self.maps     = maps
        self.context  = context
        self.children = children

    def check( self, literals, allliterals=False, context=None ) :
        """Check whether the permission map has 'literals' match. If the
        match does not succeed, then the child PMSystems are checked."""

        # Fetch the permission maps.
        if isinstance( self.maps, types.FunctionType ) :
            maps = self.maps()
        else :
            maps = self.maps

        # Fetch the context.
        ctxts = context or self.context
        if isinstance( ctxts, types.FunctionType ) :
            ctxts = ctxts()
        else :
            ctxts = ctxts

        # Check permission for this node.
        #   for each context value index into the map and fetch and collect 
        #   permission names. Compare the fetched (granted) permissions with
        #   requested permissions (`literals`)
        if maps and ctxts :
            domain = []
            [ domain.extend( maps.get( ctxt, [] )) for ctxt in ctxts ]
            macro = allliterals and all or any
            if literals and macro([ l in domain for l in literals ]) :
                return True

        # If permission is not granted at this node, then descend into its
        # children
        for c in self.children :
            if c.check( literals, allliterals=allliterals, context=context ) :
                return True
        else :
            # Give up !!.
            return False
