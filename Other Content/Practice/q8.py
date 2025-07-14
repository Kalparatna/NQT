'''
Find Equilibrium Point
You are given a 
0− indexed integer array 
nums. Your task is to find the leftmost equilibrium index in the array. An equilibrium index is defined as an index i such that the 
sum of the elements to the left of i is equal to the sum of the elements to the right of i.
Formally, the equilibrium index i satisfies the condition:

sum(nums[0]+nums[1]+.nums[i−])=sum(nums[i+1]+nums[+2]+...+nums[num.length−1])
sum(nums[0]+nums[1]+...+nums[i−1])=sum(nums[i+1]+nums[i+2]+...+nums[nums.length−1])

Conditions:

If ii is 00, the left sum is considered 00.If ii is (n−1)
(n−1), the right sum is considered 0.
Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input:
The first line contains an integer 
N
N, length of array.
The next line contain an array 
nums
nums of length N.
Output Format
For each test case, return the leftmost equilibrium index if it exists, or return −1 if there is no such index.


Sample 1:
Input
Output
3
5
1 -1 2 1 -2
3
1 -1 4
6
1 2 3 4 5 6
0
2
-1
Explanation:
Test Case 1: For index 0, the left side is considered 0, and the right side sum is -1 + 2 + 1 + (-2) = 0. Hence, index 0 is an equilibrium index.
Test Case 2: For index 2, the sum of numbers before index 2 is: 1 + -1 = 0 and sum of numbers after index 2 is: 0.
Test Case 3: No index satisfies the equilibrium condition.
'''
T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]

        if right_sum == left_sum:
            print(i)
            break
        
        left_sum += nums[i]
    else:
        print(-1)

#https://www.codechef.com/practice/course/tcs-nqt-questions/TCSNQTC/problems/TCSNQTCP10