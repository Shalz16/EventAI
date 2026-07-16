from fastapi import APIRouter
from app.schemas.registration import RegistrationCreate, RegistrationUpdate
from app.services.registration_service import (
    add_registration,
    get_all_registrations,
    get_registration,
    update_registration,
    delete_registration
)

router = APIRouter(
    prefix="/registration",
    tags=["Registration Management"]
)


@router.post("/register")
def register(registration: RegistrationCreate):
    return add_registration(registration)


@router.get("/")
def all_registrations():
    return get_all_registrations()


@router.get("/{registration_id}")
def single_registration(registration_id: str):
    return get_registration(registration_id)


@router.put("/{registration_id}")
def edit_registration(
    registration_id: str,
    registration: RegistrationUpdate
):
    return update_registration(
        registration_id,
        registration
    )


@router.delete("/{registration_id}")
def remove_registration(registration_id: str):
    return delete_registration(registration_id)