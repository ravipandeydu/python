from fastapi import FastAPI
from .database import engine, Base

# Import the new routers
from .routes import restaurants, customers, orders, menu_items, reviews

# This line creates the database tables.
# In a production environment with Alembic, you might remove this.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Zomato v3 - Food Delivery System",
    description="A complete food delivery ecosystem with customers, orders, delivery tracking, and reviews.",
    version="3.0.0",
)

# Include all the routers from the 'routes' package
app.include_router(restaurants.router)
app.include_router(customers.router)
app.include_router(orders.router)
# Add the new routers to the app
app.include_router(menu_items.router)
app.include_router(reviews.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Zomato v3 API"}
