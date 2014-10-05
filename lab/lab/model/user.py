from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from lab.model.meta import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    # Max-length of an email is 254 chars (RFC 5321)
    email = Column(String(254))
    password = Column(String(100))

    def __init__(self, first_name='', last_name='', email='', password=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User('{email}')>".format(email=self.email)
