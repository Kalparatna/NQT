#print(.5 + .5 == 1)
#print(.1 + .2 == .3)
#dec to bin
#float to bin
if __name__ == '__main__':
    N = int(input())
    list = [N]
    list.insert(0, 5)
    print(list)
    list.insert(1, 10)
    list.insert(2, 6)
    print(list)
    list.remove(5)
    list.append(3)
    list.sort()
    print(list)
    list.pop()
    list.reverse()
    print(list)
    