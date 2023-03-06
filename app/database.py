import time
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'postgres'
password = 'password123'
postgresserver = 'localhost'
db = 'fastapi'
SQLALCHEMY_DATABASE_URL = f"""postgresql://{user}:{password}@{postgresserver}/{db}"""


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:

#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='fastapi',
#             user='postgres',
#             password='password123',
#             cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('db is ok!')
#         break
#     except Exception as error:
#         print('db failed')
#         print(error)
#         time.sleep(2)
