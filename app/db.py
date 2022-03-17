from pydbantic import Database, DataBaseModel  # type: ignore

from app.model import (Address, Contacts, Login, Organization,
                   Partner, Persona, Reports)  # type: ignore

from os import getenv

from dotenv import load_dotenv

import asyncio


async def setup_database():
    load_dotenv()
    database_uri = getenv('SQLALCHEMY_DATABASE_URI')
    db = await Database.create(
        database_uri,
        tables=[Address, Contacts, Organization, Login, Persona, Partner, Reports]
    )


if __name__ == '__main__':
    asyncio.run(setup_database())
