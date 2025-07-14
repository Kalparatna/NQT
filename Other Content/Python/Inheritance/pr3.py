#Function Overiding 

class Emplyee:
    def __init__(self):
        self.eno = None
        self.ename = None
        self.esal = None
    
    def inputData(self):
        self.eno = int(input("Enter Employee Number: "))
        self.ename = (input("Enter Employee Name: "))
        self.esal = int(input("Enter Employee Salary: "))

    def work(self):
        print("Employee is Working on chatbot model")

    def getSalary(self, s):
        s = self.esal
        print(s)

class HRManager(Emplyee):
    def showData(self):
        print("Eno = ", self.eno)
        print("EName = ", self.ename)
        print("ESalary = ", self.esal)

    def work(self):
        print("Manager Has Assigned task of submitting projetcr today itself ")

    def setSalary(self):
        super().getSalary(8000)
        self.esal = self.s + self.esal
        

h =HRManager()
h.inputData()
h.showData()
h.setSalary()
h.getSalary()

