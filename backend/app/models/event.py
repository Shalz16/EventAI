from datetime import datetime

def create_event(event):
    return {
        "title": event.title,
        "description": event.description,
        "venue": event.venue,
        "event_date": str(event.event_date),
        "expected_participants": event.expected_participants,
        "created_at": datetime.utcnow()
    }