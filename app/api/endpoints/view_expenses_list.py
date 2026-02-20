from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session,selectinload
from app.api.deps import get_db,get_current_user
from app.models import *



router=APIRouter(tags=["Expense Tracker"])

@router.get('/view_expenses_list',description="This Route is for view expense list")
def view_expenses_list(db:Session=Depends(get_db),current_user=Depends(get_current_user)):

    get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.user_id==current_user.id,ExpenseTracker.status==1).all()

    get_wallet=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()

    if not get_expense:
        return{"msg":"No Expense Data Found"}
    expense_data=[]
    for exp_data in get_expense:
        expense_record={
            "id":exp_data.id, 
            "title":exp_data.exp_title,
            "amount":exp_data.amount,
            "category":exp_data.category,
            "date":exp_data.exp_date,
            "time":exp_data.exp_time,
            "mode":exp_data.mode,
            
        }
        expense_data.append(expense_record)
    return{
        "expense_data":expense_data,
        "wallet_balance":get_wallet.balance
    }
        
     
    
        
     
    
    
      