# connection from sqlite to fastapi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

URL_DATABASE = "sqlite:///./messages.db"

engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass