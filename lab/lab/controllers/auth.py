import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session
from lab.model import User

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def __before__(self):
        self.user_q = Session.query(User)

    def register(self):
        """GET/POST /register: register new user."""
        return render('/register.mako')

    def login(self):
        """GET/POST /login: login new session as existing user."""
        return render('/login.mako')

    def logout(self):
        """POST /logout: logout existing session."""
        return "Logout"
