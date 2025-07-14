'''
Identify row with maximum 1s

input
2

3 4
0 0 1 0        
0 1 1 0     #1st row having max 1s
0 1 0 0

2 2
1 1          #0th row having max 1s
0 1

2 1          #no row have 1s
0
0

Output:
1
0
-1


'''
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    matrix = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    max_ones = 0
    row_index = -1

    for i in range(n):
        ones = matrix[i].count(1)
        if ones > max_ones:
            max_ones = ones
            row_index= i

    if max_ones == 0:
        print(-1)
    else:
        print(row_index)
