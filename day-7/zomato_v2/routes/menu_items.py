from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/menu-items", tags=["Menu Items"])

# This endpoint needs to be in the `restaurants` router but is a core menu function
# It is implemented here logically and added to the app in main.py
# For better organization, it could also be defined in `restaurants.py`
# I'll create it separately and it will be attached to the root of the app
menu_item_creation_router = APIRouter(tags=["Menu Items"])


@menu_item_creation_router.post(
    "/restaurants/{restaurant_id}/menu-items/",
    response_model=schemas.MenuItem,
    status_code=status.HTTP_201_CREATED,
)
def create_menu_item_for_restaurant(
    restaurant_id: int, item: schemas.MenuItemCreate, db: Session = Depends(get_db)
):
    # Check if restaurant exists first
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return crud.create_restaurant_menu_item(
        db=db, item=item, restaurant_id=restaurant_id
    )


@router.get("/", response_model=List[schemas.MenuItem])
def read_menu_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_menu_items(db, skip=skip, limit=limit)
    return items


@router.get("/search", response_model=List[schemas.MenuItem])
def search_menu_items(
    category: Optional[str] = None,
    vegetarian: Optional[bool] = None,
    vegan: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    items = crud.search_menu_items(
        db, category=category, vegetarian=vegetarian, vegan=vegan
    )
    return items


@router.get("/{item_id}", response_model=schemas.MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item


@router.get("/{item_id}/with-restaurant", response_model=schemas.MenuItemWithRestaurant)
def read_menu_item_with_restaurant(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_menu_item_with_restaurant(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item


@router.put("/{item_id}", response_model=schemas.MenuItem)
def update_menu_item(
    item_id: int, item: schemas.MenuItemUpdate, db: Session = Depends(get_db)
):
    db_item = crud.update_menu_item(db, item_id=item_id, item_update=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return None
