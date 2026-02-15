from fastapi import APIRouter,Depends,Form
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *



router=APIRouter(tags=["Expense Tracker"])

@router.post('/view_expense_detail',description="This Route is for view expense details")
def view_expense_detail(expense_id:int=Form(...),db:Session=Depends(get_db),current_user=Depends(get_current_user)):

    get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.id==expense_id,ExpenseTracker.user_id==current_user.id).options(joinedload(ExpenseTracker.expense_medias).joinedload(ExpenseMedia.medias)).all()


    if not get_expense:
        return{"msg":"No Expense Data Found"}
    expense_data=[]
    for exp_data in get_expense:
        expense_record={
            "id":exp_data.id,
            "title":exp_data.exp_title,
            "amount":exp_data.amount,
            "date":exp_data.exp_date,
            "time":exp_data.exp_time,
            "mode":exp_data.mode,
            "file":[]
        }
        for exp_media in exp_data.expense_medias:
            expense_record["file"].append(exp_media.medias.img_path)
        expense_data.append(expense_record)
    return{
        "expense_data":expense_data
    }
        
     
    
        
     
    
    
      