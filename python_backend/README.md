# FastAPI Backend Demo

## Overview
This is a demo backend application built with FastAPI. It provides basic CRUD endpoints for managing `Item` objects. This project is designed to show structured backend development and can be extended with databases, validation, testing, and AI features.

## Features Implemented
- In-memory CRUD API
  - `POST /items` — create a new item
  - `GET /items` — list all items
  - `PUT /items/{index}` — update an item by index
  - `DELETE /items/{index}` — delete an item by index
- Clean project structure with `app/` package
- Separate modules for routes, models, and app initialization

## Running the Project

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows

2. Install dependencies
    pip install -r requirements.txt

3. Run the server
    uvicorn app.main:app --reload

4. Visit the docs at: http://127.0.0.1:8000/docs

## Next Steps
Integrate SQLite database
Add Pydantic models with validation
Implement testing (pytest)
Add authentication and deployment pipeline