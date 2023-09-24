"""Задание №6
📌 Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja
для динамического формирования HTML страницы.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс User с полями id, name, email и password.
📌 Создайте список users для хранения пользователей.
📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать
заголовок страницы, таблицу со списком пользователей и кнопку для добавления нового пользователя.
📌 Создайте маршрут для отображения списка пользователей (метод GET).
📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.."""
from enum import Enum

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List, Dict
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users1 = [
    {'id': 1, 'name': 'Вася', 'email': 'qqq@qqq.we', 'password': '123'},
    {'id': 2, 'name': 'Петя', 'email': 'www@qqq.we', 'password': '123'},
    {'id': 3, 'name': 'Коля', 'email': 'eeee@qqq.we', 'password': '123'},
    {'id': 4, 'name': 'Миша', 'email': 'rrrr@qqq.we', 'password': '123'},
    {'id': 5, 'name': 'Юра', 'email': 'ssss@qqq.we', 'password': '123'},
]

users = []


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str


class User(UserIn):
    id: int


for i in users1:
    users.append(User(
        id=i.get('id'),
        name=i.get('name'),
        email=i.get('email'),
        password=i.get('password'),
    )
    )


@app.get("/user", response_class=HTMLResponse)
async def get_user(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})



@app.get("/user/add", response_class=HTMLResponse)
async def show_add_user(request: Request):
    return templates.TemplateResponse("add_user.html", {"request": request, "users": users})



@app.post("/user", response_model=list[User])
async def add_user(new_user: UserIn):
    users.append(User(
        id=len(users) + 1,
        name=new_user.name,
        email=new_user.email,
        password=new_user.password
    ))
    return users


@app.put("/user", response_model=User)
async def edit_user(user_id: int, edit_user: UserIn):
    current_user = None
    for i in users:
        if i.id == user_id:
            current_user = i
    if current_user:
        current_user.name = edit_user.name
        current_user.email = edit_user.email
        current_user.password = edit_user.password
    else:
        raise HTTPException(status_code=404, detail="Task not found!")
    return current_user


@app.delete("/user", response_model=dict)
async def del_user(id_deleted_task: int):
    for i in users:
        if i.id == id_deleted_task:
            users.pop(i.id - 1)
            return {"mess": f"users {i} was deleted"}
    raise HTTPException(status_code=404, detail="Users not found!")






if __name__ == "__main__":
    uvicorn.run("sem_05_task_6:app", host="127.0.0.1", port=8000, reload=True)
