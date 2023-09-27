from pydantic import Field, BaseModel, EmailStr

class OrderIn(BaseModel):
    user_id: int
    prod_id: int
    date_order: str


class Order(OrderIn):
    status: str
