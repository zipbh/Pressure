import uvicorn  # type: ignore

from app import create_app

from dotenv import load_dotenv


if __name__ == '__main__':
    uvicorn.run(create_app, host='127.0.0.1', port=9000, reload=False)
