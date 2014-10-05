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
        if request.method == 'GET':
            c.form_errors = []
            return render('/register.mako')

        first_name = request.params.get('firstName', None)
        last_name = request.params.get('firstName', None)
        email = request.params.get('email', None)
        password = request.params.get('password', None)
        user = self.user_q.filter_by(email=email,
                                     password=password).first()

        if user:
            c.form_errors = ['That email is already registered.']
            return render('/register.mako')
        else:
            user = User(first_name=first_name, last_name=last_name,
                        email=email, password=password)
            Session.add(user)
            Session.commit()
            session['logged_in'] = True
            session['user'] = user
            session.save()
            redirect(url('/'))

    def login(self):
        """GET/POST /login: login new session as existing user."""
        if request.method == 'GET':
            c.form_errors = []
            return render('/login.mako')

        email = request.params.get('email', None)
        password = request.params.get('password', None)
        user = self.user_q.filter_by(email=email,
                                     password=password).first()

        if user:
            session['logged_in'] = True
            session['user'] = user
            session.save()
            redirect(url('/'))
        else:
            c.form_errors = ['Invalid username/password.']
            return render('/login.mako')

    def logout(self):
        """POST /logout: logout existing session."""
        return "Logout"
