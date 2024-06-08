from fastapi import Depends, HTTPException
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import Session

from core.database import Base, get_db
from core.ults import verify_password


class Shop(Base):
    id = Column(Integer, primary_key=True)
    shop_name = Column(String(120))
    phone_number = Column(String(13), primary_key=True)
    password = Column(String(15))


# ------------------------------>      Create shop     <------------------------------------- #
def create_shop(name, number, password, db: Session = Depends(get_db)):
    query = db.query(Shop).filter(Shop.phone_number == number).first()
    if not query:
        shop = Shop(shop_name=name, phone_number=number, password=password)
        db.add(shop)
        db.commit()
        db.refresh(shop)
    else:
        raise HTTPException(status_code=409, detail='Bu telefon raqamli dokon mavjud')
    return shop


def get_shop(number, password, db: Session = Depends(get_db)):
    shop = db.query(Shop).filter(Shop.phone_number == number).first()
    if not shop:
        raise HTTPException(status_code=409, detail='Bu telefon raqamli dokon mavjud emas')
    if not verify_password(password, shop.password):
        raise HTTPException(status_code=409, detail='Parol Xato')
    return shop

# ------------------------------------------------------------------------------------------------- #
