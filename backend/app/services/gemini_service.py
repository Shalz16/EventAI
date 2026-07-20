from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_event_plan(data):

    prompt = f"""
You are an AI Event Coordinator.

Create a detailed event plan.

Event Name: {data.event_name}
Type: {data.event_type}
Participants: {data.participants}
Budget: {data.budget}
Venue: {data.venue}

Provide:

1. Event Schedule
2. Volunteer Allocation
3. Budget Suggestions
4. Risk Prediction
5. Promotion Strategy
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
    )

    return response.text