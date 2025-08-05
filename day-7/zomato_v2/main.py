from fastapi import FastAPI
from . import models
from .database import engine
from .routes import restaurants, menu_items

# Create all database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Zomato v2 API",
    description="An API for managing restaurants and their menus.",
    version="2.0.0",
)

# Include the routers
app.include_router(restaurants.router)
app.include_router(menu_items.router)
# Include the special creation router which has a nested path
app.include_router(menu_items.menu_item_creation_router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Zomato v2 API!"}
