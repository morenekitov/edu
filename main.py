from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from loguru import logger
from typing import List

app = FastAPI()


class UsersGet(BaseModel):
    id: int
    gender: int
    age: int
    country: str
    city: str
    exp_group: str
    os: str
    source: str

    class Config:
        orm_mode = True


@app.get("/")
def say_hello():
    return "hello"


@app.get("/sum/")
def sum_two(a: int, b: int) -> int:
    return a + b


@app.get("/number/{number}")
def print_num(number: int):
    return number * 2


@app.post("/user")
def print(name: str):
    return {"message": f'hello,{name}'}


@app.get('/user/all',response_model=UsersGet)
def all_bookings():
    conn = psycopg2.connect(
        database="startml",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432,
       cursor_factory=RealDictCursor
    )
    cursor = conn.cursor()
    cursor.execute('''
    
    SELECT *
    FROM "user"
    LIMIT 10;
    
    ''')
    result = cursor.fetchall()
    logger.info(result)
