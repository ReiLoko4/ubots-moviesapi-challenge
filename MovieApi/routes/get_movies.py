from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from MovieApi.models import Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.get('/movies', response_model=list[Movie])
async def get_movies(
        db: Session = Depends(get_session)
    ):
    movie = db.exec(select(Movie)).all()
    return movie
