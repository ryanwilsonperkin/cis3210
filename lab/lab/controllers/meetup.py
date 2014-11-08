import logging
import requests

from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session

log = logging.getLogger(__name__)

class MeetupController(BaseController):

    def groups(self, id):
        url = 'https://api.meetup.com/find/groups'
        params = {
            'text': id,
            'location': 'Guelph',
            'radius': 50,
            'country': 'CA',
            'category': 34,
            'page': 3,
            'sign': 'true',
            'photo-host': 'public',
            'key': config['meetup.apikey'],
            'order': 'most_active',
        }
        resp = requests.get(url, params=params)
        if resp.ok:
            response.headers['Content-Type'] = resp.headers.get(
                'Content-Type',
                'application/javascript')
            return resp.content
        else:
            abort(resp.status_code)
