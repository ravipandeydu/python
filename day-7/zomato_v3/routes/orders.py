from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db
from ..utils import business_logic

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{order_id}", response_model=schemas.Order)
def read_order_details(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.put("/{order_id}/status", response_model=schemas.Order)
def update_order_status(
    order_id: int,
    status_update: schemas.OrderStatusUpdate,
    db: Session = Depends(get_db),
):
    updated_order = crud.update_order_status(
        db, order_id=order_id, status=status_update.status
    )
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.get_order(db, updated_order.id)


@router.post("/{order_id}/review", response_model=schemas.Review, status_code=201)
def add_review_for_order(
    order_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)
):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if db_order.order_status != models.OrderStatus.delivered:
        raise HTTPException(status_code=400, detail="Can only review delivered orders.")
    if db_order.review:
        raise HTTPException(
            status_code=400, detail="A review for this order already exists."
        )

    created_review = crud.create_order_review(
        db,
        review=review,
        order_id=order_id,
        customer_id=db_order.customer_id,
        restaurant_id=db_order.restaurant_id,
    )

    # After adding a review, update the restaurant's average rating
    business_logic.update_restaurant_rating(db, restaurant_id=db_order.restaurant_id)

    return created_review
