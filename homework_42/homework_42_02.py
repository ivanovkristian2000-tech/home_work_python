""" 02 Добавление заметок

Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя в формате dict (а не tuple!)

Пример вывода:

All notes:
{'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}

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
        self.cursor = self.connection.cursor(dictionary=True)
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

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
            id INT PRIMARY key AUTO_INCREMENT,
            title VARCHAR(50),
            content VARCHAR(200)
	        )
            """)

        user_title = input("Enter title: ")
        user_content = input("Enter content: ")

        self.cursor.execute(
            """
            INSERT INTO notes (title, content)
            VALUES
                (%s, %s)
            """, (user_title, user_content))

    def get_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        print("All notes:")
        notes = self.cursor.fetchall()
        print(notes)



with CreateDB(dbconfig_write) as db:
    # db.create_table()
    db.get_notes()








# Database 'notes_app_112226_abcdefg' created or already exists.
#
# All notes:
# {'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}
#
# Process finished with exit code 0
