try:
    num = int(input("enter the number: "))
    a = [2, 4]
    print(a[num])

except ValueError:
    print("Not Integer")

except IndexError:
    print("Index Error")