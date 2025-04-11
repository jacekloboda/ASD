# find eulerian circuit
# using bool list of visited status for edges, and dfs algorithm
# time complexity: O(E+V)

def dfs(G):

    eulerian_circuit = []
    n = len(G)
    T = [[] for _ in range(n)]  # copy of G list but with better order
    ind = 0

    for u in range(n):  # filling T list

        for v in G[u]:

            if u < v:

                # adding indexes to E list, for O(1) checking if edge was visited
                T[u].append((v, ind))
                T[v].append((u, ind))
                ind += 1

    # list of visited status for edges, edge u->v and v->u have the same index
    E = [False]*ind

    def dfs_visit(G, E, u):

        nonlocal eulerian_circuit

        print(u)

        for v, ind in G[u]:

            if not E[ind]:

                E[ind] = True
                dfs_visit(G, E, v)

        eulerian_circuit.append(u)

    dfs_visit(T, E, 0)

    return eulerian_circuit


G = [[1, 2],
     [0, 2, 3, 4],
     [0, 1],
     [1, 4],
     [1, 3]]

G1 = [
    [1, 2, 3, 5],    # 0 → 1, 2, 3, 5
    [0, 2, 4, 5],    # 1 → 0, 2, 4, 5
    [0, 1, 3, 4],    # 2 → 0, 1, 3, 4
    [0, 2, 4, 5],    # 3 → 0, 2, 4, 5
    [1, 2, 3, 5],    # 4 → 1, 2, 3, 5
    [0, 1, 3, 4]     # 5 → 0, 1, 3, 4
]

print(dfs(G))
