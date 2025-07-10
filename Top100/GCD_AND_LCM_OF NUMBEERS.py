a = int(input())
b = int(input())

def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

gcd = find_gcd(a, b)

lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
