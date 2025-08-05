from sqlalchemy.orm import Session, joinedload, selectinload
from . import models, schemas
from typing import Optional, List

# ==================================
# Restaurant CRUD Operations
# ==================================


def get_restaurant(db: Session, restaurant_id: int):
    return (
        db.query(models.Restaurant)
        .filter(models.Restaurant.id == restaurant_id)
        .first()
    )


def get_restaurants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Restaurant).offset(skip).limit(limit).all()


def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.model_dump())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


def delete_restaurant(db: Session, restaurant_id: int):
    db_restaurant = (
        db.query(models.Restaurant)
        .filter(models.Restaurant.id == restaurant_id)
        .first()
    )
    if db_restaurant:
        db.delete(db_restaurant)
        db.commit()
    return db_restaurant


# --- Enhanced Restaurant Queries ---


def get_restaurant_with_menu(db: Session, restaurant_id: int):
    """
    Efficiently fetches a restaurant and its menu items using selectinload.
    """
    return (
        db.query(models.Restaurant)
        .options(selectinload(models.Restaurant.menu_items))
        .filter(models.Restaurant.id == restaurant_id)
        .first()
    )


# ==================================
# Menu Item CRUD Operations
# ==================================


def get_menu_item(db: Session, item_id: int):
    return db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()


def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MenuItem).offset(skip).limit(limit).all()


def get_menu_items_for_restaurant(
    db: Session, restaurant_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.MenuItem)
        .filter(models.MenuItem.restaurant_id == restaurant_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_restaurant_menu_item(
    db: Session, item: schemas.MenuItemCreate, restaurant_id: int
):
    db_item = models.MenuItem(**item.model_dump(), restaurant_id=restaurant_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_menu_item(db: Session, item_id: int, item_update: schemas.MenuItemUpdate):
    db_item = get_menu_item(db, item_id)
    if not db_item:
        return None

    update_data = item_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_menu_item(db: Session, item_id: int):
    db_item = get_menu_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item


# --- Enhanced Menu Item Queries ---


def get_menu_item_with_restaurant(db: Session, item_id: int):
    """
    Fetches a menu item and its parent restaurant using joinedload.
    """
    return (
        db.query(models.MenuItem)
        .options(joinedload(models.MenuItem.restaurant))
        .filter(models.MenuItem.id == item_id)
        .first()
    )


def search_menu_items(
    db: Session,
    category: Optional[str],
    vegetarian: Optional[bool],
    vegan: Optional[bool],
    skip: int = 0,
    limit: int = 100,
):
    query = db.query(models.MenuItem)
    if category:
        query = query.filter(models.MenuItem.category.ilike(f"%{category}%"))
    if vegetarian is not None:
        query = query.filter(models.MenuItem.is_vegetarian == vegetarian)
    if vegan is not None:
        query = query.filter(models.MenuItem.is_vegan == vegan)
    return query.offset(skip).limit(limit).all()
