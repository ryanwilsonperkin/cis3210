CIS3210 Lab Application
=======================

http://ryanwilsonperkin.com/cis3210

This is an application under active development for my CIS3210 Computer
Networks course at the University of Guelph.

The main application is a simple page featuring "Links the Cat" (of Microsoft
Office fame) and several interactive buttons.

There is also a secondary application running at the /hello/index sub-page
that displays the `environ` variable that is available within the running Pylons
webframework.

Installation
------------

Note: To run the application on your own computer, you will require python packages
that can be fetched using *pip*. Instructions for installing pip can be found 
[here](http://pip.readthedocs.org/en/latest/installing.html).

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
cd helloworld
paster serve --reload development.ini
```

Navigate to http://localhost:5000 in your browser.
    
Technologies
------------
* [Pylons](http://www.pylonsproject.org/projects/pylons-framework/about)
* [Bootstrap 2](http://getbootstrap.com/2.3.2)
* [jQuery](http://jquery.com/)
* [clippy.js](https://www.smore.com/clippy-js)
