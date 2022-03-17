from fastapi import APIRouter

signup = APIRouter()


@signup.post('/')
async def root():
    pass
