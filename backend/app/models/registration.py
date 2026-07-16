from datetime import datetime


def create_registration(registration):
    return {
        "participant_name": registration.participant_name,
        "email": registration.email,
        "phone": registration.phone,
        "event_id": registration.event_id,
        "created_at": datetime.utcnow()
    }