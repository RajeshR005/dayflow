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
    updated_path=None
    try:

        get_expense=db.query(ExpenseTracker).filter(ExpenseTracker.id==expense_id,ExpenseTracker.user_id==current_user.id,ExpenseTracker.status==1).options(joinedload(ExpenseTracker.expense_medias).joinedload(ExpenseMedia.medias)).first()
        if not get_expense:
            return{"status":0,"msg":"no expense data found"}

        get_wallet=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()
        if not get_wallet:
            return{"status":0,"msg":"no wallet data found"}
        
        if mode or amount is not None:
            #reverse old transcation
            old_mode=get_expense.mode
            old_amount=get_expense.amount
            if old_mode=="cash_in":
                get_wallet.balance-=old_amount
            else:
                get_wallet.balance+=old_amount
            
            #add new values
            if mode is not None:
                new_mode=mode
            else:
                new_mode=old_mode
            if amount is not None:
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
       
        
        
        if update_file:
            for exp_media in get_expense.expense_medias:
                old_path=os.path.normpath(exp_media.medias.img_path)
                if old_path:
                   os.remove(old_path)
                file_path,file_exe=file_storage(update_file,update_file.filename,sub_folder="expenses_imgs")
                
                exp_media.medias.img_path=file_path
                updated_path=old_path
        db.commit()
        return{
        "status":1,
        "msg":"data updated successfully"
    }
    except Exception as e:
        db.rollback()
        if updated_path:
            os.remove(updated_path)
        return {
        "status": 0,
        "msg": "Something went wrong",
        "error": str(e)
    }
   

    