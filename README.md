# Time & Greeting API

A simple FastAPI application built with Python 3.11+ and Uvicorn that shows the current time and greets users by username.

## Features

- ⏰ **Get Current Time** - Retrieve current date and time with multiple formats
- 👋 **Greet Users** - Personalized greetings with current timestamp
- 🏥 **Health Check** - Monitor API status
- 📚 **Interactive API Docs** - Built-in Swagger UI documentation
- ⚡ **Fast & Modern** - Built with FastAPI and Python 3.11+

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn

## Installation

```bash
# Clone the repository
git clone https://github.com/praju-hubexo/testing_github_pages.git
cd testing_github_pages

# Create a virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

### Option 1: Direct Python Execution
```bash
python app.py
```

### Option 2: Using Uvicorn directly
```bash
uvicorn app:app --reload
```

### Option 3: With custom host and port
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns welcome message and list of available endpoints.

**Response:**
```json
{
  "message": "Welcome to Time & Greeting API",
  "endpoints": {
    "time": "/time - Get current date and time",
    "greet": "/greet?username=John - Greet a user by username",
    "health": "/health - Health check"
  }
}
```

### 2. Get Current Time
```
GET /time
```
Returns the current date and time in multiple formats.

**Response:**
```json
{
  "timestamp": "2024-09-10T10:30:45.123456",
  "date": "2024-09-10",
  "time": "10:30:45",
  "day": "Wednesday",
  "timezone": "UTC"
}
```

### 3. Greet User (Query Parameter)
```
GET /greet?username=Alice
```
Greets a user by their username with current time.

**Response:**
```json
{
  "greeting": "Hello, Alice! 👋",
  "current_time": "10:30:45",
  "current_date": "2024-09-10",
  "message": "Welcome Alice, nice to see you!",
  "timestamp": "2024-09-10T10:30:45.123456"
}
```

### 4. Greet User (Path Parameter)
```
GET /greet/Alice
```
Alternative endpoint using path parameter instead of query parameter.

**Response:** Same as above

### 5. Health Check
```
GET /health
```
Simple health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-09-10T10:30:45.123456",
  "service": "Time & Greeting API"
}
```

### 6. Application Info
```
GET /info
```
Returns application metadata.

**Response:**
```json
{
  "app_name": "Time & Greeting API",
  "version": "1.0.0",
  "python_version": "3.11+",
  "server": "Uvicorn",
  "description": "A simple API to get current time and greet users",
  "started_at": "2024-09-10T10:30:45.123456"
}
```

## Usage Examples

### Using cURL

```bash
# Get current time
curl http://localhost:8000/time

# Greet a user
curl http://localhost:8000/greet?username=John

# Using path parameter
curl http://localhost:8000/greet/Sarah

# Health check
curl http://localhost:8000/health
```

### Using Python Requests

```python
import requests

# Get current time
response = requests.get("http://localhost:8000/time")
print(response.json())

# Greet a user
response = requests.get("http://localhost:8000/greet", params={"username": "Alice"})
print(response.json())
```

## Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

These provide interactive API documentation where you can test endpoints directly.

## Project Structure

```
testing_github_pages/
├── app.py              # Main FastAPI application
├── requirements.txt    # Project dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Development

### Reload on Changes
Use the `--reload` flag when running with Uvicorn to automatically restart the server when code changes:

```bash
uvicorn app:app --reload
```

### Debug Mode
Enable debug logging:

```bash
uvicorn app:app --log-level debug
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK` - Successful request
- `400 Bad Request` - Missing or invalid username
- `404 Not Found` - Endpoint not found
- `500 Internal Server Error` - Server error

Example error response:
```json
{
  "detail": "Username is required. Use /greet?username=YourName"
}
```

## License

Open source - feel free to use and modify!

## Version

- **Version**: 1.0.0
- **Python**: 3.11+
- **Framework**: FastAPI
- **Server**: Uvicorn
