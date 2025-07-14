#from given list of number check if number if every no. is palindrome and it to another list

L = [12, 11, 245, 222, 333, 54]
NewL = []

for num in L:
    org = num
    rev = 0
    while num != 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num //= 10
    if org == rev:
        NewL.append(org)

for num in NewL:
    print(num)

   
