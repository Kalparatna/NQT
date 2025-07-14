#print the numbers in reverse order with diffrence two

N = 55434
rev = 0
while N != 0:
    rem = N % 10
    rev = (rev * 10) + rem
    N //= 10
print(rev - 2)