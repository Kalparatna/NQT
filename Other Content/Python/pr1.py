'''
import math

#Print Answer for (a+b)^2
a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = ((a+b)**2)
print(c)
'''

'''
#Print Greatest Of Three Nos

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))

if a > b:
    if a > c:
        print( a, " Is Greater")

    else:
        print(c," Is greter")

else:
    if b > c:
        print(b, " Is Greater")
    else:
        print(c, " Is Greater")
'''
'''
#Find Squreroot OF Number

Number = int(input("Enter the number : "))
Squareroot = Number ** .5
print(Squareroot)

'''

#Billing Calculator

U = int(input("Enter Billing Unit: "))

if U > 0 and U <= 50:
    Bill= U * 2.60 + 24
    print(Bill)

elif U >= 51 and U < 100:
    U = U - 50
    Bill = (U * 3.25 + 35) + (50 * 2.60)
    print(Bill)

elif U >= 100 and U < 200:
    U =  U - 100 
    Bill = (U * 5.26 + 45 ) +(50 * 3.25) + (50 * 2.60)
    print(Bill)

else:
    U  = U - 200
    Bill =  (U * 8.25 + 75)+ (100 * 5.26) +(50 * 3.25) + (50 * 2.60)
    print(Bill)






