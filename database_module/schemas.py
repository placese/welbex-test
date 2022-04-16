from pydantic import BaseModel

class EntityBase(BaseModel):
    """Pydantic base model of Entity table"""
    title: str
    quantity: int
    distance: float

class EntityCreate(EntityBase):
    """Pydantic model of Entity to create record/instance"""
    pass

class Entity(EntityBase):
    """Pydantic model of Entity to read record/instance"""
    id: int

    class Config:
        orm_mod = True
