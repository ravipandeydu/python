from fastapi import FastAPI
from .database import engine, Base
from . import routes


# Asynchronously create the database tables on startup
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app = FastAPI(
    title="Zomato API - v1",
    description="This is the first version of a Zomato-like food delivery API.",
    version="1.0.0",
)


@app.on_event("startup")
async def on_startup():
    await create_tables()


# Include the router from routes.py
app.include_router(routes.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Zomato API v1. Visit /docs for API documentation."}
