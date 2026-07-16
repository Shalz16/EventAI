from fastapi import APIRouter

from app.schemas.registration import (
    RegistrationCreate,
    RegistrationUpdate
)

from app.services.registration_service import (
    add_registration,
    get_all_registrations,
    get_registration,
    update_registration,
    delete_registration,
    generate_registration_qr
)


router = APIRouter(
    prefix="/registration",
    tags=["Registration Management"]
)


# Create Registration
@router.post("/register")
def register(registration: RegistrationCreate):
    return add_registration(registration)


# Get All Registrations
@router.get("/")
def all_registrations():
    return get_all_registrations()


# Get Single Registration
@router.get("/{registration_id}")
def single_registration(registration_id: str):
    return get_registration(registration_id)


# Update Registration
@router.put("/{registration_id}")
def edit_registration(
    registration_id: str,
    registration: RegistrationUpdate
):
    return update_registration(
        registration_id,
        registration
    )


# Delete Registration
@router.delete("/{registration_id}")
def remove_registration(registration_id: str):
    return delete_registration(registration_id)


# Generate QR Code
@router.post("/{registration_id}/generate-qr")
def create_qr(registration_id: str):

    return generate_registration_qr(
        registration_id
    )