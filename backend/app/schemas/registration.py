from pydantic import BaseModel, EmailStr


class RegistrationCreate(BaseModel):
    participant_name: str
    email: EmailStr
    phone: str
    event_id: str


class RegistrationUpdate(BaseModel):
    participant_name: str
    email: EmailStr
    phone: str
    event_id: str