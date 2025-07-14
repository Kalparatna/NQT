# Original list
list1 = [1, 2, 3]

list2 = [4, 5, 6]

# list1.append(list2)  X

# for element in list2:
#     list1.append(element)

#or

list1.extend(list2)

print(list1)  # Output: [1, 2, 3, 4, 5, 6]
