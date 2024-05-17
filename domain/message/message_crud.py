import datetime
from sqlalchemy import and_
from sqlalchemy.orm import Session

from domain.message import message_schema
import models

def create_message(db: Session, 
                    message_create: message_schema.messageCreate,
                    user: models.User):
    db_message = models.MessageQueue(username=user,
                                    message=message_create.message,
                                    create_date=datetime.datetime.now())
    print(f"db_message : {db_message}")

    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_message(db: Session, user: models.User):
    message_user = db.query(models.MessageQueue).filter(models.MessageQueue.username == user.username).first()
    return message_user

def get_message_list(db: Session):
    message_list = db.query(models.MessageQueue).order_by(models.MessageQueue.create_date.desc()).all()
    return message_list