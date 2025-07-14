'''
Longest Common Prefix
You are given a list of strings str. Your task is to find the longest common prefix among all the strings in the list. 
If there is no common prefix, return −1.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input:
The first line contains an integer N, the number of strings.
The next line contain a string array str.
Output Format
For each test case, output the longest common prefix. If there is no common prefix, output −1.

Constraints

All strings consist of lowercase alphabetical characters.

INPUT:
2
3
flower flow flight
2
dog racecar

OUTPUT: 
fl
-1

'''

T = int(input())

for i in range(T):
    n = int(input())
    str_list = list(map(str, input().split()))

    if not str_list:
        print("-1")
    
    prefix = str_list[0]

    for i in str_list[1:]:
        while not i.startswith(prefix):
            prefix  = prefix[: -1]

            if not prefix:
                break
    if prefix:
        print(prefix)
    else:
        print(-1)
    
