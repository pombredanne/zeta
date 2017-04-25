# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Script to handle staticwiki sub-command from paster
        zwiki upgradedb"""

################ NOT USED. Instead pasteradmin controller is used ##########

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
# Todo    : 
#   1. Should we implement authentication mechanism to access database via
#      'paster zwiki' commands ?

from   paste.script          import command
from   pylons                import config
from   zeta.comp.environ     import open_environment

class CmdZwiki( command.Command ) :
    max_args = 1
    min_args = 1

    usage       = "upgradedb"
    summary     = "Upgrade the translated HTML content to latest zwiki"
    group_name  = "zeta_zwiki"

    parser      = command.Command.standard_parser( verbose=True )

    def command( self ) :
        """Handle the sub-command"""
        from   zeta.comp.system  import SystemComponent
        from   zeta.comp.ticket  import TicketComponent
        from   zeta.comp.wiki    import WikiComponent

        if len(self.args) == 1 and self.args[0] == 'upgradedb' :
            syscomp = SystemComponent( compmgr )
            tckcomp = TicketComponent( compmgr )
            wikicomp= WikiComponent( compmgr )

            count = syscomp.upgradewiki()
            print "Upgraded %s static wiki pages ... ok" % count
            count = tckcomp.upgradewiki()
            print "Upgraded %s ticket comments ... ok" % count
            cnt_wcnt, cnt_wcmt = wikicomp.upgradewiki()
            print "Upgraded %s wiki contents and %s wiki comments ... ok" % \
                  ( cnt_wcnt, cnt_wcmt )
        else :
            print "Please provide a valid command. Use -h to know the usage ..."
