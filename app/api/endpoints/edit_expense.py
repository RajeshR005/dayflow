from fastapi import APIRouter,Depends,Form,UploadFile,File
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *
from app.utils import *
from decimal import Decimal
from datetime import date
import os


router=APIRouter(tags=["Expense Tracker"])

@router.put('/edit_expense/{expense_id}',description="This Route is for Editing the Expense Data")
def edit_expense_data(expense_id:int, title:str=Form(None),amount:Decimal=Form(None),category:str=Form(None),mode:str=Form(None),exp_date:date=Form(None),exp_time:str=Form(None), update_file:UploadFile=File(None),db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    
    try:

        get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.id==expense_id,ExpenseTracker.user_id==current_user.id).options(joinedload(ExpenseTracker.expense_medias).joinedload(ExpenseMedia.medias)).first()

        get_wallet=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()
        if not get_expense:
            return{"status":0,"msg":"no data found"}
        
        #reverse old transcation
        old_mode=get_expense.mode
        old_amount=get_expense.amount
        if old_mode=="cash_in":
            get_wallet.balance-=old_amount
        else:
            get_wallet.balance+=old_amount
        
        #add new values
        if mode:
            new_mode=mode
        else:
            new_mode=old_mode
        if amount:
            new_amount=amount
        else:
            new_amount=old_amount

        #add new transcation
        if  new_mode=="cash_in":
            get_wallet.balance+=new_amount
        else:
            get_wallet.balance-=new_amount
        get_expense.mode=new_mode
        get_expense.amount=new_amount
        
            
        if title:
            get_expense.exp_title=title
        if category:
            get_expense.category=category
        if exp_date:
            get_expense.exp_date=exp_date
        if exp_time:
            get_expense.exp_time=exp_time
       
        
        updated_path=None
        if update_file:
            for exp_media in get_expense.expense_medias:
                os.remove(exp_media.media.img_path)
                file_path,file_exe=file_storage(update_file,update_file.filename,sub_folder="expenses_imgs")
                
                exp_media.media.img_path=file_path
                updated_path=file_path
        db.commit()
    except Exception as e:
        db.rollback()
        if updated_path:
            os.remove(updated_path)
    return{
        "status":1,
        "msg":"data updated successfully"
    }

    