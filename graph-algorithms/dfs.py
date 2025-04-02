# implementation of deep first search algorithm in python using recursion
def dfs(G, s):  # G is list of links in graph, s is starting node

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
