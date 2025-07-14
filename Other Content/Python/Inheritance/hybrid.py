#Hybrid Inheritance

class A:
    def showA(self):
        print("i am in class A")

class B(A):
    def showB(self):
        print("i am in class B")

class C(A):
    def showC(self):
        print("i am in class C")

class D(B,C):
    def showD(self):
        print("i am in class D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()
