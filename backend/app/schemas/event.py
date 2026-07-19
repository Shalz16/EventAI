from pydantic import BaseModel
from datetime import date

class EventCreate(BaseModel):
    title: str
    description: str
    venue: str
    event_date: date
    expected_participants: int

class EventUpdate(BaseModel):
    title: str
    description: str
    venue: str
    event_date: date
    expected_participants: int