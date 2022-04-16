from sqlalchemy.orm import Session

from . import models, schemas

def get_entity(db: Session, id: int):
    """Returns entity from table by id"""
    return db.query(models.Entity).filter(models.Entity.id == id).first()

def get_entities(db: Session, skip: int = 0, limit: int = 25):
    """Returns list of entities"""
    return db.query(models.Entity).offset(skip).limit(limit).all()

def create_entity(db: Session, entity: schemas.EntityCreate):
    """Creates entity in db and returns it"""
    db_entity = models.Entity(date=entity.date, title=entity.title, quantity=entity.quantity, distance=entity.distance)
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity
