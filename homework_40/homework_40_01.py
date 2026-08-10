"""
Электронное письмо
Реализуйте класс Email, который представляет электронное письмо. Каждое письмо должно содержать:

sender — адрес отправителя

recipient — адрес получателя

subject — тема письма

body — текст письма

date — дата отправки

Класс должен поддерживать:

Сравнение писем по дате

Преобразование письма в строку

Получение длины текста письма

Проверку на наличие текста в письме или не состоит ли текст только из пробелов
"""
from functools import total_ordering
from datetime import datetime



@total_ordering
class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date


    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    def __str__(self):
        return (f"From: {self.sender}\n"
                f"To: {self.recipient}\n"
                f"Subject: {self.subject}\n"
                f"Body: {self.body}")

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())




email1 = Email(
    "alice@gmail.com",
    "bob@gmail.com",
    "Meeting",
    "Let's meet at 10am",
    datetime(2026, 8, 5, 10, 0)
)

email2 = Email(
    "charlie@gmail.com",
    "bob@gmail.com",
    "Report",
    "Here is the report",
    datetime(2026, 8, 6, 9, 30)
)



print(email1)
print(f"Длина текста: {len(email1)}")
print(f"Есть текст: {bool(email1)}")
print(f"email2 новее email1: {email2 > email1}")
