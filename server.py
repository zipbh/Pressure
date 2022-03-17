import uvicorn  # type: ignore

from app import create_app

from os import getenv

from dotenv import load_dotenv


load_dotenv()

port = int(getenv('PORT'))
host = getenv('HOST')
reload = bool(getenv('RELOAD'))

if __name__ == '__main__':
    uvicorn.run(create_app, host=host, port=port, reload=False)
