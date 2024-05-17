from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, create_engine, MetaData
from sqlalchemy.orm import relationship

from database import Base
from dbCreate import db_create

engine = create_engine(url=db_create.MYSQL_URL)
metadata = MetaData()

Base.metadata.create_all(bind=engine)

class MessageQueue(Base):
    __tablename__ = "messageQueue"

    no = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey("user.username"), unique=True, nullable=False, default="test")
    message = Column(Text, nullable=False)   # 가변 길이 문자열
    create_date = Column(DateTime, nullable=False)


class User(Base):
    __tablename__ = "user"

    no = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    create_date = Column(DateTime, nullable=False)

metadata.create_all(engine)