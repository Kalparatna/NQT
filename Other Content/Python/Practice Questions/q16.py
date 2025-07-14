#check if the number is armstrong number 
#an n-digit number is an Armstrong number if the sum of its digits, each raised to the power of n, is equal to the number itself.
#Ex - For example, 153 is an Armstrong number because:        1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153         
#1634: 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
#armstrong number = narcissistic number =  pluperfect digital invariant =  or pluperfect digital number
while True:
    Num = int(input("Enter the number: "))
    Num_str = str(Num)
    Num_digit = len(Num_str)

    Sum = 0
    for digit_str in Num_str:
        digit = int(digit_str)
        Sum  += digit ** Num_digit


    if Num == Sum:
        print(f"{Num} is Armstrong number")
    else:
        print(f"{Num} is not Armstrong number") 


