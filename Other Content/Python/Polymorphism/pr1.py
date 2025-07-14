class MyPython:
    def sum(self, *n):
        total = 0
        for x in n:
            total = total + x
        print("Sum = ", total)


m = MyPython
m.sum(10, 20)
m.sum(10, 20 ,30)
m.sum(10,20,30,40)
m.sum(10)
m.sum()
