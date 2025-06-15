def is_palindrome(num):
    strnum = str(num)
    return strnum == strnum[: : -1]

num = int(input())
palindromes = []
for i in range(num):
    if is_palindrome(i):
        palindromes.append(i)

print(*palindromes)