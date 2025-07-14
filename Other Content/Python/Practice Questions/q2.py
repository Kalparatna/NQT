#Find largest among three numbers
'''
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
a = int(input("No 1: "))
b = int(input("No 2: "))
c = int(input("No 3: "))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)