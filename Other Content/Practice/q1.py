'''
Count Pairs divisible by 2
You're given a list of numbers. Your task is to find how many pairs of numbers in that list add up to an even number. A pair consists of two different numbers from the list. For example, in the list [1, 2, 3, 4], the pairs that sum to an even number are (1, 3) and (2, 4).

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contain 
N
N, length of array 
a
r
r
arr.
The second line consist of the array 
a
r
r
arr.
Output Format
For each test case, output on a new line the number of divisible pairs.

Constraints
1≤T≤100
2≤N≤10^5
0≤arr[i]≤10^5
 
Sample 1:
3  
4
6 1 2 3
6
2 2 1 7 5 3
2
4 8

output
2
7
1
Explanation:
Test Case 1: There are only two pairs formed- (6,2) and (1,3).
Test case 2: These are the 7 pairs that are formed- (2,2), (1,7), (1,5), (1,3), (7,5), (7,3), (5,3).
Test case 3: There is only one pair that is formed- (4,8).
'''
t= int(input())
while t>0:
    arr = list(map(int, input().split()))
    even, odd = 0, 0

    for num in arr:
        if num % 2 ==0:
            even += 1
        else:
            odd += 1

    even_pairs = (even * (even -1)) // 2
    odd_pairs = (odd * (odd -1)) // 2

    print(even_pairs + odd_pairs)
    break
