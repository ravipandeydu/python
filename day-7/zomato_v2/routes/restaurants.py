from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.post(
    "/", response_model=schemas.Restaurant, status_code=status.HTTP_201_CREATED
)
def create_restaurant(
    restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)
):
    return crud.create_restaurant(db=db, restaurant=restaurant)


@router.get("/", response_model=List[schemas.Restaurant])
def read_restaurants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    restaurants = crud.get_restaurants(db, skip=skip, limit=limit)
    return restaurants


@router.get("/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.delete("/{restaurant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.delete_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return None


# --- New Endpoints with Relationships ---


@router.get("/{restaurant_id}/with-menu", response_model=schemas.RestaurantWithMenu)
def read_restaurant_with_menu(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant_with_menu(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.get("/{restaurant_id}/menu", response_model=List[schemas.MenuItem])
def read_menu_for_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    # First, check if the restaurant exists
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    menu_items = crud.get_menu_items_for_restaurant(db, restaurant_id=restaurant_id)
    return menu_items
