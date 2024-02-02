from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from MovieApi.models import Review, Movie
from MovieApi.connection import get_session


router = APIRouter()


@router.put('/update_review/{review_id}', response_model=Review)
async def update_review(
        review_id: int,
        review: Review,
        db: Session = Depends(get_session)
    ):
    movie_db = db.get(Movie, review.movie_id)
    if not movie_db:
        raise HTTPException(404, "Review's movie not found")
    review_db = db.get(Review, review_id)
    if not review_db:
        raise HTTPException(404, f'Review with id {review_id} not found')
    review_data = review.model_dump(exclude_unset=True)
    for key, value in review_data.items():
        setattr(review_db, key, value)
    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db
