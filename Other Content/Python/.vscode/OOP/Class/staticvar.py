#Static Variable

class mypython:
    x = 10  #static avriable
    def __init__(self):
        self.y = 20  #Instance avariable

m1 = mypython()
m2 = mypython()
print("m1 -- ", m1.x, m1.y)
print("m2 -- ", m2.x, m2.y)

mypython.x = 111

m1.y = 222

print("m1 --", m1.x, m1.y)
print("m2--", m2.x, m2.y)