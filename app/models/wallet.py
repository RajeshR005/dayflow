from sqlalchemy import Column,Numeric,ForeignKey,Integer,DateTime
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Wallet(Base):
    __tablename__="wallet"

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    balance=Column(Numeric(12,2))
    updated_by=Column(Integer,ForeignKey('users.id'))
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)


    #User table realtionship
    users=relationship("User", back_populates="wallets", foreign_keys=[user_id])
    updated_data=relationship("User", back_populates="wallet_updated", foreign_keys=[updated_by])
    

