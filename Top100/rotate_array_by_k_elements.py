k = int(input())
arr = list(map(int, input().split()))

k = k % len(arr)  #when k lenght more than array  ex k = 7 arr = 5 ->  7 % 5 = 2(k)
rotated = arr[k:] + arr[:k]
print(rotated)
