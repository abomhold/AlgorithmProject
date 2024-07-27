from graph import generate_points, Point, calculate_distance, create_distance_dict
# from math import inf
import graph


# max_node_count: int = 13
# node_count: int
# node_array: list[Point]
# distance_dict: dict[tuple[Point, Point], float]


def solve(input_list: list[Point]) -> tuple[float, list[Point]]:
    distance_dict = create_distance_dict(input_list)
    return christofides(input_list, distance_dict)


def christofides(node_array: list[Point], distance_dict: dict[tuple[Point, Point], float]) \
        -> tuple[float, list[Point]]:

    # Step 1: Create a minimum spanning tree
    mst = prims_mst(node_array, distance_dict)
    # print(f"MST: {mst}")

    # Step 2: Find odd-degree vertices
    degree = {}
    for points in mst:
        (point1, point2) = points
        if point1 not in degree:
            degree[point1] = 0
        if point2 not in degree:
            degree[point2] = 0
        degree[point1] += 1
        degree[point2] += 1
    # print(f"Degree: {degree}")

    # # Find odd-degree vertices
    odd_vertices = [node for node in degree if degree[node] % 2 == 1]
    # print(f"Odd Vertices: {odd_vertices}")

    # Step 3: Find minimum weight perfect matching
    matching = min_weight_matching(odd_vertices, distance_dict)
    # print(f"Matching: {matching}")

    # Step 4: Combine MST and matching
    combined_graph = mst + matching
    # print(f"Combined Graph: {combined_graph}")

    # Step 5: Find a route that visits each vertex exactly once (Eulerian circuit)
    complete_path = find_path(combined_graph)
    # print(f"Path: {complete_path}")

    # Step 6: Make Hamiltonian circuit
    hamiltonian_circuit = list(dict.fromkeys(complete_path))
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    # print(f"Hamiltonian Circuit: {hamiltonian_circuit}")
    # print(f"Cost: {graph.path_distance(hamiltonian_circuit)}")
    return graph.path_distance(hamiltonian_circuit), hamiltonian_circuit


def find_path(nodes: list[tuple[Point, Point]]) -> list[Point]:
    path = []
    for (p1, p2) in nodes:
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


def prims_mst(node_array: list[Point], distance_dict: dict[tuple[Point, Point], float]) -> list[tuple[Point, Point]]:
    unselected = set(node_array.copy())
    mst = []
    for _ in range(len(unselected) - 1):
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


def min_weight_matching(odd_vertices: list[Point], distance_dict: dict[tuple[Point, Point], float]) \
        -> list[tuple[Point, Point]]:
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

# if __name__ == '__main__':
#     i = max_node_count
#     node_count = i
#     node_array = generate_points(node_count)
#     print(f"Path: {node_array}")
#     distance_dict = create_distance_dict(node_array)
#     path = christofides()
#     cost = graph.path_distance(path)
#     print(f"{i},{cost},{graph.calculations},{path}")
#
