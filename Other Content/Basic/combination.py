

def combinations(items, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])  # copy the current combination
            return
        for i in range(start, len(items)):
            path.append(items[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

items = [1, 2, 3, 4]
combs = combinations(items, 2)
print(combs)


# combination function

import itertools

itmes = [1,2,3,4]
comb = itertools.combinations(itmes, 2)
print(list(comb))
#or
for com in comb:
    print(com)

#Or
