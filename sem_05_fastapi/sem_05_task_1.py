"""Задание №1
📌 Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять, удалять и получать список задач.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс Task с полями id, title, description и status.
📌 Создайте список tasks для хранения задач.
📌 Создайте маршрут для получения списка задач (метод GET).
📌 Создайте маршрут для создания новой задачи (метод POST).
📌 Создайте маршрут для обновления задачи (метод PUT).
📌 Создайте маршрут для удаления задачи (метод DELETE).
📌 Реализуйте валидацию данных запроса и ответа."""
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

task = []


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: str


# @app.get("/")
# async def root():
#     return {"message": "Hello World123"}
#


@app.get("/tasks", response_model=list[Task])
async def tasks():
    return task


@app.post("/tasks", response_model=list[Task])
async def create_task(new_task: TaskIn):
    task.append(
        Task(
            id=len(task) + 1,
            title=new_task.title,
            description=new_task.description,
            status=new_task.status,
        )
    )
    return task


@app.put("/tasks", response_model=Task)
async def edit_task(task_id: int, edit_task: TaskIn):
    current_task = None
    for i in task:
        if i.id == task_id:
            # current_task = i[task_id - 1]
            current_task = i
    if current_task:
        current_task.title = edit_task.title
        current_task.description = edit_task.description
        current_task.status = edit_task.status
    else:
        raise HTTPException(status_code=404, detail="Task not found!")
    return current_task


@app.delete("/tasks", response_model=dict)
async def del_task(id_deleted_task: int):
    for i in task:
        if i.id == id_deleted_task - 1:
            task.pop(i.id)
            return {"mess": f"task {i} was deleted"}
    raise HTTPException(status_code=404, detail="Task not found!")


if __name__ == "__main__":
    uvicorn.run("sem_05_task_1:app", host="127.0.0.1", port=8000, reload=True)
