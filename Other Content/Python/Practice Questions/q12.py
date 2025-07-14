#Count the number of digits in given number
Num = int(input("Enter the Number: "))

Num = abs(Num)  # Handle negative numbers

Count = 0
while Num:
    Count += 1
    Num //= 10

print("Number of digits:", Count)

