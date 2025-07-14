num  = input("Enter the Number: ")

try:
    for i in range(1, 11):
        print(f'{int(num)} x {i} = {int(num) * i}')
except Exception as e:
    print("Invalid Input")
    print("Program Terminated")


#OR

num  = input("Enter the Number: ")

try:
    for i in range(1, 11):
        print(f'{int(num)} x {i} = {int(num) * i}')
except Exception as e:
    print(e)

print("Program Terminated")
