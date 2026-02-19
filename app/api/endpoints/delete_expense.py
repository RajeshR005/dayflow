from fastapi import APIRouter,Depends,Form,UploadFile,File
from sqlalchemy.orm import Session,joinedload
from app.api.deps import get_db,get_current_user
from app.models import *
from app.utils import *
from decimal import Decimal
from datetime import date
import os

router=APIRouter(tags=["Expense Tracker"])

@router.delete('/delete_expense/{expense_id}',description="This Route is for deleting the expenses")
def delete_expense_data(expense_id:int,)