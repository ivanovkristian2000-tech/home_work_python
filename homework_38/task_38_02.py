"""
История операций

Доработайте класс BankAccount.

Каждая операция пополнения и снятия должна сохраняться в историю.

История должна быть доступна через property history только для чтения.

История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).
"""



class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__history = []
        if balance < 0:
            raise ValueError("Bank account must be positive.")
        else:
            self.__balance = balance

    def account_top_up(self, top_up):
        if top_up > 0:
            self.__balance += top_up
            self.__history.append(f"Deposit: {top_up}")
        else:
            raise ValueError("Amount must be positive.")

    def withdrawal_of_funds(self, withdraw):
        if withdraw <= 0:
            raise ValueError("Amount must be positive.")

        if self.__balance < withdraw:
            raise ValueError("Not enough funds.")
        else:
            self.__balance = self.__balance - withdraw
            self.__history.append(f"Withdraw: {withdraw}")

    def current_balance(self):
        return f"Current balance: {self.__balance}"

    @property
    def history(self):
        return self.__history



current_balance = 0
b = BankAccount("Kris", current_balance)


print(b.current_balance())
b.account_top_up(100)
print(b.current_balance())
b.withdrawal_of_funds(50)
print(b.current_balance())
print(b.history)