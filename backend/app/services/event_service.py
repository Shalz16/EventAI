from bson import ObjectId
from app.database import db
from app.models.event import create_event


def add_event(event):
    events = db.events

    new_event = create_event(event)

    result = events.insert_one(new_event)

    return {
        "message": "Event Created Successfully",
        "event_id": str(result.inserted_id)
    }


def get_all_events():
    events = db.events.find()

    data = []

    for event in events:
        event["_id"] = str(event["_id"])
        data.append(event)

    return data


def get_event(event_id):
    event = db.events.find_one({"_id": ObjectId(event_id)})

    if not event:
        return {"message": "Event not found"}

    event["_id"] = str(event["_id"])

    return event


def delete_event(event_id):
    result = db.events.delete_one({"_id": ObjectId(event_id)})

    if result.deleted_count == 0:
        return {"message": "Event not found"}

    return {"message": "Event Deleted Successfully"}

def update_event(event_id, event):

    result = db.events.update_one(
        {"_id": ObjectId(event_id)},
        {
            "$set": {
                "title": event.title,
                "description": event.description,
                "venue": event.venue,
                "event_date": str(event.event_date),
                "expected_participants": event.expected_participants
            }
        }
    )

    if result.modified_count == 0:
        return {"message": "Event not found or no changes made"}

    return {"message": "Event Updated Successfully"}