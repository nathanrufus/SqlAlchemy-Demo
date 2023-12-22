from datetime import datetime
from sqlalchemy import Column,DateTime
from sqlalchemy.orm import declarative_base
from connect import Session,session

model=declarative_base()
model.query = session.query_property()

class TimeStampModel(model):
    __abstract__ =True

    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,onupdate=datetime.utcnow())

    