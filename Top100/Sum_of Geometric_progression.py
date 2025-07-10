a = int(input())
r = int(input())
n = int(input())

if r == 1:
    total = a * n
else:
    total = a * ((1 - r ** n) / (1 - r))

print(total)
