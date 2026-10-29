from pydantic import BaseModel, ConfigDict, Field

class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    year: int = Field(gt=-3000, lt=3000)
    author: str = Field(min_length=1, max_length=100)

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: int

    model_config = ConfigDict(from_attributes=True)
    # tells Pydantic to check for object attributes (fields) if dictionary look-ups fail