arr = list(map(int, input().split()))
increasing = sorted(arr)
decreasing = sorted(arr, reverse=True)

print(f"Increasing Order : {increasing}")
print(f"Decreasing Order: {decreasing}")
