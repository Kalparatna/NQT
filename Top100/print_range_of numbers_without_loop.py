def print_nums(n, Upto):
    if n<= Upto:
        print(n)
        print_nums(n+1, Upto)
        
start = int(input())
Upto = int(input())

print_nums(start, Upto)

#or

list(map(print, range(1, 10+1)))