#swap
a , b = 4, 5
#1
a = a + b
b = a - b
a = a -  b

print(a, b)

#2 
c , d = 4, 5

temp =  c
c = d
d = temp

print(c, d)

#3
e,f = 4, 5
f, e = 4, 5
print(e, f)

#4
g, h =4, 5

g = g ^ h
h = g ^ h
g = g ^ h

print(g, h)

#5
i, j = 4, 5

i  = i * j
j = i // j
i = i // j

print(i, j)