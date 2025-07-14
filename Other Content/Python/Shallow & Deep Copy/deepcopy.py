import copy

# Original list
original_list = [8, [2, [5, 6], 3], 4]

# Deep copy of the original list
deep_copied_list = copy.deepcopy(original_list)

# Modifying the deep copy
deep_copied_list[0] = 'A'  # Change the first element of the copied list to 'A'
deep_copied_list[1][0] = 'B'  # Change the first element of the nested list to 'B'
deep_copied_list[1][1][0] = 'C'  # Change the first element of the innermost nested list to 'C'

# Displaying the original and deep copied lists after the first modifications
print("After the first modifications:")
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

print("\n")

# Modifying the deep copy again
deep_copied_list[0] = 'A'  # Change the first element of the copied list to 'A'
deep_copied_list[1][0] = 'B'  # Change the first element of the nested list to 'B'
deep_copied_list[1][1][0] = 'C'  # Change the first element of the innermost nested list to 'C'

# Displaying the original and deep copied lists after the second modifications
print("After the second modifications:")
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)
