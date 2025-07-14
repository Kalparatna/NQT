#Reserver the number

#N = int(input("Enter the Number: "))
N = 55434
rev = 0
while N != 0:
    rem = N % 10
    rev = (rev * 10) + rem
    N //= 10
print(rev)

