# checks if graph is bipartite using bfs algorithm

from collections import deque


def is_bipartite(G):

    n = len(G)
    # color of every node -1 if not colored yet, it also checks if node vas visited
    col = [0]*n
    q = deque()

    q.append(0)
    col[0] = 1

    while len(q) > 0:

        u = q.popleft()

        c = 1 if col[u] == 0 else 2  # color of nodes connected to u

        for v in G[u]:

            if col[u] == 0:

                col[u] = c

            elif col[u] == col[v]:  # col[u] != 0 and col[u] == vol[v]

                return False

        return True  # it was posibble to color whole graph with 2 colors
