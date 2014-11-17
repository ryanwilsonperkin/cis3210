import logging
import requests

from pylons import config, request, response, session, tmpl_context as c, url
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
        auth = (config['github.oauth'], 'x-oauth-basic')
        github_response = requests.get(url, auth=auth, headers=headers)
        response.content_type = 'application/json'
        return github_response.content

    def repos(self,id):
        url = 'https://api.github.com/users/{user}/repos'.format(user=id)
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'github-reportcard-ryanwilsonperkin',
        }
        params = {
            'per_page': 100,
        }
        auth = (config['github.oauth'], 'x-oauth-basic')
        github_response = requests.get(url, auth=auth, params=params, headers=headers)
        response.content_type = 'application/json'
        return github_response.content
