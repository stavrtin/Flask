from pydantic import Field
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    email: str = Field(max_length=100)
    password: str = Field(min_length=3)

class User(UserIn):
    id: int
