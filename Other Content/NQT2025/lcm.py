def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1% n2
    return n1

def lcm(n1, n2):
    l = (n1 * n2) // gcd(n1, n2)
    return l

print(gcd(12,15))
print(lcm(12,15))




