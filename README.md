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

### DOS (Denial of Service)

Since denial of service is such a wide range of attacks, there are several
ways to mitigate their impact. We will discuss a few, but forgo implementation
to reduce the overhead of setup for this application. To properly mitigate all
attacks would involve the installation and configuration of other libraries
and tools, which are not expected to be present on the instructor's lab
computer.

One form of denial of service is attempting to crash the server, by uploading
tremendous amounts of data. This can be mitigated by using Content-Length
limiting for POST requests, through upgraded versions of the WebOb middleware.

Another form of denial of service is SYN-flooding, whre a malicious user
attempts to overwhelm the server with SYN packets causing the server to send
back a large number of ACK packets (as per TCP handshake protocol). This
form of attack can be mitigated by the use of a custom WSGI HTTP server such as
Gunicorn, that can add additional attack-detection middleware and ignore
further packets from malicious users.

Finally, we will consider Distributed Denial of Service (DDOS), where many
users are performing a DOS attack concurrently against the server. This attack
can be handled by implementing a reverse-proxy such as
[nginx](http://wiki.nginx.org/Main) to handle the automatic blacklisting of IP
addresses based on attack-detection protocols.

### RCE (Remote Code Execution)

There is no evaluation of user supplied values on the server-side, thus the
system is not vulnerable to RCE.

### Configuration Vulnerabilities

Pylons ships with certain secret keys set by default. Since Pylons is an open
source web framework, these values are known to attackers and will be used to
exploit the server. To mitigate this, the initial values have been modified to
be unknown to the attacker. Unfortunately, as previously mentioned, this
project is also open-source and thus the new values are also known to an
attacker. In a true production system, the production.ini file containing
secret keys would be kept private.

### AJAX Vulnerabilities

The only supplied AJAX is generated from static, project defined data.
Therefore it is safe to assume that any AJAX requests made to/from the server
are safe and valid.

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
