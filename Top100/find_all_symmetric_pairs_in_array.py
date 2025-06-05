#Symmetric Pairs
#ex - if (a,b) then (b, a) should also present

arr = []
n = int(input("No of pairs: "))

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))
dic = {}
result = []
for a, b in arr:
    if dic.get(b) == a:
        result.append((a, b))
    else:
        dic[a] = b
print(result)
