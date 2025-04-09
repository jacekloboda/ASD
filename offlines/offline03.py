# Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
# zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
# z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algo-
# rytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową

# Algorytm należy zaimplementować jako funkcję która przyjmuje graf G oraz numery wierzchołków
# s, t i zwraca dowolną krawędź spełniającą warunki zadania, lub None jeśli takiej krawędzi w G nie ma.
# Graf przekazywany jest jako lista list sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i.
# Wierzchołki numerowane są od 0. Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków
# pomiędzy którymi jest krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma.
# Jeśli w grafie oryginalnie nie było ścieżki z s do t to funkcja powinna zwrócić None.


from collections import deque


def bfs(G, s):

    q = deque()
    V = [False for _ in range(len(G))]
    D = [float('inf') for _ in range(len(G))]  # distance from s

    q.append(s)
    D[s] = 0
    V[s] = True

    while len(q) > 0:

        u = q.popleft()

        for v in G[u]:

            if not V[v]:

                V[v] = True
                q.append(v)
                D[v] = D[u]+1

    return D


def longer(G, s, t):

    n = len(G)

    dist_s = bfs(G, s)
    dist_t = bfs(G, t)

    shortest = dist_s[t]  # length of fastest route from s to t

    for u in range(n):

        for v in G[u]:

            if v <= u:
                continue

            if (dist_s[u] + dist_t[v] + 1 == shortest) or (dist_s[v] + dist_t[u] + 1 == shortest):

                if (dist_s[u] != dist_s[v]) and (dist_t[u] != dist_t[v]):

                    return (u, v)

    return None


G = [[1, 2],
     [0, 2],
     [0, 1]]

s = 0
t = 2

print(longer(G, s, t))
