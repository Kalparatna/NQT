class Person:
    def __init__(self,id ,n , c):
        self.pid = id
        self.name = n
        self.city = c

    def show(self):
        print("pid = ", self.pid)
        print("Name = ", self.name)
        print("City = ", self.city)

P = Person(101, "Kalparatna", "Jalgaon")
P.show()
