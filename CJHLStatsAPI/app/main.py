from fastapi import FastAPI
from app.routers import mhl # etc.

app = FastAPI(title="Junior A Hockey Stats API")

@app.get("/favicon.ico")
def favicon():
    return {}

@app.get("/")
def read_root():
    return {"message": "Junior A Hockey Stats API is running!"}

app.include_router(mhl.router, prefix="/stats")

