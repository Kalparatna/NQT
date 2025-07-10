def isprime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def isSumOfPrimes(num):
    for i in range(2, num):
        if isprime(i) and isprime(num - i):
            print(f"{num} = {i} + {num - i}")
            return True
    return False

num = 26
print(isSumOfPrimes(num))
