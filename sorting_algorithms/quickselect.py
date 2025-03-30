# quick select aplication in python

def quick_select(T, k):

    def partition(T, l, r):  # partition lomuto

        mid = (l+r)//2
        if T[mid] < T[l]:
            T[mid], T[l] = T[l], T[mid]
        if T[r] < T[l]:
            T[r], T[l] = T[l], T[r]
        if T[mid] < T[r]:
            T[mid], T[r] = T[r], T[mid]

        i = l-1

        for j in range(l, r):

            if T[j] < T[r]:

                i += 1
                T[i], T[j] = T[j], T[i]

        i += 1
        T[i], T[r] = T[r], T[i]

        return i

    def select(T, l, r):

        if l == r:
            return T[k]

        p = partition(T, l, r)

        if p == k:
            return T[p]
        if p < k:
            return select(T, p+1, r)
        if p > k:
            return select(T, l, p-1)

        return select(T, 0, len(T)-1)
