from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type is ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        if (self.contact_type is ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signal must include a message")
        return self


def main() -> None:
    print("Alien contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    contact = AlienContact(contact_id="AC_2024_001",
                           contact_type=ContactType.radio,
                           timestamp=datetime(2024, 2, 15, 2, 5, 0),
                           location="Area 51, Nevada",
                           signal_strength=8.5, duration_minutes=45,
                           witness_count=5,
                           message_received="'Greetings from Zeta Reticuli'")

    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received}")
    print()
    print("======================================")
    print("Expected validation error:")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001", contact_type=ContactType.telepathic,
            timestamp=datetime(2024, 8, 15, 5, 0, 0),
            location="Area 51, Nevada",
            signal_strength=8.5, duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticul'"
            )
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'][13:])


if __name__ == "__main__":
    main()
