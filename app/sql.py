import pymysql
import config

from typing import List, Dict


def connection():
    try:
        connection = pymysql.connect(
            host=config.host,
            port=3306,
            user=config.user,
            password=config.password,
            database=config.name_database,
            cursorclass=pymysql.cursors.DictCursor
        )
        print(f'Успешно подключен к БД: {config.name_database}')
    except Exception as err:
        print(f'Ошибка: {err}')
    return connection


def select(sql: str) -> List[Dict]:
    connect = connection()
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
    finally:
        connect.close()
    return rows


def insert(sql: str) -> None:
    connect = connection()
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql)
            connect.commit()
    finally:
        connect.close()


update = insert
