from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        if not any(
                member.rank in (Rank.commander, Rank.captain)
                for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            validate: int = sum(1 for member in self.crew
                                if member.years_experience >= 5)
            if validate < len(self.crew) / 2:
                raise ValueError("Long missions need 50%% experienced crew")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    sarah = CrewMember(name="Sarah Connor", member_id="id1",
                       rank=Rank.commander, specialization="Mission Command",
                       years_experience=10, is_active=True,
                       age=40)
    jhon = CrewMember(name="John Smith", member_id="id2",
                      rank=Rank.lieutenant, specialization="Navigation",
                      years_experience=10, is_active=True,
                      age=40)
    alice = CrewMember(name="Alice Jhonson", member_id="id3",
                       rank=Rank.officer, specialization="Engineering",
                       years_experience=10, is_active=True,
                       age=40)
    valid_mission = SpaceMission(mission_name="Mars Colony Establishment",
                                 mission_id="M2024_MARS", destination="Mars",
                                 duration_days=900, budget_millions=2500.0,
                                 crew=[sarah, jhon, alice],
                                 launch_date=datetime(2028, 1, 15, 8, 0, 0))
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    print(f"- {valid_mission.crew[0].name} ({valid_mission.crew[0].rank})"
          f" - {valid_mission.crew[0].specialization}")
    print(f"- {valid_mission.crew[1].name} ({valid_mission.crew[1].rank})"
          f" - {valid_mission.crew[1].specialization}")
    print(f"- {valid_mission.crew[2].name} ({valid_mission.crew[2].rank})"
          f" - {valid_mission.crew[2].specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        alice = CrewMember(name="Alice Jhonson", member_id="id3",
                           rank=Rank.officer, specialization="Engineering",
                           years_experience=10, is_active=True,
                           age=40
                           )
        valid_mission = SpaceMission(mission_name="Mars Colony Establishment",
                                     mission_id="M2024_MARS",
                                     destination="Mars",
                                     duration_days=900, budget_millions=2500.0,
                                     crew=[alice],
                                     launch_date=datetime(2024, 5, 5, 8, 0, 0))
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'][13:])


if __name__ == "__main__":
    main()
