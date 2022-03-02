import os
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

with open('1gbfile', "wb") as file:
    file.seek(1073741824)
    file.write(b"\0")
    print('файл 1gbfile успешно создан')
myfl = os.path.abspath('1gbfile')
try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute('create database post_pyt_db')
    print("БазаДанных post_pyt_db успешно создана")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="post_pyt_db")
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute('''CREATE TABLE big_file (file bytea); ''')
        connection.commit()
        print("Таблица big_file успешно создана")

    with connection.cursor() as cursor:
        cursor.execute(
            '''ALTER TABLE big_file ALTER COLUMN file SET STORAGE plain; ''')
        connection.commit()
        print("STORAGE колонки file успешно определен как plain ")

    with connection.cursor() as cursor:
        content = f"INSERT INTO big_file (file) VALUES ('{myfl}'); "
        cursor.execute(content)
        connection.commit()
        print("Файл успешно добавлен в таблицу")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        connection.close()
        print("Соединение с PostgreSQL закрыто")
