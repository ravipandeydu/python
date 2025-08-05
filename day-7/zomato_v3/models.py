import enum
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
    Enum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


# Enum for Order Status
class OrderStatus(enum.Enum):
    placed = "placed"
    confirmed = "confirmed"
    preparing = "preparing"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"
    cancelled = "cancelled"


# Association table for Order <-> MenuItem (Many-to-Many with payload)
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), index=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), index=True)
    quantity = Column(Integer, nullable=False)
    item_price = Column(Float, nullable=False)  # Price at the time of order
    special_requests = Column(String, nullable=True)

    order = relationship("Order", back_populates="items")
    menu_item = relationship("MenuItem")


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    location = Column(String, index=True)
    cuisine = Column(String, index=True)
    rating = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    menu_items = relationship(
        "MenuItem", back_populates="restaurant", cascade="all, delete-orphan"
    )
    orders = relationship("Order", back_populates="restaurant")
    reviews = relationship("Review", back_populates="restaurant")


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)

    restaurant = relationship("Restaurant", back_populates="menu_items")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True)
    address = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(
        Integer, ForeignKey("customers.id"), nullable=False, index=True
    )
    restaurant_id = Column(
        Integer, ForeignKey("restaurants.id"), nullable=False, index=True
    )
    order_status = Column(Enum(OrderStatus), default=OrderStatus.placed)
    total_amount = Column(Float, nullable=False)
    delivery_address = Column(String, nullable=False)
    special_instructions = Column(String, nullable=True)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    delivery_time = Column(DateTime(timezone=True), nullable=True)

    customer = relationship("Customer", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    items = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )
    review = relationship(
        "Review", back_populates="order", uselist=False, cascade="all, delete-orphan"
    )


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(
        Integer, ForeignKey("customers.id"), nullable=False, index=True
    )
    restaurant_id = Column(
        Integer, ForeignKey("restaurants.id"), nullable=False, index=True
    )
    order_id = Column(
        Integer, ForeignKey("orders.id"), unique=True, nullable=False
    )  # One review per order
    rating = Column(Integer, nullable=False)  # e.g., 1 to 5
    comment = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews")
    order = relationship("Order", back_populates="review")
