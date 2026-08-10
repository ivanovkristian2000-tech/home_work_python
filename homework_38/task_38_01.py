"""
Банковский счёт
Создайте класс BankAccount, описывающий банковский счёт.
Объект должен хранить имя владельца и текущий баланс.

Реализуйте методы:

пополнение счёта

снятие средств

отображение баланса

При попытке снять больше, чем есть на счёте, операция не должна выполняться.
Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
"""


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            raise ValueError("Bank account must be positive.")
        else:
            self.__balance = balance

    def account_top_up(self, top_up):
        if top_up > 0:
            self.__balance += top_up
        else:
            raise ValueError("Amount must be positive.")

    def withdrawal_of_funds(self, withdraw):
        if withdraw <= 0:
            raise ValueError("Amount must be positive.")

        if self.__balance < withdraw:
            raise ValueError("Not enough funds.")
        else:
            self.__balance = self.__balance - withdraw

    def current_balance(self):
        return f"Current balance: {self.__balance}"




current_balance = 0
b = BankAccount("Kris", current_balance)


print(b.current_balance())
b.account_top_up(100)
print(b.current_balance())
b.withdrawal_of_funds(50)
print(b.current_balance())