from zeta.tests import *

class TestSiteadminController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='siteadmin', action='index'))
        # Test response...
