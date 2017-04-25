# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
#       Copyright (c) 2009 SKR Farms (P) LTD.

from   __future__ import with_statement
import unittest

from   pylons            import config

from   zeta.model        import meta
from   zeta.model.tables import System


class TestSystem( unittest.TestCase ) :
    def test_system( self ) :
        msession   = meta.Session()
        sysvalues = { 'product_name'     : 'zeta',
                      'product_version'  : config['zetaversion'],
                      'database_version' : config['dbversion'],
                      'sitename'         : config['zeta.sitename'],
                      'timezone'         : config['zeta.timezone'],
                      'unicode_encoding' : config['zeta.unicode_encoding'],
                      'siteadmin'        : config['zeta.siteadmin'],
                      'envpath'          : config['zeta.envpath'],
                      'wikipage_count'   : str(0)
                    }
        with msession.begin() :
            sys_rows = msession.query( System )
            for row in sys_rows :
                if row.field == 'wikipage_count' :
                    continue
                assert sysvalues[ row.field ] == row.value, \
                       row.field + ' : ' + row.value + ' not ' + sysvalues[row.field]
