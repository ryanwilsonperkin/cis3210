from lab.model.meta import Session, Base
from lab.model.user import User

def init_model(engine):
    Session.configure(bind=engine)
