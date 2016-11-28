#Bubble sort

bb_vec = [10, 8, 6, 4]
dif = [10, 3, 8, 1]
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
#print(bubble(dif, 0))

    #order = 0 if ascending order and 1 if descending order is wanted.

#Quick sort
def qsort (vec, bottom, top):
    if bottom < top:
        qpiv = part(vec, bottom, top)
        qsort(vec, bottom, qpiv -1)
        qsort(vec, qpiv+1, top)
    return(vec)

def part (vec, bottom, top):
    pivot = top
    x = bottom

    for i in range(bottom, top):
        if vec[i] < vec[pivot]:
            vec[i], vec[x] = vec[x], vec[i]
            x+=1

    vec[pivot], vec[x] = vec[x], vec[pivot]

    return(x)
c=[9, 4, 82, 19]
q = [1, 0, 2,3,4,6,5,8,7]
print(qsort(bb_vec, 0, len(bb_vec)-1))
#arguments must include the list of numbers, 0 (starting point), and the length of the
#   list being sorted.
