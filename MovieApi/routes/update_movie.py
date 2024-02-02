from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Movie
from MovieApi.connection import get_session
from MovieApi.utilities import string_to_time, string_to_datetime


router = APIRouter()


@router.put('/update_movie/{movie_id}', response_model=Movie)
async def update_movie(
        movie_id: int,
        movie: Movie,
        db: Session = Depends(get_session)
    ):
    movie_db = db.get(Movie, movie_id)
    if not movie_db:
        raise HTTPException(404, f'Movie with id {movie_id} not found')
    movie_data = movie.model_dump(exclude_unset=True, exclude_defaults=True)
    for key, value in movie_data.items():
        if key == 'id':
            continue
        setattr(movie_db, key, value)
        if key == 'duration':
            movie_db.duration = string_to_time(movie_db.duration)
        if key == 'release_date':
            movie_db.release_date = string_to_datetime(movie_db.release_date)
    db.add(movie_db)
    db.commit()
    db.refresh(movie_db)
    return movie_db
