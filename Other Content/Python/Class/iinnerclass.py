#Inner Class:- 
'''
A class defined in another class is known as an inner class or nested class. 
If an object is created using child 
class means inner class then the object can also be used by 
parent class or root class. A parent class can have one or more
 inner classes but generally inner classes are avoided.
We can make our code even more object-oriented by using an inner class.
 A single object of the class can hold multiple sub-objects.
  We can use multiple sub-objects to give a good structure to our program.
'''

#Annynymous Function

class SVKM:
    def __init__(self):
        print("SVKM Default construnctor is called..")
    class IT:
        def __init__(self):
            print("IT Default Constryctor callled..")

        def techfest(self):
            print("SVKM - IT bracn Techfest execution")

r = SVKM()
print("\n")
obj = r.IT()
print("\n")
obj.techfest()

print("\n")

obj1 = SVKM().IT()
print("\n")
obj1.techfest()

print("\n")
SVKM().IT().techfest()