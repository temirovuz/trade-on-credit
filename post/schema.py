from pydantic import BaseModel


class CreateCustomer(BaseModel):
    name: str
    phone: str
    price: str
