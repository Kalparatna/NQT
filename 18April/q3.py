'''
Shift -2 
Question 2: 2D Array Row Order Based on Even/Odd Row Index
Problem Statement:
Given a 2D array with m rows and n columns, print the elements of the array such that:

Rows with even indices (0, 2, 4, ... ) are printed in the same order.
Rows with odd indices (1, 3, 5, ... ) are printed in reverse order.
Input Format:

First line: Two integers m and n
Next m lines: Each contains n integers

Test Case 1:
Input:

4 4

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:

1 2 3 4
8 7 6 5
9 10 11 12
16 15 14 13

Test Case 2:
Input:

3 5
10 20 30 40 50
60 70 80 90 100
110 120 130 140 150

Output:

10 20 30 40 50
100 90 80 70 60
110 120 130 140 150

'''

def rev(arr):
    return arr[::-1]

T = int(input())
for i in range(T):
    m, n = map(int, input().split())
    matrix = []

    for row in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    for row in range(m):
        if row % 2 == 0:
            print(*matrix[row])
            
        else:
            print(*rev(matrix[row]))

#or

T = int(input())
for i in range(T):
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    for ind in range(rows):
        if ind % 2 == 0:
            print(*matrix[ind])
        else:
            print(*matrix[ind][:: -1])


