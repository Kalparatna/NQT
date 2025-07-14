# combination function

import itertools

itmes = [1,2,3,4]
comb = itertools.combinations(itmes, 2)
print(list(comb))
#or
for com in comb:
    print(com)