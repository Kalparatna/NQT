"Sum of prime numbers from 2 to n"

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False       
    return True

n = int(input())
prime = 0
for i in range(2, n+1):
    if isPrime(i):
        prime += i

print(prime)

        


