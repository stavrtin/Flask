from typing import List

from fastapi import APIRouter
from db import users_tab, database
from models.users_model import User, UserIn
from sqlalchemy import select

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users_tab.insert().values(username=f'user{i}',
                                          email=f'mail{i}@mail.ru',
                                          password=f'mail{i}@mail.ru', )
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.get("/users/", response_model=list[User])
async def view_user():
    query = users_tab.select()
    return await database.fetch_all(query)

