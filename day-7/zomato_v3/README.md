# Zomato v3: Complete Food Delivery System

This project is a complete food delivery API built with FastAPI and SQLAlchemy. It implements a complex relational schema to manage restaurants, menu items, customers, orders, and reviews.

## Directory Structure
    zomato_v3/
    ├── main.py              # App entry point
    ├── database.py          # SQLAlchemy setup
    ├── models.py            # SQLAlchemy ORM models
    ├── schemas.py           # Pydantic schemas
    ├── crud.py              # Data Access Layer functions
    ├── routes/              # API endpoint routers
    │   ├── init.py
    │   ├── restaurants.py
    │   ├── customers.py
    │   └── orders.py
    ├── utils/               # Business logic helpers
    │   ├── init.py
    │   └── business_logic.py
    ├── requirements.txt     # Project dependencies
    └── README.md

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd zomato_v3
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Application

1.  Navigate to the project's parent directory (the one containing the `zomato_v3` folder).
2.  Run the application using Uvicorn:
    ```bash
    uvicorn zomato_v3.main:app --reload
    ```
    The `--reload` flag automatically restarts the server when you make changes to the code.

3.  **Access the API:**
    Once the server is running, you can access the interactive API documentation at:
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

    The API root is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Key Features Implemented

* **Full CRUD** for Restaurants and Customers.
* **Complex Order Management:** Place orders with multiple items, update status, and view history.
* **Many-to-Many Relationship:** `Orders` and `MenuItems` are linked via an `OrderItem` association object that stores quantity and price.
* **Review System:** Customers can review delivered orders, which updates the restaurant's average rating.
* **Business Logic:**
    * Automatic calculation of order totals.
    * Validation to prevent reviewing incomplete orders.
    * Updating of restaurant average rating upon new reviews.
* **Analytics Endpoints:**
    * Get restaurant performance (revenue, total orders, popular items).
* **Advanced Search & Filtering:**
    * Find restaurants by cuisine or minimum rating.
* **Detailed & Nested Responses:** API responses include related data (e.g., an order includes customer, restaurant, and item details).