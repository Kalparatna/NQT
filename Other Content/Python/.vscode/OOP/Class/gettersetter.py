class Student:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setPercentage(self, percentage):
        self.percentage = percentage
    def getPercentage(self):
        return self.percentage

n = int(input("Enter no of Student: "))
s = Student()
for i in range(n):
    name = input("Enter name of student: ")
    s.setName(name)
    percentage = int(input("Enter student percenatage: "))
    s.setPercentage(percentage)
    print("Hi", s.getName(), "Your percentage is: ", s.getPercentage())
    print()