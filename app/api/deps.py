from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator
from fastapi import Depends,HTTPException,status
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from app.models import User

oauth2_schema=OAuth2PasswordBearer(tokenUrl='dayflow/login')

load_dotenv()

def get_db() -> Generator:
       
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()

"""The Below code is for JWT Encoding and Decoding"""

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

def create_jwt_token(data:dict):
     
    encoded_data=jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_data

 
def verify_jwt_token(token,credentials_exception):
    try:
     
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

        user_id=payload.get("user_id")
        if user_id is None:
            raise(credentials_exception)
        return user_id
    except JWTError:
        raise(credentials_exception)
    
def get_current_user(token:str= Depends(oauth2_schema),db:Session=Depends(get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials",headers={"WWW-Authenticate":"Bearer"})

    user_id=verify_jwt_token(token,credentials_exception)

    user_data=db.query(User).filter(User.id==user_id).first()

    return user_data



    

     

     


