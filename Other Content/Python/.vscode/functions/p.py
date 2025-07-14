def make_adder(x):
    def adder(y):
        return x + y
    return adder

add4 = make_adder(4)
add6 = make_adder(6)

print(add4(3))
print(add6(5))