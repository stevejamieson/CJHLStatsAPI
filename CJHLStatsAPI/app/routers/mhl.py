from fastapi import APIRouter, Header, HTTPException, Depends
from app.services.mhl_scaper import scrape_mhl_stats
from app.models import PlayerStats
from dotenv import load_dotenv
import os

router = APIRouter()

## env 
load_dotenv()

API_KEYS = {
    "Scout": os.getenv("API_KEY_SCOUT"),
    "Team": os.getenv("API_KEY_TEAM"),
    "Elite": os.getenv("API_KEY_ELITE"),
}

## Verify API Key Method
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS.values():
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key

## MHL EndPoint with API KEY LOCK 
@router.get("/stats/mhl", dependencies=[Depends(verify_api_key)])
def get_mhl_stats():
    # Return player stats
    return scrape_mhl_stats()
