'''
The number of permutations in which N people can occupy R seats (where R≤N) is given by the permutation formula:
permutaions(N, R) = N!//(N-R)!
'''

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

def permutation(N, R):
    if R > N:
        return 0
    else:
        perm = factorial(N) // factorial(N-R)
        return perm

N = int(input())
R = int(input())
print(permutation(N, R))
