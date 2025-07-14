#check if the given number is palindrome 

Num = int(input("Enter the Number: "))
Org = Num
Rev = 0

while Num != 0:
    Rem = Num % 10
    Rev = (Rev * 10) + Rem
    Num //= 10

if Org == Rev:
    print("Palindrome")
else:
    print("Not Palindrome") 