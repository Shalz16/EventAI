from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.event import router as event_router
from app.routes.budget import router as budget_router
from app.routes.volunteer import router as volunteer_router
from app.routes.registration import router as registration_router

app = FastAPI(title="EventPilot AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "EventPilot AI Backend Running"}

app.include_router(auth_router)
app.include_router(event_router)
app.include_router(budget_router)
app.include_router(volunteer_router)
app.include_router(registration_router)