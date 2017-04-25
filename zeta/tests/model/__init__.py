# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Test package to create a demo database.
"""

from   sqlalchemy                import engine_from_config
from   paste.util.import_string  import eval_import
import pylons.test

from   zeta.auth.perm            import permissions
from   zeta.model                import init_model, create_models, delete_models
from   zeta.model                import meta
from   zeta.tests.model.populate import pop_permissions, pop_user

def setUpPackage() :
    pylons.test.pylonsapp.config['userscomp'] = meta.userscomp

def tearDownPackage() :
    pass