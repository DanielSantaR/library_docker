from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id : int
    name : str
    literary_genre : Optional[str]
    author : Optional[str]
    year : Optional[str]
    price : Optional[float]

class BookCreate(Book):
    name : str
    literary_genre : Optional[str]
    author : Optional[str]
    year : Optional[str]
    price : Optional[float]

class BookUpdate(Book):
    name : Optional[str]
    literary_genre : Optional[str]
    author : Optional[str]
    year : Optional[str]
    price : Optional[float]
    price : Optional[float]

