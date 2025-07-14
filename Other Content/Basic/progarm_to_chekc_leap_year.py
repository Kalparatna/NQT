# Python program to check if a year is a leap year

year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is leap year")
else:
    print("Not leap year")