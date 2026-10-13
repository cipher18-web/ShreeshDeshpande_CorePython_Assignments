#creating bank account system using oops 

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawal Successful")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

name = input("Account Holder: ")
balance = int(input("Initial Balance: "))
account = BankAccount(name, balance)

deposit_amt = int(input("Enter deposit amount: "))
account.deposit(deposit_amt)

withdraw_amt = int(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amt)

account.display_balance()