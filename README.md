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

API Integration
---------------

This project makes use of the Twitter API for custom buttons and widgets.
The front page contains a dynamically updating list of tweets containing the
hashtag '#3210gatelessgate'. 

Below every koan there will be a link that shows a heart icon and says 'Tweet
this koan' which, when clicked, will allow the user to tweet about the website.
The tweet will automatically include the hashtag and the title of the koan and
can be customized by the user.

Technologies
------------
* [Pylons](http://www.pylonsproject.org/projects/pylons-framework/about)
* [Bootstrap 3](http://getbootstrap.com/)
* [jQuery](http://jquery.com/)
* [Twitter widgets and buttons](https://twitter.com/settings/widgets)
