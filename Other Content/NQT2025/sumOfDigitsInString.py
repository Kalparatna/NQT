'''
Calcualte the sum of digits in string

example
input:
qew45frrsf54

output:
18
'''

s = input()

res = 0
for i in range(len(s)):
    if s[i].isdigit():
        res += int(s[i])

print(res)

#OR

s = input()

res = 0  
for c in s:
    if '0' <= c <= '9':  
        res += ord(c) - ord('0')  

print(res)
