def isprime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True


n = int(input("Enter Number: "))
if isprime(n):
    print("Prime")
else:
    print("Not Prime")