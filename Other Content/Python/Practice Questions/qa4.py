# accept the numbers and check if palindrome or not

N = int(input())
Ori = N
rev = 0
while N != 0:
    rem = N % 10
    rev = (rev * 10) + rem
    N //= 10

if N == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

