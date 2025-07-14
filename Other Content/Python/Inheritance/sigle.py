class A:
    def showA(self):
        print("i am in class A")

class B(A):
    def showB(self):
        print("i am in class b")

obj = A()
obj.showA()

obj2 = B()
obj2.showA()
obj2.showB()
