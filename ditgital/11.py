'''

write a program to merge to sorted arrays
'''

def merge(arr1, arr2):
    merged = []
    i, j , k = 0, 0 , 0
    merged = [0] * (len(arr1) + len(arr2))

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        merged[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        merged[k] = arr2[j]
        j += 1
        k += 1
    return merged
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(merge(arr1, arr2))
