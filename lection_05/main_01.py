# pip install fastapi
# pip install "uvicorn[standard]"
# --------------- uvicorn lection_05.main_01:app  -------------ЗАПУСК СЕРВЕРА -----------

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_1():
    return {"message": "Привет мир!"}
