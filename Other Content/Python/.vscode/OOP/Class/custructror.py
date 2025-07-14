class Mypython:
    def __init__(self):
        print("Constructor is Called")
    def func(self):
        print("Func code execution")

m1 = Mypython()
m1.func()
print("----------------------------")
class MYpython:
    def __init__(self):
        print("Frist")
    def __init__(self):
        print("second")

m = MYpython()

print("----------------------------")

#delete instance variable (ex - self. s)

class Mypython:
    def __init__(self):
        self.a = 100
        self.b = 30
        self.c = 40
        self.d = 50

    def func(self):
        del self.d
m = Mypython()
print(m.__dict__)
m.func()
print(m.__dict__)
del m.c
print(m.__dict__)