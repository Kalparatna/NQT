# find gcd of number and LCM

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)  

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Finding GCD and LCM
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

print(f"GCD of {num1} and {num2} is {gcd_result}")
print(f"LCM of {num1} and {num2} is {lcm_result}")

