'''
Vehicle Manufacturing
You are tasked with determining the number of two-wheelers and four-wheelers that need to be manufactured based on the given total number of vehicles and the total number of wheels.

You are provided with two integers:

v: the total number of vehicles (both two-wheelers and four-wheelers).
w: the total number of wheels for all the vehicles combined.
Your task is to calculate and print how many two-wheelers and four-wheelers must be manufactured based on the input data. If it's not possible to manufacture such a combination, print 
−
1
−1.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line contains an integer 
v
v — the total number of vehicles.
The second line contains an integer 
w
w — the total number of wheels.
Output Format
For each test case,

If a valid combination of two-wheelers and four-wheelers exists, print two integers:
The number of two-wheelers, the number of four-wheelers.
If no valid combination is possible, print -1.


INPUT:

2
12 
34
10 
25

OUTPUT:

7 5           (7 Two wheeler & 5 Four Wheeler)
-1           (not Combination)

'''

T = int(input())
for _ in range(T):
    v= int(input())
    w = int(input())

    if w % 2 != 0 or w < 2 * v or w > 4 * v:
        print(-1)
    else:
        y = (w - (v * 2)) // 2     
        x= v - y 
        print(x, y)                                              
    


# x + y = v        (1)  # total vehicles
# 2x + 4y = w      (2)  # total wheels


# 2*(v - y) + 4y = w
# => 2v - 2y + 4y = w
# => 2v + 2y = w
# y = (w * ( 2v)) / 2
