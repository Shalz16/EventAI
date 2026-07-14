from fastapi import APIRouter
from app.schemas.event import EventCreate, EventUpdate
from app.services.event_service import (
    add_event,
    get_all_events,
    get_event,
    update_event,
    delete_event
)

router = APIRouter(
    prefix="/events",
    tags=["Event Management"]
)


# Create Event
@router.post("/create")
def create(event: EventCreate):
    return add_event(event)


# Get All Events
@router.get("/")
def all_events():
    return get_all_events()


# Get Single Event
@router.get("/{event_id}")
def single_event(event_id: str):
    return get_event(event_id)


# Update Event
@router.put("/{event_id}")
def edit_event(event_id: str, event: EventUpdate):
    return update_event(event_id, event)


# Delete Event
@router.delete("/{event_id}")
def remove_event(event_id: str):
    return delete_event(event_id)