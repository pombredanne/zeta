from zeta.tests import *

class TestAttachmentController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='attachment', action='index'))
        # Test response...
