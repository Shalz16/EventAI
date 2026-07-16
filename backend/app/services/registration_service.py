from bson import ObjectId
from app.database import db
from app.models.registration import create_registration


def add_registration(registration):
    registrations = db.registrations

    new_registration = create_registration(registration)

    result = registrations.insert_one(new_registration)

    return {
        "message": "Registration Created Successfully",
        "registration_id": str(result.inserted_id)
    }


def get_all_registrations():
    registrations = db.registrations.find()

    data = []

    for registration in registrations:
        registration["_id"] = str(registration["_id"])
        data.append(registration)

    return data


def get_registration(registration_id):
    registration = db.registrations.find_one(
        {"_id": ObjectId(registration_id)}
    )

    if not registration:
        return {"message": "Registration not found"}

    registration["_id"] = str(registration["_id"])

    return registration


def update_registration(registration_id, registration):

    result = db.registrations.update_one(
        {"_id": ObjectId(registration_id)},
        {
            "$set": {
                "participant_name": registration.participant_name,
                "email": registration.email,
                "phone": registration.phone,
                "event_id": registration.event_id
            }
        }
    )

    if result.modified_count == 0:
        return {"message": "Registration not found or no changes made"}

    return {"message": "Registration Updated Successfully"}


def delete_registration(registration_id):

    result = db.registrations.delete_one(
        {"_id": ObjectId(registration_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Registration not found"}

    return {"message": "Registration Deleted Successfully"}