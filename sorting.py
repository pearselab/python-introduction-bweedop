bb_vec = [8,2,4,10,6]

def bubble (dan, order):
    foo = len(dan) - 1
    bb_sort = False
    if order == 0:
        while not bb_sort:
            bb_sort = True
            for i in range(foo):
                if dan[i]>dan[i+1]:
                    bb_sort = False
                    dan[i], dan[i+1] = dan[i+1], dan[i]
        return(dan)
    if order == 1:
        while not bb_sort:
            bb_sort = True
            for i in range(foo):
                if dan[i]<dan[i+1]:
                    bb_sort = False
                    dan[i], dan[i+1] = dan[i+1], dan[i]
        return(dan)
print(bubble(bb_vec, 1))
#order = 0 if ascending order and 1 if descending order is wanted.
