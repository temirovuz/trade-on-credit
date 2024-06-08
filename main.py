from fastapi import FastAPI

from auth.router import router as auth_router
from post.router import router as post_router

api = FastAPI()

api.include_router(auth_router)
api.include_router(post_router)
