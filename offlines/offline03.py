# algorytm zwraca krawedz w grafie ktorej usuniecie wydluzy najkrotsza sciezke z s do t (usuniecia jedynego polaczenia to tez wydluzenie)
#
# dzialanie: uzywajac algorytmu bfs sprawdzam ktore krawedzie w G naleza do najkrotszych sciezek, za pomoca dfs szukam mostu w grafie zlozonym z najkrotszych sciezek i go zwracam
#
# zlozonosc czasowa: O(E+V)

def bfs(G, s):

    from collections import deque

    n = len(G)
    q = deque()
    V = [False] * n  # visited status
    D = [float('inf')] * n  # distance from s

    q.append(s)
    V[s] = True
    D[s] = 0

    while q:  # q not empty

        u = q.popleft()

        for v in G[u]:

            if not V[v]:

                V[v] = True
                D[v] = D[u]+1
                q.append(v)

    return D


def find_bridge(G, in_Paths):

    n = len(G)
    V = [False] * n  # visited status
    T = [0] * n  # discovery time
    low = [0] * n  # for indentifying bridges
    Bridges = []
    time = 1

    def dfs_visit(u, parent):

        nonlocal time

        V[u] = True
        T[u] = time
        low[u] = time
        time += 1

        for v in G[u]:

            if not in_Paths[v]:
                continue

            if not V[v]:

                dfs_visit(v, u)

                if low[v] > T[u]:

                    Bridges.append((u, v))

                low[u] = min(low[u], low[v])

            elif v != parent:

                low[u] = min(low[u], T[v])

    for u in range(n):

        if not in_Paths[u]:
            continue

        if not V[u]:

            dfs_visit(u, -1)

    return Bridges[0] if len(Bridges) > 0 else None


def longer(G, s, t):

    n = len(G)

    Dist_s = bfs(G, s)
    Dist_t = bfs(G, t)

    if Dist_t[s] == float('inf'):

        return None

    in_Paths = [False] * n

    for u in range(n):

        if Dist_s[u] + Dist_t[u] == Dist_t[s]:
            in_Paths[u] = True

    for u in range(n):

        if not in_Paths[u]:
            continue

    return find_bridge(G, in_Paths)
