# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Functions to upgrade database from a previous version to current version.
The Database version is store in the 'system' table, while the current
database version supported by the application is available from the code.

"""
# Scope :
#
#   1. Table additions. Table deletions. Alter Tables.
#   2. Table schema modification.
#       * Changing the name and nature of un-constrained / constrained column.
#       * Changing the value(s) of one or more table column to different set.
#       * Adding or Deleting un-constrained / constrained column.
#       * Data transformations on table columns.
#
#   Upgradation can only happen from one verion to immediately next version.
#   So, be careful to write upgradation code dependant on rest of the
#   application.

from   __future__                   import with_statement
import os
from   os.path                      import join, isfile, dirname, splitext, \
                                           basename
from   hashlib                      import sha1

from   pylons                       import config

from   zeta.model.tables            import *
from   zeta.model                   import meta
from   zeta.lib.error               import *

g_user = u'admin'

def _sequence( dbver_db, dbver_app ) :
    """Sequence the upgradation from the current database version to the
    current database version supported by app"""
    versions  = dbversion_keys
    index_db  = versions.index( dbver_db )
    index_app = versions.index( dbver_app )
    if index_app < index_db :
        raise ZetaError(
            "Application's DB version is less than or equal to Database version"
        )
    elif index_app == index_db :
        print "No upgrade required for database"

    return  versions[index_db:index_app]


def upgradedb( dbver_db, dbver_app, defenv, appenv ) :
    """Upgrade the database from its current version to application compatible
    version"""
    #from   zeta.lib.upgradeenv import cleardata
    #cleardata( appenv )         # Clean data/cache, data/templates

    for ver in _sequence( dbver_db, dbver_app  ) :
        print "Upgrading database from version %s ..." % ver
        dbversions[ ver ]( defenv, appenv )


def upgradesw( file, path ) :
    """Helper function to push static wiki pages from File System to DB"""
    from zeta.config.environment    import syscomp
    
    print "  Pushing static-wiki page `%s` into Database ..." % path
    if isfile( file ) :
        syscomp.set_staticwiki(
                unicode(path), unicode( open(file).read() ), byuser=g_user )
    else :
        raise Exception( 'help/PasterAdmin file not found' )


def rmsw( paths ) :
    """Remove static wiki pages identified by lists of `paths`"""
    from zeta.config.environment    import syscomp
    
    for path in paths :
        syscomp.remove_staticwiki( paths=path, byuser=g_user )
        print "  removed static wiki, `%s`" % path


def upgradewithscripts( fromver, defenv, appenv ) :
    """Helper function detects sql scripts for each type of database and
    applies them to the current database.
    This way of upgrade is typically used for altering table schemas
    """
    scriptdir  = join( dirname(__file__), 'upgradescripts' )
    dbtype     = meta.engine.name
    scripts    = [ join( scriptdir, f )
                   for f in os.listdir( scriptdir ) 
                   if basename(f) == '%s.%s'%(fromver,dbtype) ]

    connection = meta.engine.connect()
    for script in scripts :
        print "  From script %s ..." % script
        stmts = open( script ).read().split( '\n\n' )
        for stmt in stmts :
            print "  Executing statement \n%s" % stmt
            connection.execute( stmt )
    connection.close()
    # Execute scripts


################# Upgrade from 1.1 to 1.2 ############################
def upgrade_1_1( defenv, appenv ) :
    """Upgrade database version from 1.1 to 1.2"""
    import zeta.lib.helpers           as h
    from   zeta.config.environment import syscomp, wikicomp, vcscomp, attachcomp

    # Upgrade with SQL scripts
    upgradewithscripts( '1_1', defenv, appenv )

    # Set created_on value for static_wiki table for older entries
    swikis = syscomp.updatecreatedon( byuser=g_user )
    print "  Updated `created_on` field for %s guest wiki entries" % len(swikis)

    # Update guest wiki pages' type attribute
    print "  Updating guest wiki pages' type attribute"
    swtype = wikicomp.get_wikitype(syscomp.get_sysentry('def_wikitype'))
    [ syscomp.set_staticwiki(sw.path, sw.text, swtype=swtype, byuser=g_user)
      for sw in syscomp.get_staticwiki() ]

    # Add wiki types,
    wikitypes = syscomp.get_sysentry( 'wikitypes' )
    wikitypes = h.parse_csv( wikitypes )
    addtypes  = h.WIKITYPES
    addtypes  = [ wt for wt in addtypes if wt not in wikitypes ]
    if addtypes :
        print "  Adding `%s` wikitype to system table" % addtypes
        wikitypes = ', '.join( wikitypes + addtypes )
        syscomp.set_sysentry({ 'wikitypes' : wikitypes }, byuser=g_user )
        print "  Adding `%s` wikitypes to wiki_type table" % wikitypes
        wikicomp.create_wikitype( addtypes, byuser=g_user )

    # Move attachment contents from database to envpath
    print "  Moving attachment contents from database to disk files "
    atts = attachcomp.get_attach()
    [ attachcomp.db2file(a)  for a in atts ]

    # Update the size field in attachment table.
    print "  Updating attachment size field in db table "
    [ attachcomp.updatesize(a) for a in atts ]

    # Add `hg` vcs type.
    vcstypes = syscomp.get_sysentry( 'vcstypes' )
    vcstypes = h.parse_csv( vcstypes )
    if 'hg' not in vcstypes :
        print "  Adding `hg` vcstype to system table"
        vcstypes = ', '.join( vcstypes + [ 'hg' ] )
        syscomp.set_sysentry({ 'vcstypes' : vcstypes }, byuser=g_user )
        print "  Adding `hg` vcstype to vcs_type table"
        vcscomp.create_vcstype( ['hg'], byuser=g_user )
    ## Should we explicitly create a table ???, 
    ## Create ticket_filter table
    #print "  Creating table for `ticket_filters`, `reviewset`, `vcsmount`\n"
    #meta.metadata.create_all( bind=meta.engine, checkfirst=True )

    ## Update `googlemaps` field in system table
    #print "  `googlemaps` should specify the generated key (No more boolean) ...\n"
    #entry   = { u'googlemaps' : u'' }
    #syscomp.set_sysentry( entry, byuser=g_user )

    ## Rename ZETA_ADMIN permission name to SITE_ADMIN permission name
    #print "  Changing permission name ZETA_ADMIN to SITE_ADMIN"
    #userscomp = config['userscomp']
    #userscomp.change_permname( 'ZETA_ADMIN', 'SITE_ADMIN', byuser=g_user )


################# Upgrade from 1.0 to 1.1 ############################
def upgrade_1_0( defenv, appenv ) :
    """Upgrade database version from 1.0 to 1.1"""
    import zeta.lib.helpers           as h
    from   zeta.config.environment    import syscomp, vcscomp, userscomp

    # Should we explicitly create a table ???, 
    # Create ticket_filter table
    print "  Creating table for `ticket_filters`, `reviewset`, `vcsmount`\n"
    meta.metadata.create_all( bind=meta.engine, checkfirst=True )

    # Update `googlemaps` field in system table
    print "  `googlemaps` should specify the generated key (No more boolean) ...\n"
    entry   = { u'googlemaps' : u'' }
    syscomp.set_sysentry( entry, byuser=g_user )

    # Rename ZETA_ADMIN permission name to SITE_ADMIN permission name
    print "  Changing permission name ZETA_ADMIN to SITE_ADMIN"
    userscomp.change_permname( 'ZETA_ADMIN', 'SITE_ADMIN', byuser=g_user )

    # Add `bzr` vcs type.
    vcstypes = syscomp.get_sysentry( 'vcstypes' )
    vcstypes = h.parse_csv( vcstypes )
    if 'bzr' not in vcstypes :
        print "  Adding `bzr` vcstype to system table"
        vcstypes = ', '.join( vcstypes + [ 'bzr' ] )
        syscomp.set_sysentry({ 'vcstypes' : vcstypes }, byuser=g_user )
        print "  Adding `bzr` vcstype to vcs_type table"
        vcscomp.create_vcstype( ['bzr'], byuser=g_user )


################# Upgrade from 0.9 to 1.0 ############################
def upgrade_0_9( defenv, appenv ) :
    """Upgrade database version from 0.9 to 1.0"""
    from zeta.config.environment    import syscomp

    print "  Adding `regrbyinvite` (default False) field to system table ...\n"
    entry   = { u'regrbyinvite' : u'False' }
    syscomp.set_sysentry( entry, byuser=g_user )

    print "  Adding `invitebyall` (default False) field to system table ...\n"
    entry   = { u'invitebyall' : u'False' }
    syscomp.set_sysentry( entry, byuser=g_user )

    print "  Adding `googlemaps` (default False) field to system table ...\n"
    entry   = { u'googlemaps' : u'' }
    syscomp.set_sysentry( entry, byuser=g_user )

    print "  Moving `strictauth` (%s) field to system table ...\n" % \
                config['zeta.strictauth']
    entry   = { u'strictauth' : unicode(config['zeta.strictauth']) }
    syscomp.set_sysentry( entry, byuser=g_user )

    # Upgrade with SQL scripts
    upgradewithscripts( '0_9', defenv, appenv )

    # Should we explicitly create a table ???
    print "  Creating table for `userinvitation`\n"
    meta.metadata.create_all( bind=meta.engine, checkfirst=True )

    # Upgrade Static wiki pages
    paths = [ 'help/pms',
              'help/vcs',
              'p_homepage',
            ]
    [ upgradesw( join(defenv, 'staticfiles', path), path ) for path in paths ]


################# Upgrade from 0.8 to 0.9 ############################
def upgrade_0_8( defenv, appenv ) :
    """Upgrade Database version from 0.8 to 0.9"""
    from zeta.config.environment    import syscomp

    print "Renaming static-wiki `p_frontpage` to `p_homepage` ..."
    sw = syscomp.get_staticwiki( u'p_frontpage' )
    msession = meta.Session()
    with msession.begin( subtransactions=True ) :
        sw.path = u'p_homepage'

    paths = [ 'help/ColorValue',
              'help/PasterAdmin',
              'help/XmlRpcApi',
              'help/ZWExtensions',
              'help/ZWMacros',
              'help/ZWTemplateTags',
              'help/admin',
              'help/features',
              'help/pms',
              'help/review',
              'help/ticket',
              'help/vcs',
              'help/zwiki',
            ]
    [ upgradesw( join(defenv, 'staticfiles', path), path ) for path in paths ]


################# Upgrade from 0.7 to 0.8 ############################
def upgrade_0_7( defenv, appenv ) :
    """Upgrade Database version from 0.7 to 0.8"""
    from zeta.config.environment    import userscomp

    print "Converting 'password' column values into message digest ..."
    users     = userscomp.get_user()
    oldpass   = dict([ (u.username, u.password) for u in users ])
    msession  = meta.Session()
    with msession.begin( subtransactions=True ) :
        for u in users :
            u.password = sha1( u.password ).hexdigest()

    # Verify
    newpass   = dict([ (u.username, u.password) for u in userscomp.get_user() ])
    assert len(newpass) == len(oldpass)
    for u in oldpass :
        assert unicode(newpass[u]) == unicode( sha1(oldpass[u]).hexdigest() )

    print "Converted %s user passwords" % len(users)


# List of all database versions that are upgradabale
dbversion_keys = [ '0.7', '0.8', '0.9', '1.0', '1.1', '1.2' ]
dbversions     = {
    '0.7' : upgrade_0_7,
    '0.8' : upgrade_0_8,
    '0.9' : upgrade_0_9,
    '1.0' : upgrade_1_0,
    '1.1' : upgrade_1_1,
    '1.2' : None,           # The latest version need not have upgrade functions
}

