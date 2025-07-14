#print Factorial of given number

Num = int(input("Enter the Number: "))


def factorial(Num):
    if Num == 0 or Num == 1:
        return 1
    else:
        return Num * factorial(Num-1)

Fact = factorial (Num)
print(f"The factorial of {Num} is {Fact}")       

'''
In Python, an f-string (formatted string literal) is a way 
to embed expressions inside string literals, allowing you to
easily incorporate variables and expressions into strings.
'''