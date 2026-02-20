from fastapi import APIRouter,Depends,Form,UploadFile,File,HTTPException,status
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *
from app.utils import *
from decimal import Decimal
from datetime import date
import os

router=APIRouter(tags=["Expense Tracker"])

@router.delete('/delete_expense/{expense_id}',description="This Route is for deleting the expenses")
def delete_expense_data(expense_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.id==expense_id,ExpenseTracker.user_id==current_user.id,ExpenseTracker.status==1).options(joinedload(ExpenseTracker.expense_medias).joinedload(ExpenseMedia.medias)).first()

    if not get_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Expense Data Found")
    
    get_wallet=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()

    if not get_wallet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Wallet Found")
    try:
        get_expense.status=0
        for exp_data in get_expense.expense_medias:
                exp_data.status=0
                exp_data.medias.status=0
        if get_expense.mode=="cash_in":
             get_wallet.balance-=get_expense.amount
        else:
             get_wallet.balance+=get_expense.amount
        db.commit()
        return{
            "message":"Expense Deleted Successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT ,detail=str(e))
