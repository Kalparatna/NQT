#List Comprehension

l1 = [2, 3, 5, 7, 5, 9, 8 ]
#l2 = (i for i in l1 if i != 5)
#l2= (i % 2 == 0 if i % 2 == 0  else i *2 for i in l1)
l2 = [i if i % 2 == 0 else i * 2 for i in l1]
print(l2)

