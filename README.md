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

Install the required packages in `requirements_production.txt`.
```bash
cd cis3210
pip install -r requirements_production.txt
```

Run the webserver.
```bash
cd lab
paster serve --reload production.ini
```

Navigate to http://localhost:5000 in your browser.

Security
--------

This application assumes that the user is malicious and takes steps
to prevent common attacks.

### Reflected XSS

XSS attacks are mitigated by the proper escaping of user data within mako
templates.  Mako provides the {var | h} shorthand for performing markupsafe
escaping on the text in var. The only data entered by users and displayed is
the first and last names given during registration. Both values have been
escaped.

### File Upload XSS

This application does not allow for files to be uploaded (through forms or
otherwise) and thus is not vulnerable to XSS by file upload.

### Elevation of Privelege

There is only currently one level of user pertaining to the system, so there is
no concern that a user could somehow elevate their privelege to that of an
admin. The system does prevent anonymous users from viewing the site, they must
first either login, or register to view the frontpage. This is guaranteed at
the controller level which checks that the user has a cookie guaranteeing they
are a user of the system.

### Cookie Manipulation

Session cookies are handled by session middleware provided by
[Beaker](http://beaker.readthedocs.org/en/latest). Beaker automatically
encrypts/decrypts cookies sent to and from the client. Since cookies are
encrypted client-side, the client is not able to modify them in order to gain
unwaranted access to the system. A noted flaw: since this entire project
is open source, including the production.ini file, it is possible for an
attacker to look at which secret key is being used for encryption by Beaker. It
is then trivial to examine the Beaker source code to discern the encryption
scheme and de-crypt the client-side cookies. Were this a true production
environment, the Beaker secret key would be private and closely guarded.

### XSRF (Cross Site Request Forgery)

Each form that involves user data (login and register pages) has a special
token embedded as a hidden input in the form. This token is randomly generated
when rendering the page and is also stored in the frontend/backend session.
When the user submits the form, the token is compared against the session
token to ensure that the two are equivalent. If the tokens are not equivalent
it is a sign that someone is attempting to submit the form without first
navigating to the page, and is likely being malicious. Rather than process the
form data, the page is immediately re-rendered with a new token and an error
message.

### XSSI (Cross Site Script Inclusion)

The site does not provide any confidential information through scripts and
thus should not be vulnerable to XSSI. Furthermore, processing of user data is
only supported through POST requests which are largely incompatible with
script inclusion vulnerabilities.

### Path Traversal

Since pylons relies on custom routes to map requests to controllers, any
attempts at path traversal will be caught and handled by the error router.

### SQL Injection

SQL injection attacks are mitigated by the proper use and implementation of the
SQLAlchemy library which provides a DB-agnostic ORM. The ORM prepares
statements in such a way that any user supplied data is properly escaped.

### Further Consideration

Given more time there are several other security topics I would like to tackle.

* Passwords should *NEVER* be stored in plain text
* Database user/password should not appear in development.ini in plain text
* Login attempts should be rate-limited
* Registration should involve a reCAPTCHA to avoid spammers
    
Technologies
------------
* [Pylons](http://www.pylonsproject.org/projects/pylons-framework/about)
* [Bootstrap 3](http://getbootstrap.com/)
* [jQuery](http://jquery.com/)
