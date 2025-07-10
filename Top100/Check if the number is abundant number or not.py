'''abundant number: is a positive integer for which the sum of its proper divisors (excluding itself)
is greater than the number itself.
Examples:
12 → divisors: 1, 2, 3, 4, 6
Sum = 1 + 2 + 3 + 4 + 6 = 16 > 12 → Abundant

18 → divisors: 1, 2, 3, 6, 9
Sum = 21 > 18 → Abundant
'''

num = int(input())
divisors_sum = 0

for i in range(1, (num // 2) + 1):
    if num % i == 0:
        divisors_sum += i

if divisors_sum > num:
    print("Abundant Number")
else:
    print("Not an Abundant Number")
