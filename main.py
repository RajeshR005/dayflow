from fastapi import APIRouter, FastAPI
from app.api.api import api_router


app=FastAPI(title="DayFlow API")

app.include_router(api_router,prefix="/dayflow")

