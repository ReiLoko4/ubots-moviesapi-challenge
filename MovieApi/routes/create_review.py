from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Review, Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.post('/create_review', response_model=Review)
async def create_review(
        review: Review,
        db: Session = Depends(get_session)
    ):
    if review.id is not None:
        raise HTTPException(404, 'The review id should not be provided, it will be generated automatically')
    movies = db.get(Movie, review.movie_id)
    if not movies:
        raise HTTPException(404, 'Movie not found')
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
