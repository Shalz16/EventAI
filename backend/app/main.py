from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.database import db

from app.routes.auth import router as auth_router
from app.routes.event import router as event_router
from app.routes.budget import router as budget_router
from app.routes.volunteer import router as volunteer_router
from app.routes.registration import router as registration_router
from app.routes.ai_coordinator import router as ai_router
from app.routes import rag
from app.rag.rag_init import initialize_rag
from app.routes.feedback import router as feedback_router
#

app = FastAPI(
    title="EventPilot AI API",
    version="1.0.0"
)


# CORS for Frontend
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


# QR Code Static Folder
os.makedirs("qr_codes", exist_ok=True)

app.mount(
    "/qr_codes",
    StaticFiles(directory="qr_codes"),
    name="qr_codes"
)
@app.on_event("startup")
def load_rag():

    initialize_rag()

# Routers
app.include_router(auth_router)
app.include_router(event_router)
app.include_router(budget_router)
app.include_router(volunteer_router)
app.include_router(registration_router)
app.include_router(ai_router)
app.include_router(rag.router)
app.include_router(feedback_router)
# Home API
@app.get("/")
def home():
    return {
        "message": "EventPilot AI Backend Running"
    }


# Health Check
@app.get("/health")
def health():
    try:
        db.list_collection_names()
        return {
            "status": "Running",
            "database": "Connected"
        }
    except Exception as e:
        return {
            "status": "Running",
            "database": "Not Connected",
            "error": str(e)
        }