from pydantic import Field
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Prod(BaseModel):
    id: int
    name: str
    description: str
    price: int
