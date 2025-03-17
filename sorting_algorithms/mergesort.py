#implementation of mergesort

def merge_sort(T):

    def merge(T, l, r):

        nonlocal B
        B[l:r+1] = T[l:r+1]
        a = l
        mid = (l+r)//2
        b = mid+1
        i = l

        while a <= mid and b <= r:

            if B[a] < B[b]:

                T[i] = B[a]
                a+=1
                i+=1

            else: #B[a] >= B[b]

                T[i] = B[b]
                b+=1
                i+=1

        while a <= mid:

            T[i] = B[a]
            a+=1
            i+=1

        while b <= r:
            T[i] = B[b]
            b+=1
            i+=1

        return

    def divide(T, l, r):

        if l == r: return

        mid = (l+r)//2

        divide(T, l, mid)
        divide(T, mid+1, r)

        merge(T, l, r)

    n = len(T)
    B = [0 for _ in T]
    

    divide(T,0,n-1)

    return

