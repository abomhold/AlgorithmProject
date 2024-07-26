from graph import generate_points, Point, calculate_distance, calculations
from math import inf


max_node_count: int = 10
node_count: int
node_array: list[Point]


def christofides(distances):
    num_vertices = len(distances)

    # Step 1: Create a minimum spanning tree
    mst = prim_mst(distances)

    # Step 2: Find odd-degree vertices
    degree = [sum(1 for edge in mst if v in edge) for v in range(num_vertices)]
    odd_vertices = [v for v in range(num_vertices) if degree[v] % 2 == 1]

    # Step 3: Find minimum weight perfect matching
    matching = min_weight_matching(distances, odd_vertices)

    # Step 4: Combine MST and matching
    combined_graph = mst + matching

    # Step 5: Find Eulerian circuit
    eulerian_circuit = find_path(combined_graph)

    # Step 6: Make Hamiltonian circuit
    hamiltonian_circuit = list(dict.fromkeys(eulerian_circuit))
    hamiltonian_circuit.append(hamiltonian_circuit[0])

    return hamiltonian_circuit


def prim_mst(distances):
    num_vertices = len(distances)
    selected = [False] * num_vertices
    mst = []
    selected[0] = True

    for _ in range(num_vertices - 1):
        min_dist = float('inf')
        min_edge = None
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and distances[i][j] < min_dist:
                        min_dist = distances[i][j]
                        min_edge = (i, j)
        mst.append(min_edge)
        selected[min_edge[1]] = True

    return mst


# def prim_mst(distances):
#     vertices = len(distances)
#     key = [] * vertices
#     parent = [None] * vertices  # Array to store constructed MST
#     key[0] = 0
#     mst_set = [False] * vertices
#     parent[0] = -1
#
#     def min_key(key, mst_set):
#         min_value = sys.maxsize
#         min_index = -1
#         for v in range(vertices):
#             if mst_set[v] is False and key[v] < min_value:
#                 min_value = key[v]
#                 min_index = v
#         return min_index
#
#     for _ in range(vertices):
#         u = min_key(key, mst_set)
#         mst_set[u] = True
#
#         for v in range(vertices):
#             if graph[u][v] > 0 and mst_set[v] == False and graph[u][v] < key[v]:
#                 key[v] = graph[u][v]
#                 parent[v] = u
#
#     return parent
#

def primMST(self):
    key = [inf] * self.V
    parent = [None] * self.V  # Array to store constructed MST
    key[0] = 0
    mstSet = [False] * self.V
    parent[0] = -1

    for cout in range(self.V):
        u = self.minKey(key, mstSet)
        mstSet[u] = True

    for v in range(self.V):
        if mstSet[v] is False and 0 < self.graph[u][v] < key[v]:
            key[v] = self.graph[u][v]
            parent[v] = u


def min_weight_matching(distances, vertices):
    n = len(vertices)
    matching = []
    used = [False] * n

    for i in range(n):
        if not used[i]:
            min_dist = float('inf')
            min_j = -1
            for j in range(i + 1, n):
                if not used[j] and distances[vertices[i]][vertices[j]] < min_dist:
                    min_dist = distances[vertices[i]][vertices[j]]
                    min_j = j
            if min_j != -1:
                matching.append((vertices[i], vertices[min_j]))
                used[i] = used[min_j] = True

    return matching


def find_path(graph):
    # Simple DFS-based Eulerian circuit finder
    adj_list = {}
    for u, v in graph:
        adj_list.setdefault(u, []).append(v)
        adj_list.setdefault(v, []).append(u)

    circuit = []

    def dfs(v):
        while adj_list[v]:
            u = adj_list[v].pop()
            adj_list[u].remove(v)
            dfs(u)
        circuit.append(v)

    dfs(graph[0][0])
    return circuit[::-1]


def create_distance_matrix(points):
    return [[calculate_distance(p1, p2) for p2 in points] for p1 in points]


if __name__ == '__main__':
    for i in range(4, max_node_count):
        node_count = i
        node_array = generate_points(node_count)
        print(f"Path: {node_array}")
        distances = create_distance_matrix(node_array)
        tour = christofides(distances)
        print(f"{i},{tour}")
        print(f"Calculations:       {calculations}\n")

# def primMST(self):
#
#     # Key values used to pick minimum weight edge in cut
#     key = [sys.maxsize] * self.V
#     parent = [None] * self.V  # Array to store constructed MST
#     # Make key 0 so that this vertex is picked as first vertex
#     key[0] = 0
#     mstSet = [False] * self.V
#
#     parent[0] = -1  # First node is always the root of
#
#     for cout in range(self.V):
#
#         # Pick the minimum distance vertex from
#         # the set of vertices not yet processed.
#         # u is always equal to src in first iteration
#         u = self.minKey(key, mstSet)
#
#         # Put the minimum distance vertex in
#         # the shortest path tree
#         mstSet[u] = True
#
#         # Update dist value of the adjacent vertices
#         # of the picked vertex only if the current
#         # distance is greater than new distance and
#         # the vertex in not in the shortest path tree
#         for v in range(self.V):
#
#             # graph[u][v] is non zero only for adjacent vertices of m
#             # mstSet[v] is false for vertices not yet included in MST
#             # Update the key only if graph[u][v] is smaller than key[v]
#             if self.graph[u][v] > 0 and mstSet[v] == False \
#                     and key[v] > self.graph[u][v]:
#                 key[v] = self.graph[u][v]
#                 parent[v] = u
#
#     self.printMST(parent)
