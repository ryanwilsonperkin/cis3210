import json

from lab.tests import *
from lab.controllers.koans import not_implemented_msg
from lab.model import Koan
from lab.model.meta import Session

class TestKoansController(TestController):

    def setUp(self):
        self.koan_q = Session.query(Koan)

    def test_index(self):
        """Tests that GET /koans returns the list of koan titles."""
        response = self.app.get(url(controller='koans', action='index'))

        koan_titles = [koan.title for koan in self.koan_q.order_by(Koan.id)]

        assert response.status_code == 200
        assert response.content_type == 'text/javascript'
        assert response.json_body == koan_titles

    def test_show(self):
        """Tests that GET /koans/id returns koan at index id as json."""
        response = self.app.get(url(controller='koans', action='show', id=1))

        assert response.status_code == 200
        assert response.content_type == 'text/javascript'

        koan = self.koan_q.filter_by(id=1).first()

        assert response.json_body.get('title') == koan.title
        assert response.json_body.get('text') == koan.text.split('\n')

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
        num_koans = len(self.koan_q.all())
        response = self.app.get(url(controller='koans',
                                    action='show',
                                    id=(num_koans + 1)),
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
