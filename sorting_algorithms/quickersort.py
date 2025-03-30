# quicker_sort algorithm implementaion
# works quicker when there are many identical values ex. T=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3], time complex: O(loglogn),

def quicker_sort(T):

    def median(ia, ib, ic):

        a = T[ia]
        b = T[ib]
        c = T[ic]

        if a <= b <= c or c <= b <= a:
            return ib

        if b <= a <= c or c <= a <= b:
            return ia

        if a <= c <= b or b <= c <= a:
            return ic

        return

    def partiton_lomuto(T, l, r):

        ipivot = median(l, (l+r)//2, r)
        # ipivot = (l+r)//2
        T[ipivot], T[r] = T[r], T[ipivot]
        i = l-1

        for j in range(l, r):

            if T[j] < T[r]:

                i += 1
                T[j], T[i], = T[i], T[j]

        i += 1
        T[r], T[i] = T[i], T[r]
        return i

    def sort(T, l, r):

        if l > r:
            return

        p = partiton_lomuto(T, l, r)
        sort(T, l, p-1)
        i = p+1
        while i <= r and T[i] == T[p]:
            i += 1

        sort(T, i, r)

        return

    n = len(T)
    sort(T, 0, n-1)

    return


T = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 3, 3]
quicker_sort(T)
print(T)
