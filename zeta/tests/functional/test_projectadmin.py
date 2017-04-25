from zeta.tests import *

class TestProjectadminController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='projectadmin', action='index'))
        # Test response...
