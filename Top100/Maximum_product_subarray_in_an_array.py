arr = list(map(int, input().split()))

arr.sort()
max_product = max(arr[0] * arr[1], arr[-1] * arr[-2])
print(max_product)

# here we could directly take arr[-1] * arr[-2] as max product but,
# for nagative it not follows
# ex arr = [-10, -9, 0, 1, 3]   here first two elements producing largest product, not last