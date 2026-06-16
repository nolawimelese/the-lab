from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine

import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins)

# add class for MessageBase

class MessageBase(BaseModel):
    string: str


class MessageModel(MessageBase):
    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post("/message/", response_model=MessageModel)
async def create_message(message: MessageBase, db: db_dependency):
    db_transaction = models.Message(**message.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@app.get("/message/", response_model=list[MessageModel])
async def read_messages(db: db_dependency, skip: int = 0, limit: int = 100):
    messages = db.query(models.Message).offset(skip).limit(limit).all()
    return messages