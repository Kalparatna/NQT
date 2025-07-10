arr = list(map(int, input().split()))

n = len(arr)
d = arr[1] - arr[0]
a = arr[0]

ap_sum = (n / 2) * (2 * a + (n - 1) * d)
print(int(ap_sum))