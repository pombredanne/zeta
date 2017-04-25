from zeta.tests import *

class TestUserpageController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='userpage', action='index'))
        # Test response...
