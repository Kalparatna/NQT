#Passing memebers of one calss to another class

class Employee:
    def __init__(self, no, name, sal):
        self.eno = no
        self.ename = name 
        self.esal =sal
    
    def showDetails(self):
        print("Employee no : ", self.eno)
        print("Employee name : ", self.ename)
        print("Employee salary : ", self.esal)
        
class Test:
    def updates(Employee):
        Employee.esal = Employee.esal + 8000
        Employee.showDetails()


e = Employee(100,"Kalparatna", 20000)
e.showDetails()
print("\n")
Test.updates(e)