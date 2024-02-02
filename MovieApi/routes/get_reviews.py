from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from MovieApi.models import Review, Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.get('/reviews/{movie_id}', response_model=list[Review])
async def get_reviews(
        movie_id: int,
        db: Session = Depends(get_session)
    ):
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(404, 'Movie not found')
    reviews = db.exec(select(Review)).all()
    return reviews
