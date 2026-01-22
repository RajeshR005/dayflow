from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class ExpenseTracker(Base):
    __tablename__="expense_tracker"

    id=Column(Integer,primary_key=True, autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'),index=True)
    exp_title=Column(String(128))
    amount=Column(Integer)
    mode=Column(String(10)) #"cash_in" or "Cash_out" for audit
    exp_date=Column(Date)
    exp_time=Column(Time)
    Balance=Column(Integer) # i can use last() in the API to get the latest rather that hitting the API to count all the stuffs
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

    #User table realtionship
    user=relationship("User", back_populates="expense", foreign_keys=[user_id])
    creator_data=relationship("User", back_populates="exp_creator", foreign_keys=[created_by])
    modified_data=relationship("User", back_populates="exp_modifier", foreign_keys=[modified_by])

    #media table realtionship
    media=relationship("Media", back_populates="expense")