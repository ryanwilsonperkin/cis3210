import json
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render
from lab.model.koans import koan_dict

log = logging.getLogger(__name__)

class KoansController(BaseController):

    def index(self):
        response.headers['content-type'] = 'text/javascript'
        return json.dumps(koan_dict.keys())

    def show(self, id):
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
