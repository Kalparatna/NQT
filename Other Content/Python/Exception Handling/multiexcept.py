# num1 , num2= map(int, input("Enter the Numbers: ").split())

# try:
#     div = num1/num2
#     print(int(di))

# except ZeroDivisionError:
#     print("We Can't Devide With Zero")

# except NameError:
#     print("Varible Name is wrong")

# print("Program Completed")

#WITHOUT CREATING MULTIPLE BLOCKS

num1 , num2= map(int, input("Enter the Numbers: ").split())

try:
    div = num1/num2
    print(int(di))

except (ZeroDivisionError,NameError) as obj:
    print(obj)



print("Program Completed")



