from app.models.feedback import feedback_collection

def add_feedback(data):
    feedback_collection.insert_one(data)
    return {"message": "Feedback submitted successfully"}

def get_feedback(event_id):
    feedback = list(
        feedback_collection.find(
            {"event_id": event_id},
            {"_id": 0}
        )
    )
    return feedback

def get_analytics(event_id):

    feedbacks = list(
        feedback_collection.find(
            {"event_id": event_id},
            {"_id": 0}
        )
    )

    total = len(feedbacks)

    if total == 0:
        return {
            "total_feedback": 0,
            "average_rating": 0
        }

    average = sum(f["rating"] for f in feedbacks) / total

    return {
        "total_feedback": total,
        "average_rating": round(average, 2),
        "five_star": sum(1 for f in feedbacks if f["rating"] == 5),
        "four_star": sum(1 for f in feedbacks if f["rating"] == 4),
        "three_star": sum(1 for f in feedbacks if f["rating"] == 3),
        "two_star": sum(1 for f in feedbacks if f["rating"] == 2),
        "one_star": sum(1 for f in feedbacks if f["rating"] == 1)
    }