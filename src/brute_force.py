from src import graph
from src.graph import generate_points, calculate_distance, Point


def solve(node_array):
    global node_count, memo
    node_count = len(node_array)
    memo = {}
    cost, path = find_shortest_path(node_array.copy(), {0})
    return cost, path


def find_shortest_path(path: list[Point], visited: set[int]) -> tuple[float, list[Point]]:
    if len(visited) == node_count:
        return calculate_distance(path[-1], path[0]), [path[0]]

    best_distance = float('inf')
    best_path = []

    for j in range(node_count):
        if j not in visited:
            current_distance, sub_path = find_shortest_path(path + [path[j]], visited | {j})
            current_distance += calculate_distance(path[-1], path[j])

            if current_distance < best_distance:
                best_distance = current_distance
                best_path = [path[j]] + sub_path
    return best_distance, best_path


if __name__ == '__main__':
    for i in range(4, 10):
        node_array = generate_points(i)
        cost, path = solve(node_array)
        print(f"{i},{cost},{graph.calculations},{path}")
