#implementation of heapsort

def heap_sort(T):

    def left(i):

        return (i+1)*2-1

    def right(i):

        return (i+1)*2

    def parent(i):

        return (i-1)//2

    def heapify(T, n, i):

        max_ind = i
        l = left(i)
        r = right(i)

        if l < n and T[l] > T[max_ind]:

            max_ind = l

        if r < n and T[r] > T[max_ind]:

            max_ind = r

        if i != max_ind:

            T[i], T[max_ind] = T[max_ind], T[i]
            heapify(T, n, max_ind)
            return

        return

    def build_heap(T, n):

        end = parent(T[n-1])

        for i in range(end, -1, -1):

            heapify(T, n, i)

        return

    n = len(T)

    build_heap(T, n)

    for i in range(n-1, -1, -1):
        
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)

    return

T = [1,2,3,4,5,6,7]

heap_sort(T)
print(T)
