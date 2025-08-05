from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas, crud
from typing import List


def calculate_and_create_order(
    db: Session, order_data: schemas.OrderCreate, customer_id: int
):
    """
    Business logic to create an order:
    1. Fetches menu items to verify existence and get current prices.
    2. Calculates total amount.
    3. Creates the Order and associated OrderItem records.
    """
    total_amount = 0
    order_items_to_create = []

    # Verify all menu items exist and calculate total price
    for item_in in order_data.items:
        menu_item = (
            db.query(models.MenuItem)
            .filter(models.MenuItem.id == item_in.menu_item_id)
            .first()
        )
        if not menu_item or not menu_item.is_available:
            raise ValueError(
                f"Menu item with ID {item_in.menu_item_id} is not available."
            )
        if menu_item.restaurant_id != order_data.restaurant_id:
            raise ValueError(
                f"Menu item {menu_item.name} does not belong to the selected restaurant."
            )

        item_total = menu_item.price * item_in.quantity
        total_amount += item_total

        # Prepare OrderItem object (without committing yet)
        order_items_to_create.append(
            models.OrderItem(
                menu_item_id=item_in.menu_item_id,
                quantity=item_in.quantity,
                item_price=menu_item.price,  # Storing price at time of order
                special_requests=item_in.special_requests,
            )
        )

    # Get customer's address if no delivery address is provided
    delivery_address = order_data.delivery_address
    if not delivery_address:
        customer = crud.get_customer(db, customer_id)
        if not customer or not customer.address:
            raise ValueError(
                "Delivery address must be provided if customer has no default address."
            )
        delivery_address = customer.address

    # Create the main order record
    db_order = models.Order(
        customer_id=customer_id,
        restaurant_id=order_data.restaurant_id,
        total_amount=round(total_amount, 2),
        delivery_address=delivery_address,
        special_instructions=order_data.special_instructions,
    )

    # Associate the items with the order
    db_order.items = order_items_to_create

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


def update_restaurant_rating(db: Session, restaurant_id: int):
    """Calculates and updates the average rating for a restaurant."""
    avg_rating = (
        db.query(func.avg(models.Review.rating))
        .filter(models.Review.restaurant_id == restaurant_id)
        .scalar()
    )

    db_restaurant = crud.get_restaurant(db, restaurant_id)
    if db_restaurant:
        db_restaurant.rating = round(avg_rating, 2) if avg_rating else 0.0
        db.commit()
        db.refresh(db_restaurant)


def get_restaurant_analytics(db: Session, restaurant_id: int):
    """Calculates performance metrics for a restaurant."""
    # Total Revenue
    total_revenue = (
        db.query(func.sum(models.Order.total_amount))
        .filter(
            models.Order.restaurant_id == restaurant_id,
            models.Order.order_status == models.OrderStatus.delivered,
        )
        .scalar()
        or 0.0
    )

    # Total Orders
    total_orders = (
        db.query(func.count(models.Order.id))
        .filter(models.Order.restaurant_id == restaurant_id)
        .scalar()
    )

    # Popular Items
    popular_items_query = (
        db.query(
            models.MenuItem.name,
            func.sum(models.OrderItem.quantity).label("total_quantity"),
        )
        .join(models.OrderItem)
        .join(models.Order)
        .filter(models.Order.restaurant_id == restaurant_id)
        .group_by(models.MenuItem.name)
        .order_by(desc("total_quantity"))
        .limit(5)
        .all()
    )

    popular_items = [
        {"name": name, "count": count} for name, count in popular_items_query
    ]

    restaurant = crud.get_restaurant(db, restaurant_id)

    return schemas.RestaurantAnalytics(
        total_revenue=round(total_revenue, 2),
        total_orders=total_orders,
        average_rating=restaurant.rating if restaurant else 0.0,
        popular_items=popular_items,
    )
