from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy import func, text

import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

# add class for MessageBase

class MessageBase(BaseModel):
    message: str


class MessageModel(MessageBase):
    id: int
    class Config:
        orm_mode = True

class StatsModel(BaseModel):
    avg_length: float

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
    db_transaction = models.Message(**message.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@app.get("/message/", response_model=list[MessageModel])
async def read_messages(db: db_dependency, skip: int = 0, limit: int = 100):
    messages = db.query(models.Message).offset(skip).limit(limit).all()
    return messages

@app.get("/message/average_length", response_model=StatsModel)
async def get_average_length(db: db_dependency):
    avg_length = db.execute(text("SELECT AVG(LENGTH(message)) FROM messages")).scalar()
    # avg_length = db.query(func.avg(func.length(models.Message.message))).scalar()
    return StatsModel(avg_length=round(avg_length, 2) if avg_length is not None else 0.0)