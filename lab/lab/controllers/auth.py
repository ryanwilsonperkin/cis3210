import logging
import random

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from lab.lib.base import BaseController, render, Session
from lab.model import User

log = logging.getLogger(__name__)

def generate_csrf_token():
    return hex(random.getrandbits(128))

class AuthController(BaseController):

    def __before__(self):
        self.user_q = Session.query(User)
        c.csrf_token = ""
        c.form_errors = []

    def register(self):
        """GET/POST /register: register new user."""
        if request.method == 'GET':
            c.csrf_token = generate_csrf_token()
            session['csrf_token'] = c.csrf_token
            session.save()
            return render('/register.mako')

        first_name = request.params.get('firstName', None)
        last_name = request.params.get('lastName', None)
        email = request.params.get('email', None)
        password = request.params.get('password', None)
        form_csrf_token = request.params.get('token', None)

        # Validate received data.
        session_csrf_token = session.get('csrf_token', None)
        if session_csrf_token is None or session_csrf_token != form_csrf_token:
            c.form_errors.append('Invalid CSRF token.')
            c.csrf_token = generate_csrf_token()
            session['csrf_token'] = c.csrf_token
            return render('/register.mako')

        if not email:
            c.form_errors.append('Email field cannot be blank.')

        if not password:
            c.form_errors.append('Password field cannot be blank.')

        user = self.user_q.filter_by(email=email).first()

        if user:
            c.form_errors.append('That email is already registered.')

        if user or not email or not password:
            c.csrf_token = generate_csrf_token()
            session['csrf_token'] = c.csrf_token
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
            c.csrf_token = generate_csrf_token()
            session['csrf_token'] = c.csrf_token
            session.save()
            return render('/login.mako')

        email = request.params.get('email', None)
        password = request.params.get('password', None)
        form_csrf_token = request.params.get('token', None)
        
        session_csrf_token = session.get('csrf_token', None)
        if session_csrf_token is None or session_csrf_token != form_csrf_token:
            c.form_errors.append('Invalid CSRF token.')
            c.csrf_token = generate_csrf_token()
            session['csrf_token'] = c.csrf_token
            session.save()
            return render('/login.mako')

        user = self.user_q.filter_by(email=email,
                                     password=password).first()

        if user:
            session['logged_in'] = True
            session['user'] = user
            session.save()
            redirect(url('/'))
        else:
            c.form_errors = ['Invalid username/password.']
            c.csrf_token = generate_csrf_token()
            session['csrf_token'] = c.csrf_token
            session.save()
            return render('/login.mako')

    def logout(self):
        """POST /logout: logout existing session."""
        session['logged_in'] = False
        session['user'] = None
        session.save()
        redirect(url('/'))
