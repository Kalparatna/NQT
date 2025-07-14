'''
Good Number
You are given a number 
N
N, and your task is to determine whether it is a "Good Number" or not. A Good Number is defined as a number that is divisible by the sum of its own digits. If the number is divisible by the sum of its digits, it is classified as Good, otherwise, it is classified as Bad.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case contains a single integer 
N
N, the number you need to check.
Output Format
For each test case, print "Good Number" if the number is a Good, otherwise print "Bad Number".

Input
3   (No of Test Cases)
18
19
21

Output:
Good Number
Bad Number
Good Number
'''

T = int(input())

for _ in range(T):  
    n = int(input())

    sum_n = sum(int(digit) for digit in str(n))  

    if n % sum_n == 0:
        print("Good Number")
    else:
        print("Bad Number")
