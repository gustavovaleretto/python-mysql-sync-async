import asyncio
import time
import aiomysql

from data_base_config import config

SQL_SELECT = "SELECT * FROM usuario"


async def fetch_data_async():
    start_time = time.time()
    conn = await aiomysql.connect(**config)

    async with conn.cursor() as cursor:
        await cursor.execute(SQL_SELECT)
        result = await cursor.fetchall()
    conn.close()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução (async): {elapsed_time:.5f} segundos")
    return result


async def main():
    data = await fetch_data_async()
    # print(data)


if __name__ == "__main__":
    asyncio.run(main())
