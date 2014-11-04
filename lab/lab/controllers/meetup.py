import logging
import urllib 
from urllib2 import HTTPError, Request, urlopen

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
        data = urllib.urlencode(params)
        remote_req = Request(url + '?' + data)
        try:
            remote_resp = urlopen(remote_req)
            response.headers['Content-Type'] = 'application/javascript'
            return remote_resp.read()
        except HTTPError as e:
            abort(e.code)

