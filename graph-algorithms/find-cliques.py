# finds and returns two cliques in a graph composed of two disjoint cliques
# algorithm finds the cliques by coloring completion of G in 2 colors
# at the end it adds uncolored nodes to every clique

def bipartite(G):  # returns list of colors for every node in G

    from collections import deque

    n = len(G)
    # color of every node (1 or -1), 0 if not visited yet
    C = [0 for _ in range(n)]
    q = deque()
    q.append(0)
    C[0] = 1

    while q:

        u = q.popleft()

        for v in G[u]:

            if not C[v]:

                C[v] = -(C[u])
                q.append(v)

    return C


def completion(G):  # returns neighborhood list for completion of G

    n = len(G)
    C = [[] for _ in range(n)]

    for u in range(n):

        for v in range(n):

            flag = False  # true if v is neighbor of u in G, false if not

            for neighbor in G[u]:

                if neighbor == v:
                    flag = True

            if not flag:

                C[u].append(v)

    return C


def clique(G):  # divides G to two cliques

    n = len(G)
    Comp = completion(G)
    Col = bipartite(Comp)

    Clique1 = []
    Clique2 = []

    for u in range(n):

        if Col[u] == 0:

            Clique1.append(u)
            Clique2.append(u)

        else:
            Clique1.append(u) if Col[u] == 1 else Clique2.append(u)

    return Clique1, Clique2


G = [[1, 2, 3],
     [0, 2, 3],
     [0, 1, 3],
     [0, 1, 2, 4, 5],
     [3, 5],
     [3, 4]
     ]

G1 = [[1, 2, 3],
      [0, 2, 3],
      [0, 1, 3, 4],
      [0, 1, 2, 4],
      [2, 3]
      ]

print(clique(G1))
