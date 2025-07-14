#In Lambda line after : by default return 
#By using lambda we can write Concise code.
#Lambda is nameless function

def squre(n):
    return n * n

print("The Square of 4 is : ",squre(4))
print("The Square of 5 is : ",squre(5))

s = lambda n: n*n

print("The Square of 5 is : ",s(5))
print("The Square of 5 is : ",s(4))


D = lambda a, b: a+ b

print("The addition : ",D(4, 5))

l = lambda a, b: a if a>b else b

print("Answer = ",l(5, 8))

def mywrapper(n):
    return lambda a: a*n

mul = mywrapper(5)

print(mul(2))





