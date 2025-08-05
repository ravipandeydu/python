from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.MenuItem])
def read_all_menu_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all menu items across all restaurants.
    """
    items = crud.get_menu_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=schemas.MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific menu item by its ID.
    """
    db_item = crud.get_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return db_item


@router.put("/{item_id}", response_model=schemas.MenuItem)
def update_menu_item(
    item_id: int, item: schemas.MenuItemUpdate, db: Session = Depends(get_db)
):
    """
    Update a menu item's details.
    """
    db_item = crud.update_menu_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return db_item


@router.delete("/{item_id}", response_model=schemas.MenuItem)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete a menu item.
    """
    db_item = crud.delete_menu_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return db_item
