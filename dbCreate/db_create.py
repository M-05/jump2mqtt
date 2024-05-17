import pymysql, os
from dotenv import load_dotenv

load_dotenv()
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB_NAME = "mqtt"

MYSQL_URL = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}'

# Connect to MySQL server
conn = pymysql.connect(
                        host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT
)
engine = conn.cursor()

def create_database():
    # Execute SQL command to create database
    engine.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB_NAME};")

def drop_database():
    # Execute SQL command to drop database
    engine.execute(f"DROP DATABASE IF EXISTS {MYSQL_DB_NAME};")


def main():
# Check if database exists
    engine.execute("SHOW DATABASES")
    databases = engine.fetchall()
    database_exists = any(MYSQL_DB_NAME in db for db in databases)

    if not database_exists:
        print(f"{MYSQL_DB_NAME} 데이터베이스가 존재하지 않습니다.\n{MYSQL_DB_NAME} 데이터베이스를 생성하겠습니다.")
        create_database()
    else:
        print(f"{MYSQL_DB_NAME} 데이터베이스가 존재합니다.\n{MYSQL_DB_NAME} 데이터베이스를 삭제 후 다시 생성하겠습니다.")
        drop_database()
        create_database()

if __name__ == "__main__":
    main()

    # create_database()

    # drop_database()