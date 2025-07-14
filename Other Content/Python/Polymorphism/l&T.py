def remove(s, x):
    result = ""
    for char in s:
        if char != x:
            result += char
    return result

s = input("Enter String: ")
x = input("Enter character to be removed: ")

output_string = remove(s, x)

print(output_string)
