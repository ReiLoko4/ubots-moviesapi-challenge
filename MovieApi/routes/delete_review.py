from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlmodel import Session
from MovieApi.models import Review, Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.delete('/delete_review/{review_id}', response_model=None)
async def delete_movie(
        review_id: int,
        db: Session = Depends(get_session)
    ):
    review_db = db.get(Review, review_id)
    if not review_db:
        raise HTTPException(404, f'Review not found with id: {review_id}')
    db.delete(review_db)
    db.commit()
    return {'ok': True, 'message': f'Review with id: {review_id} deleted'}
