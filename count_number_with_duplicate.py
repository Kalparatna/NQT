'''
Problem Description -:  Given two non-negative integers n1 and n2, where n1
For example:
Suppose n1=11 and n2=15.
There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

Example1:
Input:

11 — Vlaue of n1
15 — value of n2
Output:

4
Example 2:

Input:

101 — value of n1
200 — value of n2
Output:

72

'''
# USing set function which is use to remove duplicate element from list

n1 = int(input())
n2 = int(input())

count= 0
for i in range(n1, n2+1):
    if len(set(str(i))) == len(str(i)):
        count += 1
print(count)
