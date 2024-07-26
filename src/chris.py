from graph import generate_points, Point, calculate_distance, create_distance_dict
# from math import inf
import graph

max_node_count: int = 13
node_count: int
node_array: list[Point]
distance_dict: dict[tuple[Point, Point], float]


def christofides():
    # node_count = len(distance_array)

    # Step 1: Create a minimum spanning tree
    mst = prims_mst()
    print(f"MST: {mst}")

    # Step 2: Find odd-degree vertices
    # # Count the degree of each vertex
    degree = {}
    for points in mst:
        (point1, point2) = points
        if point1 not in degree:
            degree[point1] = 0
        if point2 not in degree:
            degree[point2] = 0
        degree[point1] += 1
        degree[point2] += 1
    print(f"Degree: {degree}")

    # # Find odd-degree vertices
    odd_vertices = [node for node in degree if degree[node] % 2 == 1]
    print(f"Odd Vertices: {odd_vertices}")

    # Step 3: Find minimum weight perfect matching
    matching = min_weight_matching(odd_vertices)
    print(f"Matching: {matching}")

    # Step 4: Combine MST and matching
    combined_graph = mst + matching
    print(f"Combined Graph: {combined_graph}")

    # Step 5: Find Eulerian circuit
    path = find_path(combined_graph)
    print(f"Path: {path}")

    # Step 6: Make Hamiltonian circuit
    hamiltonian_circuit = list(dict.fromkeys(path))
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    print(f"Hamiltonian Circuit: {hamiltonian_circuit}")
    print(f"Cost: {graph.path_distance(hamiltonian_circuit)}")
    return hamiltonian_circuit


def find_path(graph):
    path = []
    for (p1, p2) in graph:
        if not path:
            path.append(p1)
            path.append(p2)
        else:
            for i in range(len(path)):
                if path[i] == p1:
                    path.insert(i + 1, p2)
                    break
                elif path[i] == p2:
                    path.insert(i + 1, p1)
                    break
    return path


def prims_mst():
    unselected = set(node_array.copy())
    mst = []
    for _ in range(node_count - 1):
        min_edge = float('inf')
        (p1, p2) = (None, None)
        for point in node_array:
            if point in unselected:
                for other_point in node_array:
                    if other_point in unselected and point != other_point:
                        if distance_dict[(point, other_point)] < min_edge:
                            min_edge = distance_dict[(point, other_point)]
                            (p1, p2) = (point, other_point)
        mst.append((p1, p2))
        unselected.remove(p1)
    return mst


def min_weight_matching(odd_vertices: list[Point]) -> list[tuple[Point, Point]]:
    matching = []
    unmatched = odd_vertices.copy()
    while unmatched:
        min_dist = float('inf')
        min_pair = None
        for (index, p1) in enumerate(unmatched):
            for j in range(index + 1, len(unmatched)):
                p2 = unmatched[j]
                if distance_dict[(p1, p2)] < min_dist:
                    min_dist = distance_dict[(p1, p2)]
                    min_pair = (p1, p2)

        if min_pair:
            matching.append(min_pair)
            unmatched.remove(min_pair[0])
            unmatched.remove(min_pair[1])
        else:
            break
    return matching


if __name__ == '__main__':
    i = max_node_count
    node_count = i
    node_array = generate_points(node_count)
    print(f"Path: {node_array}")
    distance_dict = create_distance_dict(node_array)
    tour = christofides()
    print(f"{i},{tour}")
    print(f"Calculations: {graph.calculations}\n")

# for j in range(n):
#     if not selected[j] and distance_array[i][j] > 0:
#         if distance_array[i][j] < min_edge:
#             min_edge = distance_array[i][j]
#             x, y = i, j
# while unmatched:
#     min_dist = float('inf')
#     min_pair = None
#     for i, v1 in enumerate(unmatched):
#         for j in range(i + 1, len(unmatched)):
#             v2 = unmatched[j]
#             if distance_dict[(v1, v2)] < min_dist:
#                 min_dist = distance_dict[(v1, v2)]
#                 min_pair = (v1, v2)
#
#     if min_pair:
#         matching.append(min_pair)
#         unmatched.remove(min_pair[0])
#         unmatched.remove(min_pair[1])
#     else:
#         break  # This should not happen in a complete graph
# def min_weight_matching(distances, vertices):
#     n = len(vertices)
#     matching = []
#     used = [False] * n
#
#     for i in range(n):
#         if not used[i]:
#             min_dist = float('inf')
#             min_j = -1
#             for j in range(i + 1, n):
#                 if not used[j] and distances[vertices[i]][vertices[j]] < min_dist:
#                     min_dist = distances[vertices[i]][vertices[j]]
#                     min_j = j
#             if min_j != -1:
#                 matching.append((vertices[i], vertices[min_j]))
#                 used[i] = used[min_j] = True
#
#     return matching
# T = {s}
# enqueue edges connected to s in PQ (by inc weight)
# while (!PQ.isEmpty)
#     if (vertex v linked with e = PQ.remove ∉ T)
#         T = T ∪ {v, e}, enqueue edges connected to v
#     else ignore e
# MST = T
