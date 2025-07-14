#print all armstromg numbers from 1 to 9000    ex (1^4 + 6^4 + 3^4 + 4^4 == 1634) 1634 is armstrong number

for Num in range(9000):
    Num_str = str(Num)
    Num_digit = len(Num_str)

    Sum = 0
    for digit_str in Num_str:
        digit = int(digit_str)
        Sum  += digit ** Num_digit

    if Num == Sum:
        print(Num)