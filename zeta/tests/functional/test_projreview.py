from zeta.tests import *

class TestProjreviewController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='projreview', action='index'))
        # Test response...
