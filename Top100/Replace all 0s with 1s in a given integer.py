

def zeroTone(n):
    return int(str(n).replace("0", "1"))

#Or

def withoutfuntion(n):
    strnum = str(n)
    result = ""
    for digit in strnum:
        if digit == "0":
            result += "1"
        else:
            result += digit
    return int(result)

if __name__ == "__main__":

    num = 110340
    print(withoutfuntion(num))