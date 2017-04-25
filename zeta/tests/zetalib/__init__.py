# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

"""Test package for `lib` modules in Zeta.
"""

from   sqlalchemy                import engine_from_config
import pylons.test
from   paste.util.import_string  import eval_import

from   zeta.auth.perm            import permissions
from   zeta.model                import init_model, create_models, delete_models
from   zeta.model                import meta
from   zeta.tests.model.populate import pop_permissions, pop_user

def setUpPackage() :
    pass

def tearDownPackage() :
    pass

