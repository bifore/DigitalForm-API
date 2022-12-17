# create new db structure for client
async def execute(conn):

    values = await conn.execute('''
        CREATE TABLE sample(
            id serial PRIMARY KEY,
            name text,
            dob date
        )
    ''')