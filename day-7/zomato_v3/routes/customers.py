from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db
from ..utils import business_logic

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Customer, status_code=201)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_customer(db=db, customer=customer)


@router.get("/", response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)


@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.post("/{customer_id}/orders/", response_model=schemas.Order, status_code=201)
def place_new_order_for_customer(
    customer_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)
):
    db_customer = crud.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    try:
        created_order = business_logic.calculate_and_create_order(
            db, order_data=order, customer_id=customer_id
        )
        return crud.get_order(
            db, created_order.id
        )  # Re-fetch to load all relationships
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{customer_id}/orders", response_model=List[schemas.Order])
def read_customer_order_history(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.get_customer_orders(db, customer_id=customer_id)


@router.get("/{customer_id}/reviews", response_model=List[schemas.Review])
def read_customer_reviews(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return crud.get_customer_reviews(db, customer_id=customer_id)
