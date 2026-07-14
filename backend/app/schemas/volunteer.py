from pydantic import BaseModel

class VolunteerCreate(BaseModel):
    name: str
    email: str
    phone: str
    role: str
    availability: str


class VolunteerUpdate(BaseModel):
    name: str
    email: str
    phone: str
    role: str
    availability: str