#Bankacount Deatails

import sys  # For the exit function

class BankAccount:
    def __init__(self):
        self.name = None
        self.ACN = None
        self.ATP = None  
        self.balance = 0
      

    def inputData(self):
        self.name = input("Enter Name: ")
        self.ACN = int(input("Enter AC Number: "))
        self.ATP = input("Enter Account Type (savings)")
        self.amount = int(input("Enter Amount: "))  

    def Display(self):
        print("Name: ", self.name)
        print("Ac. Number: ", self.ACN)
        print("Ac Type: ", self.ATP)
        print("Balance: ", self.balance)  

    def Deposit(self):
        deposit_amount = int(input("Enter amount to deposit: "))  
        self.balance += deposit_amount  
        print("Deposited:", deposit_amount)

    def Withdraw(self):
        withdraw_amount = int(input("Enter amount to withdraw: "))  
        if withdraw_amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= withdraw_amount  
            print("Withdrawn:", withdraw_amount)
bank = BankAccount()

while True:
    print("1. Input Data")
    print("2. Display")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    ch = int(input("Enter Your Input: "))
    if ch == 1:
        bank.inputData()
    elif ch == 2:
        bank.Display()
    elif ch == 3:
        bank.Deposit()
    elif ch == 4:
        bank.Withdraw()
    elif ch == 5:
        sys.exit()
    else:
        print("Invalid input.")
