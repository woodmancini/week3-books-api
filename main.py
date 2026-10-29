from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models, schemas
from database import engine, get_db

# creates database tables if they don't already exist
models.Base.metadata.create_all

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Books API is running."}

@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    courses = db.query(models.Book).all()
    return courses


@app.get("/book/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

# TO DO:
# @app.post("/books" ... )