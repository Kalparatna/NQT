#Equilibrium Index: Where leftsum and rightsum in equal 

arr = list(map(int, input().split()))
left_sum = 0
right_sum = 0
total_sum = sum(arr)

for i in range(len(arr)):
    right_sum = total_sum - left_sum -arr[i]
    if left_sum == right_sum:
        print(i)
        break
    left_sum += arr[i]
else:
    print(-1)
