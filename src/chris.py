import heapq

from src import graph
from src.graph import Point, create_distance_dict, generate_points


def solve(input_list: list[Point]) -> tuple[float, list[Point]]:
    return christofides(input_list, create_distance_dict(input_list))


def christofides(node_array: list[Point], distance_dict: dict[tuple[Point, Point], float]) \
        -> tuple[float, list[Point]]:
    # Step 1: Create a minimum spanning tree
    mst = prims_mst(node_array, distance_dict)
    print(f"MST: {len(mst)}  {mst}")

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
    # print(f"Degree: {len(degree)}  {degree}")

    # # Find odd-degree vertices
    odd_vertices = [node for node in degree if degree[node] % 2 == 1]
    # print(f"Odd Vertices: {len(odd_vertices)} {odd_vertices}")

    # Step 3: Find minimum weight perfect matching
    matching = min_weight_matching(odd_vertices, distance_dict)
    # print(f"Matching: {len(matching)}  {matching}")

    # Step 4: Combine MST and matching
    combined_graph = mst + matching
    print(f"Combined Graph: {len(combined_graph)} {combined_graph}")

    # TODO: Path does not include all nodes
    # Step 5: Find a route that visits each vertex exactly once (Eulerian circuit)
    complete_path = find_path(combined_graph)
    print(f"Route: {len(complete_path)} {complete_path}")

    better_path = depth_first_search(combined_graph, distance_dict)
    print(f"Route: {len(better_path)} {better_path}")

    # Step 6: Make Hamiltonian circuit
    hamiltonian_circuit = list(dict.fromkeys(complete_path))
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    # print(f"Hamiltonian Circuit: {len(hamiltonian_circuit)} {hamiltonian_circuit}")
    # print(f"Cost: {graph.path_distance(hamiltonian_circuit)}")
    return graph.path_distance(hamiltonian_circuit), hamiltonian_circuit



def depth_first_search(edges: list, distance_dict: dict) -> list[Point]:
    visited = set()
    route = []
    stack = []
    for edge in edges:
        heapq.heappush(stack, (distance_dict[edge], edge))

    while stack:
        (dist, (p1, p2)) = heapq.heappop(stack)
        if p1 not in visited:
            route.append(p1)
            visited.add(p1)
        if p2 not in visited:
            route.append(p2)
            visited.add(p2)
    return route

def prims_mst(node_array: list[Point], distance_dict: dict[tuple[Point, Point], float]) \
        -> list[tuple[Point, Point]]:
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


if __name__ == '__main__':
    i = 14
    node_count = i
    node_array = generate_points(node_count)
    print(f"Path:{len(node_array)} {node_array}")
    distance_dict = create_distance_dict(node_array)
    path = christofides(node_array, distance_dict)
    cost = graph.path_distance(path[1])
    print(f"{i},{cost},{graph.calculations},{path}, {len(path[1])}")
