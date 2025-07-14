'''
Count Character Occurrences
You are given two strings, str1 and str2. Your mission is to calculate the total number of occurrences of each unique character of str2 within the string str1. The task is to find the sum of occurrences of all unique characters from str2 in str1 and return this total count.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
For each test case:
The first line contains the string str1.
The second line contains the string str2.
Output Format
For each test case, output the total sum of occurrences of characters in str2 found in str1 on a new line.

Sample 1:

3
helloworld
do
abacabadabacaba
abcd
abc 
abcdabcdabcdabcd


Output
3
15
3


Explanation:
Test Case 1: the character 'd' appears once and 'o' appears twice in "helloworld", so the total count is 3.
Test Case 2: The characters from "abcd" appear as follows in "abacabadabacaba": 'a': 7 occurrences 'b': 4 occurrences 'c': 2 occurrences 'd': 2 occurrences Total = 7 + 4 + 2 + 2 = 15.
Test Case 3: The characters appear only once in abc as we are calculating the unique characters of abcdabcdabcdabcd.

'''

from collections import Counter

def sum_of_occurrences(str1, str2):
    freq = Counter(str1) 
    total = 0
    for ch in set(str2): 
        total += freq.get(ch, 0) 
    return total

t = int(input()) 
for _ in range(t):
    str1 = input().strip()
    str2 = input().strip()
    print(sum_of_occurrences(str1, str2))
