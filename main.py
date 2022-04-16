from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

from database_module import crud, models, schemas
from database_module.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/entities/", response_model=list[schemas.Entity])
def read_entities(
                    sort_field: str | None = None,
                    sort_type: str | None = None,
                    filter_field_1: str | None = None,
                    filter_condition_1 : str | None = None,
                    filter_field_2: str | None = None,
                    filter_condition_2 : str | None = None,
                    skip: int = 0,
                    limit: int = 25,
                    db: Session = Depends(get_db),
                ):
    entities = crud.get_entities(db=db, skip=skip, limit=limit)
    return entities


@app.post("/entities/", response_model=schemas.Entity)
def create_entity(entity: schemas.EntityCreate, db: Session = Depends(get_db)):
    return crud.create_entity(db=db, entity=entity)
