from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from . import crud, schemas
from .database import get_db

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.post(
    "/", response_model=schemas.Restaurant, status_code=status.HTTP_201_CREATED
)
async def create_restaurant(
    restaurant: schemas.RestaurantCreate, db: AsyncSession = Depends(get_db)
):
    db_restaurant = await crud.get_restaurant_by_name(db, name=restaurant.name)
    if db_restaurant:
        raise HTTPException(
            status_code=400, detail="Restaurant with this name already exists"
        )
    return await crud.create_restaurant(db=db, restaurant=restaurant)


@router.get("/", response_model=List[schemas.Restaurant])
async def read_restaurants(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    restaurants = await crud.get_restaurants(db, skip=skip, limit=limit)
    return restaurants


@router.get("/active", response_model=List[schemas.Restaurant])
async def read_active_restaurants(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    restaurants = await crud.get_active_restaurants(db, skip=skip, limit=limit)
    return restaurants


@router.get("/search", response_model=List[schemas.Restaurant])
async def search_restaurants(
    cuisine: str = Query(..., min_length=3, description="Search by cuisine type"),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    restaurants = await crud.search_restaurants_by_cuisine(
        db, cuisine=cuisine, skip=skip, limit=limit
    )
    if not restaurants:
        raise HTTPException(
            status_code=404, detail=f"No restaurants found for cuisine: {cuisine}"
        )
    return restaurants


@router.get("/{restaurant_id}", response_model=schemas.Restaurant)
async def read_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    db_restaurant = await crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.put("/{restaurant_id}", response_model=schemas.Restaurant)
async def update_restaurant(
    restaurant_id: int,
    restaurant: schemas.RestaurantUpdate,
    db: AsyncSession = Depends(get_db),
):
    updated_restaurant = await crud.update_restaurant(
        db=db, restaurant_id=restaurant_id, restaurant_update=restaurant
    )
    if updated_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return updated_restaurant


@router.delete("/{restaurant_id}", response_model=schemas.Restaurant)
async def delete_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    deleted_restaurant = await crud.delete_restaurant(db, restaurant_id=restaurant_id)
    if deleted_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return deleted_restaurant
