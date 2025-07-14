class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

myDog= Dog("Buddy")
myCat = Cat("Fluffy")

print(myDog.name + " says " + myDog.speak())
print(myCat.name + " says " + myCat.speak())
