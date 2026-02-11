from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db,get_current_user
from app.models import *


router=APIRouter(tags=["Expense Tracker"])

@router.post('/view_expenses',description="This Route is for view expenses")
def view_expense_data(db:Session=Depends(get_db),current_user=Depends(get_current_user)):

    get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.user_id==current_user.id).all()

    get_wallet=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()
     
    li_expenses=[]
    for i in get_expense:
    
            li_expenses.append({
            "title":i.exp_title,
            "amount":i.amount,
            "date":i.exp_date,
            "time":i.exp_time,
            "mode":i.mode
            })
    return{
          "expenses":li_expenses,
          "wallet_balance":get_wallet.balance
    }
        
     
    
    
