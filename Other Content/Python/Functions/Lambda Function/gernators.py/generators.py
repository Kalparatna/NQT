def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
x = fib(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))