from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.get('/movie/{movie_id}', response_model=Movie)
async def get_movie(
        movie_id: int,
        db: Session = Depends(get_session)
    ):
    movie = db.get(Movie, movie_id)
    if not movie:
        raise HTTPException(404, 'Movie not found')
    return movie
