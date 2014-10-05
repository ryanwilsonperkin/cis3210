"""Setup the lab application"""
import logging

import pylons.test

from lab.config.environment import load_environment
from lab.data.koans import koan_dict
from lab.model.koan import Koan
from lab.model.meta import Session, Base

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup lab here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)

    # Populate koan table with static data
    for title, text in koan_dict.iteritems():
        koan = Koan(title=title, text='\n'.join(text))
        Session.add(koan)
        Session.commit()
