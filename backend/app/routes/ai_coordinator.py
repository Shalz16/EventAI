from fastapi import APIRouter

from app.schemas.ai_schema import EventAIRequest

from app.services.gemini_service import generate_event_plan


router=APIRouter(
    prefix="/ai",
    tags=["AI Coordinator"]
)



@router.post("/event-plan")
def event_plan(data:EventAIRequest):

    result=generate_event_plan(data)

    return {
        "result":result
    }