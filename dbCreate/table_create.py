from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, VARCHAR, ForeignKey, Text, ForeignKeyConstraint, text
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


import pymysql, os
from dotenv import load_dotenv

load_dotenv()
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB_NAME = "mqtt"

MYSQL_URL = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}'


def create_table():
    engine = create_engine(MYSQL_URL)

    # print(f"engine : {engine}")

    metadata = MetaData()

    # user 테이블을 정의합니다.
    user_table = Table(
        'user', metadata,
        Column('no', Integer, primary_key=True, autoincrement=True),
        Column('username', VARCHAR(10), unique=True, nullable=False),
        Column('create_date', DateTime, nullable=False)
    )

    # messageQueue 테이블을 정의합니다.
    messageQueue_table = Table(
        'messageQueue', metadata,
        Column('no', Integer, primary_key=True, autoincrement=True),
        Column('username', VARCHAR(10), ForeignKey('user.username'), unique=True, nullable=False, default='test'),
        Column('message', String(255), nullable=False),
        Column('create_date', DateTime, nullable=False)
    )
    # Create the table
    metadata.create_all(engine)

def drop_table():
    engine = create_engine(MYSQL_URL)
    print(f"engine : {engine}")


    metadata = MetaData()

    with engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
        metadata.reflect(bind=engine)

        # Reflect the existing tables
        if 'messageQueue' in metadata.tables:
            messageQueue_table = Table('messageQueue', metadata, autoload_with=engine)
            messageQueue_table.drop(engine, checkfirst=True)
        
        if 'user' in metadata.tables:
            user_table = Table('user', metadata, autoload_with=engine)
            user_table.drop(engine, checkfirst=True)

        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))

def main():
    try:
        drop_table()
        print(f"테이블을 삭제 후 생성하겠습니다.")
        
    except Exception as e:
        print(f"테이블 존재하지 않습니다.\n 오류는 {e}")
    create_table()


if __name__ == "__main__":
    main()

    # create_table()

    # drop_table()