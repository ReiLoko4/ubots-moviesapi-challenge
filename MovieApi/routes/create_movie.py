from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Movie
from MovieApi.connection import get_session
from MovieApi.utilities import string_to_time, string_to_datetime


router = APIRouter()


@router.post('/create_movie', response_model=Movie)
async def create_movie(
        movie: Movie,
        db: Session = Depends(get_session)
    ):
    if movie.id is not None:
        raise HTTPException(404, 'The movie id should not be provided, it will be generated automatically')
    movie.duration = string_to_time(movie.duration)
    movie.release_date = string_to_datetime(movie.release_date)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie
    