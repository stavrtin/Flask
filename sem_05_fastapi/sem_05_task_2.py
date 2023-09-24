"""Задание №2
📌 Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов по заданному жанру.
📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
📌 Создайте класс Movie с полями id, title, description и genre.
📌 Создайте список movies для хранения фильмов.
📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
📌 Реализуйте валидацию данных запроса и ответа."""
from enum import Enum

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

move_list = [
    {'id': 1, 'title': 'МиБ1', 'description': 'мммм ыва', 'genre': 'фант'},
    {'id': 2, 'title': 'Мимино', 'description': 'мими', 'genre': 'драма'},
    {'id': 3, 'title': 'Осень', 'description': 'ооооооо', 'genre': 'боевик'},
    {'id': 4, 'title': 'Клад', 'description': 'кло', 'genre': 'ужасы'},
    {'id': 5, 'title': 'Интерст', 'description': 'интинтинт', 'genre': 'фант'},
]

# class Genre(Enum):
#     fantast = 'фант'
#     comedy = 'комед'
#     drame = 'драма'
#     boevik = 'боевик'
#     triller = 'триллер'


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


class MovieNew(BaseModel):
    title: str
    description: str
    genre: str


@app.get("/film", response_model=list[Movie])
async def films():
    return move_list


@app.get("/film/{genre}", response_model=list[Movie])
async def get_films(find_genre: str):
    move_genre_list = []
    for move in move_list:
        if move.get('genre') == find_genre:
            move_genre_list.append(move)
    return move_genre_list

@app.post("/film", response_model=list[Movie])
async def add_films(new_film: MovieNew):
    # print(Genre.__members__.values())
    move_list.append(
        Movie(
        id=len(move_list) + 1,
        title=new_film.title,
        description=new_film.description,
        genre=new_film.genre
    ))
    return move_list


if __name__ == "__main__":
    uvicorn.run("sem_05_task_2:app", host="127.0.0.1", port=8000, reload=True)
