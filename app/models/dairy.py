from sqlalchemy import Column,String,Integer,Date,DateTime,ForeignKey,Text,Time
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,time,datetime,timedelta

class Diary(Base):
    __tablename__="dairy"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    dairy_title=Column(String(128))
    dairy_description=Column(Text)
    dairy_date=Column(Date)
    dairy_time=Column(Time)
    status=Column(Integer,default=1)
    created_by=Column(Integer,ForeignKey('users.id'))
    created_at=Column(DateTime,default=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)

     #User table realtionship
    user=relationship("User", back_populates="dairy", foreign_keys=[user_id])
    creator_data=relationship("User", back_populates="dairy_creator", foreign_keys=[created_by])
    modified_data=relationship("User", back_populates="dairy_modifier", foreign_keys=[modified_by])

    #media table realtionship
    media=relationship("Media",back_populates="dairy")

