from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.models import create_shop
from auth.schema import CreateShop
from core.database import get_db

router = APIRouter(prefix='/shop', tags=['shop'])


@router.post('signup', status_code=201)
def create_shop_(user_data: CreateShop, db: Session = Depends(get_db)):
    shop = create_shop(user_data.name, user_data.phone, user_data.password, db)
    return shop

@router.post('/login', status_code=200, response_model=Token)
def login():
    pass