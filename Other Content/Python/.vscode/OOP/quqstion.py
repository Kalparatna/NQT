class Electricity:
    def __init__(self):
        self.c_id = int(input("Enter ID "))
        self.c_name = input("Enter C Name ")
        self.unit = int(input("Enter Unit "))
        self.bill = 0
        self.charges = 0
        self.totalbill = 0


    def calculate(self):

        print(self.c_id)
        print(self.c_name)
        print(self.unit)

        if self.unit > 0 and self.unit< 30:
            self.bill = self.unit * 1.5
            print(self.bill)
        elif self.unit > 30 and self.unit<= 200:
            self.bill = self.unit * 3
            print(self.bill)
        elif self.unit > 200 and self.unit<= 300:
            self.bill = self.unit * 3.5
            print(self.bill)
        elif self.unit > 300:
            self.bill = self.unit * 4.25
            print(self.bill)
        else:
            print("invalid Input")

        if self.bill > 500:
            self.charges = self.bill * 0.15
            print(self.charges)
            self.totalbill = self.unit * 1.5
            print(self.totalbill)

        

        
        

        
        
        

C = Electricity()
C.calculate()

        