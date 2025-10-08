'''A Strong number is a number whose sum of the factorials of its digits is equal to the number itself.

Example:
145 is a Strong number because:
1! + 4! + 5! = 1 + 24 + 120 = 145  '''

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

def isstrong(num):
    res = 0
    for digit in str(num):
        res += factorial(int(digit))

    if num ==res:
        return "strong"
    else:
        return "Not"


    
num = int(input())

print(isstrong(num))

