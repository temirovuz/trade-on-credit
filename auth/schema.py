from pydantic import BaseModel


class CreateShop(BaseModel):
    name: str
    phone: str
    password: str


class GetShop(BaseModel):
    phone: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
