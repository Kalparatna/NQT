import sys
from abc import ABC, abstractmethod

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
    
    @abstractmethod
    def deposit(self):
        pass
    
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):
    def deposit(self):
        amt = int(input("Enter Amount to deposit: "))
        self.balance += amt

    def withdraw(self):
        amt = int(input("Enter Amount to withdraw: "))
        if self.balance - amt < 1000:
            print("Insufficient balance")
        else:
            self.balance -= amt

    def getInterest(self, rate):
        if rate >= 4:
            interest = (rate/100) * self.balance
            print("Interest for Savings Account: ", interest)
        else:
            print("No")

class CurrentAccount(BankAccount):
    def deposit(self):
        amt = int(input("Enter Amount to deposit: "))
        self.balance += amt

    def withdraw(self):
        if self.balance <= 1000:
            amt = int(input("Enter Amount to withdraw: "))
            if amt <= self.balance:
                self.balance -= amt
        else:
            print("Insufficient balance!")

    def getInterest(self, rate):
        interest = (rate/100) * self.balance
        print("Interest for Current Account: ", interest)

class Interest1(SavingsAccount):
    def setInterest(self):
        super().getInterest(4)

class Interest2(CurrentAccount):
    def setInterest(self):
        super().getInterest(2)

account = SavingsAccount()
while True:
    print("1. Input Data")
    print("2. Display")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Saving Account Interest")
    print("6. Current Account Interest")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        account.inputData()
    elif ch == 2:
        account.display()
    elif ch == 3:
        account.deposit()
    elif ch == 4:
        account.withdraw()
    elif ch == 5:
        account.getInterest(4)
    elif ch == 6:
        account.getInterest(2)
    elif ch == 7:
        sys.exit()
    else:
        print("Invalid Choice!")
