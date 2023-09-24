# pip install fastapi
# pip install "uvicorn[standard]"
# uvicorn lection_05.main_02:app
# --------------- uvicorn lection_05.main_01:app  -------------ЗАПУСК СЕРВЕРА -----------

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root_1():
    return "<h2>DSF DFsdfsd"


@app.get("/mess", response_class=JSONResponse)
async def root_2():
    message = {"message": "sdfsfs"}
    return JSONResponse(content=message, status_code=200)
