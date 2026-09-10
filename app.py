"""
FastAPI Application - Time & Greeting Service
A simple API application that shows current time and greets users by username.

Python 3.11+ required
"""

from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Optional

app = FastAPI(
    title="Time & Greeting API",
    description="A simple API to get current time and greet users by username",
    version="1.0.0"
)


@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message and API documentation.
    """
    return {
        "message": "Welcome to Time & Greeting API",
        "endpoints": {
            "time": "/time - Get current date and time",
            "greet": "/greet?username=John - Greet a user by username",
            "health": "/health - Health check"
        }
    }


@app.get("/time")
async def get_time():
    """
    Returns the current date and time.
    """
    now = datetime.now()
    return {
        "timestamp": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day": now.strftime("%A"),
        "timezone": "UTC"
    }


@app.get("/greet")
async def greet_user(username: Optional[str] = None):
    """
    Greets a user by their username and shows the current time.
    
    Parameters:
    - username (optional): The name of the user to greet
    
    Example: /greet?username=Alice
    """
    if not username:
        raise HTTPException(
            status_code=400,
            detail="Username is required. Use /greet?username=YourName"
        )
    
    if not username.strip():
        raise HTTPException(
            status_code=400,
            detail="Username cannot be empty"
        )
    
    now = datetime.now()
    greeting = f"Hello, {username}! 👋"
    
    return {
        "greeting": greeting,
        "current_time": now.strftime("%H:%M:%S"),
        "current_date": now.strftime("%Y-%m-%d"),
        "message": f"Welcome {username}, nice to see you!",
        "timestamp": now.isoformat()
    }


@app.get("/greet/{username}")
async def greet_user_path(username: str):
    """
    Alternative endpoint to greet a user using path parameter.
    
    Example: /greet/Alice
    """
    if not username.strip():
        raise HTTPException(
            status_code=400,
            detail="Username cannot be empty"
        )
    
    now = datetime.now()
    greeting = f"Hello, {username}! 👋"
    
    return {
        "greeting": greeting,
        "current_time": now.strftime("%H:%M:%S"),
        "current_date": now.strftime("%Y-%m-%d"),
        "message": f"Welcome {username}, nice to see you!",
        "timestamp": now.isoformat()
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Time & Greeting API"
    }


@app.get("/info")
async def app_info():
    """
    Returns application information.
    """
    return {
        "app_name": "Time & Greeting API",
        "version": "1.0.0",
        "python_version": "3.11+",
        "server": "Uvicorn",
        "description": "A simple API to get current time and greet users",
        "started_at": datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    
    # Run with: python app.py
    # Or: uvicorn app:app --reload
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
