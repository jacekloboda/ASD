#Jacek Loboda
#funkcja strong_string zwraca ilosc wystapien lidera w liscie T, jesli jakis element w T jest odwrotny do innego to uznaje je za rowne sobie. funkcja zamienia kazdy element tablicy na odwrotny jesli odwrotny jest mniejszy leksykograficznie nastepnie hashuje wszytskie elementy tablicy, potem przy urzyciu sortowania mergesort uklada zhashowane elementy rosnaco, na koniec przechodzi przez cala tablice i szuka najwiekszej liczby wystopien jednego elementu i ja zwraca, zlozonosc czasowa: O(N+nlogn), zlozonosc pamieciowa: O(N) [gdzie n to rozmiar T a N to suma znakow w wszytskich elementow w T]

def strong_string(T):

    def s_to_hash(s):

        n = len(s)
        ans = 0
        w = 1 #waga znakow w s
        mult = 31 # baza wagi
        mod = 786433 #zakres hashowania

        for i in range(n):

            ans = (ans + ord(s[i]) * w) % mod
            w = (w*mult) % mod

        return ans
    #end def

    def merge_sort(T, n):

        B = [0 for _ in range(n)]

        def divide(T, n, l, r):

            if l == r: return

            m = (l+r)//2

            divide(T,n,l,m)
            divide(T,n,m+1,r)

            merge(T,n,l,r)
        #end def

        def merge(T,n,l,r):

            nonlocal B
            B[l:r+1] = T[l:r+1]
            mid = (l+r)//2
            a = l
            b = mid+1
            i = l

            while a <= mid and b <= r:

                if B[a] < B[b]:
            
                    T[i] = B[a]
                    a+=1

                else:

                    T[i] = B[b]
                    b+=1

                i+=1

            while a <= mid:

                T[i] = B[a]
                i+=1
                a+=1

            while b <= r:

                T[i] = B[b]
                i+=1
                b+=1
    
            return
        #end def

        divide(T,n,0,n-1)           
    #end def

    def find_leader(T,n):

        max_ = 1
        curr = 1
        last = T[0]


        for i in range(1,n):

            if T[i] != last:
  
                curr = 1
                last = T[i]

            else:

                curr += 1

            max_ = max(max_,curr)

        return max_
    #end def
        

    n = len(T)
   
    for i in range(n):
        
        T[i] = s_to_hash(min(T[i],T[i][::-1]))
    
    merge_sort(T,n)

    return find_leader(T,n)
    return -1
#end def


