class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, balance: int):
        if balance < 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += balance

    def withdraw(self, balance: int):
        if balance < 0:
            raise ValueError("Сумма должна быть положительной")
        if balance > self.balance:
            raise ValueError("Сумма не может быть больше, чем есть на счете")
        self.balance -= balance
