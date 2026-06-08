# connection from sqlite to fastapi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

URL_DATABASE = "sqlite:///./sql_app.db"

engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = DeclarativeBase()