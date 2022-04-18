from pydantic import BaseModel, NonNegativeInt
from datetime import date

class EntityBase(BaseModel):
    """Pydantic base model of Entity table"""
    date: date
    title: str
    quantity: NonNegativeInt
    distance: float

class EntityCreate(EntityBase):
    """Pydantic model of Entity to create record/instance"""
    pass

class Entity(EntityBase):
    """Pydantic model of Entity to read record/instance"""
    id: int

    class Config:
        orm_mode = True
