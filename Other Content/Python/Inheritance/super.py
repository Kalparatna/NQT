class Parent1:
    def show1(self, n):
        print("Parent1 Mehthod", n)

class Parent2(Parent1):
    def show2(self):
        super().show1("Ashish")
        print("Parent Method")

c = Parent2()
c.show2()