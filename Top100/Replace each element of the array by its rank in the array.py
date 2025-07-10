arr = list(map(int, input().split()))  # Read input as space-separated numbers
sorted_arr = sorted(set(arr))  # Sort unique elements to assign ranks
rank_dict = {num: rank for rank, num in enumerate(sorted_arr)}

# Replace elements with their ranks
arr = [rank_dict[num] for num in arr]
print(arr)

#Input: 1 5 3 2 4
#output: [0, 4, 2, 1, 3]