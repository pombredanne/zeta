# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Script to handle staticwiki sub-command from paster"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    :
#   1. Should we implement authentication mechanism to access database via
#      'paster staticwiki' commands ?

from   os.path               import abspath

from   paste.script          import command

from   zeta.comp.environ     import open_environment

class CmdStaticWiki( command.Command ) :
    max_args = 2
    min_args = 2

    usage       = "action <dir>"
    summary     = "Pull or push static wiki tree from file system to DataBase"
    group_name  = "zeta_staticwiki"

    parser      = command.Command.standard_parser( verbose=True )

    def command( self ) :
        """Handle the sub-command"""
        from   zeta.comp.system  import SystemComponent

        # Create component manager.
        compmgr = open_environment( False )

        syscomp = SystemComponent( compmgr )

        if len(self.args) == 2 :
            action  = self.args[0]
            rootdir = abspath ( self.args[1] )
        else :
            action  = ''
            rootdir = ''

        if action == 'pull' :
            print "Pulling Static wiki files into %s ..." % rootdir
            files   = syscomp.pull_staticwiki( rootdir )
            for f in files :
                print "    ", f
        elif action == 'push' :
            print "Pushing Static wiki files from %s ..." % rootdir
            files, skipped = syscomp.push_staticwiki( rootdir )
            for f in files :
                print "    ", f
            print "Skipped files ..."
            for f in skipped :
                print "    ", f
        else :
            print "Please provide a valid command. Use -h to know the usage ..."

