class Mobile:
    def __init__(self):
        self.ram =None
        self.storage = None
        self.__price = None
    
    def set_price(self, amount):
        if 0 < amount < 500:
            self.__price += amount

    def get_price(self):
        return self.__price

Mob1 = Mobile('2gb','5gb', 100)
Mob1.set_price(400)

print(Mob1.ram, Mob1.storage, Mob1.get_price())
