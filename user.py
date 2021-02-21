class User:
    
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

Jonathan = User("Jonathan")
Natalie = User("Natalie")
Carmen = User("Carmen")

Jonathan.make_deposit(100)
Jonathan.make_deposit(10000)
Jonathan.make_deposit(333)
Jonathan.make_withdrawal(4000)
Jonathan.display_user_balance()

Natalie.make_deposit(500)
Natalie.make_deposit(8000)
Natalie.make_withdrawal(122)
Natalie.make_withdrawal(344)
Natalie.display_user_balance()

Carmen.make_deposit(700000)
Carmen.make_withdrawal(555)
Carmen.make_withdrawal(3333)
Carmen.make_withdrawal(888)
Carmen.display_user_balance()