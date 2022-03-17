from fastapi import FastAPI

from app.v1.db import setup_database  # type: ignore

from app.v1.routers.create_report import create_report  # type: ignore

from app.v1.routers.get_reports import get_reports  # type: ignore

from app.v1.routers.login import login  # type: ignore

from app.v1.routers.signup import signup  # type: ignore

from app.v1.routers.route_homepage import general_pages_router


def include_router(app):
    app.include_router(create_report, prefix='/create_report')
    app.include_router(get_reports, prefix='/get_reports')
    app.include_router(login, prefix='/login')
    app.include_router(signup, prefix='/signup')
    app.include_router(general_pages_router)


def create_app():
    app = FastAPI()
    include_router(app)

    return app