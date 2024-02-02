from sqlmodel import SQLModel, Field


class Review(SQLModel, table=True):
    __tablename__ = 'reviews'
    id: int = Field(primary_key=True, default=None)
    movie_id: int = Field(foreign_key='movies.id', default=None)
    rating: float
    title: str
    text: str
    reviewer: str
