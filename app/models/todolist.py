from sqlalchemy import Column, Text,String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class Todolist(Base):
    __tablename__="todolist"


    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'),index=True)
    todo_title=Column(String(128))
    todo_description=Column(Text)
    todo_date=Column(Date)
    todo_time=Column(Time)
    status=Column(Integer,default=1)#1 - Incomplete 0 - complete -1 - softdelete
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

    #User table realtionship
    users=relationship("User", back_populates="todolist", foreign_keys=[user_id])
    creator_data=relationship("User", back_populates="todolist_creator", foreign_keys=[created_by])
    modified_data=relationship("User", back_populates="todolist_modifier", foreign_keys=[modified_by])

    #Todolist_media table realtionship
    todolist_medias=relationship("TodolistMedia",back_populates="todolists")

