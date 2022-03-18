from fastapi import APIRouter

create_report_v1 = APIRouter()


@create_report_v1.post('/')
async def root():
    return {"hello": "world"}
