# Lingolift FastAPI

A backend API built with [FastAPI](https://fastapi.tiangolo.com/) for language learning applications.

## Tools & Technologies

- **FastAPI**: Web framework for building APIs with Python 3.7+
- **Uvicorn**: ASGI server for running FastAPI apps
- **Pydantic**: Data validation and settings management
- **SQLAlchemy** (optional): ORM for database interactions
- **Alembic** (optional): Database migrations
- **Python-dotenv**: For environment variable management

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/lingolift-fastapi.git
    cd lingolift-fastapi
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the App

1. **Start the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    - Replace `main:app` with the actual Python file and app instance if different.

2. **Access the API docs:**
    - Open [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## Configuration

- Environment variables can be set in a `.env` file.

## Testing

- Run tests (if available):
  ```bash
  pytest
  ```

## License

MIT License
