'''
Problem Statement: 2
3. Find a Unique Element in an Array
You are given an array containing N integers where only one element is unique (appears exactly once), while all other elements appear twice. 
Find and return the unique element.
Example:
Input:
arr = [5, 3, 2, 3, 2]
Output:
5

'''

arr = list(map(int, input().split()))

unique = 0
for i in arr:
    unique ^= i
print(unique)

#Or

arr = list(map(int, input().split()))
print(2 * sum(set(arr)) - sum(arr))  

#OR

arr = list(map(int, input().split()))

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        print(arr[i])

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr.count(arr[i]) == 1:
        print(arr[i])
        