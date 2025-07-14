'''
Convert number to words
You are tasked with creating a program that converts a given integer (up to 4 digits) into its corresponding English words.

Input Format
First line of input contains a single integer 
T
T, the number of test cases.
Each test case consists of a single line containing a number N.
Output Format
For each test case, output the number in words, following the English naming conventions. 
Each number should be converted to its corresponding words in lowercase, with words separated by a single space.

Constraints

1≤T≤100
0≤N≤9999

INPUT: 

2

7824
378

OUTPUT:

seven thousand eight hundred twenty four
three hundred seventy eight

Explanation:
Test Case 1: The number 7824 is broken down as follows: 7 in thousands place = "seven thousand" 8 in hundreds place = "eight hundred" 2 
in tens place = "twenty" 4 in units place = "four"
Test Case 2: The number 370 is represented as: 3 in hundreds place = "three hundred" 7 in tens place = "seventy" 8 in units place = "eight"

'''

T = int(input())

for i in range(T):
    n = int(input())

    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    words = []

    if n == 0:
        print("Zero")
        continue

    if n >= 1000:
        words.append(ones[n//1000])
        words.append("thausand")
        n %= 1000
    
    if n >= 100:
        words.append(ones[n//100])
        words.append("hundred")
        n %= 100

    if n >= 20:
        words.append(tens[n // 10])
        n %= 10
    
    if 0< n <= 20:
        words.append(ones[n])

    print(" ".join(words))
