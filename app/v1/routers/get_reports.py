from fastapi import APIRouter

get_reports = APIRouter()


@get_reports.get('/')
async def root():
    return {"hello": "world"}
