import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_utils import Base


engine = create_engine('postgresql://{}:{}@{}:5432/{}'.format(
    os.environ['LOGIN_DB_USER'],
    os.environ['LOGIN_DB_PASSWORD'],
    os.environ['LOGIN_DB_HOST'],
    os.environ['LOGIN_DB_NAME']
))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

from .HttpAuthProvider import HttpAuthProvider

__all__ = [
    'Session'
    'HttpAuthProvider'
]
