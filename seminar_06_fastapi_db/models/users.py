from dataclasses import Field

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    id: int
    username: str = Field(title="Username", max_length=50)
    email: EmailStr = Field(title="email", max_length=100)
    password: int = Field(..., title='password', le=3)


