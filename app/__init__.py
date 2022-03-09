from os import getenv

from db import setup_database  # type: ignore

from . import models  # type: ignore

from dotenv import load_dotenv


def main():
    load_dotenv()

    sqlalchemy_database_uri = getenv('SQLALCHEMY_DATABASE_URI')
