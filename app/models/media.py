from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta


class Media(Base):
    __tablename__="media"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'),index=True)
    img_path=Column(String(300))#Image path
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)


    #User table realtionship
    users=relationship("User", back_populates="medias", foreign_keys=[user_id])
    creator_data=relationship("User", back_populates="media_creator", foreign_keys=[created_by])
    modified_data=relationship("User", back_populates="media_modifier", foreign_keys=[modified_by])

    #todolist_media table relationship
    todolist_medias=relationship("TodolistMedia", back_populates="medias")

    #Diary_media table relationship
    diary_medias=relationship("DiaryMedia", back_populates="medias")

    #Expense_media table relationship
    expense_medias=relationship("ExpenseMedia", back_populates="medias")




