from datetime import datetime


def create_volunteer(volunteer):
    return {
        "name": volunteer.name,
        "email": volunteer.email,
        "phone": volunteer.phone,
        "department": volunteer.department,
        "year": volunteer.year,
        "skills": volunteer.skills,
        "availability": volunteer.availability,
        "assigned_event": volunteer.assigned_event,
        "created_at": datetime.utcnow()
    }