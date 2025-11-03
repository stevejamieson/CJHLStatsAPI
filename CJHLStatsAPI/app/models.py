from pydantic import BaseModel, Field

class PlayerMetadata(BaseModel):
    birthdate: str
    age: int
    draft_eligible: bool
    is_rookie: bool


class PlayerStats(BaseModel):
    name: str
    position: str= Field(..., alias="Pos")
    team: str
    GP: int= Field(..., alias="GamesPlayed")
    G: int= Field(..., alias="Goals")
    A: int= Field(..., alias="Assists")
    Points: int= Field(..., alias="P")
    metadata: PlayerMetadata
