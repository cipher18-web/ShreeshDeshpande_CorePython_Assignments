


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Deposit Amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid Withdrawal Amount")
        else:
            self.__balance -= amount
            print("Withdrawal Successful")

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Current Balance: {self.__balance}")


name = input("Account Holder: ")
balance = int(input("Initial Balance: "))
account = BankAccount(name, balance)

deposit_amt = int(input("Enter deposit amount: "))
account.deposit(deposit_amt)

withdraw_amt = int(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amt)

account.display_balance()
