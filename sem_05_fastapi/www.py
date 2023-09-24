import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List, Dict
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

users1  = [
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
    email= i.get('email'),
    password=i.get('password'),
    )
                 )
print(users)