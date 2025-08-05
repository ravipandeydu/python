from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db
from ..utils import business_logic

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.Review])
def read_all_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all reviews in the system (e.g., for admin purposes).
    """
    reviews = crud.get_reviews(db, skip=skip, limit=limit)
    return reviews


@router.get("/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    """
    Get a single review by its ID.
    """
    db_review = crud.get_review(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review


@router.put("/{review_id}", response_model=schemas.Review)
def update_review(
    review_id: int, review: schemas.ReviewUpdate, db: Session = Depends(get_db)
):
    """
    Update a review. (Note: In a real app, you'd add ownership checks).
    """
    db_review = crud.update_review(db, review_id=review_id, review=review)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")

    # After updating the rating, recalculate the restaurant's average rating
    business_logic.update_restaurant_rating(db, restaurant_id=db_review.restaurant_id)

    return db_review


@router.delete("/{review_id}", response_model=dict)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    """
    Delete a review. This will also trigger a recalculation of the restaurant's average rating.
    """
    # The crud function returns the restaurant_id of the deleted review
    restaurant_id = crud.delete_review(db, review_id=review_id)

    if restaurant_id is None:
        raise HTTPException(status_code=404, detail="Review not found")

    # Recalculate the average rating for the affected restaurant
    business_logic.update_restaurant_rating(db, restaurant_id=restaurant_id)

    return {"message": "Review deleted successfully and restaurant rating updated."}
