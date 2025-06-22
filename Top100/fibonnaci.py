def fibonacci(n):
    if n ==  0:
        return 0
    elif n ==1 :
        return 1
 
    return fibonacci(n-1) +fibonacci(n-2)

num = int(input())
print(fibonacci(num))


#or (Faster)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

num = int(input())
print(fibonacci(num))
