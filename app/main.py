from fastapi import FastAPI
from uvicorn import run
import time


app = FastAPI(
    title="test",
    description="",
)

import os
from dotenv import load_dotenv
load_dotenv()
CONTAINER = os.getenv('CONTAINER')

@app.get("/")
def test():
    print(f'Начало работы модуля {CONTAINER}')
    time.sleep(30)
    print(f'Конец работы модуля {CONTAINER}')
    return {"Работа": "Закончена"}

def main() -> None:
    run(
        app,
        host='0.0.0.0',
        port=8080
    )
