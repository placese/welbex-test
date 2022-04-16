from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Table(BaseModel):
    id: int
    date: str
    quantity: int
    title: str
    distance: float


fake_db = [
    {"id": 1, "date": datetime.now().strftime("%d-%m-%Y"), "quantity": 2, "title": "first", "distance": 100},
    {"id": 2, "date": datetime.now().strftime("%d-%m-%Y"), "quantity": 4, "title": "second", "distance": 150},
    {"id": 3, "date": datetime.now().strftime("%d-%m-%Y"), "quantity": 6, "title": "third", "distance": 120}
]


@app.get("/", response_model=list[Table])
async def root():
    return fake_db
