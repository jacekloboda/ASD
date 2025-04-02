# aplication of breadth first search algorithm in python
from queue import Queue


def bfs(G, s):  # G is list edges, s is starting node

    n = len(G)
    q = Queue()
    V = [False for _ in range(n)]  # if node i is visited V[i]=True else Fasle
    # distance from i-node to s-node, -1 if there is no connection
    D = [-1 for _ in range(n)]

    V[s] = True
    D[s] = 0
    q.put(s)

    while (not q.empty()):

        u = q.get()

        for v in G[u]:

            if not V[v]:

                q.put(v)
                D[v] = D[u]+1
                V[v] = True

    return
