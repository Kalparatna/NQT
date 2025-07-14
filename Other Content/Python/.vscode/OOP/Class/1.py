class Person:
    def __init__(self):
        self.pid = 101
        self.name = "Kalparatna"
        self.city = "Dhule"

    def show(self):
        print("pid = ", self.pid)
        print("Name = ", self.name)
        print("City = ", self.city)

P = Person()
P.show()
