def decimal_to_binary(num):
    if num == 0:
        return "0"

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary 
        num //= 2

    return binary






decimal_number = 13
binary_number = decimal_to_binary(decimal_number)
print(binary_number)