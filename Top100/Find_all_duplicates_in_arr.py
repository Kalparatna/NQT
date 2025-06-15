arr = list(map(int, input().split()))

fre = {}
result = []

for i in arr:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

for key, value in fre.items():
    if value > 1:
        result.append(key)

print(result)