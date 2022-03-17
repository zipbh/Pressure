from os import getenv

from dotenv import load_dotenv

from fastapi import FastAPI

from app.db import setup_database  # type: ignore

from app.routers.create_report import create_report  # type: ignore

from app.routers.get_reports import get_reports  # type: ignore

from app.routers.login import login  # type: ignore

from app.routers.signup import signup  # type: ignore


def create_app():
    app = FastAPI()
    app.include_router(create_report, prefix='/create_report')
    app.include_router(get_reports, prefix='/get_reports')
    app.include_router(login, prefix='/login')
    app.include_router(signup, prefix='/signup')

    @app.get('/')
    async def root():
        return {"hello": "world"}

    return app
