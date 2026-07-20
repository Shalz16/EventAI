from fastapi import APIRouter
from app.schemas.feedback import FeedbackCreate
from app.services.feedback_service import (
    add_feedback,
    get_feedback,
    get_analytics
)

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback & Analytics"]
)

@router.post("/")
def submit_feedback(feedback: FeedbackCreate):
    return add_feedback(feedback.dict())

@router.get("/{event_id}")
def view_feedback(event_id: str):
    return get_feedback(event_id)

@router.get("/analytics/{event_id}")
def analytics(event_id: str):
    return get_analytics(event_id)