class Test:
    def __init__(self):
        print("No Arguments")

    def __init__(self, a):
        print("One Arguments: ",a)

    def __init__(self, a ,b):                              #Highest priority 
        print("Two Arguments: ",(a+b))

#t = Test()
t = Test(10, 20)