'''
Find Uniques Charecter in string

ex
input:

"qerer"

output:
q

'''

arr = input()

for i in range(len(arr)):
    if arr.count(arr[i]) == 1:
        print(arr[i])
        break

#Or

arr = input()
unique = 0

for char in arr:
    unique ^= ord(char)  

print(chr(unique))  

#Or

arr = input()

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    
    if count == 1:
        print(arr[i])

#OR

from collections import Counter

arr = input()
freq = Counter(arr)  

for char in arr: 
    if freq[char] == 1:  
        print(char)
        break  