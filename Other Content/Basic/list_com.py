
#List comprehension is a short and simple way to create a new list by applying an expression to each item in an existing iterable
l = [ 23, 13, 2, 5, 2]
greter = [i for i in l if i > 10]
print(greter)

names = ["sunny", "Amit", "Arun", "is", "harrry"]
required = [name for name in names if len(name) > 4]
print(required)

matrix = [[1,2, 3], [4, 5 , 6], [7, 8, 9]]
simple = [element for row in matrix for element in row]
print(simple) 