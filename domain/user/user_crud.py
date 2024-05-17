import datetime
from sqlalchemy.orm import Session

from domain.user import user_schema
import models

def create_user(db: Session, user_create: user_schema.UserCreate):
    db_user = models.User(username=user_create.username, 
                            create_date=datetime.datetime.now())
    db.add(db_user)
    db.commit()


def get_existing_user(db: Session, user_create: user_schema.UserCreate):
    user =  db.query(models.User).filter(
        (models.User.username == user_create.username)
    ).first()

    print(f"user : {user}")
    if user:
        return user_schema.User.from_orm(user)
    return None

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()