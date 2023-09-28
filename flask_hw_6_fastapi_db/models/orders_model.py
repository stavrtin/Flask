from pydantic import Field
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr



class Order(BaseModel):
    user_id: int
    prod_id: str
    order_date: str
    status: str
