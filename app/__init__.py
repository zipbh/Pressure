from fastapi import FastAPI

from app.v1.db import setup_database  # type: ignore

from app.v1.routers.create_report_v1 import create_report_v1  # type: ignore

from app.v1.routers.get_reports_v1 import get_reports_v1  # type: ignore

from app.v1.routers.login import login  # type: ignore

from app.v1.routers.signup import signup  # type: ignore


def include_router(app):
    app.include_router(create_report_v1, prefix='/v1/create_report')
    app.include_router(get_reports_v1, prefix='/v1/get_reports')
    app.include_router(login, prefix='/login')
    app.include_router(signup, prefix='/signup')


def create_app():
    app = FastAPI()
    include_router(app)

    return app
