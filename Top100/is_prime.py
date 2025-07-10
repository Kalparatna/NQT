def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i ==0:
            return False
        
    return True

num = int(input())
prime_numbers = []
for i in range(num):
    if is_prime(i):
        prime_numbers.append(i)

print(*prime_numbers)
