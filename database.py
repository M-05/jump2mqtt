from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dbCreate import db_create

engine = create_engine(url=db_create.MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# MySQL에 맞는 Metadata 생성

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
