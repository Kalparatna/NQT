class Mobile:

    # Here def __init__ works as Constructor
    def __init__(self,ram, storage, price):                     #Every __init__ has first parameter as self
        self.ram = ram
        self.storage = storage 
        self.__price = price           #__price is private 
        #self.cost = price   # price stored  in cost        here self is just an parameter

    #method
    def set_price(self, amount):
        if 0 < amount <500:
            self.price += amount

#Creating An Obejct
#Mobile()
#Mobile()
#Mobile()

#Creating Reference Variable
#mob1 = Mobile() 
#mob1 = Mobile() 

mob1 = Mobile('2gb', '128gb', 1000)    #Here mob1 is reference varibale actually, as we can call it object        
mob2 = Mobile('3gb', '64gb', 9000)  #Here mob2  is reference varibale actually, as we can call it object
#mob1.price = 5000

print(mob1.price)
#print(mob1.cost)                     #ere Price, Cost ram are our atribute

mob2.ram = '8gb'
print(mob2.ram)


mob1.set_price(500)

#print(mob1.price)