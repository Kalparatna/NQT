#Heirarchical Inheritance

class A:
    def showA(self):
        print("I Am in A")

class B(A):
    def showB(self):
        print("I Am in B")

class C(A):
    def showC(self):
        print("I Am in C")

obj1 = B()
obj1.showA()
obj1.showB()
print("\n")
obj2 = C()
obj2.showA()
obj2.showC()