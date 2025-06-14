# A perfect number is a positive intger that is equal to the sum of its proper positive divisors(excluding number itself)
#ex - 28 is perfect number
# 1 + 2 + 4 + 7 + 14 = 28

num = int(input())
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0 :
        sum_of_divisors += i

if sum_of_divisors == num:
    print(f"{num} is perfect number")
else:
    print("Not perfect")