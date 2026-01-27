from sqlalchemy import Column,String,Integer,Date,DateTime,ForeignKey,Text,Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,time,datetime,timedelta

class Diary(Base):
    __tablename__="diary"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    diary_title=Column(String(128))
    diary_description=Column(Text)
    diary_date=Column(Date)
    diary_time=Column(Time)
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

     #User table relationship
    users=relationship("User", back_populates="diaries", foreign_keys=[user_id])
    creator_data=relationship("User", back_populates="diary_creator", foreign_keys=[created_by])
    modified_data=relationship("User", back_populates="diary_modifier", foreign_keys=[modified_by])

    #Diary_media table realtionship
    diary_medias=relationship("DiaryMedia",back_populates="diaries")

