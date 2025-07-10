def sort_by_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    def sorting_criteria(x):
        return (-freq[x], x)

    arr.sort(key=sorting_criteria)  
    return arr

arr = list(map(int, input().split()))
print(sort_by_frequency(arr))
