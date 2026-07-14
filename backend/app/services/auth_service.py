from app.database import db
from app.models.user import create_user
from app.utils.security import hash_password, verify_password
from app.schemas.user import UserRegister
from app.utils.security import verify_password, create_access_token
from app.schemas.user import UserLogin
def register_user(user: UserRegister):
    users = db.users

    # Check existing email
    if users.find_one({"email": user.email}):
        return {"message": "Email already exists"}

    # Create user
    new_user = create_user(
        user.name,
        user.email,
        hash_password(user.password)
    )

    users.insert_one(new_user)

    return {"message": "User Registered Successfully"}
def login_user(user: UserLogin):
    users = db.users

    existing_user = users.find_one({"email": user.email})

    if not existing_user:
        return {"message": "User not found"}

    if not verify_password(user.password, existing_user["password"]):
        return {"message": "Invalid password"}

    token = create_access_token(
        {"sub": existing_user["email"]}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }