import sys

class BankAccount:
    def __init__(self):
        self.name = None
        self.acno = None
        self.balance = None

    def inputData(self):
        self.name = input("Enter your Name: ")
        self.acno = int(input("Enter Your Account No.: "))
        self.balance = int(input("Enter Your Balance: "))

    def display(self):
        print("Name:", self.name)
        print("AcNo:", self.acno)
        print("Balance:", self.balance)

    def deposit(self):
        amt = int(input("Enter Amount to deposit: "))
        self.balance += amt

    def withdraw(self):
        amt = int(input("Enter Amount to withdraw: "))
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance!")

class SavingsAccount(BankAccount):
    def withdraw(self):
        amt = int(input("Enter Amount to withdraw: "))
        if self.balance - amt < 1000:
            print("Insufficient balance")
        else:
            self.balance -= amt

bank = SavingsAccount()

while True:
    print("1. Input Data")
    print("2. Display")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        bank.inputData()
    elif ch == 2:
        bank.display()
    elif ch == 3:
        bank.deposit()
    elif ch == 4:
        bank.withdraw()
    elif ch == 5:
        sys.exit()
    else:
        print("Invalid Choice!")
