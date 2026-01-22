from fastapi import APIRouter, Depends
from app.models import User
from app.utils import *
from app.api.deps import get_db,create_jwt_token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(tags=["Authentication"])

@router.post('/login',description="This Route is for User's Login")
def user_login(login_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    check_user=db.query(User).filter(User.email==login_data.username).first()
    if not check_user:
        return{"status":0,"msg":"invalid credentials"}
    check_password=verify_password(login_data.password,check_user.password)
    if not check_password:
        return{"status":0,"msg":"invalid credentials"}
    token=create_jwt_token(data={"user_id":check_user.id})
    # return[
    #     {
    #         "name":f'{check_user.first_name} {check_user.last_name}',
    #         "email":check_user.email,
    #         "msg":"Login Successful"
    #     }
    # ]
    return{"access_token":token,"token_type":"bearer"}
    