
'''
from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class MyPython(Test):
    pass

m = MyPython()
'''

from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class MyPython(Test):
    def m1(self):
        print("m1 Method implementation")

    def m2(self):
        print("m2 Method implementation")

m = MyPython()
m.m1()
m.m2()