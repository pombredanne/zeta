# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Setup the Tables and populate them with initial values"""

from   __future__         import with_statement
import os
from   hashlib            import sha1

from   pylons             import config

from   zeta.model         import meta
from   zeta.model.tables  import *
from   zeta.lib.constants import *

__all__  = [ 'create_models', 'delete_models' ]
g_byuser = u'admin'

def _system_table( config, sysentries_cfg ) :
    """`entries` is a dictionary of 'field': 'value' which should be populated
    into the database."""
    from zeta.config.environment    import syscomp
    syscomp.set_sysentry( sysentries_cfg, byuser=g_byuser )
    
def _permissions( config, permissions ) :
    from zeta.config.environment import userscomp

    userscomp.create_apppermissions( permissions, byuser=g_byuser )

def _user_table( config ) :
    from zeta.config.environment import userscomp

    msession  = meta.Session()
    with msession.begin( subtransactions=True ) :
        admin    = User( unicode(config['zeta.siteadmin']),
                         ADMIN_EMAIL,
                         sha1( ADMIN_PASSWORD ).hexdigest(),
                         DEFAULT_TIMEZONE 
                       )
        admininfo= UserInfo( config['zeta.siteadmin'],
                             config['zeta.siteadmin'],
                             config['zeta.siteadmin'],
                             None, None, None, None, None, None, None )
        admin.userinfo = admininfo
        msession.add(admin)

        anony    = User( u'anonymous',
                         ANONYMOUS_EMAIL,
                         sha1( ANONYMOUS_PASSWORD ).hexdigest(),
                         DEFAULT_TIMEZONE 
                       )
        anonyinfo= UserInfo( u'anonymous', u'anonymous', u'anonymous',
                             None, None, None, None, None, None, )
        anony.userinfo = anonyinfo
        msession.add(anony)

def _userrelation_types( config ) :
    from zeta.config.environment import userscomp

    userscomp.userreltype_create( config['zeta.userrel_types'],
                                  byuser=g_byuser )

def _projteam_types( config ) :
    from zeta.config.environment    import projcomp
    projcomp.create_projteamtype( config['zeta.projteamtypes'],
                                  byuser=g_byuser )

def _ticket_type( config ) :
    from zeta.config.environment    import tckcomp
    tckcomp.create_tcktype( config['zeta.tickettypes'], byuser=g_byuser )

def _ticket_status( config ) :
    from zeta.config.environment    import tckcomp
    tckcomp.create_tckstatus( config['zeta.ticketstatus'], byuser=g_byuser )

def _ticket_severity( config ) :
    from zeta.config.environment    import tckcomp
    tckcomp.create_tckseverity( config['zeta.ticketseverity'], byuser=g_byuser )

def _reviewcomment_nature( config ) :
    from   zeta.comp.review   import ReviewComponent
    from zeta.config.environment    import revcomp
    revcomp.create_reviewnature( config['zeta.reviewnatures'], byuser=g_byuser )

def _reviewcomment_action( config ) :
    from zeta.config.environment    import revcomp
    revcomp.create_reviewaction( config['zeta.reviewactions'], byuser=g_byuser )

def _vcs_type( config ) :
    from zeta.config.environment    import vcscomp
    vcscomp.create_vcstype( config['zeta.vcstypes'], byuser=g_byuser )

def _wiki_type( config ) :
    from zeta.config.environment    import wikicomp
    wikicomp.create_wikitype( config['zeta.wikitypes'], byuser=g_byuser )

def _special_tags( config ) :
    from zeta.config.environment    import tagcomp
    for tagname in config['zeta.specialtags'] :
        tagcomp.create_tag( tagname, byuser=g_byuser )

def _staticwiki( config ) :
    from zeta.config.environment    import syscomp
    rootdir = os.path.abspath( os.path.join( config['zeta.envpath'],
                                             DIR_STATICWIKI ))
    print "   Pushing static files from %s ... " % rootdir
    files, skipped = syscomp.push_staticwiki( rootdir, byuser=g_byuser )
    for f in files :
        print "    ", f
    print "   Skipped files ... "
    for f in skipped :
        print "    ", f


def create_models( engine, config, tables=None, sysentries_cfg=None,
                   permissions=None ) :
    """Create all the Tables."""
    meta.metadata.create_all( bind=engine, checkfirst=True, tables=tables )
    _user_table( config )
    if sysentries_cfg :
        _system_table( config, sysentries_cfg )
    if permissions :
        _permissions( config, permissions )
    _userrelation_types( config )
    _projteam_types( config )
    _ticket_status( config )
    _ticket_type( config )
    _ticket_severity( config )
    _reviewcomment_nature( config )
    _reviewcomment_action( config )
    _vcs_type( config )
    _wiki_type( config )
    _special_tags( config )

    # Populate static files from the default environment into the database.
    _staticwiki( config )


def delete_models( engine, tables=None ) :
    meta.metadata.drop_all( bind=engine, tables=tables )
    meta.Session.close_all()    # To expunge in-memory instances of table entries
