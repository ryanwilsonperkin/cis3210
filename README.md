CIS3210 Lab Application
=======================

This is an application under active development for my CIS3210 Computer
Networks course at the University of Guelph.

The name of the application is Polyglot. It will be an aggregator of
information and resources to help you learn a new programming language.

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

This application makes use of the Meetup.com API. It allows the user to enter
technologies that they are interested in and find local meetups based on
their search query.

I intend to add additional API integrations with Reddit, Wikipedia, and Amazon.

Technologies
------------
* [Pylons](http://www.pylonsproject.org/projects/pylons-framework/about)
* [Bootstrap 3](http://getbootstrap.com/)
* [jQuery](http://jquery.com/)
