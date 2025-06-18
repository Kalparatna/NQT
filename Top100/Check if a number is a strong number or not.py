'''A Strong number is a number whose sum of the factorials of its digits is equal to the number itself.

Example:
145 is a Strong number because:
1! + 4! + 5! = 1 + 24 + 120 = 145  '''

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
    
num = int(input())

factorial_sum = 0
for digit in str(num):
    factorial_sum += factorial(int(digit))

if factorial_sum == num:
    print("Strong Number")
else:
    print("Not")