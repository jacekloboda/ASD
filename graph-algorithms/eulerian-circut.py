# algorithm finds eulerian cycle in graph using dfs algorithm and returns it

from typing import ValuesView


def dfs(G):

    n = len(G)
    V = [False for _ in range(n)]
    C = []  # list of cycles in G
    flag = False

    # list of used ststaus for every edge in G
    U = [[False for _ in range(n)] for _ in range(n)]

    E_cnt = [len(G[u]) for u in range(n)]
    U_cnt = [0 for u in range(n)]

    for u in range(n):

        for v in G[u]:

            U[u][v] = False

    def dfs_visit(G, u, s):

        nonlocal V
        nonlocal C
        nonlocal flag

        C[-1].append(u)

        if len(C[-1]) > 1 and u == s:

            flag = True
            return

        for v in G[u]:

            if flag:
                return

            if not V[v] and not U[u][v]:

                print(u, v, G[u], end=" ")

                U[u][v] = True
                U[v][u] = True
                U_cnt[u] += 1
                U_cnt[v] += 1

                print(G[u], flag)

                if U_cnt[u] == E_cnt[u]:
                    V[u] = True

                dfs_visit(G, v, s)

        return

    for u in range(n):

        if not V[u]:

            flag = False
            print("new cycle")
            C.append([])
            dfs_visit(G, u, u)

    print(C)

    for cycle in C:
        pass

    return


def new_dfs(G):

    n = len(G)
    V = [False for _ in range(n)]
    P = []  # current path
    ind = 0  # current index in path

    def DFSvisit(G, u, ind):

        nonlocal P

        V[u] = True

        P.insert(ind, u)
        ind += 1

        for v in G[u]:

            if not V[v]:

                DFSvisit(G, v, ind)

    DFSvisit(G, 0, ind)

    return P


G = [
    [1, 2],  # stopień 2
    [0, 2],  # stopień 2
    [0, 1, 3, 4],  # stopień 4
    [2, 4],  # stopień 2
    [2, 3],   # stopień 2
]

G1 = [[1, 2],
      [0, 2, 3, 4],
      [0, 1],
      [1, 4],
      [1, 3]]

G3 = {
    0: {1, 2},
    1: {0, 2},
    2: {0, 1, 3},
    3: {2, 4, 5},
    4: {3, 5},
    5: {3, 4}
}

print(dfs(G))
