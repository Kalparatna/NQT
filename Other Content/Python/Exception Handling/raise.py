try:
    age = int(input("Enter your age: "))
    if age<0:
        raise ValueError
    
    print("Your age is : ", age)

except ValueError as var:
    print(var)

print("rest of code")