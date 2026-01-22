from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user_get_schema
from app.api.deps import get_db
from app.utils import *
from app.models import User
router = APIRouter( tags=["Authentication"])


@router.post("/user_registration",description="Register a new user")
def register_user(user_data:user_get_schema.UserGetSchema, db: Session = Depends(get_db)):

    user_exist=db.query(User).filter(User.email==user_data.email).first()
    if user_exist:
        return{"status":0,"msg":"user already exist! try logging in"}
    if user_data.password!=user_data.confirm_password:
        return{"status":0,"msg":"passwords not match"}
    
    if len(user_data.phone_number)!=10:
        return{"status":0,"msg":"invalid phone number"}

    
    user_data.password=hash_password(user_data.password)

    new_user = User(**user_data.model_dump(exclude={"confirm_password"}))
    db.add(new_user)
    db.flush()
    new_user.created_by=new_user.id
    new_user.modified_by=new_user.id
    db.commit()

    return {"message": "User registered successfully", "user_id": new_user.id, "email": new_user.email}