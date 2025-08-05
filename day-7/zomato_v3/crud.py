from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, desc
from . import models, schemas
from typing import List, Optional
from datetime import date


# Restaurant CRUD
def get_restaurant(db: Session, restaurant_id: int):
    return (
        db.query(models.Restaurant)
        .options(joinedload(models.Restaurant.menu_items))
        .filter(models.Restaurant.id == restaurant_id)
        .first()
    )


def get_restaurants(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    cuisine: Optional[str] = None,
    min_rating: Optional[float] = None,
):
    query = db.query(models.Restaurant)
    if cuisine:
        query = query.filter(models.Restaurant.cuisine.ilike(f"%{cuisine}%"))
    if min_rating:
        query = query.filter(models.Restaurant.rating >= min_rating)
    return query.offset(skip).limit(limit).all()


def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


# Menu Item CRUD
def create_restaurant_menu_item(
    db: Session, item: schemas.MenuItemCreate, restaurant_id: int
):
    db_item = models.MenuItem(**item.dict(), restaurant_id=restaurant_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Customer CRUD
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


# Order CRUD
def get_order(db: Session, order_id: int):
    return (
        db.query(models.Order)
        .options(
            joinedload(models.Order.items).joinedload(models.OrderItem.menu_item),
            joinedload(models.Order.customer),
            joinedload(models.Order.restaurant),
            joinedload(models.Order.review).joinedload(models.Review.customer),
        )
        .filter(models.Order.id == order_id)
        .first()
    )


def get_customer_orders(db: Session, customer_id: int):
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()


def get_restaurant_orders(
    db: Session,
    restaurant_id: int,
    status: Optional[schemas.OrderStatus] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
):
    query = db.query(models.Order).filter(models.Order.restaurant_id == restaurant_id)
    if status:
        query = query.filter(models.Order.order_status == status)
    if start_date:
        query = query.filter(models.Order.order_date >= start_date)
    if end_date:
        query = query.filter(models.Order.order_date <= end_date)
    return query.order_by(desc(models.Order.order_date)).all()


def update_order_status(db: Session, order_id: int, status: schemas.OrderStatus):
    db_order = get_order(db, order_id=order_id)
    if db_order:
        db_order.order_status = status
        db.commit()
        db.refresh(db_order)
    return db_order


# Review CRUD
def get_restaurant_reviews(db: Session, restaurant_id: int):
    return (
        db.query(models.Review)
        .options(joinedload(models.Review.customer))
        .filter(models.Review.restaurant_id == restaurant_id)
        .all()
    )


def get_customer_reviews(db: Session, customer_id: int):
    return (
        db.query(models.Review).filter(models.Review.customer_id == customer_id).all()
    )


def create_order_review(
    db: Session,
    review: schemas.ReviewCreate,
    order_id: int,
    customer_id: int,
    restaurant_id: int,
):
    db_review = models.Review(
        **review.dict(),
        order_id=order_id,
        customer_id=customer_id,
        restaurant_id=restaurant_id,
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


# --- Menu Item CRUD ---
def get_menu_item(db: Session, item_id: int):
    return db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()


def get_menu_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MenuItem).offset(skip).limit(limit).all()


def update_menu_item(db: Session, item_id: int, item: schemas.MenuItemUpdate):
    db_item = get_menu_item(db, item_id)
    if not db_item:
        return None
    item_data = item.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_menu_item(db: Session, item_id: int):
    db_item = get_menu_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item


# --- Review CRUD ---
def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Review).offset(skip).limit(limit).all()


def update_review(db: Session, review_id: int, review: schemas.ReviewUpdate):
    db_review = get_review(db, review_id)
    if not db_review:
        return None
    review_data = review.dict(exclude_unset=True)
    for key, value in review_data.items():
        setattr(db_review, key, value)
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    db_review = get_review(db, review_id)
    if not db_review:
        return None

    # Store restaurant_id before deleting for rating recalculation
    restaurant_id = db_review.restaurant_id

    db.delete(db_review)
    db.commit()

    return restaurant_id
