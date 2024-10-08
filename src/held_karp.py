from src import graph
from src.graph import generate_points, calculate_distance, Point

max_node_count: int = 11


def solve(input_list: list[Point]) -> tuple[float, list[Point]]:
    in_node_count = len(input_list)
    in_node_array = input_list
    in_memo = {}
    distance, path = solve_loop(0, 1, in_node_array, in_node_count, in_memo)
    return distance, path + [path[0]]


def solve_loop(pos: int, mask: int, node_array: list[Point], node_count: int,
               memo: dict[tuple[int, int], tuple[float, list[Point]]]) -> tuple[float, list[Point]]:
    # Check if all positions have been visited this recursive call
    if mask == (1 << node_count) - 1:
        return calculate_distance(node_array[pos], node_array[0]), [node_array[0]]

    # Check if the current combination has been calculated before
    if (pos, mask) in memo:
        (best_distance, best_path) = memo[(pos, mask)]
        return best_distance, best_path

    best_distance = float('inf')
    best_path = []

    for j in range(node_count):
        # if the index is not in the mask...
        if not (mask & (1 << j)):
            current_distance, sub_path = solve_loop(j, mask | (1 << j), node_array, node_count, memo)
            current_distance += calculate_distance(node_array[pos], node_array[j])

            if current_distance < best_distance:
                best_distance = current_distance
                best_path = [node_array[j]] + sub_path

    memo[(pos, mask)] = (best_distance, best_path)
    return best_distance, best_path


if __name__ == '__main__':
    print(solve([Point(1, 1), Point(-2, -1), Point(2, 1), Point(-3, 5)]))
# for i in range(4, 14):
#     graph.calculations = 0
#     node_array = generate_points(i)
#     cost, path = solve(node_array)
#     print(f"{i},{cost},{graph.calculations},{path}")
