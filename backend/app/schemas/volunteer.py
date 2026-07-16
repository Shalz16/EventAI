from pydantic import BaseModel, EmailStr


class VolunteerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    department: str
    year: int
    skills: str
    availability: str
    assigned_event: str


class VolunteerUpdate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    department: str
    year: int
    skills: str
    availability: str
    assigned_event: str