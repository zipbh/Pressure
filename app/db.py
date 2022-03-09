from pydbantic import Database


async def setup_database(database_uri, tables):
    return Database.create(
        database_uri,
        tables=tables
    )
