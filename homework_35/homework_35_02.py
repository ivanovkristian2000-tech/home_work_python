""" 02. Проверка данных пользователя

Доработайте класс User.
- Добавьте валидации полей при создании.
- Имя должно быть непустой строкой.
- Пароль должен быть строкой длиной не менее 5 символов.
- Если данные некорректны — выбрасывайте ValueError.
- Добавьте строковое представление объекта.
- Проверьте работу класса с разными значениями.
"""

class User:
    total_users = 0

    def __init__(self, username, password):
        if not self.is_username_value(username):
            raise ValueError ("Неправильно введён логин")
        self.username = username
        if not self.is_password_value(password):
            raise ValueError ("Неправильно введён пароль")
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

    @staticmethod
    def is_username_value(username):
        return isinstance(username, str) and len(username) > 0

    @staticmethod
    def is_password_value(password):
        return isinstance(password, str) and len(password) >= 5

    def __str__(self):
        return f"Имя пользователя: {self.username}"



try:
    user1 = User("alice", "pass123")
    print(user1)  # User(username='alice')
except ValueError as e:
    print("Error:", e)

try:
    user2 = User("", "12345")  # Некорректное имя
except ValueError as e:
    print("Error:", e)

try:
    user3 = User("bob", "123")  # Слишком короткий пароль
except ValueError as e:
    print("Error:", e)

print(f"Total users: {User.get_total()}")
# Должно быть 1, только валидные пользователи считаются
