

try:
    n1 , n2  = map(int, input("enter input: ").split())
    print(n1+n2)

except:
    print("Something went wrong")

finally:
    print("Always Execute")