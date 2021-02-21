class User:
    
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

Jonathan = User("Jonathan")
Natalie = User("Natalie")
Carmen = User("Carmen")

Jonathan.make_deposit(100).make_deposit(10000).make_deposit(333).make_withdrawal(4000).display_user_balance()

Natalie.make_deposit(500).make_deposit(8000).make_withdrawal(122).make_withdrawal(344).display_user_balance()

Carmen.make_deposit(700000).make_withdrawal(555).make_withdrawal(3333).make_withdrawal(888).display_user_balance()