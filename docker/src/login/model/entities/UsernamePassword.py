from sqlalchemy import Column, String

from model_utils import Base

class Password(Base):

    __tablename__ = 'user_password'

    ''' para ser compatible con el código actual '''
    __table_ops__ = [{'schema':'credentials'}]

    username = Column(String)
    password = Column(String)
