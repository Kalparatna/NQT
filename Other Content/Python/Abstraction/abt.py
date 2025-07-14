#if the child class is unable to provide implementation of all 
# method of abtract class then we can declare the child class 
# method with @Abrtractmethod and ....


from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        print("m2 Method implentation")

class MyPython(Test):
    @abstractmethod
    def m1(self):
        pass

class Child(MyPython):
    def m1(self):
        print("m1 Method Implementation")

m = Child()
m.m1()
m.m2()