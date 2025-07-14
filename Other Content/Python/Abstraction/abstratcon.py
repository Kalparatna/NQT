#- it is possible to declare constuctor inside abstract class, but object not created


#Inside the Abtract class we can declare the constructor abtract
#  class constructor is excecuted but object is not created 

from abc import ABC, abstractmethod

class Test(ABC):
    def __init__(self):
        print("Constructor is called....")


    @abstractmethod
    def m1(self):
        pass

class MyPython(Test):
    def m1(self):
        print("m1 nethod Implemetation")

m = MyPython()
m.m1()
#m.m2()