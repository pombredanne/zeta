# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Pylons environment configuration"""

# -*- coding: utf-8 -*-

# Gotchas : None
# Notes   : None
#   * The environment loading sequence, 
#       * Populate the `config` dict with pythonized objects
#       * Create the sysentries_cfg for the purpose of populating the 
#         system table if the application is installed or upgraded.
#   * Always use syscomp.get_entry to consume system fields.
#   * Note that, the .ini file is not automatically upgraded, so a config
#     options might not even be entered in the .ini file, so always use
#       config.get( '....', <def-string> )
# Todo    : None

import os
from   os.path                            import join, isfile
import re

from   mako.lookup                        import TemplateLookup
from   pylons.error                       import handle_mako_error
from   pylons                             import config
from   pylons                             import request, response, session
from   pylons.controllers.util            import abort
from   sqlalchemy                         import engine_from_config
from   pylons.configuration               import PylonsConfig
from   paste.util.import_string           import eval_import

import zeta.lib.app_globals               as app_globals
import zeta.lib.helpers                   as h
from   zeta.lib.cache                     import cachemanager
from   zeta.lib.constants                 import *
from   zeta.config.routing                import *
from   zeta.model                         import init_model, meta, create_models
from   zeta.ccore                         import ComponentManager
from   zeta.comp.environ                  import open_environment
import zeta.auth.perm                     as permmod

try :
    from   pylons           import tmpl_context as c
except ImportError :
    import pylons
    pylons.tmpl_context = {}
    from   pylons           import tmpl_context as c

dirname = os.path.dirname

dbversion   = u'1.2'
zetaversion = u'0.71b1'
zetacreators= u'SKR Farms (P) Ltd'

pkg_path    = dirname( dirname( dirname( __file__ )))   # zeta package path
root        = join( pkg_path, 'zeta' )                  # zeta module root.
envpath     = ''
paths       = dict( root=root,
                    controllers = join( root, 'controllers' ),
                    static_files= '',
                    templates   = [ join( root, 'templates-dojo' ) ]
                  )
tmplmoddir  = None
tckfilters  = []

compmgr = userscomp = syscomp = attcomp = attachcomp = liccomp = None
projcomp = prjcomp = revcomp = revwcomp = tagcomp = tckcomp = None
tlcomp = vcscomp = votecomp = votcomp = None
wikicomp = xintcomp = xicomp = srchcomp = zmailcomp = mailcomp = vfcomp = None

# Now, carefully read this comment.
# All the configuration parameters from the .ini file are available under
# `config` object. Since this `config` object is shared with pylons and our
# app, the whole initialization sequence is a bit screwed. In our case, we
# need to access the `config` object while,
#   1. Application setup (websetup.py)
#   2. Application run-time
#   3. Unit-testing.
#
# To get compatibility with run-time and unit testing, 
#   h.fromconfig()
# api is defined. It will try to intelligently use the right config object.
#
# On top of it, websetup.py, will setup the following attribute
# `websetupconfig` once a valid config object is initialized during the setup
# time. h.fromconfig() will now check for this attribute.
websetupconfig = None


def load_environment( global_conf, app_conf, userscomp=None ) :
    """Configure the Pylons environment. Will be executed only once, when
    the application is started."""
    global compmgr, tckfilters
    config = PylonsConfig()

    do_paths( app_conf )
    parseconfig( config, global_conf, app_conf )
    setup_sysentries_cfg( config )

    # Load components
    compmgr = config['compmgr'] = open_environment( config )
    compmgr.config = config
    loadcomponents( config, global_conf, app_conf )

    # Load complex configuration files
    h.mstnccodes   = open( config['zeta.mstnccodes'] ).read()
    h.tckccodes    = open( config['zeta.tckccodes'] ).read()
    h.webanalytics = ''
    if isfile( config['zeta.webanalytics'] ) :
        h.webanalytics = open( config['zeta.webanalytics'] ).read()

    try :
        tckfilters = eval( open( config['zeta.tckfilters'] ).read() )
    except :
        tckfilters = []

    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    init_model( engine )

    return config

def setup_environment( global_conf, app_conf ) :
    """Configure the Pylons environment via the ``pylons.config`` object, will
    be executed when the application is setup"""
    global compmgr
    config = PylonsConfig()
    do_paths( app_conf )
    parseconfig( config, global_conf, app_conf )
    setup_sysentries_cfg( config )

    # Load components
    compmgr = config['compmgr'] = open_environment( config )
    compmgr.config = config
    loadcomponents( config, global_conf, app_conf )

    return config

def setup_models( config, userscomp ) :
    """Initialize and setup database tables"""
    # Gotcha : Workaround to load 'userscomp'.
    config['userscomp'] = userscomp

    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    init_model( engine )
    create_models( engine,
                   config,
                   sysentries_cfg=meta.sysentries_cfg,
                   permissions=permmod.permissions
                 )
    return config


