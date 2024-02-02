from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.delete('/delete_movie/{movie_id}', response_model=None)
async def delete_movie(
        movie_id: int,
        db: Session = Depends(get_session)
    ):
    movies_db = db.get(Movie, movie_id)
    if not movies_db:
        raise HTTPException(404, f'Movie not found with id: {movie_id}')
    db.delete(movies_db)
    db.commit()
    return {'ok': True, 'message': f'Movie with id: {movie_id} deleted'}
