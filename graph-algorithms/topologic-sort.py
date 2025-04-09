# dfs algorithm returns list of nodes in graph sorted topologically

def dfs(G):

    n = len(G)
    V = [False for _ in range(n)]  # list with visited status of every node
    S = []  # list of sorted nodes

    def dfs_visit(G, u):

        nonlocal V
        nonlocal S

        V[u] = True

        for v in G[u]:

            if not V[v]:

                dfs_visit(G, v)

        S.append(u)

    for u in range(n):

        if not V[u]:

            dfs_visit(G, u)

    return S[::-1]


G = [
    [],
    [],
    [3],
    [1],
    [0, 1],
    [0, 2]
]

print(dfs(G))
