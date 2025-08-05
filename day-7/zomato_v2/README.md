# Zomato v2: Restaurant-Menu System

This project is a FastAPI-based application for managing restaurants and their menus, demonstrating a one-to-many relationship using SQLAlchemy and Pydantic.

## Features

-   Full CRUD operations for both Restaurants and Menu Items.
-   One-to-many relationship: One Restaurant has many Menu Items.
-   Cascade Deletion: Deleting a restaurant automatically deletes its associated menu items.
-   Efficient Querying: Uses `selectinload` to prevent N+1 query issues when fetching related items.
-   Advanced Search: Filter menu items by category and dietary preferences (vegetarian/vegan).
-   Nested Schemas: Provides detailed responses, such as a restaurant with its full menu.
-   Data Validation: Uses Pydantic for robust request data validation (e.g., positive prices).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd zomato_v2_project
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**
    Open the `zomato_v2/database.py` file and update the `DATABASE_URL` with your database connection string (e.g., for PostgreSQL or SQLite).

5.  **Run the application:**
    ```bash
    uvicorn zomato_v2.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## API Documentation

Interactive API documentation (provided by Swagger UI and ReDoc) is available at:

-   **Swagger UI:** `http://127.0.0.1:8000/docs`
-   **ReDoc:** `http://127.0.0.1:8000/redoc`

### Key API Endpoints

#### Restaurants

-   `POST /restaurants/`: Create a new restaurant.
-   `GET /restaurants/`: Get a list of all restaurants.
-   `GET /restaurants/{restaurant_id}`: Get details of a specific restaurant.
-   `GET /restaurants/{restaurant_id}/menu`: Get all menu items for a specific restaurant.
-   `GET /restaurants/{restaurant_id}/with-menu`: Get restaurant details along with its complete menu.
-   `DELETE /restaurants/{restaurant_id}`: Delete a restaurant and all its menu items.

#### Menu Items

-   `POST /restaurants/{restaurant_id}/menu-items/`: Add a new menu item to a specific restaurant.
-   `GET /menu-items/`: Get a list of all menu items from all restaurants.
-   `GET /menu-items/search`: Search for menu items.
    -   *Query Parameters:* `category` (str), `vegetarian` (bool), `vegan` (bool)
    -   *Example:* `/menu-items/search?category=Appetizer&vegetarian=true`
-   `GET /menu-items/{item_id}`: Get details of a specific menu item.
-   `GET /menu-items/{item_id}/with-restaurant`: Get a menu item's details along with its parent restaurant's details.
-   `PUT /menu-items/{item_id}`: Update a menu item.
-   `DELETE /menu-items/{item_id}`: Delete a menu item.