import time
from typing import List, Optional
from fastapi import Body, Depends, FastAPI, HTTPException, Response, status
import psycopg2
from sqlalchemy.orm import Session

from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# while True:

#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', password='password123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('db is ok!')
#         break
#     except Exception as error:
#         print('db failed')
#         print(error)
#         time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
async def root():
    return {"message": "Anna, I love you!"}
