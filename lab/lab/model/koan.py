from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Text

from lab.model.meta import Base

class Koan(Base):
    __tablename__ = 'koan'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    text = Column(Text)

    def __init__(self, title='', text=''):
        self.title = title
        self.text = text

    def __repr__(self):
        return "<Koan('{title}')>".format(title=self.title)
