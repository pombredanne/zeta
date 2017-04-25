from zeta.tests import *

class TestPasteradminController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='pasteradmin', action='index'))
        # Test response...
