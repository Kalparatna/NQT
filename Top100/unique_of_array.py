#With XOR Operation
arr = list(map(int, input().split()))
unique = 0
for i in arr:
    unique ^= i

print(unique)


#or Using Hashmap

arr = list(map(int, input().split()))
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    if value == 1:
        print(key)

