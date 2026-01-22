from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class ExpenseMedia(Base):
    __tablename__="expense_media"

    id=Column(Integer,primary_key=True,autoincrement=True)
    expense_id=Column(Integer,ForeignKey('expense_tracker.id'))
    media_id=Column(Integer,ForeignKey('Media.id'))
    status=Column(Integer,default=1)

    #media table relationship
    medias=relationship("Media",back_populates="expense_medias",foreign_keys=[media_id])
    
    #diary table relationship
    expenses=relationship("ExpenseTracker", back_populates="expense_medias", foreign_keys=[todolist_id])


