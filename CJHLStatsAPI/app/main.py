from fastapi import FastAPI
from app.routers import mhl # etc.

app = FastAPI(title="CJHL Stats API")

@app.get("/favicon.ico")
def favicon():
    return {}

@app.get("/")
def read_root():
    return {"message": "CJHL Stats API is up and running!"}

app.include_router(mhl.router, prefix="/stats")

