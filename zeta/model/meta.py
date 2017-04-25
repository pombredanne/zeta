# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""SQLAlchemy Metadata and Session object"""
from sqlalchemy     import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

__all__ = ['engine', 'Session', 'metadata', 'tbl_mappers' ]

# SQLAlchemy database engine.  Updated by model.init_model()
engine = None

# SQLAlchemy session manager.  Updated by model.init_model()
Session = None

# Dictionary of map objects between Tables and Plain Python Objects. Updated
# by model.init_model()
tbl_mappers = {}

# Dictionary of WikiPage tables.
wiki_tables      = {}
# Dictionary of WikiPage Classes
wikipage_factory = {}

# 1. Dictionary of system entries, as provided by the .ini file.
#    The only purpose of this dictionary is collect the data from .ini file and
#    reflect them in the database.
# 2. For run-time consumption 'c.sysentries' dictionary is used.
sysentries_cfg   = {}

#---- Attributes for MultiGate ---
# Once the authentication user class is initialized the following attribute
# will be instantiated.
userscomp           = None

# Global metadata. If you have multiple databases with overlapping table
# names, you'll need a metadata for each database.
# We are using Declarative ORM, where metadata is automatically created.
# metadata = MetaData()
metadata = MetaData()
