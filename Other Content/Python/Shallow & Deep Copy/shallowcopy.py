import copy

# Original list
original_list = [8, [2, [5, 6], 3], 4]

# Shallow copy of the original list
shallow_copied_list = copy.copy(original_list)

# Modifying the shallow copy
shallow_copied_list[0] = 'A'  # Change the first element of the copied list to 'A'
shallow_copied_list[1][0] = 'B'  # Change the first element of the nested list to 'B'
shallow_copied_list[1][1][0] = 'C'  # Change the first element of the innermost nested list to 'C'

# Displaying the original and shallow copied lists after the first modifications
print("After the first modifications:")
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

print("\n")

# Modifying the shallow copy again
shallow_copied_list[0] = 'A'  # Change the first element of the copied list to 'A'
shallow_copied_list[1][0] = 'B'  # Change the first element of the nested list to 'B'
shallow_copied_list[1][1][0] = 'C'  # Change the first element of the innermost nested list to 'C'

# Displaying the original and shallow copied lists after the second modifications
print("After the second modifications:")
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
