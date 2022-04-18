from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from loguru import logger

from database_module import crud, models, schemas
from database_module.database import SessionLocal, engine
from utils import FieldSortParams, filter_entities

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@logger.catch
@app.get("/entities/", response_model=list[schemas.Entity])
def read_entities(field_to_sort_by: str = 'quantity',
                  order_by: str = 'asc',
                  filter_field: str | None = None,
                  filter_type: str | None = None,
                  filter_value: str | None = None,
                  skip: int = 0,
                  limit: int = 100,
                  db: Session = Depends(get_db)):
    """Returns entities in JSON format"""
    if field_to_sort_by in FieldSortParams._member_names_:
        result = sorted(jsonable_encoder(crud.get_entities(db=db)), key=lambda k: k[field_to_sort_by])
        if order_by == 'asc':
            result = filter_entities(result, filter_field, filter_type, filter_value)
        elif order_by == 'desc':
            result = filter_entities(result, filter_field, filter_type, filter_value)[::-1]
        return result
    raise HTTPException(status_code=400, detail="Wrong field to sort by")


@app.post("/entities/", response_model=schemas.Entity)
def create_entity(entity: schemas.EntityCreate, db: Session = Depends(get_db)):
    """Creates entity in db and returns it"""
    return crud.create_entity(db=db, entity=entity)
