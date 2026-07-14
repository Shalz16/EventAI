from bson import ObjectId
from app.database import db
from app.models.volunteer import create_volunteer


def add_volunteer(volunteer):
    volunteers = db.volunteers

    new_volunteer = create_volunteer(volunteer)

    result = volunteers.insert_one(new_volunteer)

    return {
        "message": "Volunteer Created Successfully",
        "volunteer_id": str(result.inserted_id)
    }


def get_all_volunteers():
    volunteers = db.volunteers.find()

    data = []

    for volunteer in volunteers:
        volunteer["_id"] = str(volunteer["_id"])
        data.append(volunteer)

    return data


def get_volunteer(volunteer_id):
    volunteer = db.volunteers.find_one({"_id": ObjectId(volunteer_id)})

    if not volunteer:
        return {"message": "Volunteer not found"}

    volunteer["_id"] = str(volunteer["_id"])

    return volunteer


def update_volunteer(volunteer_id, volunteer):

    result = db.volunteers.update_one(
        {"_id": ObjectId(volunteer_id)},
        {
            "$set": {
                "name": volunteer.name,
                "email": volunteer.email,
                "phone": volunteer.phone,
                "role": volunteer.role,
                "availability": volunteer.availability
            }
        }
    )

    if result.modified_count == 0:
        return {"message": "Volunteer not found or no changes made"}

    return {"message": "Volunteer Updated Successfully"}


def delete_volunteer(volunteer_id):

    result = db.volunteers.delete_one({"_id": ObjectId(volunteer_id)})

    if result.deleted_count == 0:
        return {"message": "Volunteer not found"}

    return {"message": "Volunteer Deleted Successfully"}