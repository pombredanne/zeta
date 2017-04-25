# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Script to handle 'backup' sub-command from paster,
    backup -z <bkpcmd>
    
    bkpcmd,     db (or) db,env (or) all
                default is all 
"""

from paste.script import command

class Backup( command.Command ) :
    max_args = 1
    min_args = 1

    usage       = "bkpcmd"
    summary     = "Backup database and environment into a tar ball"
    group_name  = "zeta_backup"

    parser      = command.Command.standard_parser( verbose=True )
    parser.add_option(              # Option for gzipping the tar-ball
        '-z',
        action='store_true',
        dest='gzip',
        help="Gzip the tar-ball"
    )

    def command( self ) :
        """Handle the backup sub-command"""
        pass
