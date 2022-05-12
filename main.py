from fastapi import FastAPI
import psycopg2

app = FastAPI()


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


@app.get('/booking/all')
def all_bookings():
    conn = psycopg2.connect(
        database="startml",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432
    )
    cursor = conn.cursor()
    cursor.execute('''
    
    SELECT *
    FROM "user"
    
    ''')
    return cursor.fetchall()
