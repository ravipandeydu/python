from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas


# CREATE
async def create_restaurant(db: AsyncSession, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(**restaurant.model_dump())
    db.add(db_restaurant)
    await db.commit()
    await db.refresh(db_restaurant)
    return db_restaurant


# READ ONE
async def get_restaurant(db: AsyncSession, restaurant_id: int):
    result = await db.execute(
        select(models.Restaurant).filter(models.Restaurant.id == restaurant_id)
    )
    return result.scalars().first()


# READ ONE BY NAME (for duplicate check)
async def get_restaurant_by_name(db: AsyncSession, name: str):
    result = await db.execute(
        select(models.Restaurant).filter(models.Restaurant.name == name)
    )
    return result.scalars().first()


# READ ALL
async def get_restaurants(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Restaurant).offset(skip).limit(limit))
    return result.scalars().all()


# UPDATE
async def update_restaurant(
    db: AsyncSession, restaurant_id: int, restaurant_update: schemas.RestaurantUpdate
):
    db_restaurant = await get_restaurant(db=db, restaurant_id=restaurant_id)
    if not db_restaurant:
        return None

    update_data = restaurant_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_restaurant, key, value)

    await db.commit()
    await db.refresh(db_restaurant)
    return db_restaurant


# DELETE
async def delete_restaurant(db: AsyncSession, restaurant_id: int):
    db_restaurant = await get_restaurant(db=db, restaurant_id=restaurant_id)
    if not db_restaurant:
        return None
    await db.delete(db_restaurant)
    await db.commit()
    return db_restaurant


# SEARCH by Cuisine
async def search_restaurants_by_cuisine(
    db: AsyncSession, cuisine: str, skip: int = 0, limit: int = 100
):
    result = await db.execute(
        select(models.Restaurant)
        .filter(models.Restaurant.cuisine_type.ilike(f"%{cuisine}%"))
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


# GET Active Restaurants
async def get_active_restaurants(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(models.Restaurant)
        .filter(models.Restaurant.is_active == True)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()
