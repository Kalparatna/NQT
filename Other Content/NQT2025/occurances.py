from collections import Counter

s = input("Enter a string: ")

if not s:
    print("Invalid Input")
else:
    l = []  
    char_count_dict = Counter(s) 
    print(char_count_dict)

    first_non_repeating_char =  0
    Most_repeated_char_count = 0

    for char in s:
        if char_count_dict[char] == 1:
            first_non_repeating_char = char
            break

    Most_repeated_char = max(char_count_dict, key = char_count_dict.get)
    Most_repeated_char_count = char_count_dict[Most_repeated_char]

    if first_non_repeating_char:
        print("First Non reapteating char", first_non_repeating_char)
    else:
        for char in s:
            if char_count_dict[char]> 1:
                print("None")
                break
    print("Most Repeated Char", Most_repeated_char, "(", Most_repeated_char_count,")")

    
        







