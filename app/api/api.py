from app.api.endpoints import user_registration,login,add_expense,add_income,view_expenses
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(user_registration.router)
api_router.include_router(login.router)
api_router.include_router(add_expense.router)
api_router.include_router(add_income.router)
api_router.include_router(view_expenses.router)

