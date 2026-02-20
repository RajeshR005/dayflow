from fastapi import APIRouter,Depends,Form,UploadFile,File,HTTPException,status
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *
from app.utils import *
from decimal import Decimal
from datetime import date
from app.schemas.restore_exp_schema import RestoreExpenseIds
import os

router=APIRouter(tags=["Expense Tracker"])

@router.patch('/restore_expense/',description="This Route is used to re-activate the expenses")
def restore_expense(expense_ids:RestoreExpenseIds,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    all_exp=[]
    for i in expense_ids:
        get_exp=db.query(ExpenseTracker).filter(ExpenseTracker.id==i).first()
        all_exp.append(get_exp)
    return all_exp
