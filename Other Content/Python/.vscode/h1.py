# Q. Perfrom list operations by taking command as user input

# Initialize an empty list
list = []

# Read the number of commands
n = int(input())

# Process each command
for _ in range(n):
    command = input().split()  # Read the command as a list of words

    # Check the command type and perform the corresponding operation
    if command[0] == "insert":
        x, y = map(int, command[1:])  # x for index position and y for index value
        list.insert(x, y)
    elif command[0] == "print":
        print(list)
    elif command[0] == "remove":
        y = int(command[1])
        list.remove(y)
    elif command[0] == "append":
        y = int(command[1])
        list.append(y)
    elif command[0] == "sort":
        list.sort()
    elif command[0] == "pop":
        list.pop()
    elif command[0] == "reverse":
        list.reverse()
