from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

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


# def verify_jwt_token(token,credentials_exception):
     


