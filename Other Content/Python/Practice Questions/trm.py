# Print numbers from one to n then without using loop

def print_numbers(lst):
    if len(lst) > 0:
        print(lst[0])
        print_numbers(lst[1:])

N = int(input('No: '))
numbers = list(range(1, N+1))
print_numbers(numbers)
