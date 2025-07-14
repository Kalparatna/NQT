#print all devisors of an integer
while True:
    
    Num = int(input("Enter the Number: "))

    for i in range(1, Num+1):
        if Num % i == 0:
            print(i)
      