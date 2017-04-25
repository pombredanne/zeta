from zeta.tests import *

class TestAboutusController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='aboutus', action='index'))
        # Test response...
