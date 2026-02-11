from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime, time, timedelta

class DiaryMedia(Base):
    __tablename__="diary_media"

    id=Column(Integer,primary_key=True,autoincrement=True)
    diary_id=Column(Integer,ForeignKey('diary.id'),index=True)
    media_id=Column(Integer,ForeignKey('media.id'))
    status=Column(Integer,default=1)

    #media table relationship
    medias=relationship("Media",back_populates="diary_medias",foreign_keys=[media_id])
    
    #diary table relationship
    diaries=relationship("Diary", back_populates="diary_medias", foreign_keys=[diary_id])

