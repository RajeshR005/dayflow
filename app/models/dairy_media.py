from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class DairyMedia(Base):
    __tablename__="dairy_media"

    id=Column(Integer,primary_key=True,autoincrement=True)
    diary_id=Column(Integer,ForeignKey('Diary.id'))
    media_id=Column(Integer,ForeignKey('Media.id'))
    status=Column(Integer,default=1)

    #media table relationship
    medias=relationship("Media",back_populates="diary_medias",foreign_keys=[media_id])
    
    #diary table relationship
    dairys=relationship("Dairy", back_populates="diary_medias", foreign_keys=[todolist_id])

