import json
import logging
import requests

from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session

log = logging.getLogger(__name__)

class SubredditController(BaseController):

    def search(self, id):
        url = 'http://www.reddit.com//subreddits/search.json'
        params = {
            'q': id,
        }
        headers = {
            'User-Agent': 'cis3210 by ryanwilsonperkin',
        }
        resp = requests.get(url, params=params, headers=headers)
        if resp.ok:
            response.headers['Content-Type'] = resp.headers.get(
                'Content-Type',
                'application/javascript')
            children = map(lambda x: x.get('data'),
                           resp.json().get('data').get('children'))
            children = [child for child in children
                        if child.get('over18') == False]
            return json.dumps(children[:3])
        else:
            abort(resp.status_code)
