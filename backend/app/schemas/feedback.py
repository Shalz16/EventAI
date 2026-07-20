from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    event_id: str
    name: str
    rating: int
    comment: str