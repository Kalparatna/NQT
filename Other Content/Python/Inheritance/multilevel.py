#Multilevel Inheritance

class A:
    def showA(self):
        print("i am in class A")

class B(A):
    def showB(self):
        print("i am in class B")

class C(B):
    def showC(self):
        print("i am in class C")


obj = A()
obj.showA()

print("\n")

obj2 = B()
obj2.showA()
obj2.showB()

print("\n")

obj3 = C()
obj3.showA()
obj3.showB()
obj3.showC()