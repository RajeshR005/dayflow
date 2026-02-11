from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time, Float, Numeric
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class ExpenseTracker(Base):
    __tablename__="expense_tracker"

    id=Column(Integer,primary_key=True, autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'),index=True)
    exp_title=Column(String(128),index=True)
    amount=Column(Numeric(10,2))
    mode=Column(String(10)) #"cash_in" or "Cash_out" for audit
    exp_date=Column(Date)
    exp_time=Column(Time)
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

    #User table realtionship
    users=relationship("User", back_populates="expenses", foreign_keys=[user_id])
    creator_data=relationship("User", back_populates="exp_creator", foreign_keys=[created_by])
    modified_data=relationship("User", back_populates="exp_modifier", foreign_keys=[modified_by])

    #expense_media table realtionship
    expense_medias=relationship("ExpenseMedia",back_populates="expenses")
    