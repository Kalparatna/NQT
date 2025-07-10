arr = list(map(int, input().split()))
find =  5
found = False
for pos , num in enumerate(arr):
    if num == find:
        print(f"Given number {find} in at position of {pos}")
        found = True
        break

if not found:
    print("Not in array")
