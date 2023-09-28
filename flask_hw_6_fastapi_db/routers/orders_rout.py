from typing import List

from fastapi import APIRouter, HTTPException
from db import users_tab, database
from models.users_model import User, UserIn
from sqlalchemy import select

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users_tab.insert().values(
                                        first_name=f'first_name{i}',
                                        last_name=f'last_name{i}',
                                          email=f'mail{i}@mail.ru',
                                          password=f'{i}{i}{i}{i}', )
        await database.execute(query)
    return {'message': f'{count} fake users create'}


# @router.get("/users/", response_model=List[User])
@router.get("/users/")
async def view_user():
    query = users_tab.select()
    # await database.execute(query)
    return await database.fetch_all(query)


@router.post("/users/", response_model=UserIn)
async def create_user(user: UserIn):
    query = users_tab.insert().values(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
        )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users_tab.select().where(users_tab.c.id == user_id)
    return await database.fetch_one(query)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users_tab.delete().where(users_tab.c.id == user_id)
    await database.execute(query)
    return {'message': f'User {user_id} deleted'}
