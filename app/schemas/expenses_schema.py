from typing import Optional
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Numeric
from datetime import date 



class UpdateExpenseData(BaseModel):
    exp_title:str
    amount:Numeric
    mode:str
    category:str
    exp_date:date
    exp_time:str

    model_config = ConfigDict(from_attributes=True)