from fastapi import FastAPI
from app.database import db

# Import Routers
from app.routes.auth import router as auth_router
from app.routes.event import router as event_router
from app.routes.budget import router as budget_router

app = FastAPI(
    title="EventPilot AI API",
    version="1.0.0"
)

# Include Routers
app.include_router(auth_router)
app.include_router(event_router)
app.include_router(budget_router)

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to EventPilot AI 🚀"
    }

# Health Check API
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