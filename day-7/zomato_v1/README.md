# Zomato API - Version 1

This project is the first version of a Zomato-like food delivery application API. It provides basic CRUD (Create, Read, Update, Delete) functionality for managing restaurants.

## Features

- Create, read, update, and delete restaurants.
- List all restaurants with pagination.
- List only active restaurants.
- Search for restaurants by cuisine type.
- Data validation for inputs.
- Automatic API documentation using Swagger UI and ReDoc.

## Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy (Async)
- **Data Validation:** Pydantic

## Setup and Installation

1.  **Clone the repository (or set up the files as described).**

2.  **Navigate to the project directory:**
    ```bash
    cd zomato_v1
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Run the application using Uvicorn:

```bash
uvicorn main:app --reload