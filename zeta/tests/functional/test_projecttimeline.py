from zeta.tests import *

class TestProjecttimelineController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='projecttimeline', action='index'))
        # Test response...
