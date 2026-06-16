# table for sqlite table

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    string = Column(String)