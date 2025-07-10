'''
Harshad number/ Niven number :  is an integer that is divisible by the sum of its digits.

18 → sum of digits = 1 + 8 = 9 → 18 % 9 == 0 → Harshad number

'''

num = int(input())

digit_sum = 0
for digit in str(num):
    digit_sum += (int(digit))

if num == digit_sum:
    print("Harshad/Niven Number")
else:
    print("Not")