# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

import unittest
from   pylons            import config

from   zeta.model.verify import verify_tables
from   zeta.model        import meta
from   zeta.model.tables import System


class TestSchemas( unittest.TestCase ) :
    def test_schemas( self ) :
        status, msg = verify_tables()
        assert status == True, msg
