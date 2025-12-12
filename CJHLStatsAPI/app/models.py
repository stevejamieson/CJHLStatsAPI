from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from statistics import stdev, mean


class PlayerMetadata(BaseModel):
    birthdate: Optional[date] = None
    age: int
    draft_eligible: bool
    is_rookie: bool


class PlayerAnalytics(BaseModel):
    GP: Optional[int] = None
    Points: Optional[int] = None

    # Raw inputs
    game_points: Optional[list[int]] = None  # Full season or recent game-by-game points
    peer_ppg_list: Optional[list[float]] = None  # For percentile comparison


    # Derived metrics
    age: Optional[int] = None
    draft_eligible: Optional[bool] = None
    points_per_game: Optional[float] = None
    percentile_rank: Optional[float] = None

    # Trend indicators
    rolling_avg_points: Optional[float] = None
    recent_points: Optional[int] = None
    consistency_score: Optional[float] = None
    hot_streak: Optional[bool] = None


    def compute_metrics(self):
        today = date.today()
        if self.birthdate:
            self.age = today.year - self.birthdate.year - (
                (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
            )
        self.draft_eligible = self.age is not None and self.age <= 20

        if self.GP and self.Points is not None:
            self.points_per_game = round(self.Points / self.GP, 2)

        if self.game_points:
            self.recent_points = sum(self.game_points[-5:]) if len(self.game_points) >= 5 else sum(self.game_points)
            self.consistency_score = round(stdev(self.game_points[-5:]), 2) if len(self.game_points[-5:]) > 1 else None
            self.rolling_avg_points = round(mean(self.game_points[-3:]), 2) if len(self.game_points) >= 3 else None
            self.hot_streak = self.recent_points >= 8

        if self.peer_ppg_list and self.points_per_game is not None:
            sorted_peers = sorted(self.peer_ppg_list)
            rank = sum(1 for p in sorted_peers if p <= self.points_per_game)
            self.percentile_rank = round(100 * rank / len(sorted_peers), 2)

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
