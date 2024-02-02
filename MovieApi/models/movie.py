from sqlmodel import SQLModel, Field
from datetime import datetime, time


class Movie(SQLModel, table=True):
    __tablename__ = 'movies'
    id: int = Field(primary_key=True, default=None)
    title: str
    synopsis: str
    dubbing: str
    subtitle: str
    director: str
    duration: time
    release_date: datetime
    rating: float
