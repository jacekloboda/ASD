#aplication of mergesort for linkedlists

class Node:

    def __init__(self, val):

        self.next = None
        self.val = val

def merge_sort(p):

    def merge(p,q): #laczy dwie posortowane linked listy zaczynajace sie od Nodow p i q w jedna posortowana, zwraca pierwszy element posortowanej linked listy

        s = Node(None) #sentinel
        s.next = p
        t = s #tail

        while p != None and q != None:

            if p.val < q.val:

                t.next = p
                t = t.next
                p = p.next

            else: #p.val >= q.val

                t.next = q
                t = t.next
                q = q.next

        if p != None:

            t.next = p
            t = t.next
            p = p.next

        if q != None:

            t.next = q
            t = t.next
            q = q.next

        return s.next

    def cut(p): #wycina z poczatku linked listy najwiekszy posortowany prefix, zwraca pierwszy element linked listy po usunieciu z niej prefixu
        
        t = p #tail

        while t.next != None and t.next.val >= t.val:
            
            t = t.next

        new_p = t.next
        t.next = None
        return new_p

    s = Node(None) #sentinel
    s.next = p

    rest = cut(p)

    while rest != None:
 
        q = rest
        rest = cut(q)

        p = merge(p,q)

    return p



#funkcje do testowania algorytmu sortujacego

def to_llist(T):

    n = len(T)
    s = Node(None) #sentinel
    t = s #tail

    for i in range(n):

        t.next = Node(T[i])
        t = t.next

    return s.next


def print_llist(p):

    while p != None:

        print(p.val,end=" ")
        p = p.next

    return



