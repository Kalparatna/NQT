#Multiple Inheritance
class A:
    def show(self):
        print("i am in class A")

class B:
    def show(self):
        print("i am in class b")

class C(A,B):
    def showC(self):
        print("i am in class B")

obj2 = C()

obj2.show()

obj2.showC()