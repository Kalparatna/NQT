class Emplyee:
    def __init__(self):
        self.eno = None
        self.ename = None
        self.esal = None
    
    def inputData(self):
        self.eno = int(input("Enter Employee Number: "))
        self.ename = (input("Enter Employee Name: "))
        self.esal = int(input("Enter Employee Salary: "))

class HRManager(Emplyee):
    def showData(self):
        print("Eno = ", self.eno)
        print("EName = ", self.ename)
        print("ESalary = ", self.esal)

h =HRManager()
h.inputData()
print("\n")
h.showData()