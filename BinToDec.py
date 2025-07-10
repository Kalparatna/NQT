#Binary to decimal

#1
def binary_to_decimal_builtin(binary_str):
    return int(binary_str, 2)


#2   Manual Method (Iterate from Right to Left – Positional Approach)
def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for digit in reversed(binary_str):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
