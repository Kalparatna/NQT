'''
Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.
'''

def product(Num1, Num2, Num3):
    if Num1 == 7:
        print(Num2 * Num3)

    elif Num2 == 7:
        print(Num3)

    elif Num3 == 7:
        print(-1)

    else:
        print(Num1 * Num2 * Num3)

x = int(input("Enter Num 1: "))
y = int(input("Enter Num 2: "))
z = int(input("Enter Num 1: "))

product(x,y,z)

     
