class Person:
    def __init__(self):
        self.pid = None
        self.name = None
        self.city = None

    def inputData(self):
        self.pid = input("Enter Id ")
        self.name = input("Enter name ")
        self.city = input("Enter city ")


    def show(self):
        print("\n Output")
        print("pid = ", self.pid)
        print("Name = ", self.name)
        print("City = ", self.city)

P = Person()
P.inputData()
P.show()
