def fibonacci_series(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_series(number -1) + fibonacci_series(number -2)
    
number = int(input())

for i in range(0, number):
    print(fibonacci_series(i))

