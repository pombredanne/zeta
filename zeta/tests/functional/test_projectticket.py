from zeta.tests import *

class TestProjectticketController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='projectticket', action='index'))
        # Test response...
