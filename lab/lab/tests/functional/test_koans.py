import json

from lab.tests import *
from lab.data.koans import koan_dict
from lab.controllers.koans import not_implemented_msg

class TestKoansController(TestController):

    def test_index(self):
        """Tests that GET /koans returns the list of koan titles."""
        response = self.app.get(url(controller='koans', action='index'))

        assert response.status_code == 200
        assert response.content_type == 'text/javascript'
        assert response.json_body == koan_dict.keys()

    def test_show(self):
        """Tests that GET /koans/id returns koan at index id as json."""
        response = self.app.get(url(controller='koans', action='show', id=0))

        assert response.status_code == 200
        assert response.content_type == 'text/javascript'

        koan_title, koan_text = koan_dict.items()[0]
        assert response.json_body.get('title') == koan_title
        assert response.json_body.get('text') == koan_text

    def test_show_no_id(self):
        """Tests that fetching no id returns 404."""
        response = self.app.get(url(controller='koans', action='show'),
                                status=404)
        
        assert response.status_code == 404

    def test_show_invalid_id_type(self):
        """Tests that a non-numeric id returns 404."""
        response = self.app.get(url(controller='koans', action='show', id='a'),
                                status=404)
        
        assert response.status_code == 404


    def test_show_invalid_id_too_high(self):
        """Tests that an id bigger than the number of koans returns 404."""
        response = self.app.get(url(controller='koans',
                                    action='show',
                                    id=len(koan_dict)),
                                status=404)
        
        assert response.status_code == 404

    def test_show_invalid_id_too_low(self):
        """Tests that a negative id returns 404."""
        response = self.app.get(url(controller='koans',
                                    action='show',
                                    id=-1),
                                status=404)
        
        assert response.status_code == 404

    # Unimplemented API endpoints due to lack of database.
    def test_create_not_implemented(self):
        """Tests that POST /koans/id returns 403."""
        response = self.app.post(url(controller='koans', action='create'),
                                 status=403)

        assert not_implemented_msg in response.body
        assert response.status_code == 403

    def test_new_not_implemented(self):
        """Tests that POST /koans/new returns 403."""
        response = self.app.post(url(controller='koans', action='new'),
                                 status=403)

        assert not_implemented_msg in response.body
        assert response.status_code == 403

    def test_update_not_implemented(self):
        """Tests that PUT /koans/id returns 403."""
        response = self.app.put(url(controller='koans', action='update'),
                                status=403)

        assert not_implemented_msg in response.body
        assert response.status_code == 403

    def test_delete_not_implemented(self):
        """Tests that DELETE /koans/id returns 403."""
        response = self.app.delete(url(controller='koans', action='delete'),
                                   status=403)

        assert not_implemented_msg in response.body
        assert response.status_code == 403
