"""Класс для работы с деньгами
Создайте класс Money, в котором можно:

складывать и вычитать объекты через операторы + и -

выводить объект как строку в виде "$<amount>"

при сложении и вычитании возвращается новый объект

если вычитание приводит к отрицательному значению — вернуть 0
"""



class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount - other.amount < 0:
            return Money(0)
        else:
            return Money(self.amount - other.amount)

    def __str__(self):
        return f"${self.amount}"



money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

