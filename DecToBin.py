#Decimal TO Binary


#Method 1
def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

decimal_number = 25
print("Binary of", decimal_number, "is", decimal_to_binary(decimal_number))

#method 2 : Built In Funtion
def decimal_to_binary_builtin(n):
    return bin(n)[2:]  # Removes '0b' prefix



#method 3: Using Python List and Join (Cleaner Version of Iterative)
def decimal_to_binary_list(n):
    if n == 0:
        return "0"
    bits = []
    while n:
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))



#Mehtod 4 :One-liner (Using format string)
def decimal_to_binary_format(n):
    return format(n, 'b')  # 'b' is for binary format




