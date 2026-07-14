from datetime import datetime

def create_volunteer(volunteer):
    return {
        "name": volunteer.name,
        "email": volunteer.email,
        "phone": volunteer.phone,
        "role": volunteer.role,
        "availability": volunteer.availability,
        "created_at": datetime.utcnow()
    }