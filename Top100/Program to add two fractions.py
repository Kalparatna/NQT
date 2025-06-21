n1 = int(input("Enter numerator of first fraction: "))
d1 = int(input("Enter denominator of first fraction: "))
n2 = int(input("Enter numerator of second fraction: "))
d2 = int(input("Enter denominator of second fraction: "))

# Using 3 Multiplication Method
mul1 = n1 * d2
mul2 = n2 * d1
mul3 = d1 * d2

N = mul1 + mul2
D = mul3

# GCD Function
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

gcd_ = gcd(N, D)

simplified_N = N // gcd_
simplified_D = D // gcd_

print(f"Unsimplified sum of fractions: {N}/{D}")
print(f"Simplified sum of fractions: {simplified_N}/{simplified_D}")
