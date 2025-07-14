def isarmstrong(num):
    numlen = len(str(num))
    res = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        res += digit ** numlen
        temp //= 10
    return num == res

num = int(input())
if isarmstrong(num):
    print("armstrong")
else:
    print("Not")
