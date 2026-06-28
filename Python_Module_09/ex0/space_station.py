from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class Spacestation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space station Data Validation")
    print("========================================")
    print("Valid station created:")
    station = Spacestation(
        station_id="ISS001",
        name="International Space station",
        crew_size=6,
        power_level=85.5,
        last_maintenance=datetime(2024, 1, 15, 5, 0, 0),
        oxygen_level=92.3,
        is_operational=True
        )
    status: str = ("Operational" if station.is_operational
                   else "Not Operational")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")
    print("\n========================================")
    print("Expected Validation error:")
    try:
        station = Spacestation(
            station_id="ISS001",
            name="International Space station",
            crew_size=21,
            power_level=85.5,
            last_maintenance=datetime(2024, 2, 15, 5, 0, 0),
            oxygen_level=92.3,
            is_operational=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
