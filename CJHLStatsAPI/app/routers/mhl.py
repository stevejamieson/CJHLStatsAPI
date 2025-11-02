from fastapi import APIRouter
from app.services.mhl_scaper import scrape_mhl_stats
from app.models import PlayerStats

router = APIRouter()

@router.get("/mhl", response_model=list[PlayerStats])
def get_mhl_stats():
    return scrape_mhl_stats()
