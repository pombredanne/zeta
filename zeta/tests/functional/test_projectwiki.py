from zeta.tests import *

class TestProjectwikiController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='projectwiki', action='index'))
        # Test response...