## ----------------------------------------------------------------------##

def do_paths( app_conf ) :
    """setup environment directories"""
    global envpath, paths 

    if not envpath :
        # Fix the environment path for zeta
        envpath = app_conf.get( 'zeta.envpath', '' )
        if not envpath :
            envpath = join( pkg_path, 'defenv' )
            app_conf['zeta.envpath'] = envpath

        # Pylons paths
        template_dir = app_conf.get( 'zeta.template_dir', '' )
        public_dir   = app_conf.get( 'zeta.public_dir', '' )
        if template_dir :
            paths['templates'] = [ template_dir ]
        paths['static_files'] = public_dir or join( envpath, 'public' )

def loadcomponents( config, global_conf, app_conf ) :
    from   zeta.auth.users          import UserComponent
    from   zeta.comp.system         import SystemComponent
    from   zeta.comp.attach         import AttachComponent
    from   zeta.comp.license        import LicenseComponent
    from   zeta.comp.project        import ProjectComponent
    from   zeta.comp.review         import ReviewComponent
    from   zeta.comp.tag            import TagComponent
    from   zeta.comp.ticket         import TicketComponent
    from   zeta.comp.timeline       import TimelineComponent
    from   zeta.comp.vcs            import VcsComponent
    from   zeta.comp.vote           import VoteComponent
    from   zeta.comp.wiki           import WikiComponent
    from   zeta.comp.xinterface     import XInterfaceComponent
    from   zeta.comp.xsearch        import XSearchComponent
    from   zeta.comp.zmail          import ZMailComponent
    from   zeta.comp.forms          import VForm
    global userscomp, syscomp, attcomp, attachcomp, liccomp, projcomp, prjcomp,\
           revcomp, revwcomp, tagcomp, tckcomp, tlcomp, vcscomp, votecomp, \
           votcomp, wikicomp, xintcomp, xicomp, srchcomp, zmailcomp, mailcomp, \
           vfcomp

    userscomp = config['userscomp'] = UserComponent(compmgr)
    syscomp = SystemComponent( compmgr )
    attcomp = attachcomp = AttachComponent( compmgr )
    liccomp = LicenseComponent( compmgr )
    projcomp = prjcomp = ProjectComponent( compmgr )
    revcomp = revwcomp = ReviewComponent( compmgr )
    tagcomp = TagComponent( compmgr )
    tckcomp = TicketComponent( compmgr )
    tlcomp = TimelineComponent( compmgr )
    vcscomp = VcsComponent( compmgr )
    votecomp = votcomp = VoteComponent( compmgr )
    wikicomp = WikiComponent( compmgr )
    xintcomp = xicomp = XInterfaceComponent( compmgr )
    srchcomp = XSearchComponent( compmgr )
    zmailcomp = mailcomp = ZMailComponent( compmgr, config=config )
    vfcomp = VForm( compmgr )
    return None

