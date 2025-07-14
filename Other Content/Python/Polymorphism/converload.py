#Constructor Overloading
class Test:
    def __init__(self,a=0, b = 0, c = 0):
        print("Constructor with 0, 1, 2, 3 arguments", a,b,c)

t = Test()
t = Test(10)
t  = Test(10,20)
t = Test(10, 22, 33)