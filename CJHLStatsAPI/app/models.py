from pydantic import BaseModel

class PlayerStats(BaseModel):
    name: str
    position: str
    team: str
    GP: int
    G: int
    A: int
    Points: int