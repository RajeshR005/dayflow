from fastapi import APIRouter,Depends,Form
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *
from app.schemas.expenses_schema import UpdateExpenseData


router=APIRouter(tags=["Expense Tracker"])

@router.put('edit_expense/{expense_id}',description="This Route is for Editing the Expense Data")
def edit_expense_data(expense_id:int, update_record=UpdateExpenseData,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return{}