CIS3210 Lab Application
=======================

This is an application under active development for my CIS3210 Computer
Networks course at the University of Guelph.

Installation
------------

Note: To run the application on your own computer, you will require python packages
that can be fetched using *pip*. Instructions for installing pip can be found 
[here](http://pip.readthedocs.org/en/latest/installing.html).

Note: This application relies on access to a database available only on UofG campus intranet.

Fetch this repository.
```bash
git clone https://github.com/ryanwilsonperkin/cis3210.git
```

Install the required packages in `requirements.txt`.
```bash
cd cis3210
pip install -r requirements.txt
```

Run the webserver.
```bash
cd lab
paster serve --reload development.ini
```

Navigate to http://localhost:5000 in your browser.

Security
--------

This application assumes that the user is malicious and takes steps
to prevent common attacks like cross site scripting and sql injection.

SQL injection attacks are mitigated by the proper use and implementation of the
SQLAlchemy library which provides a DB-agnostic ORM. The ORM prepares
statements in such a way that any user supplied data is properly escaped.

XSS attacks are mitigated by the proper escaping of user data within mako
templates.  Mako provides the {var | h} shorthand for performing markupsafe
escaping on the text in var. The only data entered by users and displayed is
the first and last names given during registration. Both values have been
escaped.

### Further Consideration

Given more time there are several other security topics I would like to tackle.

* Forms should include session tokens to avoid CSRF attacks
* Passwords should *NEVER* be stored in plain text
* Database user/password should not appear in development.ini in plain text
* Login attempts should be rate-limited
* Registration should involve a reCAPTCHA to avoid spammers
    
Technologies
------------
* [Pylons](http://www.pylonsproject.org/projects/pylons-framework/about)
* [Bootstrap 3](http://getbootstrap.com/)
* [jQuery](http://jquery.com/)
