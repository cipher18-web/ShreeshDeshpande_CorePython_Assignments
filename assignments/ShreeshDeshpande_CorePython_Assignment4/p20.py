class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = int(balance)  # Double underscore for strict encapsulation

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit Successful")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawal Successful")

    def check_balance(self):
        return self.__balance

    def display_details(self):
        print(f"""Account Holder: {self.name}
Account Number: {self.account_number}
Current Balance: ₹{self.__balance}""")

name1 = input("Account Holder: ")
acc_num1 = input("Account Number: ")
balance1 = int(input("Initial Balance: ₹"))
account1 = BankAccount(name1, acc_num1, balance1)

deposit_amt = int(input("Enter deposit amount: ₹"))
account1.deposit(deposit_amt)

withdraw_amt = int(input("Enter withdrawal amount: ₹"))
account1.withdraw(withdraw_amt)

account1.display_details()
account2 = BankAccount("nilesh", 102, 500000)
