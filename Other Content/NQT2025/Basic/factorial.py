def factorial(num):
    if num <= 1:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact
    
num = int(input())

print(factorial(num))


#OR 

number = int(input("enter: "))

if number <= 0:
    print(1)
else:
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    print(fact)
