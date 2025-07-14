class Base:
    def add(self):
        a = int(input("Enter the Value for a: "))
        b = int(input("Enter the Value for b: "))
        res = a + b
        print(res)

    def sub(self):
        a = int(input("Enter the Value for a: "))
        b = int(input("Enter the Value for b: "))
        res = a - b
        print(res)

class child(Base):
    def mul(self):
        a = int(input("Enter the Value for a: "))
        b = int(input("Enter the Value for b: "))
        res = a * b
        print(res)

    def div(self):
        a = int(input("Enter the Value for a: "))
        b = int(input("Enter the Value for b: "))
        res = a / b
        print(res)


obj = child()

obj.add()
obj.sub()
obj.mul()
obj.div()



    
