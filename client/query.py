import asyncpg # asynchronous driver for postgres
from decouple import config # store env variables in .env or ini

# create new db structure for client

async def execute(client):

    try:
        conn = await asyncpg.connect(user=config('USER'), password=config('PASSWORD'),
                                        database=config('DATABASE'), host=config('HOST'))
        print('current database')
            
        database = client.client_name
        await conn.execute(f'CREATE DATABASE "{database}"')

        await conn.close()

        conn = await asyncpg.connect(user=config('USER'), password=config('PASSWORD'),
                                        database=database, host=config('HOST'))
        print('new database created')

        await conn.close()
            
        print("done")
    
    except Exception as e:
        print(e)









    # values = await conn.execute('''
    #     CREATE TABLE sample(
    #         id serial PRIMARY KEY,
    #         name text,
    #         dob date
    #     )
    # ''')