import heapq
from typing import List, Tuple

from src import graph
from src.graph import Point, create_distance_dict, generate_points, calculate_distance


def solve(input_list: list[Point]) -> tuple[float, list[Point]]:
    return christofides(input_list)


def christofides(node_array: list[Point]) \
        -> tuple[float, list[Point]]:
    # Step 1: Create a minimum spanning tree
    mst = prims_mst(node_array)
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
    # # Find odd-degree vertices
    odd_vertices = [node for node in degree if degree[node] % 2 == 1]
    # Step 3: Find minimum weight perfect matching
    matching = min_weight_matching(odd_vertices)
    # Step 4: Combine MST and matching
    combined_graph = mst + matching
    # Step 5: Find a route that visits each vertex exactly once (Eulerian circuit)
    complete_path = find_complete_path(combined_graph, node_array)
    # Step 6: Make Hamiltonian circuit
    hamiltonian_circuit = trim_path(complete_path)
    return graph.path_distance(hamiltonian_circuit), hamiltonian_circuit


def find_complete_path(edges: list, node_array: list[Point]) -> list[Point]:
    # this is a dictionary of lists where the key is a node
    # and the value is a list of nodes that are connected to it
    connected_nodes = {nodes: [] for nodes in node_array}
    for (node_one, node_two) in edges:
        connected_nodes[node_one].append(node_two)
        connected_nodes[node_two].append(node_one)

    # Find the node with the highest degree
    start_node = max(connected_nodes, key=lambda x: len(connected_nodes[x]))
    stack = [start_node]
    complete_path = []
    while stack:
        current_node = stack.pop()
        complete_path.append(current_node)
        for neighboring_node in connected_nodes[current_node]:
            if current_node in connected_nodes[neighboring_node]:
                connected_nodes[neighboring_node].remove(current_node)
            if connected_nodes[neighboring_node]:
                stack.append(neighboring_node)
    return complete_path


def trim_path(completed_path: list[Point]) -> list[Point]:
    trimmed_path = []
    visited = set()
    for node in completed_path:
        if node not in visited:
            trimmed_path.append(node)
            visited.add(node)
    # Complete the loop
    trimmed_path.append(trimmed_path[0])
    return trimmed_path


def prims_mst(node_array: list[Point]) \
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
                        dist_to_other = calculate_distance(point, other_point)
                        if dist_to_other < min_edge:
                            min_edge = dist_to_other
                            (p1, p2) = (point, other_point)
        mst.append((p1, p2))
        unselected.remove(p1)
    return mst


def min_weight_matching(odd_vertices: list[Point]) \
        -> list[tuple[Point, Point]]:
    matching = []
    unmatched = odd_vertices.copy()
    while unmatched:
        min_dist = float('inf')
        min_pair = None
        for (index, p1) in enumerate(unmatched):
            for j in range(index + 1, len(unmatched)):
                p2 = unmatched[j]
                dist_to_p2 = calculate_distance(p1, p2)
                if dist_to_p2 < min_dist:
                    min_dist = dist_to_p2
                    min_pair = (p1, p2)

        if min_pair:
            matching.append(min_pair)
            unmatched.remove(min_pair[0])
            unmatched.remove(min_pair[1])
        else:
            break
    return matching


if __name__ == '__main__':
    for i in range(4, 14):
        graph.calculations = 0
        node_array = generate_points(i)
        cost, path = solve(node_array)
        print(f"{i},{cost},{graph.calculations},{path}")
