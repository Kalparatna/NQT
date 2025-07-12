'''
Problem Statement:-

Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number 
greater than b by interchanging the digits of a and if not possible print -1.

Input Format
2 numbers a and b, separated by space.
Output Format
A single number greater than b.
If not possible, print -1

Constraints
1 <= a,b <= 10000000

Example 1:

Sample Input:

    459 500

Sample Output:
    549

Example 2:

Sample Input:

    645757 457765

Sample Output:
    465577

'''
from itertools import permutations

a, b = map(int, input().split())

p = list(permutations(str(a)))

array = ["".join(perm) for perm in p]

sorted_arr = sorted(array)
for i in sorted_arr:
    if int(i) > b:
        print(i)
        break
    
#or 

def generate_permutations(chars, index, result, b):
    if index == len(chars):
        num = int("".join(chars))
        if num > b:
            result.append(num)
        return

    used = set()
    for i in range(index, len(chars)):
        if chars[i] in used:
            continue
        used.add(chars[i])
        chars[i], chars[index] = chars[index], chars[i]
        generate_permutations(chars[:], index + 1, result, b)

def find_next_larger(a, b):
    chars = list(str(a))
    chars.sort()
    result = []
    generate_permutations(chars, 0, result, b)
    return min(result) if result else -1

# Input
a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)

# Output
print(find_next_larger(a, b))
