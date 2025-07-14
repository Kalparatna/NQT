#The Value which is not usable is garbage

#Calloc()  , malloc(), free()

import gc 

class Time:
    def __init__(self):
        print("Constructor is calleld\n")
    
    def __del__(self):
        print("Destructor is called\n")

t = Time()
t = None
print("Application is Added\n")


#del used for destroying objects

class Time:
    def __init__(self):
        print("Costructor is called")

    def __del__(self):
        print("Destructor is called")

t1 = Time()
#t2 = Time()
#t3 = t1
del t1