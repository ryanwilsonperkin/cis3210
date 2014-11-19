GitHub Resume
=============

This is an application under active development for my CIS3210 Computer
Networks course at the University of Guelph.

The name of the application is GitHub Resume. It will be a stripped down
and beautified version of the GitHub.com/:username page with an emphasis
on readability and aesthetic minimalism.

------------

Note: To run the application on your own computer, you will require python packages
that can be fetched using *pip*. Instructions for installing pip can be found 
[here](http://pip.readthedocs.org/en/latest/installing.html).

Fetch this repository.
```bash
git clone https://github.com/ryanwilsonperkin/github-resume.git
```

Install the required packages in `requirements.txt`.
```bash
cd github-resume
pip install -r requirements.txt
```

Run the webserver.
```bash
cd lab
paster serve --reload production.ini
```

Navigate to http://localhost:5000 in your browser.

API Integration
---------------

This application makes use of the GitHub.com API. It allows the user to enter
a GitHub username and retrieve information on that user.

Technologies
------------
* [Pylons](http://www.pylonsproject.org/projects/pylons-framework/about)
* [Bootstrap 3](http://getbootstrap.com/)
* [jQuery](http://jquery.com/)
