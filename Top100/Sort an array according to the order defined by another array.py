# Sort an array according to the order defined by another array

def sorted_by_order(arr1, arr2):
    fre_map = {}
    result = []

    for num in arr1:
        fre_map[num] = fre_map.get(num, 0) + 1

    for num in arr2:
        if num in fre_map:
            result.extend([num] * fre_map[num])
            del fre_map[num]

    remaining = []

    for num in fre_map:
        remaining.extend([num] * fre_map[num])


    result.extend(sorted(remaining))

    return result

arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

print(sorted_by_order(arr1, arr2))