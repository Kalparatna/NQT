'''
Problem Statement: 1
Given a range [m, n] (both inclusive) where 0 <= m, n <= 10000, find the sum of all integers between m and n
Example:
Input:
0 3
Output:
6
Explanation:
0+1+2+3 = 6

'''
m,n = map(int, input().split())

result = 0
for i in range(m,n+1):
    result += i

print(result)
