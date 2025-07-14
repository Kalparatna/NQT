class Test: 
    def func(self):
        print("No Argument method")

    def func(self,a):
        print("One Argument method: ", a)

    def func(self,a, b):
        print("Two Argument method: "(a+b))

t = Test()
#t.func()
#t.func(10)
t.func(10,20)