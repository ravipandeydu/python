import re
from datetime import time
from pydantic import BaseModel, Field, validator
from typing import Optional

# Phone number regex for basic validation
PHONE_NUMBER_REGEX = r"^\+?[1-9]\d{1,14}$"


class RestaurantBase(BaseModel):
    name: str = Field(
        ..., min_length=3, max_length=100, description="Name of the restaurant"
    )
    description: Optional[str] = Field(
        None, description="A short description of the restaurant"
    )
    cuisine_type: str = Field(..., description="Type of cuisine served")
    address: str = Field(..., description="Physical address of the restaurant")
    phone_number: str = Field(..., description="Contact phone number")
    rating: float = Field(0.0, ge=0.0, le=5.0, description="Rating from 0.0 to 5.0")
    is_active: bool = True
    opening_time: time
    closing_time: time

    @validator("phone_number")
    def validate_phone_number(cls, v):
        if not re.match(PHONE_NUMBER_REGEX, v):
            raise ValueError("Invalid phone number format.")
        return v

    @validator("closing_time")
    def validate_time(cls, v, values, **kwargs):
        if "opening_time" in values and v <= values["opening_time"]:
            raise ValueError("Closing time must be after opening time.")
        return v


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = None
    cuisine_type: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)
    is_active: Optional[bool] = None
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None

    @validator("phone_number")
    def validate_phone_number(cls, v):
        if v and not re.match(PHONE_NUMBER_REGEX, v):
            raise ValueError("Invalid phone number format.")
        return v


class Restaurant(RestaurantBase):
    id: int
    created_at: Optional[str] = (
        None  # Using str to handle SQLAlchemy's timezone-aware datetime
    )
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True
