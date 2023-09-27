from pydantic import Field, BaseModel, EmailStr


class UserIn(BaseModel):
    first_name: str = Field(title="first_name", max_length=50)
    last_name: str = Field(title="last_name", max_length=50)
    email: EmailStr = Field(title="email", max_length=100)
    password: str = Field(..., title="password", min_length=3)

class User(UserIn):
    id: int
