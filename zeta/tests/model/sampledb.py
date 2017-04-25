# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Zeta test package for SQL models.

SQL tables are modeled into python objects and this package provides several
test cases to verify and validate the models, both for functionality and
performance.
"""

import random

from   sqlalchemy               import engine_from_config
import pylons.test
from   paste.util.import_string import eval_import
import datetime                 as dt

from   zeta.auth.perm           import permissions
from   zeta.model               import init_model, create_models, delete_models
from   zeta.model               import meta
from   populate                 import pop_permissions, pop_user, \
                                       pop_licenses, pop_projects, pop_tickets, pop_reviews, \
                                       pop_vcs, pop_wikipages, fix_mstn_duedate, fix_ts_duedate
from   zeta.tests.tlib          import *

# TODO :
#   1. Populate the database with sample data during the setup time and dump 
#      the entire database into a file. Later once all the test under this
#      package is executed, dump the entire database into another file and
#      compare it with the first one. Both should match

config          = pylons.test.pylonsapp.config

no_of_users     = 15
no_of_relations = 4
no_of_tags      = 4
no_of_attachs   = 1
no_of_projects  = 9
no_of_tickets   = 350
no_of_vcs       = no_of_projects * 2
no_of_reviews   = 50
no_of_wikis     = 50
#no_of_users     = 100
#no_of_relations = 10
#no_of_tags      = 4
#no_of_attachs   = 1
#no_of_projects  = 20
#no_of_tickets   = 10000
#no_of_vcs       = no_of_projects * 2
#no_of_wikis     = 200
#no_of_reviews   = 200

seed    = None

def setUpModule() :
    global seed
    seed = config['seed'] and int(config['seed']) or genseed()
    random.seed( seed )
    # Setup SQLAlchemy database engine
    engine = engine_from_config( config, 'sqlalchemy.' )
    #init_model( engine )
    create_models( engine, config, sysentries_cfg=meta.sysentries_cfg, 
                   permissions=permissions )
    config['userscomp'] = meta.userscomp
    # Populate DataBase with sample entries
    try :
        print "Populating permissions ..."
        pop_permissions( seed=seed )
        print "Populating users ( no_of_users=%s, no_of_relations=%s ) ..." % \
               ( no_of_users, no_of_relations )
        pop_user( no_of_users, no_of_relations, seed=seed )
        print "Populating license ..."
        pop_licenses( no_of_tags, no_of_attachs, seed=seed )
        print "Populating projects ( no_of_projects=%s ) ..." % no_of_projects
        pop_projects( no_of_projects, no_of_tags, no_of_attachs, seed=seed )
        print "Populating tickets ( no_of_tickets=%s ) ..." % no_of_tickets
        pop_tickets( no_of_tickets, no_of_tags, no_of_attachs, seed=seed )
        print "Populating vcs ( no_of_vcs=%s ) ..." % no_of_vcs
        pop_vcs( no_of_vcs=no_of_vcs, seed=seed )
        print "Populating wikis ( no_of_wikis=%s ) ..." % no_of_wikis
        pop_wikipages( no_of_tags, no_of_attachs, seed=seed )
        print "Populating reviews ( no_of_reviews=%s ) ..." % no_of_reviews
        pop_reviews( no_of_reviews, no_of_tags, no_of_attachs, seed=seed )
        # Fix due_dates
        print "Fixing milestone due_date(s) ..."
        fix_mstn_duedate( seed=seed )
        print "Fixing tickets status due_date(s) ..."
        fix_ts_duedate( seed=seed )
    except :
        print "Deleting models ... and Reraising the exception"
        delete_models( meta.engine )
        raise

def tearDownModule() :
    # print "Deleting models ... "
    #delete_models( meta.engine )
    pass

class TestSampleDB( object ) :

    def testsampledb( self ) :
        """Creating sample database"""
        pass
