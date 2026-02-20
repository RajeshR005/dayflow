from fastapi import APIRouter,Depends,Form,UploadFile,File,HTTPException,status
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *
from app.utils import *
from decimal import Decimal
from datetime import date
import os

router=APIRouter(tags=["Expense Tracker"])

@router.get('/deleted_expenses_list/',description="This Route is used to get the Deleted expense list")
def deleted_expenses_data(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    get_deleted_expenses=db.query(ExpenseTracker).filter(ExpenseTracker.user_id==current_user.id,ExpenseTracker.status==0).all()

    if not get_deleted_expenses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Deleted Expenses")
    li_del_expenses=[]
    for i in get_deleted_expenses:
            li_del_expenses.append({
                    "id":i.id,
                    "title":i.exp_title,
                    "amount":i.amount,
                    "category":i.category,
                    "date":i.exp_date,
                    "time":i.exp_time,
                    "mode":i.mode
                })
    return{"status":1,"deleted_expenses_list":li_del_expenses}