""" 01 Список всех стран

Используя базу данных world, вывести названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe

Попробуйте решить задачи используя стиль Data Access Object (DAO).
"""

import mysql.connector
from local_settings import dbconfig



class MySQLConnector:
    def __init__(self, db_config, autocommit=False):
        self.db_config = db_config
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.db_config, use_pure=True)
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
            print("Ошибка:", e)

        finally:
            if self.cursor:
                self.cursor.close()

            if self.connection:
                self.connection.close()


class World(MySQLConnector):
    def fetch_country(self):
        self.cursor.execute("SELECT Name FROM country")
        countries = self.cursor.fetchall()

        for i, country in enumerate(countries, start=1):
            print(f"{i}. {country[0]}")



if __name__ == "__main__":
    with World(dbconfig) as world_db:
        world_db.fetch_country()
