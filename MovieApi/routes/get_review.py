from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Review
from MovieApi.connection import get_session


router = APIRouter()


@router.get('/review/{review_id}', response_model=Review)
async def get_review(
        review_id: int,
        db: Session = Depends(get_session)
    ):
    review = db.get(Review, review_id)
    if not review:
        raise HTTPException(404, 'Review not found')
    return review
