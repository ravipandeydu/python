from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import crud, models, schemas
from ..database import get_db
from ..utils import business_logic

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Restaurant, status_code=201)
def create_restaurant(
    restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)
):
    return crud.create_restaurant(db=db, restaurant=restaurant)


@router.get("/", response_model=List[schemas.Restaurant])
def read_restaurants(
    skip: int = 0,
    limit: int = 10,
    cuisine: Optional[str] = Query(None, description="Filter by cuisine type"),
    min_rating: Optional[float] = Query(
        None, ge=0, le=5, description="Filter by minimum rating"
    ),
    db: Session = Depends(get_db),
):
    restaurants = crud.get_restaurants(
        db, skip=skip, limit=limit, cuisine=cuisine, min_rating=min_rating
    )
    return restaurants


@router.get("/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.post(
    "/{restaurant_id}/menu-items/", response_model=schemas.MenuItem, status_code=201
)
def create_menu_item_for_restaurant(
    restaurant_id: int, item: schemas.MenuItemCreate, db: Session = Depends(get_db)
):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.create_restaurant_menu_item(
        db=db, item=item, restaurant_id=restaurant_id
    )


@router.get("/{restaurant_id}/orders", response_model=List[schemas.Order])
def get_restaurant_orders_history(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.get_restaurant_orders(db, restaurant_id=restaurant_id)


@router.get("/{restaurant_id}/reviews", response_model=List[schemas.Review])
def get_all_restaurant_reviews(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.get_restaurant_reviews(db, restaurant_id=restaurant_id)


@router.get("/{restaurant_id}/analytics", response_model=schemas.RestaurantAnalytics)
def get_restaurant_performance(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return business_logic.get_restaurant_analytics(db, restaurant_id=restaurant_id)
