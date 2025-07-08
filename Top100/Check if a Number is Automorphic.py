'''
An Automorphic number (also known as a circular number) is a number whose square ends with the number itself.

Examples:
5² = 25 → ends with 5 → Automorphic
76² = 5776 → ends with 76 → Automorphic
6² = 36 → does not end with 6 → Not Automorphic
'''

num = int(input())

square = num ** 2

if str(square).endswith(str(num)):
    print("Automorphic/Circular Number")
else:
    print("Not an Automorphic Number")
