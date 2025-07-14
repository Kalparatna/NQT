#Print the sum of odd numbers from 1 to n

Num = int(input("Enter the Number: "))
Sum = 0
for i in range(1, Num+1):
    if i % 2 != 0:
        Sum +=i

print("\n")
print(f'The sum of numbers from 1 to {Num} is: {Sum}')