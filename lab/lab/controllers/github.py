import logging
import requests

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session

log = logging.getLogger(__name__)

class GithubController(BaseController):

    def user(self,id):
        url = 'https://api.github.com/users/{user}'.format(user=id)
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'github-reportcard-ryanwilsonperkin',
        }
        github_response = requests.get(url, headers=headers)
        response.content_type = 'application/json'
        return github_response.content
