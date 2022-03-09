from pydbantic import Database  # type: ignore


async def setup_database(database_uri, tables):
    return await Database.create(
        database_uri,
        tables=tables
    )
