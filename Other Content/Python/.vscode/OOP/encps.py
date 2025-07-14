
'''
#Public

class Mobile:
    def __init__(self,ram, storage, price):
        self.ram = ram
        self.storage  = storage
        self.price = price

Mob = Mobile('2gb', '64gb', 8000)              
Mob.price += 600                             #We Can change value for price 


print(Mob.price)

#Private

class Mobile:
    def __init__(self):
        self.ram = None
        self.storage  = None
        self.price = None

    def set_price(self, amount):
       # amount =int(input())
        if 0 < amount <500:
            self.price += amount
           

    def get_price(self):
        return self.price
    

Mob = Mobile()
Mob.ram = '2gb'
Mob.storage = '64gb'
#Mob.price = 5000
#print(Mob.price)

'''

class Mobile:
    def __init__(self):
        self.ram = None
        self.storage  = None
       # self.__price = None                   
       

    def set_price(self, amount):
       # amount =int(input())
        if 0 < amount <500:
            self.__price += amount

    def get_price(self):
        return self.__price
      

Mob = Mobile()
Mob.ram = '2gb'
Mob.storage = '64gb'
Mob.set_price(300)
print(Mob.get_price())
