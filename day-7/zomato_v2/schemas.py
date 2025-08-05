from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from decimal import Decimal
import datetime

# ==================================
# Base and Create Schemas
# ==================================

# --- Restaurant Schemas ---


class RestaurantBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    location: str
    cuisine: Optional[str] = None
    rating: Optional[Decimal] = Field(None, ge=0, le=5)


class RestaurantCreate(RestaurantBase):
    pass


# --- Menu Item Schemas ---


class MenuItemBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    price: Decimal = Field(..., decimal_places=2)
    category: str
    is_vegetarian: bool = False
    is_vegan: bool = False
    is_available: bool = True
    preparation_time: int

    @field_validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        return value


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, decimal_places=2)
    category: Optional[str] = None
    is_vegetarian: Optional[bool] = None
    is_vegan: Optional[bool] = None
    is_available: Optional[bool] = None
    preparation_time: Optional[int] = None


# ==================================
# Full Schemas for API Responses
# ==================================

# --- Basic Response Schemas ---


class MenuItem(MenuItemBase):
    id: int
    restaurant_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


class Restaurant(RestaurantBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True


# --- Nested Response Schemas ---


class RestaurantWithMenu(Restaurant):
    menu: List[MenuItem] = []


class MenuItemWithRestaurant(MenuItem):
    restaurant: Restaurant
