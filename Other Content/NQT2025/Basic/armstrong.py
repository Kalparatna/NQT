def arm(num):
    temp = num
    digit = 0
    result = 0
    while temp> 0:
        digit = temp % 10
        result += digit ** 3
        temp //= 10
    
    return result == num

num = 153
if arm(num):
    print("Num is Armstrong")

else:
    print("Not")
