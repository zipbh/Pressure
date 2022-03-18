from fastapi import APIRouter

get_reports_v1 = APIRouter()


@get_reports_v1.get('/')
async def root():
    return {"hello": "world"}
