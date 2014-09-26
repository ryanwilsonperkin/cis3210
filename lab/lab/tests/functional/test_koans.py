import json

from lab.tests import *
from lab.model.koans import koan_dict
from lab.controllers.koans import not_implemented_msg

class TestKoansController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='koans', action='index'))

        assert response.status_code == 200
        assert response.content_type == 'text/javascript'
        assert response.json_body == koan_dict.keys()

    def test_show(self):
        response = self.app.get(url(controller='koans', action='show', id=0))

        assert response.status_code == 200
        assert response.content_type == 'text/javascript'

        koan_title, koan_text = koan_dict.items()[0]
        assert response.json_body.get('title') == koan_title
        assert response.json_body.get('text') == koan_text

    def test_show_no_id(self):
        response = self.app.get(url(controller='koans', action='show'),
                                status=404)
        
        assert response.status_code == 404

    def test_show_invalid_id_type(self):
        response = self.app.get(url(controller='koans', action='show', id='a'),
                                status=404)
        
        assert response.status_code == 404


    def test_show_invalid_id_too_high(self):
        response = self.app.get(url(controller='koans',
                                    action='show',
                                    id=len(koan_dict)),
                                status=404)
        
        assert response.status_code == 404

    def test_show_invalid_id_too_low(self):
        response = self.app.get(url(controller='koans',
                                    action='show',
                                    id=-1),
                                status=404)
        
        assert response.status_code == 404
