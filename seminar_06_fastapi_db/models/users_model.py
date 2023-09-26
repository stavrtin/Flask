from pydantic import Field
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str = Field(title="Username", max_length=50)
    email: EmailStr = Field(title="email", max_length=100)
    password: int = Field(..., title="password", min_length=3)

class User(UserIn):
    id: int
