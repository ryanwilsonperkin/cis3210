import json
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render
from lab.model.koans import koan_dict

log = logging.getLogger(__name__)

class KoansController(BaseController):

    def index(self):
        """GET /koans: fetch list of koans."""
        if request.method != 'GET':
            abort(405)
        response.headers['Content-Type'] = 'text/javascript'
        return json.dumps(koan_dict.keys())

    def show(self, id):
        """GET /koans/id: access koan at index id."""
        if request.method != 'GET':
            abort(405)

        if id.isdigit() and 0 <= int(id) < len(koan_dict):
            id = int(id)
        else:
            abort(404)

        title, text = koan_dict.items()[id]

        response.headers['Content-Type'] = 'text/javascript'
        return json.dumps({
            "title": title,
            "text": text
        })

    # Unimplemented API endpoints due to lack of database.
    def create(self):
        """POST /koans: create a new koan."""
        if request.method != 'POST':
            abort(405)
        else:
            abort(403, comment='Method not yet implemented.')

    def new(self):
        """POST /koans/new: form for creating a new koan."""
        if request.method != 'POST':
            abort(405)
        else:
            abort(403, comment='Method not yet implemented.')

    def update(self, id):
        """PUT /koans/id: update existing koan at index id."""
        if request.method != 'PUT':
            abort(405)
        else:
            abort(403, comment='Method not yet implemented.')

    def delete(self, id):
        """DELETE /koans/id: delete koan at index id."""
        if request.method != 'DELETE':
            abort(405)
        else:
            abort(403, comment='Method not yet implemented.')

    def edit(self, id):
        """GET /koans/id: form to edit koan at index id."""
        if request.method != 'GET':
            abort(405)
        else:
            abort(403, comment='Method not yet implemented.')
