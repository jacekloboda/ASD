# Jacek Loboda
# funkcja count_inveriosns zwraca liczbe inwersji w tablicy T robi to za pomoca algorytmu mergesort, podczas laczenia dwoch posortowanych tablic w mergesort gdy element z prawej tablicy jest mniejszy od tego z lewej to element z prawej jest w inwersji ze wszystkimi elementami ktore zostaly na lewej tablicy, zlozonosc czasowa: O(nlogn), zlozonosc pamieciowa: O(n)

def count_inversions(T):

    def merge(T, l, r):

        nonlocal cnt  # licznik inwersji
        nonlocal B
        B[l:r+1] = T[l:r+1]
        a = l  # iterator po lewej polowie scalanego B
        mid = (l+r)//2
        b = mid+1  # iterator po prawej polowie scalanego B
        i = l  # iterator po liscie T

        while a <= mid and b <= r:

            if B[a] <= B[b]:

                T[i] = B[a]
                a += 1
                i += 1

            else:  # B[a] > B[b]

                T[i] = B[b]
                b += 1
                i += 1
                # jesli B[a] > B[b] to znaczy ze wszytskie elementy ktore znajduja sie w B[a:mid+1] sa wieksze od B[b] wiec B[b] jest z nimi w inwersji
                cnt += (mid-a+1)

        while a <= mid:

            T[i] = B[a]
            a += 1
            i += 1

        while b <= r:

            T[i] = B[b]
            b += 1
            i += 1

        return

    def divide(T, l, r):

        if l == r:
            return

        mid = (l+r)//2

        divide(T, l, mid)
        divide(T, mid+1, r)

        merge(T, l, r)

        return

    n = len(T)
    B = [0 for _ in range(n)]
    cnt = 0  # licznik inwersji

    divide(T, 0, n-1)  # uruchamiam mergesort

    return cnt
