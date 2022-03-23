import uvicorn  # type: ignore

from app import create_app

from app.config import settings


port = settings.PORT
host = settings.HOST
reload = settings.RELOAD

if __name__ == '__main__':
    uvicorn.run(create_app, host=host, port=port, reload=False)
