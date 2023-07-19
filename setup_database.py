import mysql.connector
import asyncio
import aiomysql
from faker import Faker

from data_base_config import config

SQL_CREATE_TABLE = "CREATE TABLE IF NOT EXISTS usuario (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
SQL_INSERT = "INSERT INTO usuario (name) VALUES (%s)"


def create_table_sync():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(SQL_CREATE_TABLE)
    conn.commit()
    conn.close()


def create_table_async():
    async def create_table():
        conn = await aiomysql.connect(**config)
        async with conn.cursor() as cursor:
            await cursor.execute(SQL_CREATE_TABLE)
            await conn.commit()
        conn.close()

    asyncio.run(create_table())


def insert_data_sync(num_records=3000):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    fake = Faker()
    data = [(fake.name(),) for _ in range(num_records)]  # Gerar nomes aleatórios
    cursor.executemany(SQL_INSERT, data)
    conn.commit()
    conn.close()


def insert_data_async(num_records=3000):
    async def insert_data():
        conn = await aiomysql.connect(**config)
        async with conn.cursor() as cursor:
            fake = Faker()
            data = [(fake.name(),) for _ in range(num_records)]  # Gerar nomes aleatórios
            await cursor.executemany(SQL_INSERT, data)
            await conn.commit()
        conn.close()

    asyncio.run(insert_data())


if __name__ == "__main__":
    create_table_sync()
    insert_data_sync(num_records=3000)
    create_table_async()
    insert_data_async(num_records=3000)
