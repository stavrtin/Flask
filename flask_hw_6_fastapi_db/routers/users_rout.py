from fastapi import APIRouter
from db import users_tab, database
from models.users_model import User, UserIn


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


@router.get("/view_all_user/")
async def view_alluser():
    query = users_tab.select()
    await database.execute(query)
    return await database.fetch_all(query)

@router.get("/view_user/{user_id}")
async def view_user(user_id: int):
    query = users_tab.select().where(users_tab.c.id == id)
    await database.execute(query)
    return await database.fetch_one(query)


@router.post("/create_user")
async def create_user(user: UserIn):
    query = users_tab.insert().values(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password)
    await database.execute(query)
    return {'message': f'{user.first_name} created'}


@router.put("/edit_user/{user_id}")
async def edit_user(user_id: int, new_data_user: UserIn):
    query = users_tab.update().where(users_tab.c.id == user_id).values(
                    first_name=new_data_user.first_name,
                    last_name=new_data_user.last_name,
                    email=new_data_user.email,
                    password=new_data_user.password)
    await database.execute(query)
    return f'Юзер с id={user_id} обновился до {new_data_user.first_name} '


@router.delete("/del_user/{user_id}")
async def del_user(user_id: int):
    query = users_tab.delete().where(users_tab.c.id == user_id)
    await database.execute(query)
    return f'Юзер с id={user_id} удален '

