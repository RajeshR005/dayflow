from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class TodolistMedia(Base):
    __tablename__="todolist_media"

    id=Column(Integer,primary_key=True,autoincrement=True)
    todolist_id=Column(Integer,ForeignKey('todolist.id'))
    media_id=Column(Integer,ForeignKey('media.id'))
    status=Column(Integer,default=1)

    #media table relationship
    medias=relationship("Media",back_populates="todolist_medias",foreign_keys=[media_id])
    
    #diary table relationship
    todolists=relationship("Todolist", back_populates="todolist_medias", foreign_keys=[todolist_id])
