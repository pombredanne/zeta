from zeta.tests import *

class TestProjectsourceController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='projectsource', action='index'))
        # Test response...
