from database import SessionLocal, engine
import models

# instructs SQLAlchemy to automatically generate and execute the raw SQL CREATE TABLE commands 
# for all the models you have defined, physically creating the tables in your database
models.Base.metadata.create_all(bind=engine)
# because base is a metaclass, it knows about its subclasses, ie Book.
# Base translates the Python columns in Book into a Table blueprint,
# which it stores inside its own internal registry: Base.metadata

db = SessionLocal()

try:

    books = [
        models.Book(title="The Hobbit", year=1937, author="J.R.R. Tolkien"),
        models.Book(title="1984", year=1949, author="George Orwell"),
        models.Book(title="To Kill a Mockingbird", year=1960, author="Harper Lee"),
        models.Book(title="The Great Gatsby", year=1925, author="F. Scott Fitzgerald"),
        models.Book(title="Pride and Prejudice", year=1813, author="Jane Austen"),
        models.Book(title="The Catcher in the Rye", year=1951, author="J.D. Salinger"),
        models.Book(title="Moby-Dick", year=1851, author="Herman Melville"),
        models.Book(title="Frankenstein", year=1818, author="Mary Shelley"),
        models.Book(title="Dune", year=1965, author="Frank Herbert"),
        models.Book(title="The Lord of the Rings", year=1954, author="J.R.R. Tolkien"),
        models.Book(title="The Hitchhiker's Guide to the Galaxy", year=1979, author="Douglas Adams")
    ]

    for book in books:
        existing_book = (
            db.query(models.Book)
            .filter(models.Book.title == book.title)
            .first()
        )

        if existing_book is None:
            db.add(book)

    db.commit()

    print("Database created and courses checked.")

finally:
    db.close()