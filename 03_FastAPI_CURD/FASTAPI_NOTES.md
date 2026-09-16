# 🚀 FastAPI Quick Notes

## 📌 What is FastAPI?

FastAPI is a modern, high-performance Python framework used to build REST APIs quickly and efficiently.

### Key Benefits

- ✅ Fast and lightweight
- ✅ Automatic API documentation (Swagger UI)
- ✅ Built-in data validation using Pydantic
- ✅ Easy to learn and use
- ✅ Supports Python type hints
- ✅ Asynchronous programming support

---

# 🏗️ FastAPI Architecture

```text
Client
   │
   ▼
FastAPI Application
   │
   ▼
API Endpoint
   │
   ▼
JSON Response
```

---

# 🚀 Creating a FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()
```

---

# 🌐 First API Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

### Output

```json
{
    "message": "Hello World"
}
```

---

# 📥 Path Parameters

Path parameters are part of the URL and are commonly used to identify a specific resource.

### URL Example

```text
/users/101
```

### Implementation

```python
from fastapi import Path

@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(
        ...,
        ge=1,
        description="User ID"
    )
):
    return {"user_id": user_id}
```

---

# 🎯 Why Use `Path()`?

`Path()` provides validation, constraints, and API documentation support.

### Features

- ✅ Input validation
- ✅ Description for Swagger UI
- ✅ Minimum and maximum value constraints
- ✅ Better API documentation

```text
           Path()
              │
    ┌─────────┼─────────┐
    │         │         │
Validation  Docs   Constraints
```

---

# 📤 Query Parameters

Query parameters are appended to the URL after a `?`.

### URL Example

```text
/products?name=laptop
```

### Implementation

```python
@app.get("/products")
def get_products(name: str):
    return {"name": name}
```

### Response

```json
{
    "name": "laptop"
}
```

---

# 📌 Query Parameter Notes

- Query parameters start after `?`
- Each parameter is a key-value pair
- Multiple parameters are separated using `&`

### Example

```text
/patient?city=Delhi&sort_by=age
```

### Common Query Parameters

```text
sort_by = name | age | weight | height

order = asc | desc
```

---

# 📦 Request Body

A request body is used to send data from the client to the server, generally with POST and PUT requests.

### Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user
```

---

# ✅ Pydantic Validation

Pydantic validates incoming request data automatically.

### Example

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

Benefits:

- Data validation
- Type checking
- Automatic error responses
- Cleaner code

---

# 🔄 HTTP Methods

| Method | Purpose |
|----------|----------|
| GET | Read data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Delete data |

---

# 📚 Swagger Documentation

Start the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically generates interactive API documentation.

---

# 📊 Common HTTP Status Codes

## Success Codes

| Code | Meaning |
|--------|----------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |

## Client Error Codes

| Code | Meaning |
|--------|----------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |

## Server Error Codes

| Code | Meaning |
|--------|----------|
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

---

# 🚨 HTTPException in FastAPI

`HTTPException` is used to return custom error responses.

### Example

```python
from fastapi import HTTPException

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):

    if patient_id != "P001":
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {"patient_id": patient_id}
```

### Response

```json
{
    "detail": "Patient not found"
}
```

---

# ➕ POST Request Workflow

POST requests are used to create new resources.

### Flow

```text
Client
   │
 POST Request
   │
   ▼
Server
   │
Validate Data
   │
Save Record
   │
   ▼
Response to Client
```

### Steps

1. Receive data from client
2. Validate using Pydantic
3. Save data to database/file
4. Return response

---

# ✏️ PUT Request (Update)

PUT requests are used to update existing records.

### Requirements

- Resource ID
- Request Body

### Example

```text
PUT /patients/P001
```

### Typical Steps

1. Check whether record exists
2. Receive updated data
3. Validate using Pydantic
4. Update record
5. Save changes
6. Return success response

### Partial Update Model

```python
class PatientUpdate(BaseModel):
    name: str | None = None
    city: str | None = None
    age: int | None = None
```

---

# ❌ DELETE Request

DELETE requests remove an existing resource.

### Example

```python
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: str):

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    del data[patient_id]

    return {
        "message": "Patient deleted successfully"
    }
```

### Flow

```text
Client
   │
DELETE Request
   │
   ▼
Find Record
   │
Delete Record
   │
   ▼
Success Response
```

---

# 🎯 FastAPI Interview Tips

### Difference Between Path and Query Parameters

| Path Parameter | Query Parameter |
|---------------|---------------|
| Required | Usually Optional |
| Part of URL | Added after `?` |
| Identifies resource | Filters/Sorts data |

Example:

```text
/users/101
```

(Path Parameter)

```text
/users?city=Mumbai
```

(Query Parameter)

---

# ✅ Useful Commands

### Install FastAPI

```bash
pip install fastapi
```

### Install Uvicorn

```bash
pip install uvicorn
```

### Run Application

```bash
uvicorn main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

### Open ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 📌 Summary

FastAPI provides:

- Fast API development
- Automatic documentation
- Built-in request validation
- Type safety using Python hints
- Easy integration with databases
- Production-ready REST APIs

A standard FastAPI project typically includes:

- FastAPI Application
- Pydantic Models
- CRUD Operations
- Validation
- Exception Handling
- Swagger Documentation