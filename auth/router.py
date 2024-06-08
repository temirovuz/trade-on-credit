from fastapi import APIRouter

router = APIRouter(prefix='/shop', tags=['shop'])


@router.post()
def create_shop():
    pass
