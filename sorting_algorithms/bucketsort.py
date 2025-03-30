# aplication of bucketsort algorithm in python,

def selection_sort(T):

    n = len(T)

    for i in range(n):

        for j in range(i, n):

            if T[j] < T[i]:

                T[i], T[j] = T[j], T[i]

    return


def bucket_sort(T):

    n = len(T)
    M = max(T)

    buckets = [[] for _ in range(n)]

    for i in range(n):

        ind = int(T[i]/M*(n-1))
        buckets[ind].append(T[i])

    sorted_T = []

    for i in range(n):

        selection_sort(buckets[i])

        sorted_T.extend(buckets[i])

    return sorted_T
