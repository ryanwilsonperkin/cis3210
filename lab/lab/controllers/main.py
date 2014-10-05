import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session

log = logging.getLogger(__name__)

class MainController(BaseController):

    def index(self):
        c.user = session.get('user', None)
        return render('/front_page.mako')
