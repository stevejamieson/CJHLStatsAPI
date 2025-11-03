from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class PlayerMetadata(BaseModel):
    birthdate: Optional[date] = None
    age: int
    draft_eligible: bool
    is_rookie: bool


class PlayerAnalytics(BaseModel):
    points_per_game: Optional[float] = None
    recent_points: Optional[int] = None  # Last 5 games
    consistency_score: Optional[float] = None  # Std dev or custom metric
    hot_streak: Optional[bool] = None
    name: str
    position: str
    team: str
    birthdate: Optional[date] = None  
    GP: int = Field(..., alias="GP")
    G: int = Field(..., alias="G")
    A: int = Field(..., alias="A")
    Points: int = Field(..., alias="Points")

    # Derived metrics
    age: Optional[int] = None
    draft_eligible: Optional[bool] = None
    points_per_game: Optional[float] = None

    # Trend indicators
    recent_points: Optional[int] = None  # Last 5 games
    consistency_score: Optional[float] = None  # Std deviation or custom metric
    hot_streak: Optional[bool] = None  # True if recent_points > threshold

    def compute_metrics(self):
        today = date.today()
        self.age = today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )
        self.draft_eligible = self.age <= 20  # Example rule
        self.points_per_game = round(self.points / self.games_played, 2) if self.games_played else 0.0
        self.hot_streak = self.recent_points is not None and self.recent_points >= 8
        # You can add logic for consistency_score based on game-by-game data

        return self


class PlayerStats(BaseModel):
    name: str
    position: str = Field(..., alias="Pos")
    team: str
    GP: int = Field(..., alias="GamesPlayed")
    G: int = Field(..., alias="Goals")
    A: int = Field(..., alias="Assists")
    Points: int = Field(..., alias="P")
    metadata: PlayerMetadata
    analytics: Optional[PlayerAnalytics] = None
