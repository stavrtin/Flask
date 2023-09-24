from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# class Item(BaseModel):
#     name: str = Field(max_length=10)
#     price: float
#     is_offer: bool = None


class Item(BaseModel):
    name: str = Field(title="Name", max_length=50)
    price: float = Field(title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10)


# class User(BaseModel):
#     username: str
#     full_name: str = None
#     age: int = Field(default=0)
class User(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100)
    age: int = Field(default=0, title='Age', le=150)


class Order(BaseModel):
    items: List[Item]
    user: User


@app.post('/items')
async def create_item(item: Item):
    return {"item": item}


if __name__ == "__main__":
    uvicorn.run(
        "main_01:app",
        host="127.0.0.1",
        port=8000,
        reload=True)
