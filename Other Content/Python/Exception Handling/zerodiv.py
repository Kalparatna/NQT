num1 , num2= map(int, input("Enter the Numbers: ").split())

try:
    div = num1/num2
    print(int(div))

except ZeroDivisionError:
    print("We Can't Devide With Zero")

print("Program Completed")

