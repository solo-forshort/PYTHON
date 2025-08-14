class BankAccount:
    def __init__(self, initial_balance, account_name):
        self.balance = initial_balance
        self.name = account_name
        print(f"\nAccount {self.name} created. \nBalance = {self.balance:.2f}\n")

    def  getBalance(self):
        print(f"Account {self.name} balance = {self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete")
        self.getBalance()