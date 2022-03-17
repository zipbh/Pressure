from fastapi import APIRouter

login = APIRouter()


@login.post('/')
async def root():
    return {"hello": "world"}