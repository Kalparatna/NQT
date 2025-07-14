'''
Calculate Factorial of number without using multiplication and devision
'''
def fact(n):
    if n <= 1: 
        return 1
    else:
        result = 0
        for i in range(n):
            result += fact(n-1)
        return result

t = int(input())

while t > 0:
    n = int(input())
    print(fact(n))  
    t -= 1