# implementation of deep first search algorithm in python
from collections import deque  # using deque as a stack


def dfs_rec(G, s):  # dfs using recursion, G is list of links in graph, s is starting node
    n = len(G)
    # if n-node was visited then V[n] = True else False
    V = [False for _ in range(n)]

    def dfs_visit(G, V, u):

        V[u] = True

        for v in G[u]:

            if not V[v]:

                dfs_visit(G, V, v)
        return

    dfs_visit(G, V, s)

    return


def dfs_stack(G, s):  # dfs using stack, G is list of links, s is starting node

    n = len(G)
    V = [False for _ in range(n)]
    st = deque()

    st.append(s)
    V[s] = True

    while len(s) > 0:

        u = st.pop()

        for v in G[u]:

            if not V[v]:

                st.append(v)
                V[v] = True

    return
