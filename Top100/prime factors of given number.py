# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Get all factors
num = int(input("Enter a number: "))
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

# Filter prime factors
prime_factors = [f for f in factors if is_prime(f)]

print("Prime factors:", *prime_factors)



#Or (efficient)