def parseconfig( config, global_conf, app_conf ) :
    """Configure the Pylons environment via the ``pylons.config`` object"""
    global tmplmoddir
    config.init_app( global_conf, app_conf, package='zeta', paths=paths )

    if config.has_key( 'zetaversion' ) :
        return

    # pylons configuration
    config['routes.map']         = make_map( config )
    config['pylons.app_globals'] = app_globals.Globals( config )
    config['pylons.h']           = h
    config['zeta.pkg_path']      = pkg_path
    config['zeta.envpath']       = envpath
    config['zeta.pageheader']    = config['zeta.pageheader'] == 'True'
    # config['pylons.strict_tmpl_context'] = False
    
    # Parse fields that will be persisted in system table.
    config['zeta.siteadmin']     = unicode( config['zeta.siteadmin'] )
    config['pylons.package']     = unicode( config['pylons.package'] )
    config['zeta.timezone']      = unicode( config['zeta.timezone'] )
    config['zeta.unicode_encoding'] = unicode( config['zeta.unicode_encoding'] )
    config['zeta.sitename']      = unicode( config['zeta.sitename'] )
    config['zeta.envpath']       = unicode( config['zeta.envpath'] )
    config['zeta.welcomestring'] = unicode( config['zeta.welcomestring'] )
    config['zeta.userrel_types'] = map( lambda x : unicode(x), 
                                        h.parse_csv( config['zeta.userrel_types'] )
                                      )
    config['zeta.projteamtypes'] = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.projteamtypes'] )
                                      )
    config['zeta.ticketstatus']  = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.ticketstatus'] )
                                      )
    config['zeta.tickettypes']   = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.tickettypes'] )
                                      )
    config['zeta.ticketseverity']= map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.ticketseverity'] )
                                      )
    config['zeta.reviewnatures'] = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.reviewnatures'] )
                                      )
    config['zeta.reviewactions'] = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.reviewactions'] )
                                      )
    config['zeta.wikitypes']     = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.wikitypes'] )
                                      )
    config['zeta.vcstypes']      = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.vcstypes'] )
                                      )
    config['zeta.ticketresolv']  = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.ticketresolv'] )
                                      )
    config['zeta.specialtags']   = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.specialtags'] )
                                      )
    config['zeta.def_wikitype']  = unicode( config['zeta.def_wikitype'] )
    config['zeta.userpanes']     = map( lambda x : unicode(x),
                                        h.parse_csv( config['zeta.userpanes'] )
                                      )

    # Fields for run-time.
    config['dbversion']          = dbversion
    config['zetaversion']        = zetaversion
    if not config['zeta.mstnccodes'] :
        config['zeta.mstnccodes'] = join( envpath, 'public', 'mstnccodes.json' )
    if not config['zeta.tckccodes'] :
        config['zeta.tckccodes']  = join( envpath, 'public', 'tckccodes.json' )
    if not config.get( 'zeta.tckfilters', None ) :
        config['zeta.tckfilters'] = join( envpath, 'public', 'tckfilters.pyd' )

    # Create the Mako TemplateLookup, with the default auto-escaping
    tmplmoddir = join( app_conf['cache_dir'], 'templates' )
    config['pylons.app_globals'].mako_lookup = \
        TemplateLookup(
            directories=paths['templates'],
            error_handler=handle_mako_error,
            module_directory=tmplmoddir,
            input_encoding='utf-8',
            output_encoding=config['zeta.unicode_encoding'],
            #filesystem_checks=config['mako.filesystem_checks']
            imports=['from webhelpers.html import escape'],
            default_filters=['escape']
        )

    # Setup cache object.
    #from zeta.lib.upgradeenv import cleardata
    #cleardata( envpath )
    config['cachemgr'] = cachemanager( envpath )

    return config


def setup_sysentries_cfg( config ) :
    """After all the configuration (both app-wide and site-wide) options are
    parsed and setup, this function should be called to populate them into a
    dictionary, which can be eventually used to create, modify, validate
    system entries from System table in the DataBase.
    If the system table is already created, then the configuration will be
    overwritten by entries in the table."""

    # The only purpose of this dictionary is collect the data from .ini file and
    # reflect them in the database.

    if not meta.sysentries_cfg :
        meta.sysentries_cfg = {
            u'product_name'     : config['pylons.package'],
            u'product_version'  : config['zetaversion'],
            u'database_version' : config['dbversion'],

            u'envpath'          : config['zeta.envpath'],

            u'siteadmin'        : config['zeta.siteadmin'],
            u'sitename'         : config['zeta.sitename'],
            u'timezone'         : config['zeta.timezone'],
            u'unicode_encoding' : config['zeta.unicode_encoding'],

            u'welcomestring'    : config['zeta.welcomestring'],
            u'specialtags'      : ', '.join(config['zeta.specialtags']),
            u'projteamtypes'    : ', '.join(config['zeta.projteamtypes']),
            u'ticketstatus'     : ', '.join(config['zeta.ticketstatus']),
            u'tickettypes'      : ', '.join(config['zeta.tickettypes']),
            u'ticketseverity'   : ', '.join(config['zeta.ticketseverity']),
            u'ticketresolv'     : ', '.join(config['zeta.ticketresolv']),
            u'reviewnatures'    : ', '.join(config['zeta.reviewnatures']),
            u'reviewactions'    : ', '.join(config['zeta.reviewactions']),
            u'vcstypes'         : ', '.join(config['zeta.vcstypes']),
            u'wikitypes'        : ', '.join(config['zeta.wikitypes']),
            u'def_wikitype'     : config['zeta.def_wikitype'],
            u'userrel_types'    : ', '.join(config['zeta.userrel_types']),
            u'strictauth'       : unicode(config.get( 'zeta.strictauth', u'False' )),
            u'googlemaps'       : unicode(config.get( 'zeta.googlemaps', u'' )),
            u'userpanes'        : config['zeta.userpanes'],
            u'regrbyinvite'     : unicode(config.get( 'zeta.regrbyinvite', u'False' )),
            u'invitebyall'      : unicode(config.get( 'zeta.invitebyall', u'False' )),

            # This entry is stringified python dictionary
            u'interzeta'        : u'{}', 
        }

    return meta.sysentries_cfg


def cleantmplmodules() :
    """Clear Mako generated template modules that are cached"""
    cmd = 'rm -rf %s' % tmplmoddir
    os.system( cmd )
