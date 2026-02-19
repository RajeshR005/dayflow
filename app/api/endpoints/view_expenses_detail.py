from fastapi import APIRouter,Depends,Form
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *



router=APIRouter(tags=["Expense Tracker"])

@router.get('/view_expense_detail/{expense_id}',description="This Route is for view expense details")
def view_expense_detail(expense_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):

    get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.id==expense_id,ExpenseTracker.user_id==current_user.id,ExpenseTracker.status==1).options(joinedload(ExpenseTracker.expense_medias).joinedload(ExpenseMedia.medias)).first()


    if not get_expense:
        return{"msg":"No Expense Data Found"}
    
    exp_files=[]
    for exp_media in get_expense.expense_medias:
        exp_files.append(exp_media.medias.img_path)
    
    return{
        "id":get_expense.id,
        "title":get_expense.exp_title,
        "amount":get_expense.amount,
        "category":get_expense.category,
        "date":get_expense.exp_date,
        "time":get_expense.exp_time,
        "mode":get_expense.mode,
        "file":exp_files
    }
    

  
        
     
    
        
     
    
    
      