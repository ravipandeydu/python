from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from .models import OrderStatus


# Base Schemas (common attributes)
class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True


class RestaurantBase(BaseModel):
    name: str
    location: str
    cuisine: str


class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: str


class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class OrderItemBase(BaseModel):
    menu_item_id: int
    quantity: int
    special_requests: Optional[str] = None


# Schemas for Creating new records
class MenuItemCreate(MenuItemBase):
    pass


class RestaurantCreate(RestaurantBase):
    pass


class CustomerCreate(CustomerBase):
    pass


class ReviewCreate(ReviewBase):
    pass


class OrderItemCreate(OrderItemBase):
    pass


class OrderCreate(BaseModel):
    restaurant_id: int
    delivery_address: Optional[str] = None  # If None, use customer's default
    special_instructions: Optional[str] = None
    items: List[OrderItemCreate]


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


# --- Response Schemas (what the API returns) ---
# Use `orm_mode` to allow Pydantic to read data from ORM models


class Config:
    orm_mode = True


class MenuItem(MenuItemBase):
    id: int
    restaurant_id: int

    class Config(Config):
        pass


class Restaurant(RestaurantBase):
    id: int
    rating: float
    created_at: datetime
    menu_items: List[MenuItem] = []

    class Config(Config):
        pass


class SimpleRestaurant(RestaurantBase):
    id: int
    rating: float

    class Config(Config):
        pass


class Customer(CustomerBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config(Config):
        pass


class SimpleCustomer(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config(Config):
        pass


class OrderItem(OrderItemBase):
    id: int
    item_price: float
    menu_item: MenuItem  # Nested Menu Item details

    class Config(Config):
        pass


class Review(ReviewBase):
    id: int
    customer_id: int
    restaurant_id: int
    order_id: int
    created_at: datetime
    customer: SimpleCustomer  # Nested customer details

    class Config(Config):
        pass


class Order(BaseModel):
    id: int
    customer_id: int
    restaurant_id: int
    order_status: OrderStatus
    total_amount: float
    delivery_address: str
    special_instructions: Optional[str] = None
    order_date: datetime
    delivery_time: Optional[datetime] = None
    items: List[OrderItem] = []
    customer: SimpleCustomer
    restaurant: SimpleRestaurant
    review: Optional[Review] = None

    class Config(Config):
        pass


# Analytics Schemas
class RestaurantAnalytics(BaseModel):
    total_revenue: float
    total_orders: int
    average_rating: float
    popular_items: List[dict]  # e.g., [{"name": "Pizza", "count": 100}]


class CustomerAnalytics(BaseModel):
    total_spent: float
    total_orders: int
    favorite_restaurant: Optional[SimpleRestaurant]
    favorite_cuisine: Optional[str]


# Schemas for Updating existing records (all fields are optional)
class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None


class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None
