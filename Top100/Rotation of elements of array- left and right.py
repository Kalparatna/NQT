def left_rotate(arr, n):
    return arr[n:] + arr[:n]

def right_rotate(arr, n):
    return arr[-n:] + arr[:-n]

array = [1, 2, 3, 4, 5]
left_rotated = left_rotate(array, 2)  
right_rotated = right_rotate(array, 2) 
print("Left Rotated:", left_rotated)
print("Right Rotated:", right_rotated)
