class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.09, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        print(self.account.balance)

    def yield_interest(self):
        self.account.yield_interest()
        return self


class BankAccount:
    def __init__(self, int_rate=0.09, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self


BankAccount_1 = BankAccount(.09, 5500)
BankAccount_2 = BankAccount(.09, 54320)

BankAccount_1.deposit(330).deposit(3000).deposit(394949).withdraw(399).yield_interest().display_account_info()
BankAccount_2.deposit(3848390).deposit(39494).withdraw(384).withdraw(384).withdraw(394).withdraw(55).yield_interest().display_account_info()
