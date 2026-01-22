from app.api.endpoints import user_registration,login
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(user_registration.router)
api_router.include_router(login.router)

