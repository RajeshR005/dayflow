from fastapi import APIRouter, Depends, Form, HTTPException,UploadFile,File
from app.api.deps import get_db,get_current_user
from sqlalchemy.orm import Session
from app.models import ExpenseTracker,ExpenseMedia,Wallet,Media
from datetime import date,time,datetime,timedelta
from decimal import Decimal
from app.utils import file_storage
import os

router=APIRouter(tags=["Expense Tracker"])

@router.post('/add_income',description="This Route is for Adding the Income Resources")
def add_income_data(title:str=Form(...),amount:Decimal=Form(...),exp_date:date=Form(...),exp_time:str=Form(...),income_receipt:UploadFile=File(None),db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    try:
        new_income_record=ExpenseTracker(
            user_id=current_user.id,
            exp_title=title,
            amount=amount,
            mode="cash_in",
            exp_date=exp_date,
            exp_time=exp_time,
            created_by=current_user.id,
            modified_by=current_user.id
        )
        db.add(new_income_record)
        receipt_path=None
        if income_receipt:
            file_path,file_exe=file_storage(income_receipt,income_receipt.filename,sub_folder="income_imgs")

            new_media_record=Media(
                user_id=current_user.id,
                img_path=file_path,
                created_by=current_user.id,
                modified_by=current_user.id
            )
            db.add(new_media_record)
            db.flush()

            new_income_receipt=ExpenseMedia(
                expense_id=new_income_record.id,
                media_id=new_media_record.id
            )
            db.add(new_income_receipt)
            receipt_path=file_path
         
        current_balance=None 
        prev_balance=db.query(Wallet).filter(Wallet.user_id==current_user.id).first()
        if prev_balance:
            prev_balance.balance=prev_balance.balance+amount
            current_balance=prev_balance.balance
        else:
            new_wallet_record=Wallet(
                user_id=current_user.id,
                balance=amount,
                updated_by=current_user.id
            )
            db.add(new_wallet_record)
            current_balance=new_wallet_record.balance
        db.commit()

    except Exception as e:
        db.rollback()
        os.remove(receipt_path)
        return{"msg":"Trascational Entry Failed","error":e}
    
    return{
        "msg":"New Income Record Added",
        "title":new_income_record.exp_title,
        "amount":new_income_record.amount,
        "date":new_income_record.exp_date,
        "time":new_income_record.exp_time,
        "receipt":receipt_path,
        "Wallet_balance":current_balance
    }
        

    