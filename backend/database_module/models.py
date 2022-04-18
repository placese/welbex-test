from sqlalchemy import Column, Integer, Date, String, Float
from .database import Base


class Entity(Base):
    """ORM class mapping to db table""" 
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    title = Column(String)
    quantity = Column(Integer)
    distance = Column(Float)

