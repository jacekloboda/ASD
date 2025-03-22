#funkcja heap insert wstawia element do listy T ulozonej w kopiec tak aby lista dalej byla kopcem, time complex: O(logn)

def heap_insert(T,i):

    def left(i):
        return i*2+1

    def right(i):
        return i*2+2

    def parent(i):
        return (i-1)//2 

    def shift_up(T,i):

        while i > 0 and T[i] > T[parent(i)]:

            T[i], T[parent(i)] = T[parent(i)], T[i]
            i = parent(i)

        return

    n = len(T)
    T.append(i)

    shift_up(T,n)

    return
