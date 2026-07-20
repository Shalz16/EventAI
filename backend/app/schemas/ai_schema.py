from pydantic import BaseModel


class EventAIRequest(BaseModel):

    event_name: str
    event_type: str
    participants: int
    budget: int
    venue: str