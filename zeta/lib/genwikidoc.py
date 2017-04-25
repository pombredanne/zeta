# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Library function to generate wiki documents from source code."""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : None

import sys
import types
import os
from   os.path      import join, dirname, abspath

stylehdr = """[< <style type="text/css"> >]
    h1, h2, h3, h4, h5 { 
        margin : 0px;
        padding: 5px 0px 2px 3px;
        background-color : #EAEAFC;
        border-bottom: 1px solid #CCCCCC;
    }
[< </style> >]
"""

schemadochdr = """
Auto generated file. Based on SQLalchemy schema definitions
-----------------------------------------------------------

( Attrs  Column_name  Column_type  Length  Constraints )

  ( attrs P - primary_key, U - Unique, N - Nullable )


"""
def schemadoc( docsdir, tables ) :

    fd      = open( join( docsdir, 'schema'), 'w' )
    fd.write( schemadochdr )
    tdata   = { 'table_name'   : '',
                'mysql_engine' : ''
              }
    cdata   = { 'column_name'  : '',
                'data_type'    : '',
                'limit'        : '',
                'constraint'   : '',
                'attributes'   : '',    # P-primarykey, N-Nullable, U-unique
              }

    for t in tables :
        table = {}
        table.update( tdata )
        table['table_name']   = t.name
        table['mysql_engine'] = t.kwargs.get( 'mysql_engine', 'NA' )
        fd.write( 
            "[ %s ] %s : " % ( table['table_name'], table['mysql_engine'] )
        )
        fd.write( "\n\n" )
        for c in t.columns :
            col = {}
            col.update( cdata )
            attr =  c.unique      and 'U' or '_'
            attr += c.nullable    and 'N' or '_'
            attr += c.primary_key and 'P' or '_'
            constraints = ', '.join([ f.target_fullname for f in c.foreign_keys ])
            col['column_name'] = c.name
            col['data_type']   = str(c.type).split('(')[0]
            col['limit']       = getattr( c.type, 'length', 'NA' )
            col['constraint']  = constraints
            col['attributes']  = attr

            fd.write( "  %-4s %-25s  %-15s  %-6s %-25s\n" % \
                      ( col['attributes'], col['column_name'], 
                        col['data_type'], col['limit'], col['constraint'] )
                    )
        fd.write( "\n\n" )


zwhtmltmpl = """
{{ Toc( float='right' ) }}

%s

== List of Templated Tags

%s
"""
def zwhtml( docsdir ) :
    import zwiki.ttags as tt

    fd     = open( join( docsdir, 'ZWTemplateTags'), 'wb')
    mods   = sorted([ attr for attr in dir(tt) if attr[:3] == 'tt_' ])
    docstr = '\n'.join([ getattr( getattr( tt, attr), 'func_doc' ) 
                         for attr in mods ])
    wikitext = zwhtmltmpl % ( tt.wikidoc, docstr )
    fd.write( stylehdr + wikitext )


zwmacrostmpl = """
{{ Toc( float='right' ) }}

%s

== List of ZWiki macros

%s
"""
def zwmacros( docsdir ) :
    import zwiki.macro as zwm

    fd   = open( join( docsdir, 'ZWMacros'), 'wb' )
    macronames = zwm.macronames[:]
    macronames.remove( 'ZWMacro' )
    macronames.sort()
    docstr = '\n'.join([ getattr(
                          sys.modules[ getattr( zwm, macroname ).__module__ ],
                          'wikidoc',
                          ''
                         ) for macroname in  macronames ])
    wikitext = zwmacrostmpl % ( zwm.__doc__, docstr )
    fd.write( stylehdr + wikitext )


zweexttmpl = """
{{ Toc( float='right' ) }}

%s

== List of ZWiki extensions

%s
"""
def zwextensions( docsdir ) :
    import zwiki.zwext as zwe

    fd = open( join( docsdir, 'ZWExtensions'), 'wb' )
    extnames = zwe.extnames[:]
    extnames.remove( 'ZWExtension' )
    extnames.sort()
    docstr = '\n'.join([ sys.modules[ getattr( zwe, extname ).__module__ ].wikidoc
                         for extname in extnames ])
    wikitext = zweexttmpl % ( zwe.__doc__, docstr )
    fd.write( stylehdr + wikitext )


