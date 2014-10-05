import json
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session
from lab.model import Koan

log = logging.getLogger(__name__)

not_implemented_msg = 'Method not yet implemented.'

class KoansController(BaseController):

    def __before__(self):
        self.koan_q = Session.query(Koan)

    def index(self):
        """GET /koans: fetch list of koans."""
        if request.method != 'GET':
            abort(405)
        response.headers['Content-Type'] = 'text/javascript'
        return json.dumps([koan.title for koan in self.koan_q.all()])

    def show(self, id):
        """GET /koans/id: access koan at index id."""
        if request.method != 'GET':
            abort(405)

        if id.isdigit() and 1 <= int(id) <= len(self.koan_q.all()):
            id = int(id)
        else:
            abort(404)

        koan = self.koan_q.filter_by(id=id).first()

        response.headers['Content-Type'] = 'text/javascript'
        return json.dumps({
            "title": koan.title,
            "text": koan.text.split('\n')
        })

    # Unimplemented API endpoints due to lack of database.
    def create(self):
        """POST /koans: create a new koan."""
        if request.method != 'POST':
            abort(405)
        else:
            abort(403, comment=not_implemented_msg)

    def new(self):
        """POST /koans/new: form for creating a new koan."""
        if request.method != 'POST':
            abort(405)
        else:
            abort(403, comment=not_implemented_msg)

    def update(self, id):
        """PUT /koans/id: update existing koan at index id."""
        if request.method != 'PUT':
            abort(405)
        else:
            abort(403, comment=not_implemented_msg)

    def delete(self, id):
        """DELETE /koans/id: delete koan at index id."""
        if request.method != 'DELETE':
            abort(405)
        else:
            abort(403, comment=not_implemented_msg)

    def edit(self, id):
        """GET /koans/id: form to edit koan at index id."""
        if request.method != 'GET':
            abort(405)
        else:
            abort(403, comment=not_implemented_msg)
