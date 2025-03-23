def quick_sort(T):

    def partition_lomuto(T, l, r):

        x = T[r]  # pivot
        i = l-1

        for j in range(l, r):

            if T[j] < x:

                i += 1
                T[j], T[i] = T[i], T[j]

        T[r], T[i+1] = T[i+1], T[r]
        return i+1

    def partition_hoar(T, l, r):

        x = T[r]  # pivot
        i = l
        j = r

        while True:

            while T[i] < x:

                i += 1

            while T[j] > x:

                j -= 1

            if i >= j:

                return j

            T[i], T[j] = T[j], T[i]

    def sort(T, l, r):

        if l < r:

            # p = partition_lomuto(T, l, r)
            p = partition_hoar(T, l, r)
            sort(T, l, p-1)
            sort(T, p+1, r)

        return

    n = len(T)
    sort(T, 0, n-1)

    return


T = [9, 3, 6, 2, 5, 7, 1, 4, 8]
quick_sort(T)
print(T)
