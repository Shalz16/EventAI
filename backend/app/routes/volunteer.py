from fastapi import APIRouter
from app.schemas.volunteer import VolunteerCreate, VolunteerUpdate
from app.services.volunteer_service import (
    add_volunteer,
    get_all_volunteers,
    get_volunteer,
    update_volunteer,
    delete_volunteer
)

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteer Management"]
)


@router.post("/create")
def create(volunteer: VolunteerCreate):
    return add_volunteer(volunteer)


@router.get("/")
def all_volunteers():
    return get_all_volunteers()


@router.get("/{volunteer_id}")
def single_volunteer(volunteer_id: str):
    return get_volunteer(volunteer_id)


@router.put("/{volunteer_id}")
def edit_volunteer(volunteer_id: str, volunteer: VolunteerUpdate):
    return update_volunteer(volunteer_id, volunteer)


@router.delete("/{volunteer_id}")
def remove_volunteer(volunteer_id: str):
    return delete_volunteer(volunteer_id)