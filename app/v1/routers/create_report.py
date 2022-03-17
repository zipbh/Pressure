from fastapi import APIRouter

create_report = APIRouter()


@create_report.post('/')
async def root():
    return {"hello": "world"}
