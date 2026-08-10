""" 02 Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны.
Пользователь должен ввести название страны.
Далее выведите все города этой страны и их численность населения.

Пример вывода 1:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560

Пример вывода 2:
Введите страну: Unknown
❌ Страна 'Unknown' не найдена
...

"""


import mysql.connector
from local_settings import dbconfig


class UnknownCountryError(Exception):
    """Chek for valid country name"""



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
            print("Commit Error", e)
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

    def search_country(self):

        user_country = input("Enter the name of country: ")

        try:
            self.cursor.execute("""
                SELECT
                    c.Name, city.Name, city.Population
                FROM
                    country AS c
                        JOIN
                    city AS city ON c.Code = city.CountryCode
                WHERE
                    c.Name = %s """, (user_country, ))
            city_country = self.cursor.fetchall()

            if not city_country:
                raise UnknownCountryError("Invalid country")

            for city in city_country:
                print(f"{city[1]} - {city[2]}")

        except UnknownCountryError as e:
            print(f"Country {user_country} not found:", e)



with World(dbconfig) as world_db:
    world_db.search_country()






























#
# import mysql.connector
from local_settings import dbconfig
#

# class DatabaseError(Exception):
#     """Общее исключение слоя доступа к данным"""
#
#
# class MySQLConnection:
#     pass
#
#
# class WorldDB(MySQLConnection):
#     def fetch_countries(self):
#         """Получить список всех стран"""
#
#
#     def fetch_cities_by_country(self, country_name):
#         """Получить все города выбранной страны с их населением"""
#
#
# if __name__ == "__main__":
#     try:
#         with WorldDB(dbconfig) as db:
#             # Список всех стран
#             countries = db.fetch_countries()
#             print("Список стран:")
#             for i, name in enumerate(countries, start=1):
#                 print(f"{i}. {name}")
#
#             # Ввод страны пользователем
#             country_input = input("\nВведите страну: ").strip()
#
#             # Получаем города выбранной страны
#             cities = db.fetch_cities_by_country(country_input)
#             if not cities:
#                 print(f"Для страны '{country_input}' нет данных о городах.")
#             else:
#                 for city in cities:
#                     # Формируем строку с названием города и населением
#                     city_name = city['Name']
#                     district = city['District']
#                     population = city['Population']
#                     # Если нужно — можно добавить район/альтернативное имя
#                     print(f"{city_name} — {population}")
#
#     except DatabaseError as e:
#         print(f"❌ {e}")
