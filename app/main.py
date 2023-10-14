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
    import time
    start_time = time.time()
    print('start')
    import sys
    sys.set_int_max_str_digits(0)

    a = 9999999999999 ** 99999
    print(str(a)[1:2])
    print("--- %s seconds ---" % (time.time() - start_time))
    print('end')
    print(f'Конец работы модуля {CONTAINER}')
    return {"Работа": "Закончена"}



def main() -> None:
    run(
        app,
        host='0.0.0.0',
        port=8080
    )
