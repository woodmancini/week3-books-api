from sqlalchemy import Column, Integer, String
from database import Base

# defines the schema for our "books" table
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    author = Column(String, nullable=False)