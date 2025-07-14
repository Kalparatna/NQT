#enumerate:enumerate is a built-in function in Python that is used to iterate over a sequence 
# (such as a list, tuple, or string) while keeping track of the index or position 
# of the current item. It returns a tuple containing 
# the index and the value of each item in the sequence.

#

L = ['a','b','c','d', 'e']

for i, letter in enumerate(L):
    print(f'{i}:{letter}')