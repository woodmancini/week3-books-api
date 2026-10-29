from database import SessionLocal
import models

db = SessionLocal()

try:
    # SQLAlchemy translates this into SELECT * FROM books
    books = db.query(models.Book).all()

    for book in books:
        print(f"{book.id}: {book.title}, {book.author}, {book.year}")

finally:
    db.close()