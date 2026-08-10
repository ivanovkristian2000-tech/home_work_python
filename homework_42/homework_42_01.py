""" 01 Создание базы

Напишите программу, которая:
- создаёт базу данных notes_app_<your_group>_<your_full_name>
- выбирает эту базу через USE notes_app
- выводит сообщение о результате

Пример вывода:
Database 'notes_app' created or already exists.
"""

import mysql.connector
from local_settings import dbconfig_write

db_name = "notes_app_06_03_2026_ptm_KriS"


class MySQLWriteConnector:
    def __init__(self, dbconfig, autocommit=False):
        self.dbconfig = dbconfig
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig, use_pure=True)
        self.cursor = self.connection.cursor()
        self.connection.autocommit = self.autocommit
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if not self.autocommit:
                if exc_type is None:
                    self.connection.commit()
                else:
                    self.connection.rollback()
        except mysql.connector.Error as e:
            print("Commit Error", e)

        finally:
            if self.cursor:
                self.cursor.close()

            if self.connection:
                self.connection.close()



class CreateDB(MySQLWriteConnector):
    def create_db(self):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.cursor.execute(f"USE {db_name}")
        print(f"Database '{db_name}' created or already exists.")


if __name__ == '__main__':
    with CreateDB(dbconfig_write) as db:
        db.create_db()

# Database 'notes_app_112226_abcdefg' created or already exists.
