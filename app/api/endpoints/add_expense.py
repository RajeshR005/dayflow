from fastapi import APIRouter, Depends, Form, HTTPException,UploadFile,File
from app.api.deps import get_db,get_current_user
from sqlalchemy.orm import Session
from app.models import ExpenseTracker,ExpenseMedia,Wallet,Media
from datetime import date,time,datetime,timedelta
from decimal import Decimal
import os
from app.utils import file_storage

router=APIRouter(tags=["Expense Tracker"])

@router.post('/add_expense',description="This Route is for Adding the Expense Data")
def add_expenses(title:str=Form(...),amount:Decimal=Form(...),exp_date:date=Form(...),exp_time:str=Form(...),add_receipt:UploadFile=File(None),db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    try:

        new_expense_record=ExpenseTracker(
            user_id=current_user.id,
            exp_title=title,
            amount=amount,
            mode="cash_out",
            exp_date=exp_date,
            exp_time=exp_time,
            created_by=current_user.id,
            modified_by=current_user.id
        )
        db.add(new_expense_record)
        db.flush()
        receipt_path=None
        if add_receipt:
            file_path,file_exe=file_storage(add_receipt,add_receipt.filename,sub_folder="expenses_imgs")

            new_media_record=Media(
                user_id=current_user.id,
                img_path=file_path,
                created_by=current_user.id,
                modified_by=current_user.id
            )
            db.add(new_media_record)
            db.flush()

            new_expense_receipt=ExpenseMedia(
                expense_id=new_expense_record.id,
                media_id=new_media_record.id
            )
            db.add(new_expense_receipt)

            receipt_path=file_path




        prev_balance=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()
        current_balance=None
        if prev_balance:
            prev_balance.balance=prev_balance.balance-amount
            current_balance=prev_balance.balance
        else:
            new_wallet_record=Wallet(
                user_id=current_user.id,
                balance=-amount,
                updated_by=current_user.id
            )
            db.add(new_wallet_record)
            current_balance=new_wallet_record.balance
        
        db.commit()
    except Exception as e:
        db.rollback()
        os.remove(receipt_path)
        return{"msg":"Transcational Entry Failed" , "error":e}
    
        
   
    return{
           "msg":"New Expense Added",
           "title":new_expense_record.exp_title,
           "amount":new_expense_record.amount,
           "date":new_expense_record.exp_date,
           "time":new_expense_record.exp_time,
           "receipt":receipt_path,
           "wallet_balance":current_balance
           }
    




    
