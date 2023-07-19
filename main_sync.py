import time

import mysql.connector

from data_base_config import config

SQL_SELECT = "SELECT * FROM usuario"


def fetch_data_sync():
    start_time = time.time()
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(SQL_SELECT)
    result = cursor.fetchall()
    conn.close()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução (async): {elapsed_time:.5f} segundos")
    return result


if __name__ == "__main__":
    data = fetch_data_sync()
    # print(data)
