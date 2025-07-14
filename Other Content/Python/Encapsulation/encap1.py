class Test1:
    _b = None
    __c = None

    def __init__(self):
        self.a = 101
        self._b = 201
        self.__c = 301

    def show1(self):
        print("a = ", self.a)
        print("b = ", self._b)
        #print("c = ", self.__c) 
        print("c = ", self.__c)

class Test2(Test1):
    def show2(self):
        print("a = ", self.a)
        print("b = ", self._b)
        #print("c = ", self.__c) 
        print("c = ", self._Test1__c)  # Correctly access __c

class Test3(Test2):
    def show3(self):
        print("a = ", self.a)
        print("b = ", self._b)
        print("c = ", self._Test1__c)  # Correctly access __c

t1 = Test1()
t1.show1()
t2 = Test2()
t2.show2()
t3 = Test3()
t3.show3()
