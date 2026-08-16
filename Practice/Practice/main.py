from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    age: int = Field(..., ge=1, le=120)
    email: str | None = None

@app.get("/hello")
def hello_world():
    return "Hello"

@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created successfully",
        "data": user
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)