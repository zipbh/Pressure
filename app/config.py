from os import getenv

from dotenv import load_dotenv


class Settings:
    load_dotenv()

    # General
    PROJECT_NAME = 'Pressure Api'
    PROJECT_VERSION = '1.0.0'
    PROJECT_AUTHOR = 'André Moreira'

    # Users and login
    USERNAME_MAX_SIZE = int(getenv('USERNAME_MAX_SIZE'))
    PASSWORD_MIN_SIZE = int(getenv('PASSWORD_MIN_SIZE'))

    # Uvicorn
    CORS_ORIGINS = getenv('CORS_ORIGINS')
    HOST = getenv('HOST')
    PORT = int(getenv('PORT'))
    RELOAD = bool(getenv('RELOAD'))

    # Database
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    REDIS_URL = getenv('REDIS_URL')


settings = Settings()
