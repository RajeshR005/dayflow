from sqlalchemy import Column,String,Integer,Date,DateTime,ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import date,datetime,time

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(Date)
    email = Column(String(100), index=True, nullable=False)
    password = Column(String(300), nullable=False)
    phone_number = Column(String(50), nullable=True)
    status=Column(Integer,default=1)
    role=Column(String(50),default="user")
    created_at = Column(DateTime,default=datetime.now)
    created_by=Column(Integer,ForeignKey('users.id'))
    modified_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    modified_by=Column(Integer,ForeignKey('users.id'))



    creator = relationship("User", remote_side=[id], foreign_keys=[created_by], backref="created_users")
    modifier = relationship("User", remote_side=[id], foreign_keys=[modified_by], backref="modified_users")

   #expense table realtionship
    expense=relationship("ExpenseTracker", back_populates="user", foreign_keys="ExpenseTracker.user_id")
    exp_creator=relationship("ExpenseTracker", back_populates="creator_data", foreign_keys="ExpenseTracker.created_by")
    exp_modifier=relationship("ExpenseTracker", back_populates="modified_data", foreign_keys="ExpenseTracker.modified_by")
    
   #Media data realtionship
    media=relationship("Media", back_populates="user", foreign_keys="Media.user_id")
    media_creator=relationship("Media", back_populates="creator_data", foreign_keys="Media.created_by")
    media_modifier=relationship("Media", back_populates="modified_data", foreign_keys="Media.modified_by")

    #Dairy table realtionship
    dairy=relationship("Dairy", back_populates="user", foreign_keys="Dairy.user_id")
    dairy_creator=relationship("Dairy", back_populates="creator_data", foreign_keys="Dairy.created_by")
    dairy_modifier=relationship("Dairy", back_populates="modified_data", foreign_keys="Dairy.modified_by")

    #Todolist table realtionship
    todolist=relationship("Todolist", back_populates="user", foreign_keys="Todolist.user_id")
    todolist_creator=relationship("Todolist", back_populates="creator_data", foreign_keys="Todolist.created_by")
    todolist_modifier=relationship("Todolist", back_populates="modified_data", foreign_keys="Todolist.modified_by")
    




