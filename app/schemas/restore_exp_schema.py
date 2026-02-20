from typing import Optional,List
from pydantic import BaseModel,ConfigDict

class RestoreExpenseIds(BaseModel):
    expense_ids:List[int]

    model_config = ConfigDict(from_attributes=True)