xmlrpctmpl = """
{{ Toc( float='right' ) }}

== XMLRPC API
XMLRPC is a way of interfacing with ''ZETA server'' via HTTP.

== List of XMLRPC API

%s
"""
def xmlrpc( docsdir ) :
    import zeta.controllers.xmlrpc as x

    fd      = open( join( docsdir, 'XmlRpcApi'), 'wb' )
    docstr  = ''
    attrs   = sorted( dir( x.XmlrpcController ))
    for attrname in attrs :
        attr = getattr( x.XmlrpcController, attrname )
        if isinstance( attr, types.MethodType ) and attrname[0] != '_' :
            docstr += '\n\n%s' % attr.func_doc

    wikitext = xmlrpctmpl % docstr
    fd.write( stylehdr + wikitext )


pasteradmintmpl = """
{{ Toc( float='right' ) }}

== Paster Admin commands
Paster-admin is a command line tool to manage the site.

== List of Commands

%s
"""
def pasteradmin( docsdir ) :
    import zeta.controllers.pasteradmin as pa

    fd      = open( join( docsdir, 'PasterAdmin'), 'wb' )
    docstr  = ''
    attrs   = sorted( dir( pa.PasteradminController ))
    for attrname in attrs :
        attr = getattr( pa.PasteradminController, attrname )
        if isinstance( attr, types.MethodType ) and attrname[0] != '_' :
            docstr += '\n\n%s' % attr.func_doc

    wikitext = pasteradmintmpl % docstr
    fd.write( stylehdr + wikitext )


pygmenttmpl = """
== List of formats supported by '/ pygments /'

{{{ Html
<table style="width: %s; margin-left: 10px;">
    <tr style="border-bottom: 1px solid gray">
        <th style="padding: 2px;">Name</th>
        <th style="padding: 2px;">Alias</th>
        <th style="padding: 2px;">File-extensions</th>
        <th style="padding: 2px;">Mime-types</th>
    </tr>
    %s
</table>
}}}
"""
pygrowtmpl = """
<tr>
    <td style="font-weight: bold; padding: 2px;">%s</td>
    <td style="font-style: italic; padding: 2px;">%s</td>
    <td style="padding: 2px;">%s</td>
    <td style="padding: 2px;">%s</td>
</tr>
"""
def pygments( docsdir ) :
    import pygments.lexers as pl

    fd      = open( join( docsdir, 'pygments'), 'wb' )
    formats = sorted( pl.get_all_lexers(), key=lambda x : x[0] )
    docstr  = ''
    for name, alias, fnames, mimetypes in formats :
        docstr += pygrowtmpl % ( name, ', '.join(alias), ', '.join(fnames),
                                 ', '.join(mimetypes) )
    wikitext = pygmenttmpl % ( '100%', docstr )
    fd.write( stylehdr + wikitext )


def vimdoc( docsdir ) :
    import imp
    vimfile = abspath( join( dirname( __file__ ),
                             '../extras/vim/plugin/zetavim.py' ))
    zetavim = imp.load_source( 'zetavim', vimfile )
    fd      = open( join( docsdir, 'VimIntegration' ), 'wb' )
    docstr  = zetavim.__doc__

    docfns  = [ 'addprofile', 'listprofiles', 'clearprofiles', 'connect',
                'listprojects', 'listgw', 'newgw', 'fetchgw', 'listwiki',
                'newwiki', 'fetchwiki', 'listticket', 'newtck', 'fetchticket',
                'addtags', 'deltags', 'vote', 'fav', 'nofav', 'comment' ]

    docstr  = docstr + '\n\n'.join( getattr( zetavim, 'doclist' ))

    wikitext = docstr
    fd.write( stylehdr + wikitext )
