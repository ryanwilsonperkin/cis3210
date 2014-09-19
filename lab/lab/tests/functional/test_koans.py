from lab.tests import *

class TestKoansController(TestController):

    def test_index(self):
        response = self.app.get(url('koans'))
        # Test response...
