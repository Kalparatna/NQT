#Local Variable

class Test:
    def func(self):
        a = 100
        print(a)

    def func2(self):
        b = 333
        a = 666
        print(b)
        print(a)

t = Test()
t.func()
t.func2()