import uvicorn
from fastapi import FastAPI

app = FastAPI()

from app.routes.student import router

app.include_router(router, prefix="/students", tags=["students"])


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
