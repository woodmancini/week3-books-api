# use Path to dynamically create ./books.db
# create URL using sqlite:///

# create engine using sqlalchemy.create_engine
# use sessionmaker to create SessionLocal

# create a Base using declarative_base()

from pathlib import Path
from sqlalchemy import create_engine

# orm stands for Object Relation Mapper
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_PATH = Path(__file__).resolve().parent / "books.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
    # by default, sqlite strictly forces a connection to stay on the exact same CPU thread 
    # that opened it to prevent data corruption

    # here we overroverride this so FastAPI can safely reuse database connections 
    # across its request threads
)

# sessionlocal is a session factory - you call SessionLocal(), it triggers the __call__ method,
# and returns a new Session object
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
# bind=engine: This connects the factory to your engine. When the session actually needs to talk 
# to the database (to query data or commit changes), it borrows a connection from the engine's pool, 
# does its work, and returns the connection.

# "Flushing" is when SQLAlchemy takes your pending changes and sends them to the database before the final commit

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()