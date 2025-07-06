'''
Question:
You are given a list of integers of length N. Every element in the list appears exactly two times,
except for one unique element, which appears exactly once. Your task is to find and print this
unique element.
Input Format:
The first line contains an integer N, the length of the list.
The second line contains N space-separated integers representing the elements of the list.
Output Format:
Print the unique element that appears exactly once.
Constraints:
Example 1:
📌 Input:
9
1 1 2 2 5 6 6 7 7
📌 Output:
5
Example 2:
📌 Input:
7
3 3 4 4 9 2 2
📌 Output:
9

'''
#But only works when element two times repeated , not more times
n = int(input())
nums = list(map(int, input().split()))

unique = 0
for i in nums:
    unique ^= i

print(unique)


#Other Approach
n = int(input())
nums = list(map(int, input().split()))

freq = {}
for i in nums:
    freq[i] = freq.get(i, 0) + 1

# Method 1: Print all unique elements (those that appear exactly once)
result = []
for key, value in freq.items():
    if value == 1:
        result.append(key)

print(*result)

# Method 2: Print only the first unique element (preserves input order)
for num in nums:
    if freq[num] == 1:
        print(num)
        break
